---
name: bs-creatormotion-spotlight-region-callout
description: A document is framed as a single evidence plane, then a precise region becomes the reading focus. A connected margin note explains its significance before the full context returns.
---

# Region Callout

Use this effect when the requested explanation needs the motion described below. Read `references/motion-spec.md` before adapting the composition.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

## Inputs

- `region` (rectangle).
- `callout` (string).
- `step` (string).
- `documentTitle`, `sectionTitle` and `rules` retain their legacy input shape for compatibility. They do not rewrite text inside a raster document; replace the document image when its content must change.

The included raster document is automatic. To replace it, pass the canonical `document` slot through `--images`. `region` is [x, y, width, height] normalized to that displayed document. `callout` changes the connected note and `step` changes the footer. Inspect all four scrim edges, the leader endpoint, and the full-view restoration.

## Create and render

1. Save the requested content as JSON.
2. Run `node scripts/create.mjs --out ./output --data ./content.json --style white-yellow --aspect 16:9 --resolution 4k`.
3. Open the editable output and check the full timeline before rendering.
4. Render with the command printed by the create script.

The other styles are `charcoal-lime` and `midnight-ice`. Keep content, fonts, and motion identical when comparing styles. Use custom semantic color tokens only when their contrast remains readable.

## Required choreography

1. Establish a full interface or document image.
2. Fade a scrim over everything outside the target rectangle while drawing its border.
3. Draw a leader from the target to a short callout; retain the separate step footer.
4. Hold the evidence, then remove the scrim and callout to restore the full interface.

## Delivery checks

Confirm the numerical values and supplied content, inspect the entry, intermediate state, and final reading hold, and confirm no text clips in any of the four aspect ratios. A real presenter input must have enough footage for its visible interval; do not loop a short take.

## Film-look direction

Use restrained document edges and two compact explanatory labels. Move the entire source-and-annotation system together in one short camera push so the connector remains registered; restore context cleanly after the reading hold. Use the established bundled fonts and semantic palettes, including the light-grey grid on every canvas. Keep the same image and motion geometry in every palette. Do not add decorative particles, extra glow, global blur or bounce. Supplied original media is the material; default demonstration content is not evidence of a real result.

Build in HyperFrames only. Review actual rendered frames at each change of focus and during the final hold. Frame-edge cropping and media overlap are intentional only where they serve the composition; essential text and interface targets must remain readable.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

## Default material alignment

The default region [0.274, 0.225, 0.49, 0.21] aligns with the generated working brief. Keep the document as a complete raster plane; recalibrate the normalized rectangle when replacing its screenshot. Input strings cannot edit words already embedded in the raster.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
