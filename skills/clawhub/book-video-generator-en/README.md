# 3-Minute Book Digest (English Version)

An English fork of the **三分钟精读一本书** book-video generator. Given a book
title + author, it produces a ~3-minute book-explainer video entirely in English:
review script → storyboard → AI illustrations → English TTS narration → subtitles → MP4.

## What's different from the Chinese version

| Area | Chinese version | This version (`book-video-generator-en`) |
|------|-----------------|------------------------------------------|
| Review script / storyboard prompts | Chinese (`references/prompts.md`) | **English** |
| On-screen text (subtitles, chapter titles, cover) | Chinese | **English** |
| TTS narration | Chinese voices (`zh_female_zhixingnv…` / `zh-CN-XiaoxiaoNeural`) | **English voices** (`en_us_amy` / `en-US-AriaNeural`) |
| Cover brand text | "3 分钟精读一本书" | "3-MINUTE BOOK DIGEST" |
| Fonts | Microsoft YaHei / PingFang / Noto CJK | Arial / Helvetica / DejaVu Sans |
| Subtitle line length | ~16 chars/line | ~42 chars/line, word-boundary wrapping |
| Output file | `{book}_三分钟精读书.mp4` | `{book}_3min_digest.mp4` |

## Workflow

1. **Stage 1** — LLM writes a ~1000-word English review script (web-search backed).
2. **Stage 2** — LLM splits it into 8–50 storyboard shots (caption + visual + image prompt).
3. **Stage 3** — LLM derives 4 ≤6-word section titles for the progress bar.
4. **Stage 4** — generate illustrations (ImageGen / Volcano / Gemini / Agnes), English TTS audio, and the opening cover.
5. **Stage 5** — `compose_video.py` composites everything into the final MP4.

See `SKILL.md` for the full guide, and `references/CROSS_PLATFORM.md` for
install + tool-adaptation steps on OpenClaw, Codex CLI, TRAE Work, Claude Code, etc.

## Requirements

```bash
pip install edge-tts imageio-ffmpeg pillow
```

- TTS: edge-tts works out of the box (no key). Set `VOLC_TTS_API_KEY` to use Volcano Engine TTS instead.
- Image generation: WorkBuddy uses the built-in `ImageGen` by default; CLI platforms use `scripts/generate_image.py` with `IMAGE_API`.
- Background music / transition SFX in `assets/` are optional.

## Troubleshooting

- **Stage 5 `compose_video.py` exits 1 with no traceback (silent kill).** The
  full ~3-minute 1080p re-encode is memory/CPU heavy and gets killed by the
  Bash sandbox. Run it with the sandbox bypassed (local ffmpeg only, no network
  needed): `python scripts/compose_video.py < segments.json` executed outside the
  sandbox. Or raise the sandbox resource limits before running.
- **Two image generations failed with `RequestLimitExceeded.JobNumExceed`.**
  The image provider caps concurrent jobs; just retry the failed shots after a
  moment. Order them into `scene_NNN.png` afterward.
- **TTS uses edge-tts (English) by default** because no `VOLC_TTS_API_KEY` is
  set. Set the key to switch to Volcano Engine TTS (`en_us_amy`).

## Files

- `SKILL.md` — skill spec and full workflow
- `references/prompts.md` — all LLM prompts (English)
- `references/CROSS_PLATFORM.md` — install/adapt for OpenClaw, Codex CLI, TRAE Work, Claude Code
- `references/workflow-original.yaml` — original Coze workflow backup
- `scripts/compose_video.py` — video composition (ffmpeg + ASS subtitles)
- `scripts/generate_audio.py` — English TTS (Volcano / edge-tts)
- `scripts/generate_cover.py` — cover image generator
- `scripts/generate_image.py` — multi-provider image generation
