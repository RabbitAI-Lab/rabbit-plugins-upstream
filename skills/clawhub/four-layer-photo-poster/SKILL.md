---
name: four-layer-photo-poster
description: Turn each supplied photo into its own 3:4 vertical, four-stage design poster with exact four-band assembly and a continuous source scene.
metadata:
  short-description: Four-layer photo design posters
---

# Four-layer photo poster

Use this skill for one independent high-design 3:4 poster per supplied photograph. The poster transitions through four contiguous horizontal bands: original photography, selective-memory stickers, watercolor ticket, and gilded enamel magnet. It is never a multi-photo collage.

## Required two-stage workflow

For each source photo, first create four separate panoramic layer assets, then assemble them deterministically. Do not ask the image model to draw the final four-band layout in one pass: it cannot reliably enforce equal bands or a seamless join.

1. Inspect one source image and derive only source-evident variables. Repeat the full workflow independently for every supplied photo.
2. Read [layer prompts](references/production-prompt.md). Use the same source image for every generated layer, requesting each layer as a single approximately 3:1 panorama.
3. Make the photo layer from the original pixels wherever the crop permits. If horizontal background expansion is necessary, use a photo-faithful, background-only outpaint; never regenerate or retouch the subject.
4. Generate the three stylized layers independently using their corresponding prompt. Preserve the same subject anchors (center, scale, silhouette, direction, viewpoint and core spatial relationship) set by the photo layer.
5. Assemble the four prepared layer files with [compose_poster.py](scripts/compose_poster.py). It creates an exact 3:4 canvas, four equal 25%-height bands, and zero inter-band pixels of space.
6. Inspect the assembled poster against the acceptance checklist. Fix the failed layer and reassemble; do not solve a stylization failure by altering the original photo band.

## Invariants

- Canvas is exactly 3:4 portrait. Bands are exactly `1:1:1:1`, from top to bottom, with no separator, border, gutter, blank seam, rounded panel, logo, watermark, or layer number.
- The source photo is the only visual source. All bands retain the same identity, subject count, structure, proportions, pose, gaze, direction, camera viewpoint, perspective, occlusion, left/right placement, foreground/background order, lighting logic, and narrative.
- Each band is a shallow landscape crop. Horizontally extend background or lightly crop only when it does not remove a head, limbs, key object, or essential relationship. Never vertically stretch the subject.
- Align subject anchors across bands: the principal silhouette, visual center, direction of motion/gaze, and key contour positions should land in comparable horizontal positions.

## Text policy

Default to no generated text. Add text only when the user supplies the copy or when a short source-supported label is safely legible. Never infer a place, date, identity, or factual identifier. Decorative ticket rules, linework and a blank stamp are preferable to garbled microtext.

## Assembly

Run the helper with four image paths in visual order:

```bash
python3 scripts/compose_poster.py --photo /path/photo.png --stickers /path/stickers.png --ticket /path/ticket.png --magnet /path/magnet.png --output /path/poster.png
```

Its default output is 1200×1600. Use `--width` with a positive integer divisible by 3 to select another 3:4 output size; each band will be exactly one quarter of the resulting height.

## Acceptance checklist

- Exactly one output per uploaded source photo, with no shared visual facts across sources.
- Final image is 3:4; its four bands are identical pixel heights and meet with no gap.
- Top band is an unillustrated faithful photo, with its subject preserved from original pixels.
- All four bands show the same moment and scene relation; no added subject, altered face, changed pose, reversed placement, missing key element, or invented setting.
- Sticker band has one main visual and six unequal, non-grid memory stickers.
- Ticket and magnet bands are restrained, legible when text exists, and contain no invented or garbled prominent copy.
