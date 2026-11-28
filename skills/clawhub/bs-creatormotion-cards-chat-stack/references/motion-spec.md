# Motion specification

## Relationship

shell → message one → message two → wrapped final message

## Must retain

- Fixed conversation shell.
- Downward message growth.
- Variable-height message wrapping.

## Distinctness

Messages have variable height inside a fixed conversation shell; equal list rows omit that layout responsibility.

## Authored direction and timing

The thick rounded application panel is removed. A broad conversation canvas contains compact dark speech balloons with matching solid tails, one speaker marker and a quiet input line; message widths and heights follow the supplied copy instead of identical large cards.

Messages arrive 0.50/1.55/2.60 s in 0.22 s with a small bottom-left anchored settle. Earlier balloons and the input area remain fixed.

Use HyperFrames only. Keep the Google font assets local and preserve the static light-grey grid on every canvas. A quiet final reading hold is intentional; do not add arbitrary ambient movement. Review real rendered frames around the principal change, not only the poster.

## Verification

Use the deterministic HyperFrames at 30 fps in each of the four aspect ratios. Keep identical content and movement across all three palettes. Verify full-frame entry, every edit or relationship change, and the final reading hold in rendered frames. Check actual text bounds, readable contrast, connector endpoints and media alignment. Intentional camera clipping or foreground occlusion is limited to the named layers; it does not excuse unreadable labels. Use bundled generated imagery or the user's supplied replacements for image content, and editable geometry for diagrams; do not fabricate metrics or source evidence.

The attachment plus is a sibling of the input strip, positioned on the chat canvas. It is not a negatively positioned child escaping the strip. The message tails use the same solid fill as their balloons, with no detached outline triangle.

## Image material contract

`chatAvatar` supplies the real portrait in the conversation speaker marker. The bundled generated portrait is automatic; replace this slot when the user names a person or provides an avatar. Keep the speech balloons, message wrapping and input line editable.

Use the raster defaults in `default-image-slots.md` when no image reference is supplied. User replacements through `--images` override only their named slots. Preserve the reference's image-rich material: photos, avatars, covers, document imagery and content thumbnails must not become HTML drawings or placeholder text lines. Text labels, real charts, controls and motion remain editable. Generated default imagery is illustrative, not factual evidence. See `image-policy.md` for generation, provenance and replacement details.
