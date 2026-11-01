---
name: wavespeed-wan-30
description: Generate and edit videos with Alibaba Wan 3.0 and its Wan 3.0 Prime tier via WaveSpeed AI. Covers text-to-video, image-to-video (first and last frame), reference-to-video (images, videos and audio), video edit and video extend, with 2-30 second clips at 480p, 720p or 1080p, optional audio, prompt expansion and seeds. Use when the user asks for Wan 3.0 or Wan 3.0 Prime, or wants to create a video from a prompt, animate an image, build a clip from reference media, edit an existing video, or continue a clip.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI Wan 3.0 Video Generation

Generate and edit videos with Alibaba's Wan 3.0 on the WaveSpeed AI platform. Text, image and reference inputs produce 2-30 second clips at 480p, 720p or 1080p with optional audio; video edit changes an existing clip and video extend appends a new segment. Every endpoint is also offered as Wan 3.0 Prime under `alibaba/wan-3.0-prime/*`, with the same input fields at a higher price.

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

Prefer MCP tools over shell commands? The same platform is exposed as an MCP server: hosted at `https://api.wavespeed.ai/mcp` (browser sign-in) or locally with `npx -y @wavespeed/mcp@latest`; every example below maps onto `run_model` with the same model id and input fields.

## Quick Start

The shortcut commands use the same model and pick the endpoint from the inputs: `wavespeed generate video "<prompt>" -m wan-3.0` (or `-m wan-3.0-prime`), and likewise `wavespeed edit video` and `wavespeed extend video`; the MCP tools `generate_video`, `edit_video` and `extend_video` take the same `model` value (confirm the keys with `wavespeed generate video --help`). Add `--estimate --json` first to see the chosen endpoint, final input and price without submitting.

```bash
wavespeed generate video "A paper boat drifting down a rain-soaked street" -m wan-3.0 --estimate --json
```

### Text-to-Video

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/text-to-video \
  -p "A golden retriever running through a field of sunflowers at sunset, slow tracking shot" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/image-to-video \
  -i image=@./photo.png \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/image-to-video \
  -i image="https://example.com/photo.jpg" \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

Each endpoint below exists in both tiers: replace `alibaba/wan-3.0/` with `alibaba/wan-3.0-prime/` for Prime; the parameters are identical. Every endpoint also takes `enable_prompt_expansion` (boolean, default `false`, turns on the prompt optimizer) and `seed` (integer, `-1` for random). The catalog also lists `image-to-video-spicy` in both tiers (same inputs as image-to-video, prompt optional).

### Text-to-Video

**Model ID:** `alibaba/wan-3.0/text-to-video` (Prime: `alibaba/wan-3.0-prime/text-to-video`)

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | What to generate |
| `aspect_ratio` | string | No | `16:9` | One of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `duration` | integer | No | `5` | Seconds. Range: 2-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Include audio in the video |
| `enable_prompt_expansion` | boolean | No | `false` | Enable the prompt optimizer |
| `seed` | integer | No | -- | Random seed; `-1` for random |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic slow pan" \
  -i duration=10 \
  -i resolution="1080p" \
  -i seed=42 \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `alibaba/wan-3.0/image-to-video` (Prime: `alibaba/wan-3.0-prime/image-to-video`)

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | First-frame image (URL or Base64) |
| `prompt` | string | Yes | -- | Motion and scene description |
| `last_image` | string | No | -- | Last-frame image (URL or Base64) |
| `aspect_ratio` | string | No | -- | One of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`. Adapts to the input image if not set |
| `duration` | integer | No | `5` | Seconds. Range: 2-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Include audio in the video |
| `enable_prompt_expansion` | boolean | No | `false` | Enable the prompt optimizer |
| `seed` | integer | No | -- | Random seed; `-1` for random |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0-prime/image-to-video \
  -i image=@./start-frame.png \
  -i last_image=@./end-frame.png \
  -p "Smooth transition from day to night as the lights come on" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```

### Reference-to-Video

**Model ID:** `alibaba/wan-3.0/reference-to-video` (Prime: `alibaba/wan-3.0-prime/reference-to-video`)

At least one reference image, video or audio is required. In the prompt, refer to inputs as `Image 1`, `Video 1`, `Audio 1`, ..., numbered per type in array order.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Scene description that names each reference |
| `reference_images` | string[] | No | -- | Up to 10 image URLs |
| `reference_videos` | string[] | No | -- | Up to 5 video URLs: MP4 or MOV, 1-15 s each, 240-4096 px per side, at most 8:1, at most 100 MB; total at most 15 s |
| `reference_audios` | string[] | No | -- | Up to 5 audio URLs; total at most 15 s |
| `aspect_ratio` | string | No | `16:9` | One of: `16:9`, `9:16`, `1:1`, `4:3`, `3:4` |
| `duration` | integer | No | `5` | Seconds, 2-30. With reference videos, input video length plus output length must not exceed 30 s |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Include audio in the video |
| `enable_prompt_expansion` | boolean | No | `false` | Enable the prompt optimizer |
| `seed` | integer | No | -- | Random seed; `-1` for random |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/reference-to-video \
  -i reference_images='["@./character.png", "@./product.png"]' \
  -p "The woman from Image 1 picks up the bottle from Image 2 and shows it to the camera, warm morning light" \
  -i aspect_ratio="9:16" \
  --json | jq -r '.outputs[0]')
```

### Video Edit

**Model ID:** `alibaba/wan-3.0/video-edit` (Prime: `alibaba/wan-3.0-prime/video-edit`)

Edits a video from a prompt with optional reference images and audio. Videos longer than 15 s are trimmed to 15 s; the output aspect ratio follows the input.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to edit |
| `prompt` | string | Yes | -- | The edit to apply |
| `reference_images` | string[] | No | -- | Up to 10 image URLs to guide the edit |
| `reference_audios` | string[] | No | -- | Up to 5 audio URLs; total at most 15 s |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Generate new audio; `false` keeps the input video's audio track |
| `enable_prompt_expansion` | boolean | No | `false` | Enable the prompt optimizer |
| `seed` | integer | No | -- | Random seed; `-1` for random |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/video-edit \
  -i video=@./street.mp4 \
  -p "Turn the scene into a snowy winter evening, keep the people and their motion" \
  -i generate_audio=false \
  --json | jq -r '.outputs[0]')
```

### Video Extend

**Model ID:** `alibaba/wan-3.0/video-extend` (Prime: `alibaba/wan-3.0-prime/video-extend`)

Continues a video from its final frame and appends the new segment; the output is the source plus the new segment, and existing source audio is kept. Inputs longer than 120 s keep their last 120 s.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | Source video URL |
| `prompt` | string | Yes | -- | The continuation |
| `last_image` | string | No | -- | Last-frame image for the new segment (URL or Base64) |
| `duration` | integer | No | `5` | Length of the new segment in seconds. Range: 2-30 |
| `resolution` | string | No | `720p` | One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Generate audio for the new segment |
| `enable_prompt_expansion` | boolean | No | `false` | Enable the prompt optimizer |
| `seed` | integer | No | -- | Random seed; `-1` for random |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-3.0/video-extend \
  -i video=@./clip.mp4 \
  -p "The camera pulls back to reveal the whole valley as the sun sets" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```

## Pricing

Estimates for a 5-second clip; cost scales with duration (10 s at 720p is $1.00 standard, $1.50 Prime) and turning off `generate_audio` does not change it. Video edit is priced on the input video, so its row assumes a 5-second input; a 5-second reference video in reference-to-video costs $1.00 (standard) or $1.50 (Prime) at 720p. Quote exact inputs with `wavespeed price <model-id> ... --upload`. Prices may change; see `https://wavespeed.ai/models/<model-id>` (e.g. [text-to-video](https://wavespeed.ai/models/alibaba/wan-3.0/text-to-video), [Prime](https://wavespeed.ai/models/alibaba/wan-3.0-prime/text-to-video)).

| Endpoint | Tier | 480p | 720p | 1080p |
|----------|------|------|------|-------|
| text / image / reference-to-video (images), video-extend | Wan 3.0 | $0.25 | $0.50 | $1.00 |
| text / image / reference-to-video (images), video-extend | Prime | $0.375 | $0.75 | $1.50 |
| video-edit (5 s input) | Wan 3.0 | $0.50 | $1.00 | $2.00 |
| video-edit (5 s input) | Prime | $0.75 | $1.50 | $3.00 |

## Prompt Tips

- Describe subject, action, camera movement, style and the sound you want
- Turn on `enable_prompt_expansion` for short prompts you want the optimizer to flesh out; leave it off when you need the prompt followed literally
- Fix `seed` to reproduce a take while you adjust other inputs
- In reference-to-video, name inputs as `Image 1`, `Video 1`, `Audio 1` and keep reference videos and audio within 15 s in total
- Draft on Wan 3.0 at 480p, then move to the `alibaba/wan-3.0-prime/` endpoint or a higher resolution for the final take

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run alibaba/wan-3.0/text-to-video -h

# Estimate the cost (no generation, no charge)
wavespeed price alibaba/wan-3.0/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run alibaba/wan-3.0/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run alibaba/wan-3.0/text-to-video -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

A `run` that fails with a gateway or network error (502/503/504, connection reset, timeout) does NOT mean the task failed, and the submit request is never retried automatically, so re-running can create a duplicate paid task. Do not re-run immediately. If the error contains a task id (`task_id` / prediction id), keep checking it with `wavespeed show <id> --json` until its status is terminal (`completed`, `failed`, `cancelled`, `timeout`, `deleted`). If no id was returned, check recent predictions with `wavespeed history --json` (add `--model <id>`; default window is the last 24h) and re-run once only if none matches. A client-side wait timeout or an interrupted `run` does not mean the task failed: tasks can run for a long time, so do not give up after a fixed time.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
