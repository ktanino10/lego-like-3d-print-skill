---
name: lego-like-3d-print
description: >-
  Design brick-style, physically separable 3D-printable models on an 8 mm pitch
  with FreeCAD, print files, BOMs, assembly guides, Blender renders/animation,
  and optional GitHub Pages. Use for "make it brick-style", "LEGO-like model",
  "レゴっぽく作って", "レゴ風", "ブロック風の3Dプリント模型", matching a previous
  block size, sorting printed parts, or improving plaques and lettering.
  Not for buying commercial LEGO sets or electronics-only design.
license: MIT
compatibility: >-
  GitHub Copilot with access to the project filesystem. Manufacturing outputs
  require a working FreeCAD environment; Blender outputs require Blender.
  A permitted shell or compatible CAD tool connection is needed for execution.
  Publishing requires an explicitly authorized destination.
---

# Brick-style 3D printing / ブロック風3Dプリント制作

An unofficial creation-support skill intended for personal hobbies and learning.
It does not imply official provision or endorsement by any company, or guarantee
compatibility or fabrication results. MIT permits commercial use too; this
statement of intent is not an additional license restriction. Read [LICENSE](LICENSE)
and [NOTICES](NOTICES.md).

個人の趣味・学習を目的とした非公式の制作支援スキルです。
各社の公式提供・推奨や、互換性・造形結果の保証を示すものではありません。
これは趣旨の説明であり、商用利用も認めるMITの許可を制限しません。

**Respond in the requester's language.** Use Japanese for a Japanese request and
English for an English request, including guides and explanations. Do not register
a second translated skill. This folder contains instructions, references and two
small environment tests, **not a complete model generator**, CAD applications,
printer settings, or an automatically installed MCP server.

## Read first

| Resource | English | 日本語 |
| --- | --- | --- |
| Dimensions, evidence and fixed sources | [Baseline](references/baseline.md) | [基準資料](references/baseline.ja.md) |
| Design-to-publication workflow | [Workflow](references/workflow.md) | [制作手順](references/workflow.ja.md) |
| Installation and safe first run | [Online guide](https://ktanino10.github.io/lego-like-3d-print-skill/en/install/) | [導入ガイド](https://ktanino10.github.io/lego-like-3d-print-skill/ja/install/) |

The core dimensions and workflow above remain available when only this folder is
copied. Reference images are **external links**, not bundled assets:
[B digital render](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/media/B-hero.png),
[print-to-assembly diagram](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/assembly-guide/media/B-first-base.png).
Use parameter data and actual CAD for dimensions, not visual estimates.

## 1. Keep the interface; adapt the subject

- Start with 8.0 mm pitch, 9.6 mm body height, 3.2 mm plates, nominal studs
  4.8 mm in diameter and 1.8 mm high. The 0.2 mm body gap is **total**, not per
  side. Female +0.04 mm clearance is **radial**, not diametral.
- Use top studs and **open undersides with walls, tubes and ribs**. Prefer
  reusable 2×2 and 2×4 parts to many tiny custom pins.
- Stack at 9.6 mm, not the 11.4 mm stud-inclusive height. Resize by changing
  block counts and layout, never by globally scaling a finished STL.
- A useful desktop reference is B's 191.8×80.2×238.6 mm assembled envelope.
  Its base alone is 191.8×79.8 mm and five layers / 48 mm high. A five-layer
  base, plaque or logo is optional, not compulsory for every subject.
- Default to **one subject, one proposal**, not the reference's A/B/C set.
  Choose subject, color and wording for this request; do not copy a mascot,
  brand mark, personal inscription or profile URL by default.
- Respect explicit limits such as "design only", "images only", or "do not
  publish". A request to edit or explain this skill does not authorize making
  models or publishing anything.

## 2. Confirm only consequential unknowns

Clarify the subject, use, scale, separable versus one-piece construction, optional
plaque, output location and publication scope only where missing. Distinguish
relief from a fully three-dimensional object, and "one print plate" from
"one fused model". Ask one focused question at a time using the host's question
tool when available. Do not re-ask known facts.

Reference repositories are read-only teaching sources, not output destinations.
Work in the designated project. Obtain approval for the exact repository,
visibility and content before creating or publishing a repository. Do not expose
another project's history, photographs or private data.

## 3. One manufacturing definition for all outputs

1. Track revision, parameters, part IDs, colors, quantities, instance IDs,
   placements, connections, print slots and steps in machine-readable data.
   Reuse the project's existing schema and generators where appropriate.
2. Create real FreeCAD solids and native FCStd; export STEP and mm-intended STL,
   then independent-part geometry 3MF layouts. A solid with drawn seams is not
   an assembly kit.
3. Use **the same meshes, placements and steps** for Blender, browser views,
   drawings, BOMs and instructions. No render-only lettering or connections.
4. Check geometry, support, staggered seams, insertion paths and hand access.
   Plaques must remain removable if replacement is promised.
5. Start with a loose fit coupon and a few production-representative parts.
   Proceed to base/front, then the remaining body only after physical feedback.

Follow the workflow reference for evidence and output checks. Never fake native
files by renaming extensions or substitute an imagined image for a mesh-derived
render. State which outputs are missing if a required tool cannot run.

## 4. Explain where each printed part goes

**Print order is not assembly order.** Preserve this bidirectional chain:

`print file → plate slot → part ID + color → assembly instance → step, position, orientation`

Show all eligible sources for interchangeable parts of the same type and color.
Regenerate the mapping from the new model's manifest; B's file names, 150 parts
and 28 steps are not defaults for a new model.

Provide numbered steps, added parts, quantities, insertion directions and
front/back/top/underside views. A 3D guide should start from an empty table,
support back/next/play/pause and highlight the current part. Separate print
layouts from assembly layouts; include static/PDF guidance and an offline ZIP
when requested.

## 5. Preserve the lessons and their limits

- Do not reintroduce the old 4 mm trial's tiny pins or treat its blocked holes
  and correction values as results for the independent 8 mm B design.
- Inspect cavities, first-layer openings, roof bridges, slots and thin walls
  in actual slicer previews as well as CAD. Do not diagnose flow, temperature
  or nozzle size from a photograph alone.
- For B-style lettering, keep the black carrier at 2.4 mm; white relief is
  1.2 mm, not the old 0.8 mm. Lower-line ink height is 10 mm. Test actual
  counters, open apertures, spacing and positive stroke widths at full size.
- "Thicken white only" must not alter the carrier or mounts. Identify changed
  parts and required reprints; preserve unrelated parts and keep revisions
  distinct.
- Separate reported progress, photographic observations, CAD checks and
  measured physical results. The reported B base/front build is not proof
  of all 150 parts, fit strength, durability or tipping safety.

## 6. Tools, publishing and handoff

Discover available tools and their schemas before using them. MCP is optional
and is neither installed nor started by this skill. Do not install applications,
dependencies or servers without appropriate user authorization.

The optional [FreeCAD smoke script](scripts/freecad_smoke.py) runs in FreeCAD's
matching Python environment and writes only to a newly created temporary folder.
The [Blender smoke script](scripts/blender_smoke.py) refuses a foreground instance;
run it in a separate background process. These make simple **test-only boxes**,
not blocks, fit coupons or printable kits. Do not modify unsaved CAD documents
or a user's live Blender scene.

Publish only approved content. Check the deployed URL, repository subpath,
downloads and desktop/mobile operation, not just CI status. Do not change
visibility, buy a plan or transfer data elsewhere to work around a restriction.
For model outputs label geometry-only files **NOT_SLICED**; a geometry 3MF is
not a P1S-configured project with verified pauses or G-code.

Hand off actual files and URLs, dimensions/counts, the first small trial and
remaining uncertainties. Never claim unperformed OS tests, slicing, full physical
assembly or compatibility certification. **Do not Send/Print to a printer.**
