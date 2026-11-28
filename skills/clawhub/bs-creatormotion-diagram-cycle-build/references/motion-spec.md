# Cycle Build and Close motion specification

## Shot design

Large icon nodes build around an elliptical path. Every new node follows its incoming arc; the closing arc completes the loop before a quiet confirmation mark appears.

Preserve the original input object documented in SKILL.md. 7.2 seconds at 30 fps, in 16:9, 4:3, 3:4 or 9:16. The exact timings live in the bundled scene function, including the optional input branches.

## Timing and layout

| Time (seconds) | Visible change |
| --- | --- |
| 0.16-0.46 | Resolve the first icon node. |
| 0.47 onward | Draw an arc, then resolve the next node; repeat around the ellipse. |
| Final arc | Close the loop using a slightly stronger connection. |
| After closure | Resolve the center confirmation mark and hold for at least two seconds. |

These timings describe the default example. Count-dependent beats remain ordered when input counts change. Keep labels concise: usually one to four words per node, at most two short lines per note. Preserve the input schema in SKILL.md. Use the exact scene function for alternate branches; do not flatten optional topology into unrelated cards.

## Content and verification

Use semantic Google font roles and the three established palettes. The Black & White canvas stays neutral with fine grid lines. Original abstract glyphs and paper geometry are part of the generated design; they are not copied creator imagery or external evidence. Supply actual media for optional media inputs.

Check the start, central transformation and settled frame in all palettes. Preserve edge alignment when moving groups. Check labels, arrow endpoints and empty-space separation with changed content. Review actual MP4 frames and full decoding; passing HTML checks alone is not visual approval.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
