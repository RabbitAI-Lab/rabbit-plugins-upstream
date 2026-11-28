# Image prompts

## Sources and references

SKILL.md Workflow step 5 is the picture policy: user pictures first, then the library question, then generation, then labeled image frames. When you generate, you may pass one or two pictures from this Skill's library (`node scripts/embed-library-images.mjs --download <id> --out <dir>`) or pictures already generated for this deck as style references, so the series keeps one look. Never pass third-party, source or reference-template images, screenshots, or photos of real people as inputs.

Pictures carry the human side of the plan; charts, discs and icons stay authored HTML/SVG. Write a full text prompt for each picture. Replace the fictional activity, setting and people with the user's case but keep the art direction: documentary editorial photography, charcoal surroundings, one quiet cobalt-blue accent, warm natural light, muted palette, no text, signage, logos or watermarks, no real or reference people.

Generate each picture at the `aspect` that `style-kit.json` lists for its slot. The sizes in the table are defaults only for a new slot with no listed aspect; frames are px on the 1280x720 page.

| Slot | Page / layout | Frame | Default size | Composition rule |
| --- | --- | --- | --- | --- |
| scene-a | audience / `bleed` | right 589px, full height | 1536x1024 | Subject in the right 60%; left edge calm (cards overlap it) |
| scene-b | channels / `bleed mirror` | left 589px, full height | 1536x1024 | Subject in the left half; right edge calm |
| team-1..4 | team / `.portrait` circles | square, round crop | 1024x1024 (one 2x2 grid, split into four) | Head and shoulders centered, same plain backdrop |
| contact | contact / `.contact` photo half | right 640px, full height | 1024x1536 portrait | Person right of center; lower-left calm for the note card |

Each semantic page gets its own picture; never reuse one on two pages.

## Patterns

**scene-a**: Original editorial documentary photograph for a fictional neighborhood learning studio launch. A welcoming host talks with three adults aged 25-44 at a communal wooden table with simple paper-craft prototypes and notebooks, shelves of unbranded materials, charcoal furniture, a subtle cobalt-blue wall, daylight from the right, wide composition with the group in the right half. No text, logos, signage, phones or watermarks.

**scene-b**: Original documentary photograph of a fictional studio host demonstrating a simple paper construction to four adults around a dark table, attentive faces and hands, clean contemporary space with a cobalt-blue wall, natural light, muted palette, subject in the left half. No text, logos, signage or watermarks.

**team**: A 2x2 grid of four separate square head-and-shoulders portraits of four different fictional adults who run the studio, separated by thin dark gaps, each centered and looking at the camera, same softly blurred deep cobalt-blue wall behind every person, warm key light from the left, editorial portrait style. No text, logos or watermarks. Split the grid into four square files before embedding.

**contact**: A tall vertical editorial photograph of a fictional studio host standing at the open doorway of a small learning studio at early evening, holding a mug and smiling, warmly lit worktables and shelves behind, cobalt-blue painted wall inside, cool dusk outside, dark calm space in the lower left. No text, signage, logos or watermarks.

Inspect faces, hands and crops after embedding. If a slot has no picture, keep its labeled image frame and report it as pending.
