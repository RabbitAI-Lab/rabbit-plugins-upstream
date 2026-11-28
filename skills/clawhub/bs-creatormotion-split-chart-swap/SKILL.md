---
name: bs-creatormotion-split-chart-swap
description: A large graph owns the main field while the speaker occupies a narrow edge. Short positional exchanges reframe the comparison, and the two strokes draw in distinct reading intervals.
---

# Chart Presenter Swap

Use this Skill when the brief needs chart presenter swap. Read `references/motion-spec.md` and `references/DESIGN.md` before adapting it. Ask only for essential missing content or media; use the included original example to demonstrate an unspecified detail.

## Create an editable project

1. Put the replacement content in a JSON object using the input names below.
2. Choose `white-yellow` by default, or `charcoal-lime` or `midnight-ice`. The three styles preserve the same motion and content.
3. Run `node scripts/create.mjs --out /absolute/output/path --data /absolute/content.json --style white-yellow --media /absolute/presenter.mp4 --aspect 16:9 --resolution 4k`.
4. Render with the command printed by the generator, then inspect the start, main change and settled hold.

Supply a continuous local presenter/background take at least 6.8 seconds long with `--media`. Never loop a shorter take. Keep videos muted; narration is a separate asset.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

For footage, pass `--focus x,y`: the centre of the presenter's face as fractions of the footage frame (for example `0.52,0.38`). Extract one frame (`ffmpeg -ss 2 -i <take> -frames:v 1 /tmp/frame.png`), look at it and estimate the face centre. The effect uses it to centre the head in the region the presenter occupies. Use landscape footage for 16:9 and 4:3 and portrait footage for 9:16 and 3:4.

## Inputs

The effect exports the following complete original example. Change values rather than modifying animation selectors:

```json
{
  "series": [
    [
      16,
      24,
      32,
      49,
      54,
      72
    ],
    [
      14,
      16,
      24,
      31,
      36,
      45
    ]
  ],
  "axisLabels": [
    "W1",
    "W2",
    "W3",
    "W4",
    "W5",
    "W6"
  ]
}
```

series accepts two arrays of up to six values from 0–100; axisLabels contains up to six labels. The actual chart and presenter regions exchange sides twice. Line drawing must happen in the settled intervals.

## Motion invariants

Chart viewport and narrow presenter region translate across each other between left/right allocations; data strokes draw during the settled intervals.

A changed palette or different wording must not replace this movement with a generic card entrance. Keep the geometry, reveal order and layer persistence described in `references/motion-spec.md`.

## Validation

Run HyperFrames lint, validate and inspect in the generated project. Check contrast, readable bounds and deterministic seeking. Visually review all three styles in all four aspect ratios when changing the module. Inspect the actual rendered video; a successful HTML build is not visual acceptance. Keep all images, fonts, video and scripts local to the generated project.

## Film-look direction

Keep the chart as a near-full-height evidence plane, increase its grid and stroke presence, and close-crop the narrow speaker. Shorten both coordinated swaps so they read as edits rather than floating panels; draw each data stroke only after its framing is settled. Use the established bundled fonts and semantic palettes, including the light-grey grid on every canvas. Keep the same image and motion geometry in every palette. Do not add decorative particles, extra glow, global blur or bounce. Supplied original media is the material; default demonstration content is not evidence of a real result.

Build in HyperFrames only. Review actual rendered frames at each change of focus and during the final hold. Frame-edge cropping and media overlap are intentional only where they serve the composition; essential text and interface targets must remain readable.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
