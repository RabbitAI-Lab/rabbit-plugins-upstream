# Image prompts

## Picture policy

SKILL.md Workflow step 5 is the only picture policy: user pictures first, then the library question, then generation with the tools it names. When you generate, one or two pictures from this Skill's library or pictures already made for this deck may be passed as style references so the series keeps one look. Never pass third-party, source, or reference-template images, screenshots, or photos of real people as inputs.

Pictures are original dark-backdrop 3D still lifes in the deck palette. Use the patterns below as composition guides: replace the fictional business, objects and setting with the user's case, keep the art direction, palette, backdrop and crop. Titles, labels, numbers and logos belong in editable HTML, never inside the image.

## Scene plan

Generate every picture at the `aspect` that `style-kit.json` and the compose report list for its slot; the aspects below are defaults only for a new slot that has no listed aspect.

| Scene | Page archetype | Default aspect | Placement |
| --- | --- | --- | --- |
| spectrum-objects | cover | square 1:1 | rounded window, right column |
| positioning-vessel | positioning | portrait 2:3 | full-bleed left half |
| refill-experience | touchpoints | landscape 16:9 | bleeds off the right edge, cards overlap its bottom |
| welcome-threshold | closing | landscape 3:2 | bleeds off the right edge, objects in the right two thirds |

Each semantic page gets its own picture; never repeat one picture on two pages. Tiles, icons, charts and decorations stay authored HTML/SVG.

## Generation notes

One picture per request, full text prompt. State the slot's aspect ratio in the prompt. Keep the backdrop near-black (#121613) so edge-bleed placements blend into the page.

Check every result for stray text, logos, warped objects and a crop that keeps the main subject clear of overlapping cards.

## Prompt patterns

### spectrum-objects (cover, square)

```text
Original premium playful 3D still life for a fictional refill shop brand strategy. Four independent chunky objects arranged in a clean two-by-two composition: a pale cream refill dispenser silhouette, an abstract green folded-paper loop, an orange rounded stacked vessel, a yellow sculptural arch. Saturated green #27ad67, blue #2eaaeb, orange #ff7b27 and yellow #eed23f appear as separate rounded rectangular plinths, deep near-black #121613 backdrop, simple cream object surfaces with soft 3D lighting, modern colorful design toy aesthetic, crisp edges and restrained shadows. No logos, brands, text, letters, icons, characters, watermarks. Design new forms, do not recreate any existing template object.
```

### positioning-vessel (positioning, portrait)

```text
Original premium playful 3D still life, portrait composition. A single chunky cream-colored reusable refill bottle with a rounded cap stands on a tall rounded saturated orange #ff7b27 plinth, a smaller blue #2eaaeb rounded block and a yellow #eed23f half-disc lean beside it, a green #27ad67 ring lies in front. Deep near-black #121613 seamless backdrop, soft studio lighting, matte tactile materials, gentle contact shadows, modern design-toy aesthetic, generous dark space above the objects. No text, no letters, no logos, no labels, no people, no watermark.
```

### refill-experience (touchpoints, landscape)

```text
Original stylized 3D scene illustrating a friendly neighborhood refill shop experience. A small cream refill station, three rounded plain reusable containers, a folded receipt with no writing, a circular floor mark and simple arch, all invented geometric forms. Compact composition on dark near-black #121613 background, saturated green #27ad67, blue #2eaaeb, orange #ff7b27 and yellow #eed23f accents, playful premium design-object rendering, soft contact shadows, tactile matte material, clean studio lighting. No real brand, logo, text, signage, watermark or stock assets. Any attached picture is only a style reference from this Skill's library or this deck; create the scene from scratch.
```

### welcome-threshold (closing, landscape)

```text
Original premium playful 3D scene, landscape composition. A small stylized neighborhood shop entrance built from rounded geometric blocks: a cream arched doorway, a green #27ad67 awning shape, a blue #2eaaeb bench, an orange #ff7b27 rounded planter with a simple plant, a yellow #eed23f circular doormat, and two plain cream refill jars waiting by the door. Deep near-black #121613 seamless backdrop, warm welcoming light glowing from inside the doorway, matte tactile materials, soft contact shadows, modern design-toy aesthetic, objects grouped in the right two thirds with empty dark space on the left. No text, no signage, no letters, no logos, no people, no watermark.
```
