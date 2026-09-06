---
name: wavespeed-image-upscaler
description: Upscale images to 2K, 4K, or 8K resolution using WaveSpeed AI's Image Upscaler. Takes an image URL and produces a higher-resolution version. Supports JPEG, PNG, and WebP output formats. Use when the user wants to upscale or enhance the resolution of an image.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Image Upscaler

Upscale images to 2K, 4K, or 8K resolution using WaveSpeed AI's Image Upscaler.

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

```bash
# Upload a local image to get a URL
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-upscaler \
  -i image=@./photo.png \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-upscaler \
  -i image="https://example.com/photo.jpg" \
  --json | jq -r '.outputs[0]')
```

## API Endpoint

**Model ID:** `wavespeed-ai/image-upscaler`

Upscale an image to a higher resolution.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the image to upscale |
| `target_resolution` | string | No | `4k` | Target resolution. One of: `2k`, `4k`, `8k` |
| `output_format` | string | No | `jpeg` | Output format. One of: `jpeg`, `png`, `webp` |

### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-upscaler \
  -i image=@./photo.png \
  -i target_resolution="8k" \
  -i output_format="png" \
  --json | jq -r '.outputs[0]')
```


## Pricing

$0.01 per image (all resolutions).

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run wavespeed-ai/image-upscaler -h

# Quote the price first
wavespeed price wavespeed-ai/image-upscaler -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run wavespeed-ai/image-upscaler -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run wavespeed-ai/image-upscaler -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
