---
name: bs-creatormotion-comparison-feature-matrix
description: Fixed option headings establish a common comparison grid. Each dimension appears first, followed by a left-to-right reveal of both values on the same baseline.
---

# Feature Matrix Reveal

Use this effect when the requested explanation needs the choreography below. Read `references/motion-spec.md` before adapting it.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

## Inputs

- `options` (string[]).
- `rows` (matrixRow[]).

The current `references/defaults.json` is the complete example input schema. `options` contains two column headers. Each `rows` item has one dimension and exactly two values. Reveal complete aligned rows so the dimension label always belongs to both values.

## Create

1. Save caller content as a JSON file.
2. Run `node scripts/create.mjs --out ./output --data ./content.json --style white-yellow --aspect 16:9 --resolution 4k`.
3. Inspect the editable output at entry, development, and final hold.
4. Render using the command printed by the create script.

The additional styles are `charcoal-lime` and `midnight-ice`. Use identical content and animation when comparing the three styles. All styles share the supplied fonts.

## Required choreography

1. Establish the two option headers and a blank comparison grid.
2. Introduce the first dimension label and its two corresponding cells.
3. Repeat the row reveal without moving prior rows, allowing different text lengths to remain aligned.
4. Hold the completed matrix with the option headers still visible.

## Verification

Check values against the supplied data, labels against the visible objects, and every terminal state against the brief. Keep at least 1.2 seconds for final reading. Do not clip text or replace the defining motion with a generic fade.

## Film-look renovation

Rebuilt the matrix as a flat editorial comparison with solid heading strips, open ruled rows and narrow indexed dimensions. Dimension labels precede cell wipes. The active row draws an accent edge once, while prior completed rows remain fully readable.

Preserve the supplied data schema and reading holds. Render all three palettes with the same content, then inspect every motion handoff.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
