# Baseline: dimensions, evidence and sources

[日本語](baseline.ja.md) · [Skill](../SKILL.md) · [Workflow](workflow.md)

## Fixed reference

The primary reference is **Copilot Brick Display / B DESK CLASSIC**,
revision **5.0-legible-plaques**, commit
`0967390547184b342adea0d7e8659dc8ac8f153b`.
The [live site](https://ktanino10.github.io/copilot-brick-display/),
[assembly guide](https://ktanino10.github.io/copilot-brick-display/assembly-guide/B.html)
and [physical build log](https://ktanino10.github.io/copilot-brick-display/build-log.html)
may change; do not mix later assets with this revision without checking them.

Fixed primary sources:
[parameters](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/design/parameters.json),
[catalog](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/design/catalog.json),
[interface](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/design/interface.json),
[mechanical design](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/design.md),
[assembly](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/assembly.ja.md),
[lettering](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/lettering.ja.md),
[build evidence](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/build-log.ja.md),
[rebuild procedure](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/docs/rebuild.md).

Visual references are links only:
[mesh-derived finished CG](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/media/B-hero.png)
and [print-slot/assembly mapping](https://github.com/ktanino10/copilot-brick-display/blob/0967390547184b342adea0d7e8659dc8ac8f153b/site/assembly-guide/media/B-first-base.png).
The first is a **digital render, not a physical completion photograph**. These
images are not bundled or licensed by this distribution; see [notices](../NOTICES.md).
Learn from stepped silhouettes, visible studs, seams and separable colors, not
from copying the original mascot, lettering or brand marks.

## Common blocks

All values are in **mm**. These are independent prototype design candidates,
not official LEGO manufacturing specifications or compatibility certification.

| Parameter | Value | Meaning |
| --- | ---: | --- |
| XY pitch | 8.0 | Adjacent stud centers |
| Brick body height | 9.6 | Excludes studs; stacking increment |
| Plate body height | 3.2 | One third of a brick |
| Total body gap | 0.2 | Subtract once per full axis; 0.1 per side |
| Nominal stud diameter | 4.8 | Before male diameter adjustment |
| Stud height | 1.8 | Normal overall height is 11.4 |
| Stud-tip lead-in | 0.25 | Entry geometry |
| Female **radial** clearance | +0.04 | Relative to nominal 4.8 stud; not diameter difference |
| Socket-entry lead-in / height | 0.2 / 0.3 | Widened entry |
| Normal roof / thin-plate roof | 1.6 / 1.0 | Underside remains open |
| Internal tube bore | 3.2 | Not an accessory-compatibility claim |
| Grid rib width | 1.2 | Supports roof and divides bridging spans |

Body size on an axis is `8*n - 0.2`; body sides run from `0.1` to `8*n-0.1`,
with stud centers at `4+8*i`.

| Type | Body W×D×H | Stud-inclusive W×D×H |
| --- | --- | --- |
| 1×2 | 7.8×15.8×9.6 | 7.8×15.8×11.4 |
| 2×2 | 15.8×15.8×9.6 | 15.8×15.8×11.4 |
| 2×4 | 15.8×31.8×9.6 | 15.8×31.8×11.4 |

Stack using **9.6**, not 11.4; lower studs enter the upper part's open underside.
Nominal headroom in a thin plate is 0.4. With baseline clearance, the inner wall
coordinate is 1.56 and actual outer wall thickness is 1.46. Multi-row tube outer
radius is approximately 3.216854, radial wall thickness approximately 1.616854;
single-row internal post radius is 1.56. Orthogonal spans between grid ribs start
at no more than 6.8. Calculate from the source parameters rather than rebuilding
from rounded values. Female geometry refers to the nominal stud diameter so
male compensation and female fit can be compared independently.

Use **open underside walls, tubes and ribs**, not a closed floor with tiny holes.
Nominal clearance is not proof of friction retention. Measure fit, warping,
elephant's foot, bridging and material/color differences physically.

### Fit candidates

- Male **diameter adjustments**: −0.10 / 0 / +0.10, giving 4.70 / 4.80 / 4.90.
- Female **radial clearances**: −0.04 / 0 / +0.04 / +0.08 / +0.12. These are
  absolute candidate settings, not offsets added to the baseline +0.04.
- The reference starts loose: `FIT-M-D470` with `FIT-F-CP12`. Negative settings
  deliberately interfere; stop if light finger pressure is insufficient.
- Only if commercial-block connection is explicitly required, separately test
  printed male → commercial female, commercial male → printed female, and
  printed → printed. Neither purchasing nor compatibility is assumed.

## Reference envelopes and base

Measured digital catalog envelopes include top studs and white lettering.

| Design | Finished W×D×H | Installed parts | Steps |
| --- | --- | ---: | ---: |
| A MINI RELIEF | 143.8×64.2×187.4 | 91 | 23 |
| **B DESK CLASSIC** | **191.8×80.2×238.6** | **150** | **28** |
| C DISPLAY SCULPT | 239.8×112.2×286.6 | 228 | 33 |

B's base is 24×10 studs, **191.8×79.8**, with five layers / 48.0 body height.
The face has 19 layers and a nominal 32 mm thickness.
**19 base + 126 face + 2 front + 3 keepers = 150** installed parts; exclude
coupons from the final BOM. Do not force these counts onto another subject.
C exceeds 256 mm overall height, which is different from the bed fit of each
separately printed part.

Stagger base seams. B's upper layer uses 6-stud lengths and a **3-stud shift**,
not a half-pitch shift, in the 3/6-stud arrangement. The frontmost 8 mm strip is
reserved for plaque slots/reinforcement. It intentionally differs from ordinary
stud/socket geometry; do not "clear" that solid band as if it were a blocked hole.

## Optional removable plaque and right logo

| Feature | B reference |
| --- | --- |
| Plaque width × height | 142×40 |
| Black carrier thickness | 2.4 |
| White relief thickness | **1.2**, changed from 0.8 |
| Total plaque thickness | 3.6 |
| Upper / lower actual ink height | 12 / 10, not font point size |
| Right logo layers | 2.4 black carrier + 0.4 black pad + 0.8 white relief |
| Logo circle / carrier width | 36 / 40 |
| Mount | Vertical tapered slot, bottom seat, top keeper |
| Keepers | 2 for plaque, 1 for logo; each 15.8×15.8×3.2 |
| Lateral receiver clearance | 0.20; candidates 0.15 / 0.20 / 0.25 |

Insert modules **from above**, seat both, then install keepers. Do not force them
in from the front. The removal reference is keeper up 6, forward **at least 32**,
then sideways; module up **at least 45**, then forward. A 20 mm parameter is a
requested minimum; the implementation extends it to a safe envelope of at least
32 mm. Do not shorten the route by quoting the parameter alone.

The lettering revision opens counters, the "e" aperture and spacing, raises lower
ink height to 10 and thickens **only white** to 1.2. B's design targets include
counter chord about 1.02 across the central 50% band, "e" opening about 1.10,
and inter-letter gap about 1.05. Results depend on the font, string and measurement
method. Check positive material widths too; do not claim these as general
printability guarantees or substitute A's different targets.

Keep the **2.4 black carrier and rear mount unchanged**. The additional 0.4 mm
projects forward: finished depth changes 79.8 → 80.2, while the black base stays
79.8. Do not inflate the base to 80.2.

On separate plates, change black to white **after black ends at z=2.4 for text,
z=2.8 for the logo**, before the first white toolpath in the actual slice.
Do not invent a layer number or G-code pause. White relief is connected to the
black backing; it is not a collection of tiny separate white BOM items.

## Print-to-assembly lessons

For **B only**, `B-black-02.3mf` slot 3 contains
`BASE3-24x10-B-562406` → `B-001`. Black 01 alone does not complete the bottom
layer. All five base layers need relevant parts from **black 01–04**.
Six interchangeable same-type/same-color parts are spread over multiple plates;
show every eligible source. Generate a new model's mapping from its own manifest.

An exploded view at 0% must exactly match assembly placement. Move front modules
out of the way before separating layers; the reference uses 20 mm additional
layer travel, giving at least 18.2 mm stud-inclusive visual gaps. This is a
display path, not proof that the whole structure can be pulled apart at once.

## Physical evidence boundary

The public build log records the maker's **2026-09-23 report of an assembled B
base and front modules**. It does **not** establish a completed face/all 150
parts, measured retention, strength, durability or tipping safety, or a complete
match of each photograph to STL hashes and slicer settings. Do not extend that
evidence to the generic public inscription, A/C or new subjects.

The separate Octoprints **r3-8mm-20260920** archive is an 8 mm common-block
revision, not B's geometry revision. Its physical fit/full assembly remain
unverified. Old 4 mm tiny-pin/blocked-hole experiences are lessons, not B test
results. The live archive also contains later experiments; a link is not an
endorsement of all its current designs. Keep rights separate: no blanket license
for the fixed B source, CC BY-NC 4.0 for the identified Octoprints model
derivatives, MIT for this skill's own documents/scripts.
