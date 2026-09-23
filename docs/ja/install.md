# 導入と最初の動作確認

[English](../en/install.md) · [使い方](usage.md) · [注意事項](notices.md)

[必要なもの](#requirements) / [スキル](#skill-install) / [更新](#updates) /
[FreeCAD](#freecad) / [Blender](#blender) / [AIとの接続](#ai-tools) / [困ったとき](#troubleshooting)

<a id="requirements"></a>
## 何をするかで必要なものが変わります

| 目的 | 必要なもの |
| --- | --- |
| 文書を読む・公開3Dを見る | ブラウザーのみ。スキルのインストールも不要 |
| AIにこの手順を使わせる | Agent Skills対応のGitHub Copilot app / CLI等、対象フォルダーへのアクセス |
| 実CAD、FCStd / STEP / STLを作る | FreeCADと、それに対応するPython実行環境 |
| 実メッシュのCG・動画・`.blend`を作る | 対応OS・GPU上のBlender |
| MP4変換・検査 | 必要な場合のみffmpeg |
| 3Dサイトのビルド | 選んだtoolchainが要求する場合のみNode.js等 |
| 実スライス | 使用プリンターに対応するslicer。Bambu Studioは該当機での例 |

この配布物は**制作手順のスキル**で、完成模型一式の生成器ではありません。
CAD、完成シーン、参考画像、フォント、MCP serverは同梱・自動導入されません。
アプリや依存のインストールは利用者が内容と権限を確認して行ってください。

参照例のFreeCAD **1.1.3** / Blender **5.1.1** / ffmpeg **8.1**は利用履歴で、
全OSでの必須版・動作保証ではありません。公式配布ページで対応OS・CPU・GPUを選びます。
特にIntel MacとApple SiliconではBlenderの対応版が違います。

<a id="skill-install"></a>
## 1. スキルをコピーする

GitHub公式の[Agent Skills説明](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)と
[CLIへの追加手順](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)に沿った配置です。
スキルは命令・コードを含むため、インストール前に内容を読んでください。
このスキルはshellの無条件事前承認（`allowed-tools`）を指定していません。

**保存するもの:** [スキルだけのZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip)
（[SHA-256](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip.sha256)）、
または[リポジトリ](https://github.com/ktanino10/lego-like-3d-print-skill)の
**Code → Download ZIP**。展開してから使います。repo全体のZIPなら、配布元は
`.github/skills/lego-like-3d-print`です。
`.github`が見えない場合、macOS Finderは`Command+Shift+.`、Linuxの多くのファイラーは`Ctrl+H`、
Windowsはエクスプローラーの隠し項目表示を確認します。

| 配置先 | 範囲 |
| --- | --- |
| `~/.copilot/skills/lego-like-3d-print` | 個人用。Windowsでは`$HOME`配下の`.copilot\skills\lego-like-3d-print` |
| 自分のrepoの`.github/skills/lego-like-3d-print` | そのプロジェクト用 |

**どちらか一方**へ、LICENSE・NOTICES・references・scriptsを含むフォルダー全体をコピーします。
日本語版と英語版を別の`SKILL.md`として登録したり、同じスキルを両方へ重複配置したりしないでください。
この配布repo自体には既にプロジェクト用スキルがあります。

### macOS / Linuxの非上書きコピー

以下は**展開したrepoのルートで**実行する例です。スキル単体ZIPなら`src="./lego-like-3d-print"`に変えます。
既存の配置先がある場合は停止し、削除・上書きしません。

```sh
(
  set -eu
  src=".github/skills/lego-like-3d-print"
  dest="$HOME/.copilot/skills/lego-like-3d-print"
  test -f "$src/SKILL.md" || { echo "STOP: source SKILL.md not found" >&2; exit 1; }
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    echo "STOP: destination exists; use the update procedure" >&2
    exit 1
  fi
  mkdir -p "$(dirname "$dest")"
  cp -R "$src" "$dest"
)
```

プロジェクト用なら`dest`を、対象repo内の`.github/skills/lego-like-3d-print`へ変更します。
例: `dest="../my-model/.github/skills/lego-like-3d-print"`。
対象repoを取り違えないよう、実行前に場所を確認してください。

### Windows PowerShellの非上書きコピー

同じく展開したrepoのルートで実行します。単体ZIPなら`$source="./lego-like-3d-print"`へ変えます。

```powershell
$ErrorActionPreference = "Stop"
$source = ".github/skills/lego-like-3d-print"
$destination = Join-Path $HOME ".copilot/skills/lego-like-3d-print"
if (-not (Test-Path -LiteralPath "$source/SKILL.md")) {
    throw "STOP: source SKILL.md not found"
}
if (Test-Path -LiteralPath $destination) {
    throw "STOP: destination exists; use the update procedure"
}
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
```

プロジェクト用は`$destination`を対象repo内の配置先へ変更します。
ターミナルを使わずファイラーでコピーしても構いませんが、置換確認が出たらキャンセルして更新手順へ進みます。

### Copilotに読み込ませる

**CLI:** 新しいセッションを開始するか、起動中の対話CLIで次を入力します。

```text
/skills reload
/skills info lego-like-3d-print
```

これらは通常のOS shellコマンドではありません。`/skills info`で意図した配置先かを確認します。
**Copilot app:** コピーした対象プロジェクトで新しいセッションを開き、
「lego-like-3d-printを使って、まず基準と利用可能ツールを説明して」と依頼します。
appのコマンド候補は`/`で確認し、CLIの`/skills reload`が必ず使えるとは仮定しません。
[app公式コマンド一覧](https://docs.github.com/en/copilot/reference/github-copilot-app-reference/slash-commands)も参照できます。

<a id="updates"></a>
## 2. 既存スキルを壊さず更新する

新版を別の作業フォルダーへ展開し、`SKILL.md`・references・scriptsの差分を確認します。
既存の個人向け変更が必要なら、新版側へ手で統合してください。
旧フォルダーを**スキル探索先の外**（例: `~/skill-backups/2026-09-23/`）へ保管してから、
上記の「配置先がない場合だけコピー」を行います。バックアップ先も既存なら別名を使います。
`.copilot/skills`内で単に旧版を改名すると、同じnameのスキルが二重に見つかる恐れがあります。
CLIはreload、appは新しいセッションで再確認します。自動上書き・`rm -rf`は不要です。

<a id="freecad"></a>
## 3. FreeCADを導入する

入手先は[公式ダウンロード](https://www.freecad.org/downloads.php)と、
そこから辿れる[公式releases](https://github.com/FreeCAD/FreeCAD/releases/latest)です。
まず安定版を選び、初心者向け手順としてweekly/developmentを既定にしません。
ページの「最新」番号を固定せず、ダウンロードする版の要件とチェックサムを確認します。

| OS | インストールと起動 |
| --- | --- |
| macOS Apple Silicon | 「このMacについて」でチップを確認。対応するarm64のDMGを開き、FreeCAD.appをApplicationsへドラッグし、Finderから起動 |
| macOS Intel | Intel / x86_64用の対応DMGを選び、同様にインストール。Apple Silicon版を選ばない |
| Windows | 「設定 → システム → バージョン情報」でシステムの種類を確認。公式配布の対応installerを実行し、保存先を記録してスタートメニューから起動。配布にないnative ARM版をあると仮定しない |
| Linux | `uname -m`でCPUを確認し、対応する公式AppImageを保存。ファイルのプロパティで実行許可を与えて起動。ディストリビューションのパッケージは版が古い場合がある |

Linuxの例（`FreeCAD-downloaded.AppImage`は**実際に保存した名前に置換**）:

```sh
chmod +x ./FreeCAD-downloaded.AppImage
./FreeCAD-downloaded.AppImage
```

公式手順: [macOS](https://wiki.freecad.org/Installing_on_Mac) /
[Windows](https://wiki.freecad.org/Installing_on_Windows) /
[Linux](https://wiki.freecad.org/Installing_on_Linux) /
[AppImage](https://wiki.freecad.org/AppImage)。
OSが危険・署名不明などを警告した場合、AIへ回避させず、入手元・署名を確認して利用者が判断してください。

### バージョンと組込みPythonを確認

FreeCADを起動し、About FreeCAD（macOSはアプリメニュー、他OSは通常Help）で版を確認します。
**View → Panels → Python console**を表示し、次を1行ずつ実行します。文書は変更しません。

```python
import FreeCAD as App
import sys
print("FreeCAD:", App.Version())
print("Python:", sys.version)
print("Application home:", App.getHomePath())
print("FreeCAD module:", App.__file__)
print("Executable:", sys.executable)
```

これはFreeCAD内のPythonです。一般の`python` / `python3`やサイト用venvとは別で、
**`pip install FreeCAD`でアプリ導入を済ませることはできません**。

### 小さな安全確認

[freecad_smoke.py](../../.github/skills/lego-like-3d-print/scripts/freecad_smoke.py)を読み、
FreeCADのPython consoleから実行します。次のpathはダウンロード・コピーした**実ファイル**へ変更します
（Windowsのpathもraw文字列内へ入力できます）。

```python
from pathlib import Path
script = Path(r"REPLACE_WITH_FULL_PATH_TO/freecad_smoke.py")
exec(compile(script.read_text(encoding="utf-8"), str(script), "exec"), {"__name__": "__main__"})
```

またはMacro → Macrosで未使用名のマクロを作り、この小スクリプトを貼って実行できます。
既存マクロを上書きしないでください。
毎回新しい一時フォルダーへ8×8×3.2 mmの**test-only小箱**のFCStd / STEP / STLを作り、
再読込を確認します。既存文書を保存・閉じず、自分で作った確認文書だけを閉じます。
成功時は`FREECAD_SMOKE_OK`と出力場所が表示されます。
小箱にはスタッドも受けもなく、嵌合試験片や印刷キットではありません。

### AIからCLI・組込みinterpreterを使う場合

上のconsole出力を手掛かりに、インストール先の実在ファイルと`--help`を確認します。
`sys.executable`はGUI本体の場合もあり、常に外部実行用Pythonとは限りません。
macOSではFinderの「パッケージの内容を表示」や次の読取で確認できます。

```sh
ls "/Applications/FreeCAD.app/Contents/MacOS"
ls "/Applications/FreeCAD.app/Contents/Resources/bin"
```

Windowsは記録したインストール先の`bin`、LinuxはAppImageの起動方法または
`command -v FreeCADCmd freecadcmd freecad`で見つかる実ファイルを確認します。
名前・場所は配布方式で異なります。
対応interpreterでもFreeCAD moduleの探索pathが別途必要な場合があります。
macOSの上記構成で`Resources/lib/FreeCAD.so`を確認できた場合の例:

```sh
PYTHONPATH="/Applications/FreeCAD.app/Contents/Resources/lib" \
  "/Applications/FreeCAD.app/Contents/Resources/bin/python" \
  ".github/skills/lego-like-3d-print/scripts/freecad_smoke.py"
```

これはrepoルートからの例で、全OS共通の固定pathではありません。
Windowsの別PythonへmacOSのmoduleを渡すなど、版・CPU・ABIの異なる環境を混ぜないでください。
分からない場合はGUI console/マクロを使います。既存GUI作業を操作しない別プロセスを優先します。

<a id="blender"></a>
## 4. Blenderを導入する

[公式download](https://www.blender.org/download/)、
[requirements](https://www.blender.org/download/requirements/)、
[installation manual](https://docs.blender.org/manual/en/latest/getting_started/installing/index.html)を確認します。

| OS | 選び方と起動 |
| --- | --- |
| macOS Apple Silicon | 対応するApple Silicon DMG。アプリをApplicationsへドラッグして起動。Blender 5以降はApple Silicon・macOS 13以降が必要（選ぶ版の要件も確認） |
| macOS Intel | **Blender 4.5 LTSがIntel Macをサポートする最後の版**。[LTS](https://www.blender.org/download/lts/)から対応版を選ぶ。Blender 5以降を案内しない |
| Windows | CPUに合うx64 / arm64の公式installerかZIPを選ぶ。installerならスタートメニュー、ZIPなら展開した`blender.exe`から起動 |
| Linux | CPUに合う公式archiveを展開し、中の`blender`を起動。OS/GPU/ドライバー要件を確認。distribution版は機能や版が異なる場合がある |

公式OS別手順: [macOS](https://docs.blender.org/manual/en/latest/getting_started/installing/macos.html) /
[Windows](https://docs.blender.org/manual/en/latest/getting_started/installing/windows.html) /
[Linux](https://docs.blender.org/manual/en/latest/getting_started/installing/linux.html)。

**版間互換性:** 参照例のBlender 5.1.1保存済み`.blend`を4.5 LTSでそのまま再現できるとは保証しません。
このスキルに完成シーンは同梱していません。利用者の対応版で実STL等からシーンを作るのが基本です。
旧版を開くために元ファイルを上書きせず、版をまたぐ移行は別コピーで確認します。

起動したsplash / About Blenderで版を確認します。CLIでは実在する実行ファイルの`--version`でも確認できます。
未保存の既存シーンを消さないよう、以下は**別のbackgroundプロセス**で行います。
コマンドは展開したrepoルートからの例です。スキル単体ZIPやコピー済みスキルを使う場合、
`--python`の後を、その`blender_smoke.py`の実際のフルpathへ変更してください。

macOS（通常のインストール位置の例）:

```sh
"/Applications/Blender.app/Contents/MacOS/Blender" --version
"/Applications/Blender.app/Contents/MacOS/Blender" --background --factory-startup \
  --python-exit-code 1 --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

Windows PowerShell（`$blender`は実際に選んだインストール先へ置換）:

```powershell
$blender = "C:\PATH_TO_BLENDER\blender.exe"
& $blender --version
& $blender --background --factory-startup --python-exit-code 1 `
  --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

Linux（展開場所へ置換。PATHへ登録済みなら`command -v blender`で確認）:

```sh
BLENDER="./PATH_TO_EXTRACTED_BLENDER/blender"
"$BLENDER" --version
"$BLENDER" --background --factory-startup --python-exit-code 1 \
  --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

[blender_smoke.py](../../.github/skills/lego-like-3d-print/scripts/blender_smoke.py)は
8×8×3.2 mm相当の**test-only小箱**を新規sceneへ作り、
新しい一時フォルダーの`.blend`へ保存して再openします。レンダーは行いません。
`BLENDER_SMOKE_OK`が成功の目印です。foregroundでは変更前に停止します。
通常のsystem Pythonへ`bpy`をimportさせる手順ではありません。
[公式CLI引数](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html)も参照できます。

<a id="ai-tools"></a>
## 5. AIから使うための境界

スキルは「何をどう確認するか」を教えますが、実行権限を増やしません。
AIには、対象プロジェクトのファイルと、承認されたshellまたは対応CADツール接続が必要です。
GUIしか使えない場合は、AIが作ったコードを利用者が内容確認してconsole/マクロへ渡せます。
CLIが使える場合は、実在path・版を確認し、最初は上のsmokeだけを依頼してください。

MCPは**任意**です。このスキルのコピーで自動導入・設定・常駐はされません。
使用する場合は接続ツールの公式手順、権限、現在のschema、シーン状態を別途確認します。
スキルだけでFreeCADやBlenderが使えるようになったとは扱いません。

<a id="troubleshooting"></a>
## 困ったとき・確認の意味

| 症状 | 次に確認すること |
| --- | --- |
| スキルが見つからない | 正確な配置と`SKILL.md`の大文字、フォルダーの入れ子、探索先の重複、CLI reload / appの新しいセッション |
| `No module named FreeCAD` | system Pythonでなく対応環境か、`App.__file__`の場所とmodule path。闇雲にpipを追加しない |
| AppImageが起動しない | 実行許可、CPU、公式AppImageのFUSE要件とdistributionの手順。未保守PPAへ安易に切り替えない |
| Blenderが起動しない | CPU/OS/GPU/ドライバー要件、Intel Macの4.5 LTS制約、実行ファイルpath |
| `.blend`を旧版で再現できない | 元ファイルは保持し、その対応版で実メッシュから作り直す。新しい版の機能を旧版が読めると仮定しない |
| Smokeが途中で失敗 | エラー全文と使用版を確認。出力が一部あっても成功にしない。共有するログの個人pathを除去 |

公式手順を確認したことと、各OS・CPU・版で実行したことは別です。
小箱の生成・再open成功も、CGレンダー、モデル一式の製造、slice、実嵌合・保持力・転倒や互換性の合格ではありません。
使用環境ごとに試し、模型の次の段階は[使い方](usage.md#trial-gates)に沿って進めます。
