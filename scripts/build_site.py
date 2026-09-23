"""Build only the bilingual documentation and portable skill download."""

from hashlib import sha256
from html import escape
from io import BytesIO
from pathlib import Path, PurePosixPath
import posixpath
from urllib.parse import unquote, urlsplit, urlunsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


ROOT = Path(__file__).resolve().parents[1]
REPO = "lego-like-3d-print-skill"
GITHUB = f"https://github.com/ktanino10/{REPO}"
SITE = f"https://ktanino10.github.io/{REPO}/"
SKILL = ROOT / ".github" / "skills" / "lego-like-3d-print"
OUTPUT = ROOT / "_site" / REPO
PAGES = ("index", "install", "usage", "examples", "notices")
LABELS = {
    "ja": ("ホーム", "導入", "使い方", "作例", "注意事項"),
    "en": ("Home", "Install", "Usage", "Examples", "Notices"),
}


def route(language, page):
    folder = PurePosixPath(language)
    if page != "index":
        folder /= page
    return folder / "index.html"


ROUTES = {
    ROOT / "docs" / language / f"{page}.md": route(language, page)
    for language in LABELS
    for page in PAGES
}


def relative_url(current, target):
    if target.name == "index.html":
        relative = posixpath.relpath(str(target.parent), str(current.parent))
        return "./" if relative == "." else relative + "/"
    return posixpath.relpath(str(target), str(current.parent))


class LinkRewriter(Treeprocessor):
    def __init__(self, md, source, current):
        super().__init__(md)
        self.source = source
        self.current = current

    def run(self, root):
        for node in root.iter("a"):
            href = node.get("href", "")
            parsed = urlsplit(href)
            if href.startswith(SITE):
                target = PurePosixPath(unquote(parsed.path[len(urlsplit(SITE).path):]))
                if parsed.path.endswith("/"):
                    target /= "index.html"
                path = relative_url(self.current, target)
            elif parsed.scheme or parsed.netloc or not parsed.path:
                continue
            else:
                target = (self.source.parent / unquote(parsed.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    raise ValueError(f"Broken source link in {self.source.relative_to(ROOT)}: {href}")
                if target in ROUTES:
                    path = relative_url(self.current, ROUTES[target])
                elif target == ROOT / "LICENSE":
                    path = relative_url(self.current, PurePosixPath("license.txt"))
                else:
                    kind = "tree" if target.is_dir() else "blob"
                    path = f"{GITHUB}/{kind}/main/{target.relative_to(ROOT).as_posix()}"
            node.set("href", urlunsplit(("", "", path, parsed.query, parsed.fragment)))


class SourceLinks(Extension):
    def __init__(self, source, current):
        self.source = source
        self.current = current
        super().__init__()

    def extendMarkdown(self, md):
        md.treeprocessors.register(LinkRewriter(md, self.source, self.current), "source-links", 5)


def skill_files():
    result = []
    for path in sorted(SKILL.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Portable skill must not contain symlinks: {path.name}")
        if path.is_file() and (path.suffix in {".md", ".py"} or path.name == "LICENSE"):
            result.append(path)
    return result


def skill_archive():
    stream = BytesIO()
    with ZipFile(stream, "w", compression=ZIP_DEFLATED) as archive:
        for path in skill_files():
            name = (PurePosixPath(SKILL.name) / path.relative_to(SKILL).as_posix()).as_posix()
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return stream.getvalue()


def document_shell(language, title, description, current, body, page=None):
    japanese = language == "ja"
    skip = "本文へ" if japanese else "Skip to content"
    nav_label = "主なページ" if japanese else "Main navigation"
    site_name = "ブロック風3Dプリント スキル" if japanese else "Brick-style 3D print skill"
    home = relative_url(current, route(language, "index"))
    navigation = ""
    language_link = ""
    source = GITHUB
    alternate_links = ""
    if page:
        links = []
        for key, label in zip(PAGES, LABELS[language]):
            selected = ' aria-current="page"' if key == page else ""
            links.append(f'<a href="{relative_url(current, route(language, key))}"{selected}>{label}</a>')
        navigation = " ".join(links)
        other = "en" if japanese else "ja"
        other_label = "English" if japanese else "日本語"
        language_link = (
            f'<a class="language-switch" data-language-link lang="{other}" hreflang="{other}" '
            f'href="{relative_url(current, route(other, page))}">{other_label}</a>'
        )
        source = f"{GITHUB}/blob/main/docs/{language}/{page}.md"
        alternate_links = "\n".join(
            f'<link rel="alternate" hreflang="{lang}" href="{SITE}{route(lang, page).parent}/">'
            for lang in LABELS
        )
    canonical = SITE + (str(current.parent) + "/" if str(current.parent) != "." else "")
    css = relative_url(current, PurePosixPath("assets/style.css"))
    script = relative_url(current, PurePosixPath("assets/site.js"))
    icon = relative_url(current, PurePosixPath("assets/icon.svg"))
    license_url = relative_url(current, PurePosixPath("license.txt"))
    notices = relative_url(current, route(language, "notices"))
    source_label = "このページの原文" if japanese else "Page source"
    rights_label = "権利と注意事項" if japanese else "Rights and notices"
    return f"""<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(description, quote=True)}">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'">
<title>{escape(title)} · {site_name}</title>
<link rel="canonical" href="{canonical}">
{alternate_links}
<link rel="icon" type="image/svg+xml" href="{icon}">
<link rel="stylesheet" href="{css}">
<script src="{script}" defer></script>
</head>
<body>
<a class="skip-link" href="#main">{skip}</a>
<header class="site-header">
<div class="header-inner">
<a class="brand" href="{home}"><span class="brick-mark" aria-hidden="true"></span><span>Brick-style<span class="brand-detail">3D print skill</span></span></a>
<div class="header-tools"><a href="{GITHUB}">GitHub</a>{language_link}</div>
</div>
<nav aria-label="{nav_label}" class="main-nav">{navigation}</nav>
</header>
<main id="main" tabindex="-1">
<p class="eyebrow">8 mm / FreeCAD / Blender / GitHub Copilot</p>
<article>{body}</article>
</main>
<footer class="site-footer">
<p><a href="{source}">{source_label}</a> · <a href="{license_url}">MIT</a> · <a href="{notices}">{rights_label}</a></p>
<p>Unofficial · 非公式 / No compatibility or fabrication guarantee.</p>
</footer>
</body>
</html>
"""


def render_document(source, current):
    text = source.read_text(encoding="utf-8")
    language = source.parent.name
    title = text.splitlines()[0].removeprefix("# ")
    description = (
        "8 mmブロック風模型のための非公式Copilotスキル。導入、制作手順、作例、確認範囲。"
        if language == "ja"
        else "An unofficial Copilot skill for 8 mm brick-style models: installation, workflow, examples and evidence."
    )
    body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "toc", SourceLinks(source, current)]
    )
    table_label = "表（横にスクロールできます）" if language == "ja" else "Table (scroll horizontally if needed)"
    body = body.replace("<table>", f'<div class="table-scroll" role="region" aria-label="{table_label}" tabindex="0"><table>')
    body = body.replace("</table>", "</table></div>")
    return document_shell(language, title, description, current, body, source.stem)


def build():
    files = {
        target: render_document(source, target).encode("utf-8")
        for source, target in ROUTES.items()
    }
    root_body = """<h1>Make something.<br>Build it in blocks.</h1>
<p class="intro">ブロック風3Dプリント模型の制作を、設計から組立まで。<br>
A workflow skill for brick-style 3D printing, from design to assembly.</p>
<div class="language-cards">
<a href="ja/" lang="ja"><span class="card-label">日本語</span><span>導入・使い方・作例・注意事項 →</span></a>
<a href="en/" lang="en"><span class="card-label">English</span><span>Install, use, explore and understand the limits →</span></a>
</div>
<p>個人の趣味・学習を目的とした非公式の制作支援スキルです。各社の公式提供・推奨や、互換性・造形結果の保証を示すものではありません。</p>
<p>An unofficial creation-support skill intended for personal hobbies and learning.
It does not imply official provision or endorsement by any company, or guarantee compatibility or fabrication results.</p>
<p>新規文書・スクリプトはMIT。商用利用も認めます。外部作品の権利は別です。<br>
Original documents/scripts are MIT licensed, including commercial use. External works retain separate rights.</p>"""
    files[PurePosixPath("index.html")] = document_shell(
        "en", "日本語 / English", "Choose a language / 言語を選ぶ",
        PurePosixPath("index.html"), root_body
    ).encode("utf-8")
    for name in ("style.css", "site.js", "icon.svg"):
        files[PurePosixPath("assets") / name] = (ROOT / "web" / name).read_bytes()
    files[PurePosixPath("license.txt")] = (ROOT / "LICENSE").read_bytes()
    archive = skill_archive()
    files[PurePosixPath("downloads/lego-like-3d-print.zip")] = archive
    files[PurePosixPath("downloads/lego-like-3d-print.zip.sha256")] = (
        f"{sha256(archive).hexdigest()}  lego-like-3d-print.zip\n"
    ).encode("ascii")

    for parent in (ROOT / "_site", OUTPUT):
        if parent.is_symlink():
            raise ValueError(f"Build destination must not be a symlink: {parent.name}")
    existing = {PurePosixPath(p.relative_to(OUTPUT).as_posix()) for p in OUTPUT.rglob("*") if p.is_file()}
    unexpected = existing - files.keys()
    if unexpected:
        raise ValueError(f"Unexpected files in generated output; inspect them before rebuilding: {sorted(map(str, unexpected))}")
    for relative, content in files.items():
        destination = OUTPUT / relative
        for path in (destination, *destination.parents):
            if path == ROOT:
                break
            if path.is_symlink():
                raise ValueError(f"Build refuses symlink: {path.name}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(content)
    print(f"Built {len(ROUTES) + 1} pages and portable skill ZIP in _site/{REPO}/")
    return files


if __name__ == "__main__":
    build()
