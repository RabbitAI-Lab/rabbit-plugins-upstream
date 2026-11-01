---
name: wavespeed-nano-banana-21
description: Generate and edit images using Google's Nano Banana 2.1 via WaveSpeed AI. The latest Nano Banana model, with gains in visual design, subject consistency and prompt adherence. Supports text-to-image and editing with up to 14 reference images, 1k / 2k / 4k output, 14 aspect ratios (including 1:4, 4:1, 1:8 and 8:1) and optional web search and image search grounding. Use when the user wants to create images from a prompt or edit and combine existing images with Nano Banana 2.1.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI Nano Banana 2.1 Image Generation/Editing

Generate and edit images using Google's Nano Banana 2.1 via the WaveSpeed AI platform. The latest Nano Banana model, with gains in visual design, subject consistency and prompt adherence, 1k to 4k output, up to 14 reference images for editing, and optional web/image search grounding.

## Setup

Install the open-source CLI once and sign in; the CLI stores the key, so never ask the user to paste an API key into the chat:

```bash
npm install -g @wavespeed/cli
wavespeed login          # opens https://wavespeed.ai/accesskey and stores the key
wavespeed status         # confirms you are signed in
```

For CI or one-off shells, `WAVESPEED_API_KEY` in the environment also works.

The same platform is exposed as an MCP server: hosted at `https://api.wavespeed.ai/mcp` (browser sign-in) or locally with `npx -y @wavespeed/mcp@latest`; every example below maps onto `run_model` with the same model id and input fields.

## Quick Start

### Text-to-Image

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/text-to-image \
  -p "A minimalist coffee shop logo with clean typography" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

The `images` parameter accepts an array of image URLs (1-14 images). For local files use the `@path` marker; the CLI uploads them for you.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/edit \
  -i images='["@./photo.png"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/edit \
  -i images='["https://example.com/photo.jpg"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

### Shortcut commands

`wavespeed generate image "<prompt>" -m nano-banana-2.1` and `wavespeed edit image "<prompt>" --image @./photo.png -m nano-banana-2.1` (MCP `generate_image` / `edit_image` with `model: "nano-banana-2.1"`) use the same model and pick the endpoint automatically.

## API Endpoints

### Text-to-Image

**Model ID:** `google/nano-banana-2.1/text-to-image`

Generate images from text prompts.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the image to generate |
| `aspect_ratio` | string | No | `1:1` | One of: `1:1`, `3:2`, `2:3`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`, `1:4`, `4:1`, `1:8`, `8:1` |
| `resolution` | string | No | `1k` | `1k`, `2k`, `4k` |
| `enable_web_search` | boolean | No | `false` | Use web search to ground the generation in real-time information |
| `enable_image_search` | boolean | No | `false` | Use image search to ground the generation in real-time information |
| `output_format` | string | No | `png` | `png` or `jpeg` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/text-to-image \
  -p "A clean infographic of the solar system with each planet labeled" \
  -i aspect_ratio="16:9" \
  -i resolution="2k" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

**Model ID:** `google/nano-banana-2.1/edit`

Edit images or combine up to 14 reference images.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the desired edit |
| `images` | string[] | Yes | -- | URLs of input images (max 14). Must be publicly accessible; use `@path` for local files. |
| `aspect_ratio` | string | No | -- | Same values as text-to-image. If omitted, it is determined automatically from the input image. |
| `resolution` | string | No | `1k` | `1k`, `2k`, `4k` |
| `enable_web_search` | boolean | No | `false` | Use web search to ground the edit in real-time information |
| `enable_image_search` | boolean | No | `false` | Use image search to ground the edit in real-time information |
| `output_format` | string | No | `png` | `png` or `jpeg` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/edit \
  -i images='["@./portrait.png"]' \
  -p "Transform into a vibrant pop art style with bold colors" \
  -i resolution="2k" \
  --json | jq -r '.outputs[0]')
```

#### Multi-Image Editing

```bash
OUTPUT_URL=$(wavespeed run google/nano-banana-2.1/edit \
  -i images='["@./face.png", "@./scene.png"]' \
  -p "Place the person from the first image into the scene from the second image" \
  -i aspect_ratio="16:9" \
  --json | jq -r '.outputs[0]')
```

## Pricing

Estimates from `wavespeed price` (per image, USD). Prices may change; check `wavespeed price <model-id> ...` or the model pages: [text-to-image](https://wavespeed.ai/models/google/nano-banana-2.1/text-to-image), [edit](https://wavespeed.ai/models/google/nano-banana-2.1/edit).

| Endpoint | `1k` | `2k` | `4k` |
|----------|------|------|------|
| Text-to-image | $0.04 | $0.06 | $0.135 |
| Edit, 1 reference image | $0.042 | $0.062 | $0.137 |

Each additional reference image adds about $0.002 (4 references at `1k`: $0.048). Turning on `enable_web_search` or `enable_image_search` raises the price (text-to-image `1k`: $0.054).

## Prompt Tips

- Describe the scene in full sentences: subject, setting, lighting, composition and style.
- Put exact text to render in quotes.
- Turn on `enable_web_search` / `enable_image_search` only when the image depends on current real-world information (recent events, real places or products); it costs more.
- Use the tall and wide ratios (`1:4`, `4:1`, `1:8`, `8:1`) for banners, strips and vertical scrolls.
- With several references, say which image supplies what ("the person from the first image", "the background of the second image").

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run google/nano-banana-2.1/text-to-image -h

# Estimate the cost (no generation, no charge)
wavespeed price google/nano-banana-2.1/text-to-image -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run google/nano-banana-2.1/text-to-image -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run google/nano-banana-2.1/text-to-image -i <field>=@./local-file.png --json

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
