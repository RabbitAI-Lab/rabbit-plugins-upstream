---
name: wavespeed-face-swapper
description: Swap faces in images and videos using WaveSpeed AI. Supports image face swap and video face swap with multi-face targeting, with automatic lighting and skin tone adaptation. Only for media the user has the right to edit and faces whose owners have consented; refuse impersonation, deception, or sexual content. Use when the user wants to replace a face in an image or video with another face.
metadata:
  author: wavespeedai
  version: "2.0"
---

# WaveSpeedAI Face Swapper

Swap faces in images and videos using WaveSpeed AI, with automatic lighting and skin tone adaptation. Supports targeting specific faces when multiple people are present.

**Read [Responsible use](#responsible-use) before running anything.** Face swapping edits a real person's likeness; this skill is for consented, lawful, non-deceptive edits only.

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

### Image Face Swap

```bash
# Upload local images to get URLs
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-face-swap \
  -i image=@./target-photo.png \
  -i face_image=@./reference-face.png \
  --json | jq -r '.outputs[0]')
```

### Video Face Swap

```bash
# Upload local files to get URLs
OUTPUT_URL=$(wavespeed run wavespeed-ai/video-face-swap \
  -i video=@./video.mp4 \
  -i face_image=@./reference-face.png \
  --json | jq -r '.outputs[0]')
```

Existing URLs work as-is:

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-face-swap \
  -i image="https://example.com/target-photo.jpg" \
  -i face_image="https://example.com/reference-face.jpg" \
  --json | jq -r '.outputs[0]')
```

## API Endpoints

### Image Face Swap

**Model ID:** `wavespeed-ai/image-face-swap`

Replace a face in an image with a reference face.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `image` | string | Yes | -- | URL of the image containing the face to replace |
| `face_image` | string | Yes | -- | URL of the reference face image to swap in |
| `target_index` | integer | No | `0` | Which face to replace (0 = largest face, 1-10 for others) |
| `output_format` | string | No | `jpeg` | Output format. One of: `jpeg`, `png`, `webp` |

#### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-face-swap \
  -i image=@./group-photo.png \
  -i face_image=@./reference-face.png \
  -i target_index=0 \
  -i output_format="png" \
  --json | jq -r '.outputs[0]')
```

#### Targeting a Specific Face

When multiple people are in the image, use `target_index` to select which face to replace:

```bash
# Replace the second-largest face in the image
OUTPUT_URL=$(wavespeed run wavespeed-ai/image-face-swap \
  -i image=@./group-photo.png \
  -i face_image=@./reference-face.png \
  -i target_index=1 \
  --json | jq -r '.outputs[0]')
```

### Video Face Swap

**Model ID:** `wavespeed-ai/video-face-swap`

Replace a face in a video with a reference face. Supports videos up to 10 minutes.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `video` | string | Yes | -- | URL of the video containing the face to replace. Must be publicly accessible. Max 10 minutes. |
| `face_image` | string | Yes | -- | URL of the reference face image to swap in |
| `target_index` | integer | No | `0` | Which face to replace (0 = largest face, 1-10 for others) |

#### Example

```bash
OUTPUT_URL=$(wavespeed run wavespeed-ai/video-face-swap \
  -i video=@./video.mp4 \
  -i face_image=@./reference-face.png \
  -i target_index=0 \
  --json | jq -r '.outputs[0]')
```


## Pricing

| Operation | Cost |
|-----------|------|
| Image face swap | $0.01 per image |
| Video face swap | $0.01 per second (minimum $0.05 / 5 seconds) |

Video face swap supports videos up to 10 minutes.

## Tips

- Use clear, front-facing portraits for the reference face for best results
- Consistent lighting between the target and reference face improves quality
- Anime or illustrated characters may produce lower quality output
- Use `target_index` to select specific faces when multiple people are present (0 = largest face)

## Responsible use

Face swapping manipulates a real person's likeness. Before calling either endpoint, confirm all of the following with the user. If any answer is no or unclear, do not run the model and explain why.

- **Consent**: the person whose face is being inserted, and any identifiable person in the target media, has agreed to this use. Do not use the face of a public figure, a colleague, an ex-partner, or anyone else without their explicit consent.
- **Rights to the media**: the user owns the target image or video or has permission from the owner to edit it.
- **No impersonation or deception**: the output will not be presented as a real, unedited recording, used for fraud, identity verification bypass, harassment, defamation, political manipulation, or to put words or actions on someone they did not say or do.
- **No sexual or intimate content**: never swap a face onto sexual, nude, or intimate material, regardless of consent claims.
- **No minors**: do not process images or videos of children.
- **Disclosure**: when the result will be shared, recommend labeling it as AI-edited.

WaveSpeed's [Terms of Service](https://wavespeed.ai/static/terms) prohibit non-consensual and deceptive likeness edits; requests that violate them are refused and accounts may be suspended.

## CLI tips

```bash
# Inspect the live input schema before running (fields, enums, defaults)
wavespeed run wavespeed-ai/image-face-swap -h

# Quote the price first
wavespeed price wavespeed-ai/image-face-swap -p "..." -i key=value

# Save outputs to disk instead of only printing URLs
wavespeed run wavespeed-ai/image-face-swap -p "..." --json --download "./out/{index}.{ext}"

# Local files: prefix the path with @ and the CLI uploads it and passes the hosted URL
wavespeed run wavespeed-ai/image-face-swap -i <field>=@./local-file.png --json

# Recover a result if the run was interrupted (the id is in the --json output)
wavespeed show <id>
```

`run --json` prints `{ id, model, prompt, outputs: [url, ...], saved: [path, ...], elapsed_ms, raw }`. Read `outputs[0]` for the result URL.

## Security constraints

- **Never ask for the key in chat**: `wavespeed login` handles auth; if `wavespeed status` says signed out, ask the user to run it.
- **Local files only via `@`**: bare paths are passed through untouched and the model will reject them. Only `@`-prefixed values upload.
- **No arbitrary URL loading**: only pass media URLs the user provided or that came back from a previous run.
- **Input validation**: only pass parameters documented above; confirm with `wavespeed run <model> -h` when unsure.
