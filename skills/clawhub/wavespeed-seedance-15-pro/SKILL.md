---
name: wavespeed-seedance-15-pro
description: Generate videos using ByteDance's Seedance V1.5 Pro model via WaveSpeed AI. Supports text-to-video and image-to-video generation with 4-12 second duration at up to 1080p. Features audio generation, camera control, smart duration, and configurable seeds. Use when the user wants to create videos from text prompts or animate images.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Seedance V1.5 Pro Video Generation

Generate videos using ByteDance's Seedance V1.5 Pro model via the WaveSpeed AI platform. Supports both text-to-video and image-to-video generation with 4-12 second duration at up to 1080p resolution, with optional audio generation.

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

Prefer MCP tools over shell commands? The same platform is exposed by [`@wavespeed/mcp`](https://github.com/WaveSpeedAI/mcp-server) (`npx -y @wavespeed/mcp`; tools `search_models`, `get_model_schema`, `get_price`, `upload_file`, `run_model`, `get_prediction`). It shares the CLI's stored login. Every example below maps one-to-one onto `run_model` with the same model id and input fields.

## Quick Start

### Text-to-Video

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/text-to-video \
  -p "A golden retriever running through a field of sunflowers at sunset" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/image-to-video \
  -i image=@./photo.png \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/image-to-video \
  -i image="https://example.com/photo.jpg" \
  -p "The person slowly turns and smiles at the camera" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Text-to-Video

**Model ID:** `bytedance/seedance-v1.5-pro/text-to-video`

Generate videos from text prompts.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the scene, style, actions, camera motion, and mood |
| `aspect_ratio` | string | No | `16:9` | Aspect ratio. One of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `duration` | integer | No | `5` | Video duration in seconds. Range: 4-12. Use `-1` for smart duration (model selects). |
| `resolution` | string | No | `720p` | Video resolution. One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Generate accompanying audio |
| `camera_fixed` | boolean | No | `false` | Keep camera fixed (true) or allow prompt-driven camera motion (false) |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic slow pan" \
  -i aspect_ratio="21:9" \
  -i duration=10 \
  -i resolution="1080p" \
  -i generate_audio=true \
  -i camera_fixed=false \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `bytedance/seedance-v1.5-pro/image-to-video`

Animate a source image into a video using a text prompt. Optionally provide an end-frame reference image.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the source image to animate |
| `prompt` | string | Yes | -- | Text description of the desired motion/animation |
| `last_image` | string | No | -- | URL of an optional end-frame reference image |
| `aspect_ratio` | string | No | -- | Aspect ratio. One of: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `duration` | integer | No | `5` | Video duration in seconds. Range: 4-12 |
| `resolution` | string | No | `720p` | Video resolution. One of: `480p`, `720p`, `1080p` |
| `generate_audio` | boolean | No | `true` | Generate accompanying audio |
| `camera_fixed` | boolean | No | `false` | Keep camera fixed (true) or allow prompt-driven camera motion (false) |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/image-to-video \
  -i image=@./landscape.png \
  -p "Clouds drift slowly across the sky, water ripples gently" \
  -i resolution="1080p" \
  -i duration=8 \
  -i generate_audio=true \
  -i camera_fixed=true \
  --json | jq -r '.outputs[0]')
```

#### With End-Frame Reference

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedance-v1.5-pro/image-to-video \
  -i image=@./start-frame.png \
  -i last_image=@./end-frame.png \
  -p "Smooth transition from day to night" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')
```


## Pricing

| Resolution | Duration | Audio | Cost |
|------------|----------|-------|------|
| 480p | 5s | No | $0.06 |
| 480p | 5s | Yes | $0.12 |
| 720p | 5s | No | $0.13 |
| 720p | 5s | Yes | $0.26 |
| 480p | 10s | Yes | $0.24 |
| 720p | 10s | Yes | $0.52 |

## Prompt Tips

- Describe scene, style, subject actions, camera motion, and mood in your prompt
- Use `camera_fixed: true` for stable tripod-style shots
- Use `camera_fixed: false` and describe camera motion: "slow pan left", "tracking shot", "zoom in"
- Set `generate_audio: false` when you plan to add your own audio track
- Use smart duration (`duration: -1`) to let the model choose the best length for text-to-video

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run bytedance/seedance-v1.5-pro/text-to-video -h

# Quote the price first
wavespeed price bytedance/seedance-v1.5-pro/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run bytedance/seedance-v1.5-pro/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run bytedance/seedance-v1.5-pro/text-to-video -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
