"""Check the local build or a served subpath using a real, isolated browser."""

import argparse
from contextlib import contextmanager
from functools import partial
from hashlib import sha256
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import urlsplit

from playwright.sync_api import sync_playwright

from build_site import OUTPUT, PAGES, REPO, ROOT, skill_archive


@contextmanager
def local_site():
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT / "_site"))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/{REPO}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def check(base_url, channel=None, screenshots=None):
    errors = []
    unexpected_requests = []
    base_url = base_url.rstrip("/") + "/"
    expected_origin = urlsplit(base_url).netloc
    with sync_playwright() as playwright:
        options = {"headless": True, "timeout": 60000}
        if channel:
            options["channel"] = channel
        browser = playwright.chromium.launch(**options)
        try:
            for width, height in ((1440, 1000), (375, 812)):
                context = browser.new_context(viewport={"width": width, "height": height})
                page = context.new_page()
                page.on("pageerror", lambda error: errors.append(str(error)))
                page.on("console", lambda message: errors.append(message.text) if message.type == "error" else None)
                page.on("request", lambda request: unexpected_requests.append(request.url)
                        if urlsplit(request.url).netloc != expected_origin else None)
                paths = [""] + [
                    language + "/" + (key + "/" if key != "index" else "")
                    for language in ("ja", "en") for key in PAGES
                ]
                for path in paths:
                    response = page.goto(base_url + path, wait_until="networkidle")
                    assert response and response.status == 200, (width, path, response.status if response else None)
                    assert page.locator("h1").count() == 1, (width, path, "one h1 required")
                    assert page.locator("body").inner_text().strip(), (width, path, "empty page")
                    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth"), (
                        width, path, "horizontal page overflow"
                    )
                    if path:
                        assert page.locator("html").get_attribute("lang") == path[:2]
                        assert page.locator('nav a[aria-current="page"]').count() == 1
                    if screenshots and path in ("", "ja/", "en/", "ja/install/", "en/install/"):
                        screenshots.mkdir(parents=True, exist_ok=True)
                        name = path.strip("/").replace("/", "-") or "language"
                        page.screenshot(path=str(screenshots / f"{name}-{width}.png"))
                page.goto(base_url + "ja/install/#freecad", wait_until="networkidle")
                page.locator("[data-language-link]").click()
                page.wait_for_url(base_url + "en/install/#freecad")
                assert page.locator("#freecad").count() == 1
                page.locator("[data-language-link]").click()
                page.wait_for_url(base_url + "ja/install/#freecad")
                page.get_by_role("navigation").get_by_role("link", name="使い方", exact=True).click()
                page.wait_for_url(base_url + "ja/usage/")

                page.goto(base_url + "en/", wait_until="networkidle")
                with page.expect_download() as event:
                    page.locator('a[href$="downloads/lego-like-3d-print.zip"]').first.click()
                download = event.value
                assert download.failure() is None
                archive = Path(download.path()).read_bytes()
                assert archive == skill_archive(), "browser download differs from source skill"
                checksum = context.request.get(base_url + "downloads/lego-like-3d-print.zip.sha256")
                assert checksum.ok and checksum.text().split()[0] == sha256(archive).hexdigest()
                context.close()

            context = browser.new_context(java_script_enabled=False, viewport={"width": 375, "height": 812})
            page = context.new_page()
            page.goto(base_url + "ja/install/", wait_until="networkidle")
            page.locator("[data-language-link]").click()
            page.wait_for_url(base_url + "en/install/")
            assert "FreeCAD" in page.locator("main").inner_text()
            context.close()
            assert not errors, errors
            assert not unexpected_requests, unexpected_requests
        finally:
            browser.close()
    print("BROWSER_OK: 11 pages at 1440px and 375px; navigation, language/section switch, ZIP/hash, no-JS, no external runtime requests.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", help="Omit to serve the existing local build at its repository subpath.")
    parser.add_argument("--channel", help="Use an existing browser, e.g. chrome; otherwise use Playwright Chromium.")
    parser.add_argument("--screenshots", type=Path, help="Optional local evidence folder; do not publish personal paths.")
    arguments = parser.parse_args()
    if arguments.base_url:
        check(arguments.base_url, arguments.channel, arguments.screenshots)
    else:
        if not (OUTPUT / "index.html").is_file():
            raise SystemExit("Build first: python scripts/build_site.py")
        with local_site() as url:
            check(url, arguments.channel, arguments.screenshots)
