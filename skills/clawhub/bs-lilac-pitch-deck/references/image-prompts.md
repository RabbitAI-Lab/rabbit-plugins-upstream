# Pictures for Lilac Glass decks

## Sources

Follow SKILL.md Workflow step 5 for picture sources, the library question and tools. Only this Skill's library pictures or pictures already made for this deck may be passed as references; never pass third-party, source, or reference-template images, screenshots, or photos of real people. Inventory every picture slot first. Each semantic page gets its own picture with a full text prompt; never show the same photo on two pages. Generate each picture at the aspect that `style-kit.json` lists for its slot (`images[].aspect`); the aspects in the slot table below are defaults for new slots with no listed aspect.

## Picture grammar

- Photography: realistic editorial scenes in calm, bright modern offices; soft daylight; pale neutral rooms with lilac objects and navy clothing; diverse adults; relaxed authentic expressions.
- Glass art (cover, roadmap): translucent violet glass slabs over a deep indigo backdrop, iridescent cyan and magenta edges, generous dark negative space where the title sits.
- Portraits (team): waist-up studio portraits on a plain pale lavender-grey backdrop, centered, vertical 2:3.
- Always: no text, lettering, logos, watermarks, readable screens, or celebrity resemblance.

## Slot sizes

| Archetype | Slot | Aspect to request |
|---|---|---|
| Cover | full-bleed glass art, subject on the right | landscape 3:2 or 16:9 |
| Overview | wide band + overlapping inset | two different landscape photos |
| Vision / Mission | tall stacked photo window | landscape with a centered subject (crops to square) or portrait |
| Chart | tall photo beside the chart card | portrait 2:3 |
| Roadmap | glass steps bleeding off the right edge | landscape, dark left half |
| Team | three tall portrait cards | portrait 2:3, one per person |
| Contact | wide photo band | landscape with faces in the upper middle |

## Example prompt

Original realistic editorial photograph: two adult colleagues at a pale wooden desk reviewing a tablet that shows an abstract violet and white bar chart with no numbers or letters. Soft natural daylight, modern calm office, lilac notebook and ceramic mug, shallow depth of field. No logos, words, watermarks, or celebrity resemblance. Portrait 2:3.

## After generation

Inspect each result, convert to WebP (quality about 88, longest edge at most 1920 px), embed it as a data URI with useful alt text, and keep masters and prompt records in the user workspace, not in the Skill folder.
