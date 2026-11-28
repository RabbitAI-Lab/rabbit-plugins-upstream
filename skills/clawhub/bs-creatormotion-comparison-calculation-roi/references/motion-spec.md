# Motion specification

Complete a multiplication, count its result, and expand a second card that compares the result to the investment.

## Ordered beats

1. Show a unit amount and reveal its quantity or frequency underneath.
2. Draw the calculation separator and count the product into the result row.
3. Expand an adjacent comparison card with input and return tracks.
4. Grow the tracks and update the return multiple, then reveal the conclusion label.

## Distinctive behavior

The arithmetic causally creates the compared result and must be visible before the second card; ratio bars begins with two supplied values.

## Controls

- `unitAmount` (number).
- `quantity` (number).
- `investment` (number).
- `currency` (string).
- `labels` (string[]).
- `conclusion` (string).

## Timing and fidelity

The first entrance starts after 0.16 seconds. Timelines are deterministic, with no clocks, randomness, or CSS keyframe loops. Increasing item counts requires enough time for reading; reduce input density instead of shrinking labels below 24 px on the design canvas. Preserve structural motion across all three color styles.

The first result is `unitAmount` multiplied by `quantity`; the return multiple is that result divided by positive `investment`. `labels` describes the three calculation rows, and `currency` formats amounts. Set `conclusion` to agree with the computed result. Inspect the second-card expansion and both proportional bars. Inspect the beginning, every motion handoff, and the final hold.

## Refinement — 2026-09-23

Create a deliberate numeric hierarchy from operands to total and return multiple, soften card arrival and reduce the badge emphasis.

- Use the shared Smiley Sans typography hierarchy; preserve duration, default content and the defining relationship above.
- Keep title, numeric result, supporting label and connector visually distinct. Use 2–3 px structural strokes and restrained entrances; avoid elastic overshoot and thick luminous selection rings.
- Verify settled frames in all three palettes. The black-and-white palette remains monochrome, with the shared fine grid behind content.

## Film-look renovation

Added a deliberate focal handoff: the calculation begins nearer the center, then slides into its final left position as the return comparison reveals at right. Increased the monetary hierarchy and removed soft card styling. Values and bar widths still derive from the same supplied unit, quantity and investment.

Keep the numerical relationships and geometry honest. The camera, masks and focused states must never hide the current reading subject. Do not replace the staged comparison with a generic card fade.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
