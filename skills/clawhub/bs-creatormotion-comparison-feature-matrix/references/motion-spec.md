# Motion specification

Keep two options and the dimension labels fixed while revealing aligned cell values row by row.

## Ordered beats

1. Establish the two option headers and a blank comparison grid.
2. Introduce the first dimension label and its two corresponding cells.
3. Repeat the row reveal without moving prior rows, allowing different text lengths to remain aligned.
4. Hold the completed matrix with the option headers still visible.

## Distinctive behavior

Its semantic alignment is by shared dimensions, not by long previews with independent overlay annotations.

## Controls

- `options` (string[]).
- `rows` (matrixRow[]).

## Timing and fidelity

The first entrance starts after 0.16 seconds. Timelines are deterministic, with no clocks, randomness, or CSS keyframe loops. Increasing item counts requires enough time for reading; reduce input density instead of shrinking labels below 24 px on the design canvas. Preserve structural motion across all three color styles.

`options` contains two column headers. Each `rows` item has one dimension and exactly two values. Reveal complete aligned rows so the dimension label always belongs to both values. Inspect the beginning, every motion handoff, and the final hold.

## Refinement — 2026-09-23

Make comparison data the focus by replacing heavy filled dimension cells with a restrained accent edge. Refine header sizing and cell corners.

- Use the shared Smiley Sans typography hierarchy; preserve duration, default content and the defining relationship above.
- Keep title, numeric result, supporting label and connector visually distinct. Use 2–3 px structural strokes and restrained entrances; avoid elastic overshoot and thick luminous selection rings.
- Verify settled frames in all three palettes. The black-and-white palette remains monochrome, with the shared fine grid behind content.

## Film-look renovation

Rebuilt the matrix as a flat editorial comparison with solid heading strips, open ruled rows and narrow indexed dimensions. Dimension labels precede cell wipes. The active row draws an accent edge once, while prior completed rows remain fully readable.

Keep the numerical relationships and geometry honest. The camera, masks and focused states must never hide the current reading subject. Do not replace the staged comparison with a generic card fade.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
