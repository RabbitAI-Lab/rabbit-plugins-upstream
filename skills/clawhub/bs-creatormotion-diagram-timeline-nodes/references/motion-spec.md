# Timeline Node Reveal motion specification

## Shot design

A full-width timeline aligns large dates, small endpoints and supporting captions. Each milestone settles completely before the next; optional presenter media stays out of the text area.

Preserve the original input object documented in SKILL.md. 6.6 seconds at 30 fps, in 16:9, 4:3, 3:4 or 9:16. The exact timings live in the bundled scene function, including the optional input branches.

## Timing and layout

| Time (seconds) | Visible change |
| --- | --- |
| 0.18-0.93 | Draw the wide timeline rule. |
| 0.55 onward | For each milestone, reveal its endpoint, large date, then supporting caption. |
| After the last milestone-6.60 | Hold the chronology; optional presenter is below the text zone. |

These timings describe the default example. Count-dependent beats remain ordered when input counts change. Keep labels concise: usually one to four words per node, at most two short lines per note. Preserve the input schema in SKILL.md. Use the exact scene function for alternate branches; do not flatten optional topology into unrelated cards.

## Content and verification

Use semantic Google font roles and the three established palettes. The Black & White canvas stays neutral with fine grid lines. Original abstract glyphs and paper geometry are part of the generated design; they are not copied creator imagery or external evidence. Supply actual media for optional media inputs.

Check the start, central transformation and settled frame in all palettes. Preserve edge alignment when moving groups. Check labels, arrow endpoints and empty-space separation with changed content. Review actual MP4 frames and full decoding; passing HTML checks alone is not visual approval.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
