---
name: wavespeed-infinitetalk
description: Generate talking head videos from a portrait image and audio using WaveSpeed AI's InfiniteTalk model. Produces lip-synced video up to 10 minutes long at 480p or 720p. Supports optional mask images to target specific faces and text prompts for additional guidance. Use when the user wants to animate a face with audio or create talking avatar videos.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI InfiniteTalk

Generate talking head videos from a portrait image and audio using WaveSpeed AI's InfiniteTalk model. Produces lip-synced video up to 10 minutes long with natural facial animations.

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
# Upload local image and audio files
OUTPUT_URL=$(wavespeed run wavespeed-ai/infinitetalk \
  -i image=@./portrait.png \
  -i audio=@./speech.mp3 \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/infinitetalk \
  -i image="https://example.com/portrait.jpg" \
  -i audio="https://example.com/speech.mp3" \
  --json | jq -r '.outputs[0]')
```

## API Endpoint

**Model ID:** `wavespeed-ai/infinitetalk`

Animate a portrait image with lip-synced audio to produce a talking head video.

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the portrait image to animate |
| `audio` | string | Yes | -- | URL of the audio to drive the animation |
| `mask_image` | string | No | -- | URL of a mask image to specify which person to animate. **Warning:** The mask should only cover the regions to animate — do not upload the full image as `mask_image`, or the result may render as fully black. |
| `prompt` | string | No | -- | Text prompt for additional guidance. Keep it short; English recommended to avoid noisy results. |
| `resolution` | string | No | `480p` | Output resolution. One of: `480p`, `720p` |
| `seed` | integer | No | `-1` | Random seed (-1 for random). Range: -1 to 2147483647 |

### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/infinitetalk \
  -i image=@./portrait.png \
  -i audio=@./speech.mp3 \
  -i resolution="720p" \
  -i seed=42 \
  --json | jq -r '.outputs[0]')
```

### Using a Mask Image

When multiple people are in the image, use a mask to specify which face to animate:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/infinitetalk \
  -i image=@./group-photo.png \
  -i audio=@./speech.mp3 \
  -i mask_image=@./mask.png \
  -i resolution="720p" \
  --json | jq -r '.outputs[0]')
```

> **Important:** The mask should only highlight the face region to animate. Using the full image as a mask will produce a fully black output.

### With Prompt Guidance

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/infinitetalk \
  -i image=@./group-photo.png \
  -i audio=@./speech.mp3 \
  -p "natural head movements, subtle expressions" \
  --json | jq -r '.outputs[0]')
```


## Resolution and Pricing

| Resolution | Cost per 5 seconds | Rate per second | Max length |
|------------|--------------------|-----------------| -----------|
| 480p | $0.15 | $0.03/s | 10 minutes |
| 720p | $0.30 | $0.06/s | 10 minutes |

Minimum charge is 5 seconds. Video length is determined by the audio duration (up to 10 minutes).

## Tips

- Use a clear, front-facing portrait for best results
- Audio quality matters — use clean speech recordings with minimal background noise
- Keep prompts short and in English to avoid noisy or unexpected results
- For group photos, always provide a `mask_image` to target the correct face
- 480p is faster to generate; use 720p when higher quality is needed
- Processing time is approximately 10-30 seconds of wall time per 1 second of video

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run wavespeed-ai/infinitetalk -h

# Quote the price first
wavespeed price wavespeed-ai/infinitetalk -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run wavespeed-ai/infinitetalk -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run wavespeed-ai/infinitetalk -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
