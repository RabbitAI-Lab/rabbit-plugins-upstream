---
name: bs-creatormotion-spotlight-metric-to-detail
description: A large circular figure temporarily overlays a moving interface. Once the camera reaches the evidence, the figure clears and precise frames identify the supporting details in place.
---

# Metric to Interface Detail

Use this effect when the requested explanation needs the choreography below. Read `references/motion-spec.md` before adapting it.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

## Inputs

- `interface` (image).
- `metric` (number).
- `metricLabel` (string).
- `cameraTarget` (rectangle).
- `detailRegions` (rectangle[]).

The current `references/defaults.json` is the complete example input schema. `interface` names an optional screenshot. `metric` is a percentage from 0 to 100 with its `metricLabel`. `cameraTarget` and each `detailRegions` entry are normalized [x, y, width, height] rectangles within the 1600 by 780 interface. Set boxes on the actual evidence, then inspect the metric overlay removal and camera destination.

## Create

1. Save caller content as a JSON file.
2. Run `node scripts/create.mjs --out ./output --data ./content.json --style white-yellow --aspect 16:9 --resolution 4k`. Bundled image defaults are automatic. Add `--images images.json` only for replacements or additional slots; relative paths resolve beside that JSON file.
3. Inspect the editable output at entry, development, and final hold.
4. Render using the command printed by the create script.

The additional styles are `charcoal-lime` and `midnight-ice`. Use identical content and animation when comparing the three styles. All styles share the supplied fonts.

## Required choreography

1. Show the supplied interface and begin a smooth camera move toward its content area.
2. Overlay a translucent metric card whose ring arc and percentage grow together.
3. Continue the viewport move while fading out the metric card.
4. Draw individual borders around the selected values or detail regions and hold the enlarged evidence.

## Verification

Check values against the supplied data, labels against the visible objects, and every terminal state against the brief. Keep at least 1.2 seconds for final reading. Do not clip text or replace the defining motion with a generic fade.

## Film-look direction

Use one coordinated camera move toward the supplied target and a compact neutral metric overlay. Speed the count to finish before the camera settles, clear the overlay cleanly, then reveal sharp-corner detail frames in reading order without pulses. Use the established bundled fonts and semantic palettes, including the light-grey grid on every canvas. Keep the same image and motion geometry in every palette. Do not add decorative particles, extra glow, global blur or bounce. Supplied original media is the material; default demonstration content is not evidence of a real result.

Build in HyperFrames only. Review actual rendered frames at each change of focus and during the final hold. Frame-edge cropping and media overlap are intentional only where they serve the composition; essential text and interface targets must remain readable.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

## Default material alignment

The default overlay reads 100 percent, Collection reviewed, over an illustrative generated content collection. The camera destination [0.06, 0.47, 0.88, 0.38] and detail regions match that raster. Use current defaults.json for exact rectangle sizes, and update coordinates and metrics together when replacing the image.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
