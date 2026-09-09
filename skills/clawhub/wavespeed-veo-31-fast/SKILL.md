---
name: wavespeed-veo-31-fast
description: Generate and extend videos using Google's Veo 3.1 Fast model via WaveSpeed AI. Supports text-to-video, image-to-video, and video extension. Features up to 4K resolution, audio generation, and chained extensions up to 148 seconds. Use when the user wants to create videos from text or images, or extend existing Veo-generated videos.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Veo 3.1 Fast Video Generation

Generate and extend videos using Google's Veo 3.1 Fast model via the WaveSpeed AI platform. Supports text-to-video, image-to-video, and video extension with up to 4K resolution and optional audio generation.

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
OUTPUT_URL=$(wavespeed run google/veo3.1-fast/text-to-video \
  -p "A drone shot flying over a lush tropical island at sunrise" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
OUTPUT_URL=$(wavespeed run google/veo3.1-fast/image-to-video \
  -i image=@./photo.png \
  -p "The flowers sway gently in the breeze" \
  --json | jq -r '.outputs[0]')
```

### Video Extend

Extend a Veo-generated video by 7 seconds per run (up to 20 extensions, 148 seconds total):

```bash
# First, generate a video
VIDEO_URL=$(wavespeed run google/veo3.1-fast/text-to-video \
  -p "A cat walking through a garden" \
  --json | jq -r '.outputs[0]')

# Then extend it
EXTENDED_URL=$(wavespeed run google/veo3.1-fast/video-extend \
  -i video="$VIDEO_URL" \
  -p "The cat jumps onto a fence and looks around" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Text-to-Video

**Model ID:** `google/veo3.1-fast/text-to-video`

Generate videos from text prompts with optional audio.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the video to generate |
| `aspect_ratio` | string | No | `16:9` | Aspect ratio. One of: `16:9`, `9:16` |
| `duration` | integer | No | `8` | Duration in seconds. One of: `4`, `6`, `8` |
| `resolution` | string | No | `1080p` | Video resolution. One of: `720p`, `1080p`, `4k` |
| `generate_audio` | boolean | No | `true` | Generate accompanying audio |
| `negative_prompt` | string | No | -- | Text describing unwanted elements |
| `seed` | integer | No | -- | Random seed for reproducibility. Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run google/veo3.1-fast/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic" \
  -i negative_prompt="blurry, low quality" \
  -i aspect_ratio="16:9" \
  -i duration=8 \
  -i resolution="1080p" \
  -i generate_audio=true \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `google/veo3.1-fast/image-to-video`

Animate a source image into a video. Optionally provide an end-frame reference image.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the source image (clear, high-quality still image) |
| `prompt` | string | Yes | -- | Text description of the desired motion/animation |
| `last_image` | string | No | -- | URL of an end-frame reference image |
| `aspect_ratio` | string | No | `16:9` | Aspect ratio. One of: `16:9`, `9:16` |
| `duration` | integer | No | `8` | Duration in seconds. One of: `4`, `6`, `8` |
| `resolution` | string | No | `1080p` | Video resolution. One of: `720p`, `1080p`, `4k` |
| `generate_audio` | boolean | No | `true` | Generate accompanying audio |
| `negative_prompt` | string | No | -- | Text describing unwanted elements |
| `seed` | integer | No | -- | Random seed for reproducibility. Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run google/veo3.1-fast/image-to-video \
  -i image=@./landscape.png \
  -p "Clouds drift slowly across the sky, water ripples gently" \
  -i resolution="1080p" \
  -i duration=8 \
  -i generate_audio=true \
  --json | jq -r '.outputs[0]')
```

#### With End-Frame Reference

```bash
OUTPUT_URL=$(wavespeed run google/veo3.1-fast/image-to-video \
  -i image=@./start-frame.png \
  -i last_image=@./end-frame.png \
  -p "Smooth transition from day to night" \
  --json | jq -r '.outputs[0]')
```

### Video Extend

**Model ID:** `google/veo3.1-fast/video-extend`

Extend a Veo-generated video by 7 seconds per run. Input must be a Veo-generated video.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the Veo-generated video to extend. Max 141 seconds. |
| `prompt` | string | No | -- | Text guidance for the extension |
| `resolution` | string | No | `1080p` | Video resolution. One of: `720p`, `1080p` |
| `negative_prompt` | string | No | -- | Text describing unwanted elements |
| `seed` | integer | No | -- | Random seed for reproducibility. Range: -1 to 2147483647 |

#### Constraints

- Input video **must be Veo-generated** (will not work with arbitrary videos)
- Each run adds **+7 seconds** to the video
- Maximum **20 extensions** in a chain
- Maximum final video length: **148 seconds**
- Output is a single MP4 (original + extension appended)
- Aspect ratio and resolution are inherited from the input video

#### Example

```bash
# Generate an initial video
VIDEO_URL=$(wavespeed run google/veo3.1-fast/text-to-video \
  -p "A surfer catches a wave at golden hour" \
  -i duration=8 \
  --json | jq -r '.outputs[0]')

# Extend it twice
EXTENDED_ONCE=$(wavespeed run google/veo3.1-fast/video-extend \
  -i video="$VIDEO_URL" \
  -p "The surfer rides the wave toward shore" \
  --json | jq -r '.outputs[0]')

EXTENDED_TWICE=$(wavespeed run google/veo3.1-fast/video-extend \
  -i video="$EXTENDED_ONCE" \
  -p "The surfer steps off the board and walks on the beach" \
  --json | jq -r '.outputs[0]')
```


## Pricing

### Text-to-Video / Image-to-Video

| Condition | Cost |
|-----------|------|
| With audio (720p or 1080p) | $1.20 per generation |
| Without audio (720p or 1080p) | $0.80 per generation |

### Video Extend

| Condition | Cost |
|-----------|------|
| Per run (+7 seconds) | $1.05 |

## Prompt Tips

- Be specific about scene, style, subject actions, camera motion, and mood
- Use `negative_prompt` to avoid artifacts: "blurry, low quality, distorted"
- For image-to-video, use a clear, high-quality still image as input
- For video extend, describe what should happen next in the scene
- Video extend chains enable building longer narratives — up to 148 seconds total

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run google/veo3.1-fast/text-to-video -h

# Quote the price first
wavespeed price google/veo3.1-fast/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run google/veo3.1-fast/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run google/veo3.1-fast/text-to-video -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
