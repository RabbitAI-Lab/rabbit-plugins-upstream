# Motion specification

Move from report context into a plot, draw observed points and connecting segments left-to-right, then extend a separate trend line.

## Ordered beats

1. Start with the report heading and chart frame visible.
2. Move the viewport toward the chart while revealing observed data points and connecting segments in x order.
3. Extend a separately styled trend line as the observed path completes.
4. Hold the full plot with labels and one short conclusion; a presenter inset may remain fixed.

## Invariants

This draws data geometry over time. The card tour instead moves between already rendered charts.

Start motion after 0.16 seconds. Retain at least 1.2 seconds for the final reading state. Use deterministic timeline animation; no clocks, random values, or CSS keyframes. All text must stay readable and the four visual styles must preserve the same structure.

## Inputs and geometry

- `title` (string).
- `points` (point[]).
- `trend` (point[]).
- `axisLabels` (string[]).
- `conclusion` (string).

`points` and `trend` are arrays of [x, y] values on the same numerical scale. The module derives both axes from their combined extent; use positive extents and at least two ordered observed points. `axisLabels` contains x then y. The trend must remain a separate dashed path, and `conclusion` appears only after the plot develops. An optional presenter is supplied with `--media`; it is not a content JSON field.

## Fidelity check

Inspect the observed path at its beginning, midpoint, and final point. Check the separate trend reveal mask, both axes, conclusion, and optional presenter spacing. The result must remain a data drawing rather than a static chart fade.

## Refinement — 2026-09-23

Use lighter chart strokes and smaller observations, clarify title/axis/conclusion hierarchy and remove point bounce. Preserve observed versus dashed trend distinction.

- Use the shared Smiley Sans typography hierarchy; preserve duration, default content and the defining relationship above.
- Keep title, numeric result, supporting label and connector visually distinct. Use 2–3 px structural strokes and restrained entrances; avoid elastic overshoot and thick luminous selection rings.
- Verify settled frames in all three palettes. The black-and-white palette remains monochrome, with the shared fine grid behind content.

## Film-look renovation

Removed the redundant eyebrow and enlarged the chart heading and drawable span. The chart establishes through a measured push from a slightly smaller reading plane; the observed series reveals linearly across the actual x range, then the dashed trend follows. Thin grid lines, larger point markers and a final conclusion strip preserve the measured data story.

Keep the numerical relationships and geometry honest. The camera, masks and focused states must never hide the current reading subject. Do not replace the staged comparison with a generic card fade.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
