---
name: bs-creatormotion-collage-evidence-summary
description: A varied wall of source notes stays available behind a concise conclusion. A small speaker appears only after the material is established, preserving the documents as the main evidence.
---

# Evidence Wall Summary

Use this Skill when the explanation benefits from this exact visual relationship: settled evidence grid → bottom summary tag → presenter window.

Preserve the defining sequence. Read `references/motion-spec.md` before editing the composition. Keep labels concise enough for the canvas in every aspect ratio; keep supporting labels at least 24 px. Use the same content and timing across the four supplied styles.

## Content controls

- `documents`: default `[{"title": "Itinerary", "lines": ["Day 1: Coast walk", "Day 2: Mountain trail", "Day 3: City market"]}, {"title": "City walks", "lines": ["Old town", "Morning light", "Slow streets"]}, {"title": "Photo picks", "lines": ["Best light", "One subject", "No crowds"]}, {"title": "Train route", "lines": ["Coast line", "Mountain pass", "City loop"]}]`.
- `summary`: default `"One trip, many useful notes"`.
- `presenter`: default `true`.

The renderer accepts local `images` and presenter `media` where the composition uses them. Reuse the bundled generated image defaults when no reference is supplied; explicit user images override the named slots. Photos, covers, content imagery and chat avatars must remain real raster images, never HTML placeholder drawings. Read `references/image-policy.md` and `references/default-image-slots.md` for material selection and replacement keys.

## Local assets

Set `presenter` to false for a document-only composition. When true, `media` supplies the circular presenter window.

## Build and review

From the extracted Skill directory, create a composition with a JSON content file:

```sh
node scripts/create.mjs --out ./output/my-video --style white-yellow --data ./content.json --aspect 16:9 --resolution 4k
```

For presenter scenes, add `--media ./presenter.mp4` when required. Image defaults are automatic; add `--images ./images.json` only to replace or extend named image slots. Its local paths resolve relative to the image JSON file. The other styles are `charcoal-lime` and `midnight-ice`.

Then inspect and render the created composition:

```sh
npx --yes hyperframes@0.8.30 inspect ./output/my-video --json
npx --yes hyperframes@0.8.30 render ./output/my-video --output ./output/my-video.mp4 --fps 30 --quality high --strict
```

Use the package renderer with local content, a selected style and any required local media. Preserve the module's deterministic GSAP timeline. Check the first visible state, each relationship change and the final reading hold. Inspect the rendered video for cropping, overlapping labels and incorrect connector endpoints. A presenter take must cover its entire visible interval; the default media window is at most 6.8 seconds.

## Scope

This is a flat labeled grid with a bottom conclusion, not a drifting field at varied depth with a central bar.

## Film-look direction

Break the equal-card grid into four differently proportioned paper planes and move document labels to small square tabs. Remove the large summary button treatment, enlarge the late presenter slightly, and keep the material visible throughout the concluding line. Use the established bundled fonts and semantic palettes, including the light-grey grid on every canvas. Keep the same image and motion geometry in every palette. Do not add decorative particles, extra glow, global blur or bounce. Supplied original media is the material; default demonstration content is not evidence of a real result.

Build in HyperFrames only. Review actual rendered frames at each change of focus and during the final hold. Frame-edge cropping and media overlap are intentional only where they serve the composition; essential text and interface targets must remain readable.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Raster slots used by the default scene: `document-1`, `document-2`, `document-3`, `document-4`. They load from the bundled image manifest when the user provides no replacements. Keep presenter video and any aligned alpha matte separate from these still-image defaults.

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

For footage, pass `--focus x,y`: the centre of the presenter's face as fractions of the footage frame (for example `0.52,0.38`). Extract one frame (`ffmpeg -ss 2 -i <take> -frames:v 1 /tmp/frame.png`), look at it and estimate the face centre. The effect uses it to centre the head in the region the presenter occupies. Use landscape footage for 16:9 and 4:3 and portrait footage for 9:16 and 3:4.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
