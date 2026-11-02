---
name: wavespeed-seedream-5-pro
description: Generate and edit images using ByteDance's Seedream 5.0 Pro (API Preview) via WaveSpeed AI. Supports text-to-image, single-image and multi-reference editing with up to 10 reference images, and layer decomposition of an image into a base image plus transparent layers. Offers 15 aspect ratios, 1k / 1.5k / 2k resolution tiers and a standard or fast prompt-optimization mode. Use when the user wants to create images from a prompt, edit or combine existing images, or split an image into layers with Seedream 5 Pro.
metadata:
  author: wavespeedai
  version: "1.0"
---

# WaveSpeedAI Seedream 5.0 Pro Image Generation/Editing

Generate and edit images using ByteDance's Seedream 5.0 Pro (API Preview) via the WaveSpeed AI platform. Three endpoints: text-to-image, editing with up to 10 reference images, and layer decomposition into a base image and transparent layers.

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
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro \
  -p "A minimalist coffee shop logo with clean typography" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

The `images` parameter accepts an array of image URLs (1-10 images). For local files use the `@path` marker; the CLI uploads them for you.

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro/edit \
  -i images='["@./photo.png"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro/edit \
  -i images='["https://example.com/photo.jpg"]' \
  -p "Add warm sunset lighting and lens flare" \
  --json | jq -r '.outputs[0]')
```

### Shortcut commands

`wavespeed generate image "<prompt>" -m seedream-5-pro` and `wavespeed edit image "<prompt>" --image @./photo.png -m seedream-5-pro` (MCP `generate_image` / `edit_image` with `model: "seedream-5-pro"`) use the same model and pick the endpoint automatically. `seedream-5-pro` is also the default model for these shortcuts.

## API Endpoints

### Text-to-Image

**Model ID:** `bytedance/seedream-v5.0-pro`

Generate images from text prompts.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the image to generate |
| `aspect_ratio` | string | No | `1:1` | One of: `1:1`, `1:2`, `2:1`, `1:3`, `3:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `9:21`, `21:9` |
| `resolution` | string | No | `1k` | Resolution tier: `1k`, `1.5k`, `2k` (also sets the price tier) |
| `output_format` | string | No | `jpeg` | `jpeg` or `png` |
| `prompt_optimization_mode` | string | No | `standard` | The model rewrites the prompt before generating. `standard` uses the full rewrite; `fast` is several times quicker but follows long or intricate prompts less closely. |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro \
  -p "A movie poster for a sci-fi thriller with bold title text 'HORIZON' at the top" \
  -i aspect_ratio="2:3" \
  -i resolution="2k" \
  -i output_format="png" \
  --json | jq -r '.outputs[0]')
```

### Image Editing

**Model ID:** `bytedance/seedream-v5.0-pro/edit`

Edit one image or generate from several reference images (up to 10).

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `prompt` | string | Yes | -- | Text description of the desired edit |
| `images` | string[] | Yes | -- | URLs of the images to edit / reference (max 10). Must be publicly accessible; use `@path` for local files. |
| `aspect_ratio` | string | No | -- | Same values as text-to-image. If omitted, it is determined automatically from the input image. |
| `resolution` | string | No | `1k` | `1k`, `1.5k`, `2k` |
| `output_format` | string | No | `jpeg` | `jpeg` or `png` |
| `prompt_optimization_mode` | string | No | `standard` | `standard` or `fast` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro/edit \
  -i images='["@./portrait.png"]' \
  -p "Transform into a vibrant pop art style with bold colors" \
  -i resolution="2k" \
  --json | jq -r '.outputs[0]')
```

#### Multi-Image Editing

```bash
OUTPUT_URL=$(wavespeed run bytedance/seedream-v5.0-pro/edit \
  -i images='["@./face.png", "@./scene.png"]' \
  -p "Place the person from the first image into the scene from the second image" \
  -i aspect_ratio="16:9" \
  --json | jq -r '.outputs[0]')
```

### Layer Decomposition

**Model ID:** `bytedance/seedream-v5.0-pro/layer-decomposition`

Separate a single image into a base image and transparent image layers. Read every entry of `outputs`, not only `outputs[0]`.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the image to decompose (use `@path` for a local file) |
| `prompt` | string | No | -- | Optional text guidance |
| `resolution` | string | No | `1k` | `1k`, `1.5k`, `2k` |
| `output_format` | string | No | `jpeg` | `jpeg` or `png` |
| `prompt_optimization_mode` | string | No | `standard` | `standard` or `fast` |

#### Example

```bash
wavespeed run bytedance/seedream-v5.0-pro/layer-decomposition \
  -i image=@./poster.png \
  -i output_format="png" \
  --json | jq -r '.outputs[]'
```

## Pricing

Estimates from `wavespeed price` (per run, USD). Prices may change; check `wavespeed price <model-id> ...` or the model pages: [text-to-image](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro), [edit](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro/edit), [layer decomposition](https://wavespeed.ai/models/bytedance/seedream-v5.0-pro/layer-decomposition).

| Endpoint | `1k` | `1.5k` | `2k` |
|----------|------|--------|------|
| Text-to-image (per image) | $0.045 | $0.045 | $0.09 |
| Edit, 1 reference image (per image) | $0.045 | $0.045 | $0.09 |
| Layer decomposition (per run) | $0.765 | $0.765 | $1.53 |

Edit cost rises slightly with more reference images (4 references at `1k`: $0.054).

## Prompt Tips

- Put text that must appear in the image in quotes inside the prompt (e.g. a title `'HORIZON'`).
- Pick `aspect_ratio` up front for the target placement (`9:16` for vertical, `21:9` for banners) instead of describing it in the prompt.
- With several references, say which image supplies what ("the person from the first image", "the background of the second image").
- Use `prompt_optimization_mode=fast` for quick drafts; keep `standard` for long or detailed prompts.
- `1.5k` costs the same as `1k`, so it is the cheapest way to get more pixels.

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run bytedance/seedream-v5.0-pro -h

# Estimate the cost (no generation, no charge)
wavespeed price bytedance/seedream-v5.0-pro -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run bytedance/seedream-v5.0-pro -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run bytedance/seedream-v5.0-pro -i <field>=@./local-file.png --json

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
