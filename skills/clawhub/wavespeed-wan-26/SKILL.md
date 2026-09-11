---
name: wavespeed-wan-26
description: Generate videos using Alibaba's Wan 2.6 model via WaveSpeed AI. Supports text-to-video and image-to-video generation with up to 15 seconds duration at 720p or 1080p. Features audio-guided generation, prompt expansion, multi-shot mode, and configurable seeds. Use when the user wants to create videos from text prompts or animate images.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Wan 2.6 Video Generation

Generate videos using Alibaba's Wan 2.6 model via the WaveSpeed AI platform. Supports both text-to-video and image-to-video generation with up to 15 seconds of video at up to 1080p resolution.

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
OUTPUT_URL=$(wavespeed run alibaba/wan-2.6/text-to-video \
  -p "A golden retriever running through a field of sunflowers at sunset" \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

The `image` parameter accepts an image URL. If you have a local file, pass it with the `@path` marker and the CLI uploads it and substitutes the hosted URL.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run alibaba/wan-2.6/image-to-video \
  -i image=@./photo.png \
  -p "The person in the photo slowly turns and smiles" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-2.6/image-to-video \
  -i image="https://example.com/photo.jpg" \
  -p "The person in the photo slowly turns and smiles" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Text-to-Video

**Model ID:** `alibaba/wan-2.6/text-to-video`

Generate videos from text prompts.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the video to generate |
| `negative_prompt` | string | No | -- | Text description of what to avoid in the video |
| `audio` | string | No | -- | Audio URL to guide generation |
| `size` | string | No | `1280*720` | Output size in pixels. One of: `1280*720`, `720*1280`, `1920*1080`, `1080*1920` |
| `duration` | integer | No | `5` | Video duration in seconds. One of: `5`, `10`, `15` |
| `shot_type` | string | No | `single` | Shot type. One of: `single`, `multi` |
| `enable_prompt_expansion` | boolean | No | `false` | Enable prompt optimizer for enhanced prompts |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-2.6/text-to-video \
  -p "A timelapse of a city skyline transitioning from day to night, cinematic" \
  -i negative_prompt="blurry, low quality, distorted" \
  -i size="1920*1080" \
  -i duration=10 \
  -i shot_type="single" \
  -i seed=42 \
  --json | jq -r '.outputs[0]')
```

### Image-to-Video

**Model ID:** `alibaba/wan-2.6/image-to-video`

Animate a source image into a video using a text prompt.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the source image to animate |
| `prompt` | string | Yes | -- | Text description of the desired motion/animation |
| `negative_prompt` | string | No | -- | Text description of what to avoid in the video |
| `audio` | string | No | -- | Audio URL to guide generation |
| `resolution` | string | No | `720p` | Output resolution. One of: `720p`, `1080p` |
| `duration` | integer | No | `5` | Video duration in seconds. One of: `5`, `10`, `15` |
| `shot_type` | string | No | `single` | Shot type. One of: `single`, `multi` |
| `enable_prompt_expansion` | boolean | No | `false` | Enable prompt optimizer for enhanced prompts |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

#### Example

```bash
OUTPUT_URL=$(wavespeed run alibaba/wan-2.6/image-to-video \
  -i image=@./landscape.png \
  -p "Clouds drift slowly across the sky, water ripples gently" \
  -i negative_prompt="static, frozen, blurry" \
  -i resolution="1080p" \
  -i duration=10 \
  -i shot_type="single" \
  --json | jq -r '.outputs[0]')
```


## Size Options (Text-to-Video)

| Size | Orientation | Use Case |
|------|-------------|----------|
| `1280*720` | Landscape 720p | Standard widescreen video |
| `720*1280` | Portrait 720p | Mobile/vertical video, stories |
| `1920*1080` | Landscape 1080p | Full HD widescreen video |
| `1080*1920` | Portrait 1080p | Full HD vertical video |

## Resolution Options (Image-to-Video)

| Resolution | Use Case |
|------------|----------|
| `720p` | Standard quality, faster generation |
| `1080p` | Full HD, higher quality |

## Pricing

| Resolution | 5 seconds | 10 seconds | 15 seconds |
|------------|-----------|------------|------------|
| 720p | $0.50 | $1.00 | $1.50 |
| 1080p | $0.75 | $1.50 | $2.25 |

## Prompt Tips

- Be specific about motion and action: "A bird takes flight from a branch" vs "a bird"
- Include camera movement: "slow pan left", "zoom in", "tracking shot"
- Describe temporal progression: "transitioning from day to night", "flowers slowly blooming"
- Use `negative_prompt` to avoid artifacts: "blurry, low quality, distorted, static"
- Enable `enable_prompt_expansion` for automatic prompt enhancement
- For `multi` shot type, describe distinct scenes for more dynamic videos

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run alibaba/wan-2.6/text-to-video -h

# Quote the price first
wavespeed price alibaba/wan-2.6/text-to-video -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run alibaba/wan-2.6/text-to-video -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run alibaba/wan-2.6/text-to-video -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
