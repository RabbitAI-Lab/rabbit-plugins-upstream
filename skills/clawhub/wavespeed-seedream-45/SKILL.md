---
name: wavespeed-seedream-45
description: Generate and edit images using ByteDance's Seedream V4.5 model via WaveSpeed AI. Supports text-to-image generation and multi-image editing with custom resolutions up to 4096x4096. Features enhanced typography for posters and logos. Use when the user wants to create or edit images with high-quality text rendering.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Seedream V4.5 Image Generation/Editing

Generate and edit images using ByteDance's Seedream V4.5 model via the WaveSpeed AI platform. Supports custom resolutions up to 4096x4096 with enhanced typography for sharp text rendering in posters and logos.

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
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5 \
  -p "A minimalist coffee shop logo with clean typography" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

The `images` parameter accepts an array of image URLs (1-10 images). For local files use the `@path` marker; the CLI uploads them for you.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5/edit \
  -i images='["@./photo.png"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5/edit \
  -i images='["https://example.com/photo.jpg"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Text-to-Image

**Model ID:** `bytedance/seedream-v4.5`

Generate images from text prompts with custom resolutions up to 4096x4096.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the image to generate |
| `size` | string | No | `2048*2048` | Output size in pixels (`WIDTH*HEIGHT`). Each dimension: 1024-4096. |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5 \
  -p "A movie poster for a sci-fi thriller with bold title text 'HORIZON' at the top" \
  -i size="2048*3072" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

**Model ID:** `bytedance/seedream-v4.5/edit`

Edit existing images using text prompts. Supports up to 10 input images. Preserves facial features, lighting, and color tone from input images.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `images` | string[] | Yes | `[]` | URLs of input images to edit (1-10 images). Must be publicly accessible. |
| `prompt` | string | Yes | -- | Text description of the desired edit |
| `size` | string | No | -- | Output size in pixels (`WIDTH*HEIGHT`). Each dimension: 1024-4096. |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5/edit \
  -i images='["@./portrait.png"]' \
  -p "Transform into a vibrant pop art style with bold colors" \
  -i size="2048*2048" \
  --json | jq -r '.outputs[0]')
```

#### Multi-Image Editing

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v4.5/edit \
  -i images='["@./face.png", "@./scene.png"]' \
  -p "Place the person from the first image into the scene from the second image" \
  --json | jq -r '.outputs[0]')
```


## Pricing

$0.04 per image (both generation and editing).

## Tips

- Seedream V4.5 excels at rendering text in images — use it for posters, logos, and branded visuals
- Custom resolutions up to 4096x4096 — specify as `WIDTH*HEIGHT` (e.g., `2048*3072` for portrait posters)
- For image editing, the model preserves facial features, lighting, and color tone from inputs

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run bytedance/seedream-v4.5 -h

# Quote the price first
wavespeed price bytedance/seedream-v4.5 -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run bytedance/seedream-v4.5 -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run bytedance/seedream-v4.5 -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
