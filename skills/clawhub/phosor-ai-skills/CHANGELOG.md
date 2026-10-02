# Changelog

Skill package versions. The API contract version is separate and lives in
`SKILL.md` as `metadata.api_version` — a skill release does not move it.

## 1.3.2 — 2026-09-25 (API v1.2.2)

`minimax/h3/reference-to-video/turbo` removed

- Requests to `minimax/h3/reference-to-video/turbo` now return an unknown-model error
- Use `minimax/h3/reference-to-video` instead — same inputs and pricing structure
- `reference-to-video` (non-turbo) is unaffected
- API contract version v1.2.2: a model id was removed; no other endpoints or parameters changed

## 1.3.1 — 2026-09-24 (API v1.2.1)

Reference-to-Video limits and pricing

- Reference caps, both 480p and 768p: 9 images when sending only images, 5 images when
  videos or audio are also present, 3 reference videos, 3 reference audios
- Total reference video length is 15.1s across all reference videos
- `reference-to-video` now uses the same rates as the rest of H3: 480p $0.0045/s,
  768p $0.012/s, reference images $0.0075 each after the first 5
- Bundled client validation and version string updated to match
- API contract version v1.2.1: Reference-to-Video limits and pricing changed; no new endpoints or parameters

## 1.3.0 — 2026-09-22 (API v1.2.0)

Reference metadata and H3 limits

- Reference labels are forwarded in the same order as image, video, and audio URLs
- 768p Ref2VA supports the same 9 image-only, 4 mixed-image, and 3 video caps as 480p
- Correct the bundled client's stale 768p validation and 15-second video budget

## 1.2.0 — 2026-09-13 (API v1.2.0)

Reference-to-Video

- Total reference video length raised from 10s to 15s, across all reference
  videos combined. `reference-to-video/turbo` is unchanged at 10s.
- No other caps moved, and pricing is unchanged.

## 1.2.0 — 2026-09-10

Pricing

- MiniMax H3 (T2V / I2V / Ref2VA / Ref2VA Turbo) now shares one per-output-second
  rate regardless of clip length: 480p $0.0045/s, 768p $0.012/s (previously 0.02 / 0.04 USD
  for T2V/I2V and 0.025 / 0.063 USD for Ref2VA)
- Ref2VA reference inputs: the first 5 reference images are free, then $0.0075 each
  (previously 0.01 USD from the first image); reference audio is free (previously 0.01 USD);
  reference video stays at the output tier rate
- `GET /api/v1/pricing/config` adds `reference_image_free_count`; the built-in
  client's price table and estimate formula follow it

Reference-to-Video Turbo

- `minimax/h3/reference-to-video/turbo` added to the model table with its own reference
  caps and 768p usage guidance (stay at or below 3 images, or 2 images plus 1 video)

Client and docs

- Environment section and `--base-url` help use placeholders instead of a specific host
- `studio-layouts` on a self-hosted deployment reads `PHOSOR_WEB_BASE_URL` for the web
  front instead of guessing ports
- Code comments in `phosor_client.py` are English throughout

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

- Advertises all five GPT Image 2 sizes; the previous release listed only
  1024x1024 and rejected the other four valid sizes
- `--version` now prints the real package version

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
