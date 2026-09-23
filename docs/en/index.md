# Build in blocks. Connect design to assembly.

**An unofficial creation-support skill intended for personal hobbies and learning. It does not imply official provision or endorsement by any company, or guarantee compatibility or fabrication results.**

Design brick-style models on an 8 mm pitch as parts you can actually separate,
print and assemble. This GitHub Copilot skill connects real FreeCAD geometry,
print parts, Blender renders, BOMs and assembly guides through the same data.

[Get started](install.md) · [See example prompts](usage.md) · [Explore public projects](examples.md)

<a id="overview"></a>
## A workflow for making, not a bundled model generator

| What the skill helps produce | What matters |
| --- | --- |
| FreeCAD solids, FCStd, STEP and STL | Open undersides, tubes/ribs and truly separate parts |
| Color-grouped geometry 3MF, BOMs and step diagrams | Traceable links from a printed file to its assembly position |
| Blender renders, assembly video and interactive 3D | The same real meshes, placements and steps |
| Approved project publication on GitHub Pages | Permission, sources, live delivery and evidence boundaries |

No complete model generator or CAD application is included. The AI reads the
workflow and performs the necessary design/generation work in your project.
You do not need FreeCAD or Blender just to read the skill or view public 3D guides.

<a id="start"></a>
## Start small

1. [Copy the skill](install.md#skill-install) and start a new session.
2. [Prepare FreeCAD and Blender](install.md#freecad); check the environment with a test-only box.
3. [Describe your subject and output location](usage.md#first-request). Default: one subject, one proposal.
4. Test fit and representative parts, then base/front, then the body. Do not commit to a full print before physical checks.

[Skill-only ZIP](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip) ·
[SHA-256](https://ktanino10.github.io/lego-like-3d-print-skill/downloads/lego-like-3d-print.zip.sha256) ·
[Skill source on GitHub](../../.github/skills/lego-like-3d-print/SKILL.md)

<a id="baseline"></a>
## An 8 mm baseline is not a physical certification

Pitch 8.0 mm, body 9.6 mm, plate 3.2 mm. Stud diameter 4.8 mm and height 1.8 mm;
total body gap 0.2 mm; female **radial** clearance +0.04 mm.
Stack at 9.6 mm and never resize by globally scaling a finished STL.

Reference B is 191.8×80.2×238.6 mm, 150 parts and 28 steps.
The 2026-09-23 physical report covers the base/front only, not the face/full
assembly or measured retention, strength or tipping. Geometry 3MF is
**NOT_SLICED**. See the [examples' evidence boundaries](examples.md).

<a id="rights"></a>
## Intent and license permission are different

Although intended for hobbies and learning, the original skill documents and
scripts are **MIT licensed, including permission for commercial use**.
There is no additional noncommercial or personal-use-only restriction. External
works, photos, logos, trademarks, fonts and applications have separate rights.
[Notices](notices.md) · [Full MIT license](../../LICENSE)
