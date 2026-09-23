# From design to an inspectable, buildable kit

[日本語](workflow.ja.md) · [Skill](../SKILL.md) · [Baseline](baseline.md)

This is a quality workflow, not a bundled generator or a requirement to create a
large system every time. Respect exclusions in the request; reuse suitable
existing project tooling. Do not clone an entire reference project and execute
it as a new model.

## 1. Scope and revision

Record subject, purpose, size, colors, optional plaque, separable versus one-piece
construction, output location and publication permission. Default to one 8 mm
desktop design with separable, glue-free blocks if not otherwise specified.
Clarify consequential ambiguity (relief versus full 3D, for example), not every
known parameter. Do not silently add electronics, magnets, hardware or purchases.

For an existing work, record the prior parameters, placements and part hashes;
separate changed parts, unchanged parts and affected documentation/renders.
Lettering changes must not redesign an unrelated body. Preview from the actual
manufacturing geometry and identify later appearance changes.

## 2. Shared machine-readable data

Use JSON/CSV or the project's equivalent; these are logical records, not a
requirement for one file per row.

| Record | Necessary information |
| --- | --- |
| Parameters | Revision, mm units, pitch, heights, studs, roofs, clearances, colors, subject dimensions |
| Part catalog | Stable part ID, geometry parameters, actual bounds, print orientation, STL path/hash |
| Assembly | Instance ID, part ID, color, position in mm, rotation convention, step/layer, role, neighbors |
| BOM | Quantity per type/color/finish, files, color-change conditions; coupons separated |
| Print plate | File, ordered slot, part/color, placement/rotation, quantity, required margins |
| Steps | Number, added instance IDs, parts, insertion direction, previous state, cautions |
| Evidence | Design version, generation conditions, checks, digital/physical distinction, file hashes |

Share repeated meshes, but retain every print quantity and assembly instance.
White plaque relief is a finish, not another installed part on top of the carrier.
One part type does not mean one printed copy.

The fixed source has files such as `design/parameters.json`,
`scripts/freecad_geometry.py` and `scripts/legible_metrics.py`. They are **external
reference files**, not scripts supplied here or automatically present in a new
project. Check rights before reusing source code.

## 3. Real CAD and assembly paths

Use FreeCAD BRep solids and FreeCAD's matching Python environment. Do not assume
system Python can import FreeCAD; do not prescribe `pip install FreeCAD`.
Preserve unsaved user documents. Prefer a separate process for automation.

Model open undersides, tubes/posts/ribs, roofs, stud lead-ins and any base slots
as real solids. Stagger vertical seams and bridge lower base joins. Check support,
insertion paths, plaque removal and finger access, not just final positions.
A convincing exploded render does not establish assemblability.

Check valid solids, intended solid counts, positive volume, finite vertices,
units and bounds; watertight/manifold meshes, normals and degenerate faces;
agreement between FCStd/STEP/STL; unintended volumetric interference; connection
and support continuity; intermediate insertion/removal states; print orientation,
bed contact, openings, bridges, thin walls and brim clearance. Save and reopen
FCStd, including relative external dependencies if any.

Document justified contact/intentional interference. Do not hide all collisions
behind a broad tolerance. CAD-volume center of mass is not sliced mass or a
measured tipping test.

## 4. Print kit and trial gates

Package type-level STL intended as mm, FCStd/STEP, separate-part color-grouped
geometry 3MF, small coupons, BOM, drawings/PDF and assembly data. 3MF needs units,
names, counts and correct transforms; a fused whole is not a parts kit.
Label geometry-only files **NOT_SLICED**. They are not printer-configured P1S
projects, verified pauses or G-code. STL carries no unit metadata: explain
mm / 100% import, extracting ZIPs first, and **not importing both STL and 3MF
copies of the same parts**.

The reference used Bambu Lab P1S / PLA, nominal build space 256×256×256 mm.
Check **each printed part and layout**, real plate exclusions, brim and
toolpaths, not only the final assembly size. A 0.4 mm body nozzle or 0.2 mm
lettering nozzle is merely a candidate: verify installed nozzle, machine,
material/color, plate and profile. Do not infer temperature, speed, flow or
layer height from photos.

Trial order:

1. One loose fit-coupon pair; small lettering/slot coupons where relevant.
2. A few real production parts, e.g. two 2×2 and two 2×4 blocks.
3. Relevant base ends/keepers. B used two ends and one keeper with those four
   blocks for a seven-part stage; do not add nonexistent parts to a new model.
4. The actual base and front modules; check full-width warping, alignment,
   retention and replacement.
5. Remaining body in small batches; repeat checks after material/color/nozzle changes.

Inspect first-layer entry openings, unwanted cavity supports/brims, the first
roof bridge, missing studs/ribs/text in **actual layer previews**. Stop for
blocked holes, parts that cannot be held or seated, strong force/tools,
whitening, cracking or poor retention. Do not normalize drilling every part or
forcing a fit. Report time/mass only from actual slicing.

Keep slicer-specific projects separate; check personal paths/settings before
publication. For two-color relief use separate plates and the actual black-to-white
boundary: B text z=2.4, logo z=2.8. Pause before the first white toolpath, not at
an invented fixed layer. A manual change may avoid AMS, but is not preconfigured
or verified unless actually checked. No printer connection, Send or Print.

## 5. Printed part to assembly location

Provide a clear starting page in the user's language: what to download, the
first small trial and how to assemble. Derive dimensions/sections from CAD and
numbered placement drawings from the catalog.

Each step shows added IDs, colors, counts, orientation and insertion direction,
distinct from completed parts. Define front/back/top/underside, especially front
slots. Derive a feasible sequence for this subject; do not blindly reuse B's
base → front → keeper → face order.

Build a bidirectional mapping:
`file → ordered slot → part ID + color → instance ID → step, position, orientation`.
Verify slot order/transforms against actual 3MF, match all print and assembly
counts, and show all eligible sources/locations for interchangeable same-type,
same-color parts. An example assignment is not an engraved serial number.
Plate numbers are not step numbers or base-layer numbers; explain differences
if a user rearranges a plate.

Include machine-readable source data. Keep revision, names and quantities
consistent across text, PDF, website and 3D guide. Explain disassembly and plaque
replacement where relevant.

## 6. Blender CG and animation

Import the distributed meshes with the same instances and transforms.
If converting mm to m, apply **0.001 once**, then check bounds. Inspect front
three-quarter, front, side, rear and exploded views. Text and logos must be
manufactured geometry, not render-only images masquerading as printable relief.

Deliver requested mesh-derived PNGs, editable/reopenable `.blend`, and an
assembly-sequence MP4 with readable IDs/steps. B's 1080×1200 render is a reference,
not a mandatory canvas. Prioritize a followable sequence over duration. A zoomed
still image is not assembly animation; a browser STL video is not a Blender
render. If using H.264/yuv420p and faststart, verify real decoding and sample frames.

Read scene state before any live MCP edits. A separate background Blender process
avoids erasing an unsaved interactive scene. Limit heavy parallel renders in a
shared environment. The small bundled smoke scripts are not render or manufacturing
validation.

## 7. Interactive and offline guide

Provide orbit/zoom, assembly/layer/step selection, part selection, BOM and exploded
amount. Include empty-table reset, first-part preview, back/next, play/pause,
replay, faded completed parts and front/side/top/back/underside views.
Display file, slot, part ID, instance and step while playing.

Distinguish step zero from first-part preview and current from completed parts.
Do not advance unnoticed in a hidden tab. Exploded 0% must restore exact
placements; fit the camera/clipping to the full spread. Use per-part bounds and
transforms rather than rebuilding all vertices each frame. Surface loading
errors instead of displaying an empty or stale success state.

If an offline ZIP is promised, aim for opening `index.html` without CDN, login
or server dependencies. Bundle permitted dependencies/notices and account for
`file://` fetch restrictions. Test it genuinely offline; HTTP success is not an
offline result.

## 8. Publication

An agreed complete model site includes description, actual renders, dimensions,
counts/colors/revision, 3D/video, downloads, print/assembly guidance, BOM/drawings,
trial history, evidence limits and rights notices.

Confirm owner/repository, visibility and content. Do not overwrite the reference
project or expose private history. Inspect source and generated text meshes,
images, videos, ZIPs and metadata for identifying information. A private source
does not make a public output private. Only publish specifically authorized
photos; remove identifying pixels/metadata rather than hiding them with CSS.
Past photo permission does not authorize reposting to another service.

Deploy only the intended static directory using the project's workflow.
Exclude CAD caches, environments, dependencies, render-frame sequences, secrets
and private logs. Use repository-subpath-safe URLs, not root-fixed `/assets/...`.
Respect approval boundaries for pushes, configuration and publishing; do not
change visibility or pay for a plan to bypass a blocker.

## 9. Evidence before completion

| Stage | Required evidence |
| --- | --- |
| CAD | Native reopen; dimensions/units; solids/meshes; connections/insertion paths |
| Quantities | BOM = instances = actual 3MF slots = instructions/UI |
| Appearance | Renders/video/viewer use the same current manufacturing geometry |
| Print pack | Orientation, units, quantities, revision, trial files and NOT_SLICED |
| Browser | Actual desktop and about 375 px mobile operation; no console errors |
| Exploded view | 0/50/100%, framing, display paths, exact return, part selection |
| Offline | Extracted ZIP actually works without a network at a file URL |
| Published | Live GETs, representative download size/hash, links/media/subpath |
| Physical | Report, photo observation and measured conditions recorded separately |

Say which checks were not run. Static checks do not replace a real browser,
CAD runtime, slicing or physical trials. A URL is not "published" until served.
Update affected hashes/assets when geometry changes and prove unchanged parts
remain unchanged. Digital completion and physical acceptance are distinct.
