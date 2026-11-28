# Image briefs

## Sources and references

SKILL.md Workflow step 5 is the picture policy: user pictures first, then the library question, then generation, then labeled image frames. Use one request per distinct scene with a full text prompt. When you generate, you may pass one or two pictures from this Skill's library (`node scripts/embed-library-images.mjs --download <id> --out <dir>`) or pictures already generated for this deck as style references, so the series keeps one look. Never pass third-party, source or reference-template images, screenshots, or photos of real people as inputs.

## Frames in this style

Generate each picture at the `aspect` that `style-kit.json` lists for its slot; the frames below (px on the 1280x720 page) tell you where the subject must sit.

| Slot | Frame | Ask for |
| --- | --- | --- |
| `.cover-art` | right 717px, full height, angled left edge | landscape; subject in the right two thirds |
| `.contents-art` | right 614px, full height | portrait-leaning crop; key subjects in the central vertical band |
| `.intro-art` | left 550px, full height | people working together, faces away from the right edge |
| `.band-art` | full-width band, bottom 317px | wide scene with interest spread across the frame |
| `.services-art` | tall framed column 461 x 598px | two people or one moment in the central vertical band |
| `.process-art` | left 435px, full height | close group or single figure, centered |
| `.closing-art` | right 589px, full height | calm, open scene that suits an ending |

Each semantic page gets its own picture; never repeat a photo on two pages.

## Prompt pattern

> Original photorealistic image for a fictional [industry] company presentation. Scene: [specific people, place and action]. Visual treatment: cobalt blue and white accents, soft daylight, clean documentary photography. No logos, signage, words, letters, digits, readable screens or watermark. Realistic people and anatomy. [Crop note from the table above].

Example scenes:

- **Architectural opening**: a contemporary building with white panels and cobalt structure in soft daylight, generous sky, no signs.
- **Shared work**: a small team reviewing printed plans at a bright desk, candid and focused.
- **Service moment**: a coordinator with a tablet handing over a parcel beside an open van at a clean loading bay.
- **Operations floor**: a high-angle view of an open-plan office with long white desks and large windows.

## Embedding

The build inlines pictures into the single HTML file; keep the deck under 20 MB and run `scripts/optimize-images.py` if the check warns about size. Keep icons, shapes and charts as native HTML/SVG, not pictures.
