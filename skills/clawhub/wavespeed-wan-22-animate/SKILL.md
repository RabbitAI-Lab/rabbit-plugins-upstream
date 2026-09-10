---
name: wavespeed-wan-22-animate
description: Animate characters from images using driving videos with WaveSpeed AI's Wan 2.2 Animate model. Supports animate mode (make image character move like video subject) and replace mode (swap video subject with image character). Outputs up to 120 seconds at 480p or 720p. Use when the user wants to animate a character from an image using a reference video.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Wan 2.2 Animate

Animate characters from images using driving videos via WaveSpeed AI's Wan 2.2 Animate model. Two modes: **animate** (make the image character move like the video subject) and **replace** (swap the video subject with the image character while preserving motion and scene).

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

### Animate Mode

Make the character in an image move like the subject in a driving video:

```bash
# Upload local image and video
OUTPUT_URL=$(wavespeed run wavespeed-ai/wan-2.2/animate \
  -i image=@./character.png \
  -i video=@./driving-video.mp4 \
  --json | jq -r '.outputs[0]')
```

### Replace Mode

Swap the subject in a video with a character from an image:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/wan-2.2/animate \
  -i image=@./character.png \
  -i video=@./driving-video.mp4 \
  -i mode="replace" \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/wan-2.2/animate \
  -i image="https://example.com/character.png" \
  -i video="https://example.com/driving-video.mp4" \
  --json | jq -r '.outputs[0]')
```

## API Endpoint

**Model ID:** `wavespeed-ai/wan-2.2/animate`

Animate a character from an image using a driving video.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the character image to animate |
| `video` | string | Yes | -- | URL of the driving video providing motion reference |
| `prompt` | string | No | -- | Text prompt for additional guidance |
| `mode` | string | No | `animate` | Operation mode. `animate`: image character moves like video subject. `replace`: video subject is swapped with image character. |
| `resolution` | string | No | `480p` | Output resolution. One of: `480p`, `720p` |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/wan-2.2/animate \
  -i image=@./dancer.png \
  -i video=@./dance-reference.mp4 \
  -p "a person dancing gracefully" \
  -i mode="animate" \
  -i resolution="720p" \
  -i seed=42 \
  --json | jq -r '.outputs[0]')
```

### Replace Mode Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/wan-2.2/animate \
  -i image=@./anime-character.png \
  -i video=@./scene-video.mp4 \
  -i mode="replace" \
  -i resolution="720p" \
  --json | jq -r '.outputs[0]')
```


## Pricing

| Resolution | Cost per 5 seconds |
|------------|--------------------|
| 480p | $0.20 |
| 720p | $0.40 |

Output duration is 5-120 seconds. Minimum charge is 5 seconds. Per-second rate: $0.04/s (480p), $0.08/s (720p).

## Tips

- Match composition and pose between the input image and driving video for best results
- Use the same or similar aspect ratio between image and video
- Avoid heavy occlusion by hands, microphones, or props in the input media
- Start with `480p` for prototyping, then move to `720p` for production quality
- **Animate mode**: best when you want the image character to perform the motions from the video
- **Replace mode**: best when you want to keep the video's scene and motion but swap in a different character

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run wavespeed-ai/wan-2.2/animate -h

# Quote the price first
wavespeed price wavespeed-ai/wan-2.2/animate -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run wavespeed-ai/wan-2.2/animate -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run wavespeed-ai/wan-2.2/animate -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
