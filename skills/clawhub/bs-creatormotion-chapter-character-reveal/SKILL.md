---
name: bs-creatormotion-chapter-character-reveal
description: A chapter label introduces a headline that becomes readable one character at a time. The completed phrase holds on a quiet full-screen stage.
---

# Chapter Character Reveal

Use this Skill when the brief needs chapter character reveal. Read `references/motion-spec.md` and `references/DESIGN.md` before adapting it. Ask only for essential missing content or media; use the included original example to demonstrate an unspecified detail.

## Create an editable project

1. Put the replacement content in a JSON object using the input names below.
2. Choose `white-yellow` by default, or `charcoal-lime` or `midnight-ice`. The three styles preserve the same motion and content.
3. Run `node scripts/create.mjs --out /absolute/output/path --data /absolute/content.json --style white-yellow --aspect 16:9 --resolution 4k`.
4. Render with the command printed by the generator, then inspect the start, main change and settled hold.

This is a graphic-only composition; a presenter file is not required.

## Aspect ratio, resolution and caption safe area

Settle these with the user before the first build and keep them for the whole series.

- **Aspect ratio**: `--aspect 16:9`, `9:16`, `4:3` or `3:4`. Each has its own native layout. With footage, read its size with ffprobe and use its ratio when it is one of the four; otherwise propose the nearest one (the footage is centre-cropped) and ask the user to confirm. Without footage, ask the user to choose.
- **Resolution**: always ask, recommending 4K. `--resolution 4k` (default, short side 2160), `2k` (1440) or `1080p` (1080): a 4K 9:16 segment is 2160×3840, a 4K 4:3 segment 2880×2160.
- **Caption safe area**: the bottom of the frame is kept free for the creator's subtitles (and the platform's captions and buttons on Shorts, Reels and TikTok). The effect places its text and graphics above it; do not move them into that band.

## Inputs

The effect exports the following complete original example. Change values rather than modifying animation selectors:

```json
{
  "label": "PART 03",
  "title": "Make feedback visible"
}
```

Title glyphs darken at fixed positions. A space is retained as a nonbreaking glyph to preserve readable word spacing. This is not a whole-headline slide.

## Motion invariants

The small label is established first; fixed-position headline glyphs change from faint to solid from left to right without moving the whole line.

A changed palette or different wording must not replace this movement with a generic card entrance. Keep the geometry, reveal order and layer persistence described in `references/motion-spec.md`.

## Validation

Run HyperFrames lint, validate and inspect in the generated project. Check contrast, readable bounds and deterministic seeking. Visually review all three styles in all four aspect ratios when changing the module. Inspect the actual rendered video; a successful HTML build is not visual acceptance. Keep all images, fonts, video and scripts local to the generated project.


## Reference-led shot treatment

A faint oversized diagonal typographic backdrop gives depth without a panel. The label is a hard-edged print strip and the 150px headline resolves rapidly in its final positions, followed by a completely stable reading hold. Follow the authored direction and timing in `references/motion-spec.md`. Keep replacement text within the same visual hierarchy.

## Typography

Smiley Sans (Deyi Hei) sets titles, copy and labels in every language, Latin and Chinese alike. It is one slanted display weight, so hierarchy comes from size, colour and spacing rather than weight. IBM Plex Mono sets axis ticks, ordinals, counters and small labels so numbers keep a stable width. Noto Sans SC stays behind Smiley Sans for rare Chinese characters; pass `--zh-font noto-sans-sc` to set Chinese content in Noto Sans SC instead. A supplied `--font` always wins. `build.json` records the choice under `typography`.

## Image material contract

Follow [the image policy](references/image-policy.md) before adapting visual content. Photos, covers, document imagery and chat avatars use actual raster assets. Without user references, reuse the generated defaults in [the slot map](references/default-image-slots.md); do not ask for every image. User-specified images replace the corresponding slots first. Keep typography, vector diagrams, masks and movement editable in HyperFrames. New image subjects require the available image-generation tool (image2 when exposed), with actual provider/model provenance; no silent HTML substitute. Required presenter video and aligned alpha mattes remain separate inputs.

---

## Part of Skillry · CreatorMotion

This skill is a free individual motion effect from **CreatorMotion** on [Skillry](https://skillry.dev).

- Looking for the full **CreatorMotion** master collection (122+ motion effects, automatic scene selection, and multi-clip assembly)? Explore [skillry.dev](https://skillry.dev).
- Connect Skillry MCP or browse all 87 free skills: `npx --yes skillry-cli@latest mcp` · [github.com/yihui-dev/skillry-skills](https://github.com/yihui-dev/skillry-skills)
