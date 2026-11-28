---
name: bs-creatormotion-comparison-line-trend
description: Observed data draws across a full-shot plot, with each point landing at its measured position. A separate dashed trend follows, then a restrained conclusion strip resolves the graph.
---

# Line and Trend Draw

Use this effect when the requested explanation needs the motion described below. Read `references/motion-spec.md` before adapting the composition.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

For footage, pass `--focus x,y`: the centre of the presenter's face as fractions of the footage frame (for example `0.52,0.38`). Extract one frame (`ffmpeg -ss 2 -i <take> -frames:v 1 /tmp/frame.png`), look at it and estimate the face centre. The effect uses it to centre the head in the region the presenter occupies. Use landscape footage for 16:9 and 4:3 and portrait footage for 9:16 and 3:4.

## Inputs

- `title` (string).
- `points` (point[]).
- `trend` (point[]).
- `axisLabels` (string[]).
- `conclusion` (string).

`points` and `trend` are arrays of [x, y] values on the same numerical scale. The module derives both axes from their combined extent; use positive extents and at least two ordered observed points. `axisLabels` contains x then y. The trend must remain a separate dashed path, and `conclusion` appears only after the plot develops. An optional presenter is supplied with `--media`; it is not a content JSON field.

## Create and render

1. Save the requested content as JSON.
2. Run `node scripts/create.mjs --out ./output --data ./content.json --style white-yellow --aspect 16:9 --resolution 4k`. Add `--media presenter.mp4` for optional footage.
3. Open the editable output and check the full timeline before rendering.
4. Render with the command printed by the create script.

The other styles are `charcoal-lime` and `midnight-ice`. Keep content, fonts, and motion identical when comparing styles. Use custom semantic color tokens only when their contrast remains readable.

## Required choreography

1. Start with the report heading and chart frame visible.
2. Move the viewport toward the chart while revealing observed data points and connecting segments in x order.
3. Extend a separately styled trend line as the observed path completes.
4. Hold the full plot with labels and one short conclusion; a presenter inset may remain fixed.

## Delivery checks

Confirm the numerical values and supplied content, inspect the entry, intermediate state, and final reading hold, and confirm no text clips in any of the four aspect ratios. A real presenter input must have enough footage for its visible interval; do not loop a short take.

## Film-look renovation

Removed the redundant eyebrow and enlarged the chart heading and drawable span. The chart establishes through a measured push from a slightly smaller reading plane; the observed series reveals linearly across the actual x range, then the dashed trend follows. Thin grid lines, larger point markers and a final conclusion strip preserve the measured data story.

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
