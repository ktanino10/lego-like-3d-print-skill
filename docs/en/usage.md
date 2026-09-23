# Usage: start small and keep the data connected

[日本語](../ja/usage.md) · [Installation](install.md) · [Baseline](../../.github/skills/lego-like-3d-print/references/baseline.md)

<a id="first-request"></a>
## A first request

```text
Use /lego-like-3d-print to make a cat as an 8 mm-pitch brick-style desktop model.
One subject, one proposal; separate glue-free parts. Save in this project.
First make a concept, one fit-coupon pair and real 2×2 / 2×4 representative parts.
Use the real FreeCAD meshes for renders and assembly guidance.
Distinguish missing outputs, NOT_SLICED and physically unverified work.
Do not publish or send anything to a printer.
```

Describe subject, use/size, separate versus one-piece construction, optional
plaque, output location and publication scope. You need not specify everything;
the AI should ask only about consequential missing choices. Distinguish "all
together" as a fused print from separate parts on the same plate.
New geometry/code is created in your project; this skill contains no complete generator.

<a id="workflow"></a>
## What to expect

| Stage | Expected artifacts and decisions |
| --- | --- |
| Specification/data | Revision, dimensions, type IDs, colors, quantities, instances, transforms, connections/steps |
| Real design | Valid FreeCAD solids, reopenable FCStd, STEP and STL intended as mm |
| Print kit | Separate-part geometry 3MF, small coupons, type/color BOM, orientation and instructions |
| Assembly | Numbered steps, insertion directions, parts, print-slot mapping, drawings/PDF |
| Appearance | Blender renders, `.blend` and requested assembly MP4 from the same meshes/placements |
| 3D/publication | Requested interactive guide/offline ZIP; public site only when authorized |

Respect limits such as "design only", "no video" or "do not publish".
Render-only text/connections and a single solid with drawn seams are not an
assembly kit. If FreeCAD/Blender cannot run, report the missing outputs;
never fake them by changing file extensions.

<a id="mapping"></a>
## From the part you printed to where it belongs

`print file → slot → part ID + color → assembly instance → step, position, orientation`

Same-type/same-color parts are interchangeable; show all source plates and
eligible positions. Print order differs from assembly order. Plate numbers also
differ from base-layer numbers. For B only, `B-black-02.3mf` slot 3 → `B-001`;
all five base layers need the relevant parts from black 01–04.
Do not paste B's filenames, 150 parts or 28 steps into a new model. Derive them
from its actual data.

<a id="trial-gates"></a>
## Small trials before the full kit

1. One loose fit pair, plus small lettering/slot coupons if relevant.
2. A few production 2×2 / 2×4 parts. Coupon success alone is insufficient.
3. Base/front: full-width warping, alignment, retention and replacement.
4. Remaining face/body; recheck when material, color or nozzle changes.

Inspect underside openings, first-layer entries, bridges, thin walls, lettering
and brim in the actual slicer. Geometry 3MF is **NOT_SLICED**, not a P1S-configured
project with pauses. Import STL as mm / 100%; do not import both STL and 3MF
copies of the same parts. Stop for blockage, poor seating, strong force,
whitening/cracks or insufficient retention. Digital checks do not establish
physical fit, strength or tipping safety. Do not automate Send/Print.

<a id="changes"></a>
## Requests for improvements or another size

```text
Make only this model's white lettering more legible.
Preserve the black carrier, mounting and body.
Check counters, open apertures, spacing and positive stroke widths.
Identify changed parts, old/new versions, required reprints and a small text coupon.
```

B's text reference is black 2.4 mm + white 1.2 mm, total 142×40×3.6 mm, lower-line
ink height 10 mm. White increases 0.8 → 1.2: the extra 0.4 changes finished depth
79.8 → 80.2, while the black base remains 79.8.
Change color after black ends at text z=2.4 / logo z=2.8 and before the first
white toolpath, not at an invented fixed layer or unverified G-code pause.

```text
Keep the same 8 mm pitch and block shapes, but reduce the width to fit my desk.
Change block counts and layout, not the scale of the entire finished STL.
Update the BOM, steps, print plates, renders and 3D guide from the same revised data.
```

<a id="publication"></a>
## When asking to publish

Specify the destination owner/repo, visibility, content and photo permissions.
Publish the artifacts made for that work, not copied reference images or private
data. Previous permission is not permission for a different project/service.
Check the live Pages URL, repository subpath, downloads and desktop/mobile
display, not merely that changes reached main.

The handoff should include actual files/URLs, dimensions/counts, the first small
trial and all missing outputs, unrun checks and physical uncertainties.
See the detailed [workflow](../../.github/skills/lego-like-3d-print/references/workflow.md)
and [notices](notices.md).
