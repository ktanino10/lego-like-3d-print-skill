import ast
from hashlib import sha256
from html.parser import HTMLParser
import importlib.util
from io import BytesIO
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

import markdown
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_site


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = []
        self.languages = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "html":
            self.languages.append(attrs.get("lang"))


def markdown_body(path):
    text = path.read_text(encoding="utf-8")
    if text.startswith("---\n"):
        text = text.split("---\n", 2)[2]
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])


def check_markdown_links(test, paths, boundary):
    boundary = boundary.resolve()
    for path in paths:
        for href in Links(markdown_body(path)).links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            test.assertTrue(target.is_relative_to(boundary), f"Escaping link: {path.name}: {href}")
            test.assertTrue(target.exists(), f"Missing link: {path.name}: {href}")
            if url.fragment and target.suffix == ".md":
                test.assertIn(unquote(url.fragment), Links(markdown_body(target)).ids, f"Missing anchor: {href}")


class DistributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = build_site.build()

    def test_single_skill_yaml(self):
        skills = list((ROOT / ".github" / "skills").rglob("SKILL.md"))
        self.assertEqual(skills, [build_site.SKILL / "SKILL.md"])
        text = skills[0].read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        frontmatter = yaml.safe_load(text.split("---\n", 2)[1])
        self.assertEqual(frontmatter["name"], "lego-like-3d-print")
        self.assertEqual(frontmatter["license"], "MIT")
        self.assertLessEqual(len(frontmatter["description"]), 1024)
        self.assertIn("brick-style", frontmatter["description"])
        self.assertIn("レゴ風", frontmatter["description"])
        self.assertNotIn("allowed-tools", frontmatter)
        self.assertIn("requester's language", text)

    def test_source_links_and_portable_copy(self):
        paths = list((ROOT / "docs").rglob("*.md")) + list(build_site.SKILL.rglob("*.md"))
        paths += list(ROOT.glob("*.md"))
        check_markdown_links(self, paths, ROOT)
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / build_site.SKILL.name
            shutil.copytree(build_site.SKILL, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            check_markdown_links(self, list(destination.rglob("*.md")), destination)
            self.assertEqual((destination / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
            self.assertFalse((destination / "assets").exists())

    def test_paired_sections_and_install_commands(self):
        for page in build_site.PAGES:
            documents = [(ROOT / "docs" / lang / f"{page}.md").read_text(encoding="utf-8") for lang in ("ja", "en")]
            anchors = [re.findall(r'<a id="([^"]+)"></a>', text) for text in documents]
            self.assertEqual(anchors[0], anchors[1], page)
            self.assertTrue(anchors[0], page)
        installs = [(ROOT / "docs" / lang / "install.md").read_text(encoding="utf-8") for lang in ("ja", "en")]
        code = [re.findall(r"```(?:sh|powershell|python|text)\n(.*?)\n```", text, re.S) for text in installs]
        self.assertEqual(code[0], code[1], "Installation commands drifted between languages")
        for text in installs:
            for term in ("4.5 LTS", "5.1.1", "1.1.3", "8.1", "/skills reload", "/skills info"):
                self.assertIn(term, text)

    def test_critical_baseline_values(self):
        expected = (
            "0967390547184b342adea0d7e8659dc8ac8f153b", "5.0-legible-plaques",
            "15.8×15.8×9.6", "15.8×31.8×9.6", "15.8×31.8×11.4",
            "191.8×80.2×238.6", "191.8×79.8", "142×40", "1.6 / 1.0",
            "+0.04", "0.2 / 0.3", "3.216854", "1.616854", "FIT-M-D470",
            "FIT-F-CP12", "B-black-02.3mf", "B-001", "r3-8mm-20260920",
            "2026-09-23", "CC BY-NC 4.0", "MIT",
        )
        for name in ("baseline.md", "baseline.ja.md"):
            text = (build_site.SKILL / "references" / name).read_text(encoding="utf-8")
            for term in expected:
                self.assertIn(term, text, (name, term))
        self.assertIn("radial", (build_site.SKILL / "references/baseline.md").read_text())
        self.assertIn("半径方向", (build_site.SKILL / "references/baseline.ja.md").read_text())

    def test_no_private_data_or_copied_media(self):
        paths = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
        ).splitlines()
        patterns = (
            r"/(?:Users|home)/[^\s/]+",
            r"[.]copilot/session[-]state",
            r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
            r"gh[pousr]_[A-Za-z0-9]{30,}",
            r"github_pat_[A-Za-z0-9_]{30,}",
            r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
        )
        allowed_repos = {build_site.REPO, "copilot-brick-display", "octoprints-brick-kit-downloads"}
        for relative in paths:
            path = ROOT / relative
            self.assertNotIn(path.suffix.lower(), {".png", ".jpg", ".jpeg", ".blend", ".stl", ".3mf", ".fcstd", ".mp4", ".woff", ".ttf"})
            text = path.read_text(encoding="utf-8")
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text, re.I), f"Private data pattern in {relative}")
            for repo in re.findall(r"github\.com/ktanino10/([A-Za-z0-9_.-]+)", text):
                self.assertIn(repo, allowed_repos, f"Unapproved example repository in {relative}")

    def test_generated_links_ids_and_language(self):
        for relative, content in self.outputs.items():
            if relative.suffix != ".html":
                continue
            parsed = Links(content.decode("utf-8"))
            self.assertEqual(len(parsed.ids), len(set(parsed.ids)), relative)
            self.assertEqual(parsed.languages, [relative.parts[0] if len(relative.parts) > 1 else "en"])
            for href in parsed.links:
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    continue
                self.assertFalse(url.path.startswith("/"), (relative, href, "root-fixed link"))
                target = (build_site.OUTPUT / relative).parent / unquote(url.path) if url.path else build_site.OUTPUT / relative
                if target.is_dir():
                    target /= "index.html"
                target = target.resolve()
                self.assertTrue(target.is_relative_to(build_site.OUTPUT), (relative, href))
                self.assertTrue(target.is_file(), (relative, href))
                if url.fragment and target.suffix == ".html":
                    self.assertIn(unquote(url.fragment), Links(target.read_text(encoding="utf-8")).ids, (relative, href))

    def test_download_is_deterministic_and_complete(self):
        payload = self.outputs[PurePosixPath("downloads/lego-like-3d-print.zip")]
        self.assertEqual(payload, build_site.skill_archive())
        checksum = self.outputs[PurePosixPath("downloads/lego-like-3d-print.zip.sha256")].decode().split()[0]
        self.assertEqual(checksum, sha256(payload).hexdigest())
        with ZipFile(BytesIO(payload)) as archive:
            expected = {
                f"{build_site.SKILL.name}/{path.relative_to(build_site.SKILL).as_posix()}": path.read_bytes()
                for path in build_site.skill_files()
            }
            self.assertEqual(set(archive.namelist()), set(expected))
            self.assertEqual(len(expected), 9)
            for name, content in expected.items():
                self.assertEqual(archive.read(name), content)

    def test_documented_copy_refuses_overwrite_and_dangling_symlink(self):
        text = (ROOT / "docs/en/install.md").read_text(encoding="utf-8")
        command = re.search(r"```sh\n(.*?)\n```", text, re.S).group(1)
        with tempfile.TemporaryDirectory() as directory:
            environment = {**os.environ, "HOME": directory}
            destination = Path(directory) / ".copilot/skills/lego-like-3d-print"
            result = subprocess.run(["sh", "-c", command], cwd=ROOT, env=environment, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            original = (destination / "SKILL.md").read_bytes()
            sentinel = destination / "keep-personal.txt"
            sentinel.write_text("preserve me")
            result = subprocess.run(["sh", "-c", command], cwd=ROOT, env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("STOP: destination exists", result.stderr)
            self.assertEqual((destination / "SKILL.md").read_bytes(), original)
            self.assertEqual(sentinel.read_text(), "preserve me")
            backup = Path(directory) / "saved-outside-discovery"
            destination.rename(backup)
            destination.symlink_to(Path(directory) / "missing-target")
            result = subprocess.run(["sh", "-c", command], cwd=ROOT, env=environment, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(destination.is_symlink())

    def test_python_syntax_and_blender_foreground_guard(self):
        for directory in (ROOT / "scripts", ROOT / "tests", build_site.SKILL / "scripts"):
            for path in directory.glob("*.py"):
                ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
        path = build_site.SKILL / "scripts/blender_smoke.py"
        spec = importlib.util.spec_from_file_location("blender_smoke_test", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with patch.dict(sys.modules, {"bpy": SimpleNamespace(app=SimpleNamespace(background=False))}):
            with self.assertRaisesRegex(RuntimeError, "separate Blender"):
                module.run()
        with patch.dict(sys.modules, {"bpy": SimpleNamespace(app=SimpleNamespace(background=True), data=SimpleNamespace(filepath="existing.blend"))}):
            with self.assertRaisesRegex(RuntimeError, "factory-startup"):
                module.run()

    def test_workflow_publication_is_main_only(self):
        workflow = yaml.safe_load((ROOT / ".github/workflows/pages.yml").read_text())
        self.assertEqual(workflow["permissions"], {"contents": "read"})
        jobs = workflow["jobs"]
        self.assertEqual(jobs["deploy"]["needs"], "build")
        self.assertIn("refs/heads/main", jobs["deploy"]["if"])
        self.assertEqual(jobs["deploy"]["permissions"], {"pages": "write", "id-token": "write"})
        for job in jobs.values():
            for step in job.get("steps", []):
                if "uses" in step:
                    self.assertRegex(step["uses"], r"^actions/[\w-]+@[0-9a-f]{40}$")


if __name__ == "__main__":
    unittest.main()
