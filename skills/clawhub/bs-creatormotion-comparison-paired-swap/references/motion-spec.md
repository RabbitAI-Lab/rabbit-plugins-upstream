# Motion specification

Keep before-and-after frames fixed while replacing complete pairs in rapid, synchronized succession.

## Ordered beats

1. Reveal two equally sized result frames with fixed comparison labels.
2. Place the first synchronized image pair into the frames.
3. Replace both images together through two or more pairs while preserving alignment and label positions.
4. Hold the final pair with an optional persistent step caption.

## Distinctive behavior

This is a synchronized montage of several complete before/after pairs; prompt results needs time to inspect and judge each prompted pair.

## Controls

- `leftLabel` (string).
- `rightLabel` (string).
- `pairs` (imagePair[]).
- `stepCaption` (string).

## Timing and fidelity

The first entrance starts after 0.16 seconds. Timelines are deterministic, with no clocks, randomness, or CSS keyframe loops. Increasing item counts requires enough time for reading; reduce input density instead of shrinking labels below 24 px on the design canvas. Preserve structural motion across all three color styles.

Each `pairs` entry is [leftImageKey, rightImageKey]. Both members must change at the same time beneath fixed `leftLabel` and `rightLabel`. If no image is supplied, the example renders editable document diagrams; provide real images for photographic comparisons. Keep the final `stepCaption` separate from the pair frames. Inspect the beginning, every motion handoff, and the final hold.

## Refinement — 2026-09-23

Refine before/after typography and frame rules; use a near-stationary synchronized dissolve so pair swaps feel deliberate.

- Use the shared Smiley Sans typography hierarchy; preserve duration, default content and the defining relationship above.
- Keep title, numeric result, supporting label and connector visually distinct. Use 2–3 px structural strokes and restrained entrances; avoid elastic overshoot and thick luminous selection rings.
- Verify settled frames in all three palettes. The black-and-white palette remains monochrome, with the shared fine grid behind content.

## Film-look renovation

Rebuilt the presentation as two large widescreen inspection windows with high-contrast stamped labels and a persistent plain caption. Pair changes are synchronized short cuts, not independent fades. Each pair gets a settled reading slot and the final example holds longer.

Keep the numerical relationships and geometry honest. The camera, masks and focused states must never hide the current reading subject. Do not replace the staged comparison with a generic card fade.

Three bundled raster pairs demonstrate notes becoming a clear presentation, a planning table becoming a working brief, and research becoming a workshop cover. User images replace the corresponding before/after slots directly.

## Image material contract

Default raster slots: `draft-1`, `draft-2`, `draft-3`, `refined-1`, `refined-2`, `refined-3`. The default generator loads these automatically; user replacements override the named slots. Image values in content may retain a filename suffix, while the image-map key uses its extension-free basename.

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
