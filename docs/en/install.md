# Installation and your first check

[日本語](../ja/install.md) · [Usage](usage.md) · [Notices](notices.md)

[Requirements](#requirements) / [Skill](#skill-install) / [Updates](#updates) /
[FreeCAD](#freecad) / [Blender](#blender) / [AI connection](#ai-tools) / [Troubleshooting](#troubleshooting)

<a id="requirements"></a>
## Requirements depend on what you want to do

| Goal | What you need |
| --- | --- |
| Read documentation or view public 3D | A browser only; no skill installation required |
| Have the AI follow this workflow | An Agent Skills-capable GitHub Copilot app / CLI or other supported host, with folder access |
| Create real CAD, FCStd / STEP / STL | FreeCAD and its matching Python environment |
| Make mesh-derived CG, video or `.blend` | Blender on a supported OS/GPU |
| Convert or inspect MP4 | ffmpeg, only when required |
| Build a 3D website | Node.js or other tools only if the chosen toolchain requires them |
| Slice real print files | A slicer for your printer; Bambu Studio is an example for relevant machines |

This distribution is a **workflow skill**, not a complete model generator.
It does not bundle or automatically install CAD, finished scenes, reference
images, fonts or an MCP server. Review installations and permissions yourself.

The reference project's FreeCAD **1.1.3**, Blender **5.1.1** and ffmpeg **8.1** are
historical tool versions, not requirements or compatibility guarantees for every
OS. Select packages for your OS, CPU and GPU from official sources.
Blender support differs notably between Intel and Apple Silicon Macs.

<a id="skill-install"></a>
## 1. Copy the skill

The layout follows GitHub's official [Agent Skills guide](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
and [CLI skill installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills).
Skills contain instructions and code: read them before installing.
This skill does not grant blanket shell preapproval through `allowed-tools`.

**Download:** the [skill-only ZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip)
([SHA-256](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip.sha256)),
or **Code → Download ZIP** in the [repository](https://github.com/ktanino10/lego-like-3d-print-skill).
Extract first. In the full repository ZIP, the source folder is
`.github/skills/lego-like-3d-print`. To see hidden `.github`, use `Command+Shift+.`
in macOS Finder, `Ctrl+H` in many Linux file managers, or enable hidden items in
Windows File Explorer.

| Destination | Scope |
| --- | --- |
| `~/.copilot/skills/lego-like-3d-print` | Personal; on Windows, `.copilot\skills\lego-like-3d-print` under `$HOME` |
| `.github/skills/lego-like-3d-print` in your own repository | Project-specific |

Choose **one location** and copy the whole folder, including LICENSE, NOTICES,
references and scripts. Do not register separate Japanese/English `SKILL.md`
files or duplicate the same skill at both scopes. This distribution repository
already has its project skill installed in the correct location.

### Non-overwriting copy on macOS / Linux

Run this example **from the extracted repository root**. For the skill-only ZIP,
change `src` to `./lego-like-3d-print`. An existing destination stops the copy;
nothing is deleted or overwritten.

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

For a project install, set `dest` to that repository's `.github/skills/lego-like-3d-print`,
for example `dest="../my-model/.github/skills/lego-like-3d-print"`.
Verify the target repository before running.

### Non-overwriting copy in Windows PowerShell

Again, run from the extracted repository root. For the skill-only ZIP, change
`$source` to `./lego-like-3d-print`.

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

For project scope, change `$destination` to the location inside the target repo.
A file-manager copy is also fine; cancel any replacement prompt and follow the
update procedure instead.

### Load it in Copilot

**CLI:** Start a new session, or type these inside an existing interactive CLI:

```text
/skills reload
/skills info lego-like-3d-print
```

These are not OS shell commands. Check that `/skills info` reports the intended
location. **Copilot app:** Open a new session in the target project after copying,
then ask "Use lego-like-3d-print; first explain the baseline and available tools."
Type `/` to inspect the app's actual command picker; do not assume the CLI's
`/skills reload` is available there. See the
[official app command reference](https://docs.github.com/en/copilot/reference/github-copilot-app-reference/slash-commands).

<a id="updates"></a>
## 2. Update without destroying an existing skill

Extract the new version into a separate staging folder. Review differences in
`SKILL.md`, references and scripts; manually integrate any personal changes into
the staged version. Preserve the old folder **outside skill discovery locations**
(for example `~/skill-backups/2026-09-23/`), then use the guarded copy above once
the destination is absent. Choose a different backup name if it already exists.
Merely renaming the old folder inside `.copilot/skills` can expose two skills
with the same name. Reload in the CLI or start a new app session. No automatic
overwrite or `rm -rf` is needed.

<a id="freecad"></a>
## 3. Install FreeCAD

Use the [official downloads](https://www.freecad.org/downloads.php) and linked
[official releases](https://github.com/FreeCAD/FreeCAD/releases/latest).
Start with a stable release, not a weekly/development build. Check the chosen
release's requirements and checksums rather than relying on a permanently
hardcoded "latest" version number.

| OS | Installation and launch |
| --- | --- |
| macOS Apple Silicon | Check the chip in About This Mac. Open the matching arm64 DMG, drag FreeCAD.app to Applications and launch from Finder |
| macOS Intel | Choose a supported Intel / x86_64 DMG and install the same way; not the Apple Silicon build |
| Windows | Check System type in Settings → System → About. Run an officially offered compatible installer, record its location and launch from Start. Do not assume a native ARM package exists if not offered |
| Linux | Check CPU with `uname -m`, download the matching official AppImage, allow execution in its file properties and launch it. Distribution packages may lag behind |

Linux example: **replace** `FreeCAD-downloaded.AppImage` with the actual filename.

```sh
chmod +x ./FreeCAD-downloaded.AppImage
./FreeCAD-downloaded.AppImage
```

Official instructions: [macOS](https://wiki.freecad.org/Installing_on_Mac) /
[Windows](https://wiki.freecad.org/Installing_on_Windows) /
[Linux](https://wiki.freecad.org/Installing_on_Linux) /
[AppImage](https://wiki.freecad.org/AppImage).
If the OS warns about unsafe or untrusted software, do not ask the AI to bypass
the warning. Verify provenance/signing and make the decision yourself.

### Confirm version and embedded Python

Launch FreeCAD and check About FreeCAD (the application menu on macOS, usually
Help elsewhere). Show **View → Panels → Python console** and enter these lines
one at a time. They do not change documents.

```python
import FreeCAD as App
import sys
print("FreeCAD:", App.Version())
print("Python:", sys.version)
print("Application home:", App.getHomePath())
print("FreeCAD module:", App.__file__)
print("Executable:", sys.executable)
```

This is FreeCAD's Python, not necessarily your system `python` / `python3` or
the site's venv. **`pip install FreeCAD` is not a substitute for installing the app.**

### A safe small check

Review [freecad_smoke.py](../../.github/skills/lego-like-3d-print/scripts/freecad_smoke.py),
then run it from the FreeCAD Python console. Replace the path below with the
**actual downloaded/copied script** (Windows paths can go in the raw string too).

```python
from pathlib import Path
script = Path(r"REPLACE_WITH_FULL_PATH_TO/freecad_smoke.py")
exec(compile(script.read_text(encoding="utf-8"), str(script), "exec"), {"__name__": "__main__"})
```

Alternatively, create a macro with an unused name through Macro → Macros, paste
this small script and run it. Do not overwrite an existing macro.
Each run creates a **test-only 8×8×3.2 mm box**, saves FCStd / STEP / STL into a
new temporary folder and checks reopening. It does not save or close your existing
documents; it closes only its own test documents. Success prints
`FREECAD_SMOKE_OK` and the output location. This box has no studs or sockets;
it is not a fit coupon or print kit.

### CLI or embedded interpreter access from the AI

Use the console output above to locate actual installed files and inspect their
`--help`. `sys.executable` may point to the GUI itself, not a standalone Python.
On macOS use Finder's Show Package Contents, or these read-only listings:

```sh
ls "/Applications/FreeCAD.app/Contents/MacOS"
ls "/Applications/FreeCAD.app/Contents/Resources/bin"
```

On Windows inspect `bin` under your recorded installation location. On Linux
use the AppImage's supported launch route or actual files discovered by
`command -v FreeCADCmd freecadcmd freecad`. Names and locations vary by package.
Even a matching interpreter can require the FreeCAD module search path.
For the macOS layout above, **after confirming** `Resources/lib/FreeCAD.so` exists:

```sh
PYTHONPATH="/Applications/FreeCAD.app/Contents/Resources/lib" \
  "/Applications/FreeCAD.app/Contents/Resources/bin/python" \
  ".github/skills/lego-like-3d-print/scripts/freecad_smoke.py"
```

This example runs from the repository root; it is not a universal OS path.
Do not mix Python versions, CPU architectures or ABIs, such as a macOS module
with another Windows Python. Use the GUI console/macro if unsure. Prefer a
separate process that does not operate on your existing GUI work.

<a id="blender"></a>
## 4. Install Blender

Read the [official download page](https://www.blender.org/download/),
[requirements](https://www.blender.org/download/requirements/) and
[installation manual](https://docs.blender.org/manual/en/latest/getting_started/installing/index.html).

| OS | Choose and launch |
| --- | --- |
| macOS Apple Silicon | Matching Apple Silicon DMG; drag the app to Applications. Blender 5+ requires Apple Silicon and macOS 13+; check the selected version too |
| macOS Intel | **Blender 4.5 LTS is the last release supporting Intel Macs.** Choose the matching [LTS](https://www.blender.org/download/lts/) package, not Blender 5+ |
| Windows | Match x64 / arm64 to your CPU. Use the official installer or ZIP; launch from Start or the extracted `blender.exe` |
| Linux | Extract the official archive for your CPU and run its `blender`. Check OS/GPU/driver requirements; distribution packages may differ in version/features |

Official OS instructions: [macOS](https://docs.blender.org/manual/en/latest/getting_started/installing/macos.html) /
[Windows](https://docs.blender.org/manual/en/latest/getting_started/installing/windows.html) /
[Linux](https://docs.blender.org/manual/en/latest/getting_started/installing/linux.html).

**Cross-version compatibility:** A reference scene saved in Blender 5.1.1 is not
guaranteed to reproduce unchanged in 4.5 LTS. This skill bundles no finished
scenes. Normally, build a scene from the real STL/meshes in your supported
Blender version. Keep originals and test migrations on separate copies.

Check the splash screen / About Blender, or use `--version` on the actual
executable. Run the following in a **separate background process** so an existing
unsaved interactive scene is not erased.
These examples run from the extracted repository root. With the skill-only ZIP
or an installed copy, replace the argument after `--python` with the actual full
path to that copy's `blender_smoke.py`.

macOS, using the usual installation location:

```sh
"/Applications/Blender.app/Contents/MacOS/Blender" --version
"/Applications/Blender.app/Contents/MacOS/Blender" --background --factory-startup \
  --python-exit-code 1 --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

Windows PowerShell: replace `$blender` with your actual installation path.

```powershell
$blender = "C:\PATH_TO_BLENDER\blender.exe"
& $blender --version
& $blender --background --factory-startup --python-exit-code 1 `
  --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

Linux: use the extracted location, or locate a PATH installation with `command -v blender`.

```sh
BLENDER="./PATH_TO_EXTRACTED_BLENDER/blender"
"$BLENDER" --version
"$BLENDER" --background --factory-startup --python-exit-code 1 \
  --python ".github/skills/lego-like-3d-print/scripts/blender_smoke.py"
```

[blender_smoke.py](../../.github/skills/lego-like-3d-print/scripts/blender_smoke.py)
creates a **test-only box equivalent to 8×8×3.2 mm** in a new scene, saves a `.blend`
in a new temporary folder and reopens it. It does not render. Look for
`BLENDER_SMOKE_OK`. It refuses a foreground instance before changing anything.
This is not a system-Python `bpy` installation procedure. See the
[official CLI arguments](https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html).

<a id="ai-tools"></a>
## 5. What the AI needs to execute

The skill explains what to do and check; it does not extend permissions.
The AI needs access to project files and a permitted shell or compatible CAD
tool connection. With GUI-only access, you can review AI-generated code and
run it yourself through the console/macro. With CLI access, identify real paths
and versions and ask for only the smoke check first.

MCP is **optional**. Copying this skill does not install, configure or start a
server. If you use one, separately review the connector's official setup,
permissions, current schema and live scene state. Installing the skill alone
does not make FreeCAD or Blender executable.

<a id="troubleshooting"></a>
## Troubleshooting, and what a check actually proves

| Symptom | Check next |
| --- | --- |
| Skill not found | Exact location, uppercase `SKILL.md`, nested folders, duplicate scopes, CLI reload / new app session |
| `No module named FreeCAD` | Matching environment rather than system Python, `App.__file__` and module path; do not install random pip packages |
| AppImage will not launch | Execute permission, CPU, official FUSE requirements and distribution guidance; do not blindly switch to an unmaintained PPA |
| Blender will not launch | CPU/OS/GPU/drivers, Intel Mac's 4.5 LTS limit and executable path |
| Older Blender cannot reproduce a `.blend` | Preserve the original and rebuild from actual meshes in the supported version; do not assume newer features work in older releases |
| Smoke script fails partway | Read the error and versions; partial output is not success. Remove personal paths before sharing logs |

Reviewing official instructions is different from executing them on every
OS/CPU/version. A box generation/reopen pass is not a render, complete-model
manufacturing, slicing, fit/retention/tipping test or compatibility guarantee.
Check your own environment, then follow the [physical trial gates](usage.md#trial-gates).
