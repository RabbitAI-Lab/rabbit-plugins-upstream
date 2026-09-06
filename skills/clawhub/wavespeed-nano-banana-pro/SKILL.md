---
name: wavespeed-nano-banana-pro
description: Generate and edit images using Google's Nano Banana Pro model via WaveSpeed AI. Supports text-to-image generation and image editing with natural language prompts. Features native 4K resolution, flexible aspect ratios, multilingual text rendering, and camera-style controls. Use when the user wants to create images from text or edit existing images.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Nano Banana Pro Image Generation/Editing

Generate and edit images using Google's Nano Banana Pro model via the WaveSpeed AI platform. Supports both text-to-image generation and natural-language image editing with up to 14 input images.

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

### Text-to-Image

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/text-to-image \
  -p "A serene Japanese garden with cherry blossoms, watercolor style" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

The `images` parameter accepts an array of image URLs. For local files use the `@path` marker; the CLI uploads them for you.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/edit \
  -i images='["@./photo.png"]' \
  -p "Replace the sky with a dramatic sunset" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/edit \
  -i images='["https://example.com/photo.jpg"]' \
  -p "Replace the sky with a dramatic sunset" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Text-to-Image

**Model ID:** `google/nano-banana-pro/text-to-image`

Generate images from text prompts.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the image to generate |
| `aspect_ratio` | string | No | -- | Output aspect ratio. One of: `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` |
| `resolution` | string | No | `1k` | Image resolution. One of: `1k`, `2k`, `4k` |
| `output_format` | string | No | `png` | Output format. One of: `png`, `jpeg` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/text-to-image \
  -p "A red vintage Porsche 911 on a winding mountain road at golden hour, photorealistic" \
  -i aspect_ratio="16:9" \
  -i resolution="2k" \
  -i output_format="png" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

**Model ID:** `google/nano-banana-pro/edit`

Edit existing images using natural language prompts. Supports up to 14 input images.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `images` | string[] | Yes | `[]` | URLs of input images to edit (1-14 images) |
| `prompt` | string | Yes | -- | Text description of the desired edit |
| `aspect_ratio` | string | No | -- | Output aspect ratio. One of: `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` |
| `resolution` | string | No | `1k` | Image resolution. One of: `1k`, `2k`, `4k` |
| `output_format` | string | No | `png` | Output format. One of: `png`, `jpeg` |

#### Example

```bash
# Upload local images first, or use existing URLs
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/edit \
  -i images='["@./living-room.png"]' \
  -p "Change the wall color to warm terracotta and add indoor plants" \
  -i aspect_ratio="16:9" \
  -i resolution="4k" \
  -i output_format="png" \
  --json | jq -r '.outputs[0]')
```

#### Multi-Image Editing

```bash
# Upload multiple local images
OUTPUT_URL=$(wavespeed run google/nano-banana-pro/edit \
  -i images='["@./face.png", "@./hairstyle.png"]' \
  -p "Apply the hairstyle from the second image to the person in the first image" \
  --json | jq -r '.outputs[0]')
```


## Aspect Ratio Options

| Aspect Ratio | Use Case |
|-------------|----------|
| `1:1` | Square — social media posts, profile pictures |
| `3:2` | Landscape — standard photography |
| `2:3` | Portrait — standard photography |
| `3:4` | Portrait — social media, product images |
| `4:3` | Landscape — presentations, web content |
| `4:5` | Portrait — Instagram posts |
| `5:4` | Landscape — print, web banners |
| `9:16` | Vertical — mobile wallpapers, stories |
| `16:9` | Widescreen — desktop wallpapers, video thumbnails |
| `21:9` | Ultra-wide — cinematic, panoramic |

## Resolution and Pricing

| Resolution | Cost |
|------------|------|
| 1k | $0.14 per image |
| 2k | $0.14 per image |
| 4k | $0.24 per image |

## Prompt Tips

- Be specific and descriptive: "A red vintage Porsche 911 on a winding mountain road at golden hour" vs "a car"
- Include style keywords: "digital art", "oil painting", "photorealistic", "watercolor", "cinematic"
- For edits, clearly describe the desired change: "Replace the sky with a dramatic sunset"
- For multi-image edits, reference images by position: "Apply the style from the second image to the first image"
- Leverage multilingual text rendering: the model supports on-image text with automatic translation
- Use camera-style control language: "shallow depth of field", "wide angle", "top-down view"

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run google/nano-banana-pro/text-to-image -h

# Quote the price first
wavespeed price google/nano-banana-pro/text-to-image -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run google/nano-banana-pro/text-to-image -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run google/nano-banana-pro/text-to-image -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
