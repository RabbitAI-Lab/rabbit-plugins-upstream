# Chapter Character Reveal motion specification

The small label is established first; fixed-position headline glyphs change from faint to solid from left to right without moving the whole line.

## Inputs and geometry

Title glyphs darken at fixed positions. A space is retained as a nonbreaking glyph to preserve readable word spacing. This is not a whole-headline slide.

This is a graphic-only composition; a presenter file is not required.

## Authored direction and timing

A faint oversized diagonal typographic backdrop gives depth without a panel. The label is a hard-edged print strip and the 150 px headline resolves rapidly in its final positions, followed by a completely stable reading hold.

Label 0.16–0.34 s; characters 0.50–1.50 s; hold complete headline through 6.8 s. No empty fade-out.

Use HyperFrames only. Keep the Google font assets local and preserve the static light-grey grid on every canvas. A quiet final reading hold is intentional; do not add arbitrary ambient movement. Review real rendered frames around the principal change, not only the poster.

## Composition constraints

Whitespace spans retain an explicit 0.28 em advance. The 150 px headline characters resolve at fixed positions, followed by a fully opaque final hold.

## Verification

Use the deterministic HyperFrames at 30 fps in each of the four aspect ratios. Keep identical content and movement across all three palettes. Verify full-frame entry, every edit or relationship change, and the final reading hold in rendered frames. Check actual text bounds, readable contrast, connector endpoints and media alignment. Intentional camera clipping or foreground occlusion is limited to the named layers; it does not excuse unreadable labels. Use bundled generated imagery or the user's supplied replacements for image content, and editable geometry for diagrams; do not fabricate metrics or source evidence.

## Image material contract

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
