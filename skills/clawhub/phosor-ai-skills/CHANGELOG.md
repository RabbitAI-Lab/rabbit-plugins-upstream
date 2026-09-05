# Changelog

Skill package versions. The API contract version is separate and lives in
`SKILL.md` as `metadata.api_version` — a skill release does not move it.

## 1.1.0 — 2026-09-03

New models

- MiniMax H3: text-to-video, image-to-video with an optional closing frame,
  and Reference-to-Video, which takes reference images, videos and audio in
  one request. 480p and 768p, 4-15 seconds, billed per output second
- GPT Image 2 text-to-image, at five sizes: 1024x1024, 1920x1072 / 1072x1920
  and 2560x1440 / 1440x2560
- FLUX.2-dev text-to-image and image edit
- Z-Image Turbo text-to-image and image-to-image, with LoRA
- Qwen3-TTS text-to-speech, billed per character, minimum $0.003 per request

New surface

- Image Studio, for e-commerce product and model photography: product suites,
  clothing and on-model suites, selling-point layouts, A+ content, white
  background, scene variation, and one-off tools for background removal,
  inpainting and image translation. Async throughout: POST returns a
  request_id, then poll until done

Client

- Advertises all five GPT Image 2 sizes. It had been cut to 1024x1024 while
  the gateway whitelist was temporarily narrowed during an upstream-size
  investigation; the gateway went back to five and the client did not, so
  agents were told four valid sizes were invalid
- `--version` now prints the real package version. It reported 0.3.0 for
  three releases while this registry showed 1.0.2

Packaging

- The package and its zip are named phosor-ai-skills, matching the folder it
  unpacks into and this skill's slug
- Two version numbers, on purpose: the skill version covers this package
  (commands, docs, bundled client), `metadata.api_version` covers the gateway
  contract. Either can move without forcing the other
- A stray compiled .pyc no longer rides along inside the archive

Docs

- `references/api.md` covers every endpoint the skill calls, with limits and
  live pricing pointers. Prices are never hardcoded — call the pricing
  endpoints for current numbers

## 1.0.2 / 1.0.1 — 2026-05

Published without changelog entries; both carried the 1.0.0 text. Recorded
here so the gap is visible rather than implied.

## 1.0.0 — 2026-03-23 — Initial release

- AI content generation platform, supporting Wan 2.2 14B text-to-video and
  image-to-video
- Upload and use custom LoRA models for style customization
- 16 CLI commands for job submission, uploads, status, results, and model
  listing
- Supports preset resolutions (480p/720p/1080p), frame alignment rules, and
  usage quotas
