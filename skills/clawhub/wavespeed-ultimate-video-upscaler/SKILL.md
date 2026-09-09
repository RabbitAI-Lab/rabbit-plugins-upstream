---
name: wavespeed-ultimate-video-upscaler
description: Upscale videos to 720p, 1080p, 2K, or 4K resolution using WaveSpeed AI's Ultimate Video Upscaler. Takes a video URL and produces a higher-resolution version. Supports videos up to 10 minutes. Use when the user wants to upscale or enhance the resolution of a video.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Ultimate Video Upscaler

Upscale videos to 720p, 1080p, 2K, or 4K resolution using WaveSpeed AI's Ultimate Video Upscaler. Supports videos up to 10 minutes long.

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
# Upload a local video to get a URL
OUTPUT_URL=$(wavespeed run wavespeed-ai/ultimate-video-upscaler \
  -i video=@./video.mp4 \
  --json | jq -r '.outputs[0]')
```

You can also pass an existing video URL directly:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/ultimate-video-upscaler \
  -i video="https://example.com/video.mp4" \
  --json | jq -r '.outputs[0]')
```

## API Endpoint

**Model ID:** `wavespeed-ai/ultimate-video-upscaler`

Upscale a video to a higher resolution.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video to upscale. Must be publicly accessible. |
| `target_resolution` | string | No | `1080p` | Target resolution. One of: `720p`, `1080p`, `2k`, `4k` |

### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/ultimate-video-upscaler \
  -i video=@./video.mp4 \
  -i target_resolution="4k" \
  --json | jq -r '.outputs[0]')
```


## Pricing

| Target Resolution | Cost per 5 seconds |
|-------------------|--------------------|
| 720p | $0.10 |
| 1080p | $0.15 |
| 2K | $0.25 |
| 4K | $0.40 |

Minimum charge is 5 seconds. Videos up to 10 minutes supported. Processing time is approximately 10-30 seconds per 1 second of video.

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run wavespeed-ai/ultimate-video-upscaler -h

# Quote the price first
wavespeed price wavespeed-ai/ultimate-video-upscaler -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run wavespeed-ai/ultimate-video-upscaler -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run wavespeed-ai/ultimate-video-upscaler -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
