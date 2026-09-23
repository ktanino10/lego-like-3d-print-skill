# lego-like-3d-print-skill

**An unofficial creation-support skill intended for personal hobbies and learning. It does not imply official provision or endorsement by any company, or guarantee compatibility or fabrication results.**

[日本語](README.md) · [English site](https://ktanino10.github.io/lego-like-3d-print-skill/en/) · [日本語サイト](https://ktanino10.github.io/lego-like-3d-print-skill/ja/)

A GitHub Copilot skill for designing brick-style models as genuinely separable,
assemblable parts on an 8 mm pitch. It connects real FreeCAD geometry to print
documentation, Blender renders/assembly video, interactive 3D guides and approved
GitHub Pages publication through **the same meshes, placements and part IDs**.

**Purpose is different from permission.** The original skill, documentation and
scripts use [MIT](LICENSE), which also allows commercial use. "For hobbies and
learning" describes intent, not a personal-use-only or noncommercial condition.
This does not relicense external works, photos, logos, trademarks, fonts,
FreeCAD or Blender. Read the [notices](NOTICES.md).

## Start here

1. **[Installation](docs/en/install.md)** — Safe skill copying, FreeCAD and Blender on macOS / Windows / Linux, and a tiny first check.
2. **[Usage and prompts](docs/en/usage.md)** — What to ask the AI for, expected artifacts and physical trial gates.
3. **[Real examples and evidence](docs/en/examples.md)** — Two public projects; renders, designs and physical reports kept distinct.

Download the [skill-only ZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip)
or use this repository's **Code → Download ZIP**, extract it and review the contents.
Copy the entire [skill folder](.github/skills/lego-like-3d-print/) to **either**
`~/.copilot/skills/lego-like-3d-print` (personal) or
`.github/skills/lego-like-3d-print` in your own repository (project).
Use the [non-overwriting installation steps](docs/en/install.md#skill-install).

In the CLI, start a new session or run `/skills reload` in an existing session,
then `/skills info lego-like-3d-print`. In the Copilot app, open a new session for
the target project after copying. Do not assume CLI slash commands exist in the app.

```text
Use /lego-like-3d-print to make a cat as an 8 mm-pitch brick-style desktop model.
Start with one proposal, a small fit trial and representative parts.
Save in this project. Use the real CAD geometry for renders and assembly guides.
Do not publish or proceed to a full production print yet.
```

## Included, and deliberately not included

| Included | Not included |
| --- | --- |
| One `SKILL.md`, English/Japanese baseline and workflow, MIT/notices | A complete model generator, CAD models or source-project images/photos |
| Bilingual installation, usage, examples, notices and static site | FreeCAD / Blender binaries, fonts or automatic MCP installation/startup |
| Test-only smoke scripts creating a small box in a new temporary folder | Sliced print files, printer settings or Send/Print automation |

You do not need CAD applications to read the skill or view public 3D guides.
Real CAD generation needs FreeCAD; mesh-based renders/video need Blender and a
permitted shell or compatible tool connection. The skill recognizes English and
Japanese requests and responds in the requester's language. The default is one
subject, one proposal. Resize by changing block counts/layout, not by scaling
an entire finished STL.

## Baseline and physical evidence

The baseline is 8.0 mm pitch, 9.6 mm bodies, 3.2 mm plates, studs 4.8 mm in diameter
and 1.8 mm high, a total 0.2 mm body gap and female **radial** clearance +0.04 mm.
See the [self-contained baseline](.github/skills/lego-like-3d-print/references/baseline.md).

Reference B is 191.8×80.2×238.6 mm / 150 parts / 28 steps, not a fixed target for
new work. The 2026-09-23 physical report covers **B's base and front only**.
The full face/assembly and measured retention, strength and tipping remain
unverified. Geometry 3MF is **NOT_SLICED**, not a configured P1S project.

[Website](https://ktanino10.github.io/lego-like-3d-print-skill/en/) ·
[Important notices](docs/en/notices.md) ·
[Rebuild and validate the site](CONTRIBUTING.md)
