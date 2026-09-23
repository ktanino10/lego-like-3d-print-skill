# Maintaining the distribution / 配布物の更新

## English

The source of truth is `.github/skills/lego-like-3d-print/` plus paired
`docs/ja/` and `docs/en/` Markdown. Pages is generated from those same docs;
do not edit `_site/`. Keep one registered `SKILL.md`. Preserve both reference
translations, technical units, physical-evidence limits and MIT/external-rights
distinctions. Do not add private data or copy reference-project media.

Python 3.11+ is sufficient for the site tooling; it is **not** FreeCAD's Python.
Create a project-local environment and install only the declared dependencies:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/check_browser.py --channel chrome
```

On Windows use `py -3 -m venv .venv` and `.venv\Scripts\python.exe`.
`--channel chrome` uses an already installed Chrome in an isolated test profile.
If no supported browser is installed, explicitly choose to install Playwright's
test Chromium with `.venv/bin/python -m playwright install chromium`, then omit
`--channel`. The CI workflow installs its browser on the disposable GitHub runner,
not on your computer. No FreeCAD or Blender is installed by CI.

For build-only work, install `requirements.txt` and run
`.venv/bin/python scripts/build_site.py`.
To preview the repository subpath, run:

```sh
.venv/bin/python -m http.server 8000 --bind 127.0.0.1 --directory _site
```

Open `http://127.0.0.1:8000/lego-like-3d-print-skill/`. Stop the server with
Ctrl+C. The builder writes only the fixed generated output directory and
refuses unexpected existing files or symlinks there. Inspect any reported file
instead of deleting the whole repository.

Tests check skill YAML, relative links including a standalone copy, paired
sections and install commands, core baseline values, private-data patterns,
non-overwriting POSIX install behavior, smoke-script safety guards, deterministic
ZIP contents, all generated links and workflow scope. Real browser checks cover
11 pages at 1440 and 375 px, navigation, corresponding language/section switches,
ZIP/hash download and JavaScript-disabled navigation. They do not certify the
meaning of every translation, every OS install, physical fit or printability;
human review and target-environment checks remain necessary.
CI retains desktop/mobile screenshots as the `site-browser-evidence` artifact
for seven days; these are not included in the deployed site or skill ZIP.

For already deployed content:

```sh
.venv/bin/python scripts/check_browser.py --channel chrome \
  --base-url https://ktanino10.github.io/lego-like-3d-print-skill/
```

`web/` contains original local CSS, a small language-anchor helper and an original
generic icon. No external CDN, analytics, font or application binary is needed.
The skill-only ZIP includes its own LICENSE/NOTICES and all relative references.
It is generated deterministically; it is not a model kit.

The official Actions workflow validates every push/PR and deploys **main only**
to the `github-pages` environment. Configure this repository's Pages source as
GitHub Actions. Actions are pinned to reviewed official release commits.
Never use a deployment to change another repository's visibility or publish
private history. Preserve the existing MIT license and author notice.

## 日本語

正本は`.github/skills/lego-like-3d-print/`と、対になった`docs/ja/`・`docs/en/`です。
同じ文書からPagesを生成し、`_site/`は直接編集しません。
登録する`SKILL.md`は1つに保ち、参照資料の翻訳、単位、物理確認範囲、
MITと外部権利の区別を揃えます。私有情報や元作品の画像を追加しません。

サイト用Pythonは3.11以降で、FreeCADのPythonとは別です。
上記のvenv手順で、このrepoの依存manifestだけを導入してください。
Windowsは`py -3 -m venv .venv`と`.venv\Scripts\python.exe`を使います。
`--channel chrome`は既存Chromeを別の検査用profileで起動します。
利用可能なbrowserがなければ、利用者の判断で`python -m playwright install chromium`を実行し、
`--channel`を省きます。CIのbrowser導入は使い捨てGitHub runnerだけです。
FreeCADやBlenderはCIで導入しません。

buildだけなら`requirements.txt`と`python scripts/build_site.py`で十分です。
上記のlocal serverを開くとrepo-subpathで表示を確認できます。終了はCtrl+Cです。
build先の不明なファイル・symlinkは上書きせずエラーにするので、
対象を点検し、repo全体を削除しないでください。

検査はYAML、単体コピーの相対リンク、日英のsection・導入コマンド、
主要寸法、私有情報pattern、POSIX非上書きcopy、smokeの保護、
再現可能ZIP、siteリンク、workflow範囲を対象にします。
実browserでは11ページを1440/375 pxで開き、移動、対応ページ/sectionの言語切替、
ZIP/hash、JavaScriptなしの導線を確認します。
全翻訳の意味・全OSでのアプリ導入・現物嵌合・造形結果を証明するものではありません。
内容レビューと対象環境での確認も必要です。
CIはPC/スマホのスクリーンショットを`site-browser-evidence` artifactに7日間保存します。
配信サイト・スキルZIPへは含めません。

`web/`は本repoで作ったCSS・小さな言語切替処理・汎用iconのみで、
外部CDN、追跡、font、アプリ本体に依存しません。
スキル単体ZIPはLICENSE/NOTICES・参照文書込みで再現可能に生成し、模型データとは区別します。

公式Actionsの固定commitを使うworkflowは各push/PRを確認し、**mainだけ**を
`github-pages`へ配信します。PagesのsourceはこのrepoのGitHub Actionsに設定します。
他repoのvisibility・private履歴を変更しないでください。MIT本文・著作権表示を保持します。
