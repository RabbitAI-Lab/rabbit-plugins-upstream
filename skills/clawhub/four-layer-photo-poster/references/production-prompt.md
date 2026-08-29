# Layer prompts

Use one prompt per layer and one source photo per run. Derive variables only from what is visible. Every generated layer should be a clean horizontal panorama near 3:1, with no exterior frame, panel border, layer label, watermark, or logo; the assembly script supplies the final geometry.

## Shared source lock

Prepend this to every generated-layer prompt:

```text
Use this one reference photograph as the sole visual source. Preserve the same subject identity, count, physical structure, proportions, pose, action direction, gaze, camera viewpoint, perspective, occlusion, left/right placement, foreground/background order and core narrative. Maintain the same approximate horizontal anchor points: [SUBJECT CENTER], [PRINCIPAL SILHOUETTE], [KEY RELATIONSHIP]. Create one full-bleed, approximately 3:1 horizontal panorama. If adaptation is needed, extend only scene-consistent background sideways or lightly crop it sideways; never vertically stretch, crop key anatomy/objects, change the scene, or invent an unrelated subject. No text unless the layer explicitly asks for user-provided copy.
```

## Layer 1 — original photography

Prefer the source image directly, cropped or background-outpainted only as necessary to form the panorama. When a generation tool is required for outpainting, append:

```text
Keep the source photograph completely photographic and unretouched. Preserve the subject pixels exactly; expand only the background at the left and/or right edge with the same environment, perspective, natural illumination, shadow direction, detail level and core colors. No face/body regeneration, illustration, beautification, material conversion, color grade, invented scenery, or decorative element.
```

## Layer 2 — selective-memory sticker reconstruction

```text
Translate the same source scene into a premium independent-publication selective-memory sticker page. Compress the scene into 3–6 large recognizable gouache, paper-cut, Risograph and screen-print flat shapes rather than tracing it. Make one dominant main visual and exactly six smaller memory stickers selected from these source-true details: [SIX SOURCE-TRUE DETAILS]. The six stickers must vary substantially in scale and importance: integrate two or three partly overlapping, clipped at an edge, or attached near the main visual; avoid a six-grid or product-catalog arrangement. Give them thick pale cut edges, relaxed asymmetric placement, gentle overlap/rotation, generous quiet negative space, and clear hierarchy.

Use opaque matte gouache color blocks, paper grain, hand-cut edges and slight print-registration offsets. Palette: airy muted powder blue, mist blue, sky blue, ivory, cream, pale beige, soft sage and architectural neutrals, with only tiny dusty-rose accents. Avoid literal photorealism, watercolor washes, dense linework, smooth vector art, 3D plastic, anime, ecommerce styling and excess detail. Do not generate text.
```

## Layer 3 — watercolor travel-ticket postcard

```text
Create a centered horizontal watercolor ticket on a spacious ivory background. Use thick matte watercolor paper, delicately serrated edges and an extremely subtle natural shadow. The ticket is structured precisely: its left 74% is a watercolor scene; its right 26% is a calm ticket-information stub; a vertical dotted/perforation/tear line separates them. Use aligned but blank information rules, short lines, dot columns and at most one unlabeled circular stamp; do not generate words, dates, place names, numbers or pseudo-text unless the user supplied exact copy.

In the 74% watercolor scene, retain the source’s recognizable subject and necessary environment relation. Paint with bright clean low-to-medium saturation watercolor, using 2–4 related tones from sage, mist blue, pale blue-gray, cream yellow, warm sand and light terracotta, with minimal warm highlights. Show paper white, thin translucent washes, wet/dry variation and soft granulation. The subject is slightly clearer than the naturally subdued environment. Avoid dirty vintage casts, heavy brown, clutter, floating information, a commercial template and photo-real rendering.
```

## Layer 4 — gilded enamel travel magnet

```text
Reduce the same source scene to one refined premium collectible enamel travel magnet/badge. Preserve the distinctive [SUBJECT SILHOUETTE / KEY STRUCTURE] and essential spatial relation while simplifying all nonessential detail. Use clean vivid harmonious colors sampled from the source; smooth real enamel fills; thin flowing gold-metal internal dividers; crisp white-metal outer contour; rounded beveled thickness; restrained metal glints; and a short soft cast shadow on a broad uncluttered cream, pale gray, pastel or source-derived light background. The badge may be mildly off-center or tilted but must feel stable and collectible.

Do not generate wording by default. If the user provided exact short copy, integrate only that copy into the badge edge or enamel nameplate. Avoid a flat sticker, cartoon, plastic 3D render, thick harsh shadow, cheap gold trim, busy decoration, ecommerce product photograph and generic template appearance.
```

## Variables and repair instructions

- **[SUBJECT CENTER]**: a source-observed horizontal anchor, such as `the cyclist centered slightly left`.
- **[PRINCIPAL SILHOUETTE]**: the dominant source-observed outline.
- **[KEY RELATIONSHIP]**: a source-observed relation, such as `the dog in front of the seated person`.
- **[SIX SOURCE-TRUE DETAILS]**: six visible, unequal-priority details: gesture, prop, material, plant, vehicle, pattern, food, light, etc.
- **[SUBJECT SILHOUETTE / KEY STRUCTURE]**: one or two distinctive source-observed outline features.

When retrying, target one defect only:

- `Restore the source subject’s identity, count, pose, direction, viewpoint and placement. Change nothing else.`
- `Preserve the existing style but realign the principal silhouette and visual center with the source-photo strip.`
- `Remove all words, numbers and pseudo-text while keeping the ticket structure.`
- `Keep exactly six varied memory stickers, with a clearly dominant main visual and no grid.`
