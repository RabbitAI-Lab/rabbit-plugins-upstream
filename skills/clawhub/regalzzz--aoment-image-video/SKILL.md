---
name: aoment-image-video
description: Limited free access is available to model resources such as Nano Banana Pro, Nano Banana 2, GPT Image 2, Gemini 3.1 Pro, and Gemini 3.5 Flash provided by Aoment AI for AI image, video, image recognition, and HD repair service. Supports text-to-image, image-to-image, image recognition, video generation, and image HD repair. Automatic Agent API key registration is supported.
metadata: {"openclaw": {"emoji": "AI"}}
user-invocable: true
---

# aoment-image-video

AI generation service powered by Aoment AI. This skill exposes dedicated skill APIs and scripts for:

- text-to-image
- image-to-image
- image recognition
- video generation
- image HD repair/upscale

Download the latest package: [https://www.aoment.com/downloads/aoment-image-video-skill.zip](https://www.aoment.com/downloads/aoment-image-video-skill.zip)

### Current Version

```text
version: 1.6.0
```

### Auto-Update Policy

Before each invocation, the Python scripts read the `version` field above and query:

```text
GET https://www.aoment.com/api/skills/aoment-image-video/version
```

If the local version is behind the remote version, the script exits with:

```json
{
  "success": false,
  "error": "update_required",
  "current_version": "1.0.0",
  "latest_version": "1.3.0",
  "message": "Skill version is outdated..."
}
```

If the version check fails because of a network problem, the script continues normally.

## Quick Start

```bash
# 1. Register an Agent account and get your API Key
uv run {baseDir}/scripts/aoment_register.py --nickname "MyBot"

# 2. Generate an image with the default N2-Fast model
uv run {baseDir}/scripts/aoment_image_video.py -k <your-api-key> -t text-to-image -p "a cute cat playing in a garden"

# 3. Repair/upscale an image
uv run {baseDir}/scripts/aoment_hd_repair.py -k <your-api-key> --image ./input.png --resolution 4K

# 4. Recognize/analyze an image
uv run {baseDir}/scripts/aoment_image_video.py -k <your-api-key> -t image-recognition -p "Describe this image" --image ./input.png

# 5. Check remaining quota
uv run {baseDir}/scripts/aoment_quota.py -k <your-api-key>
```

## Authentication

This skill requires an Agent API Key via:

```text
Authorization: Bearer <api_key>
```

The API Key format is `aoment_` followed by 32 hex characters.

### Get your API Key - Agent Registration

AI Agent Bots can register directly via CLI. No web login is required:

```bash
uv run {baseDir}/scripts/aoment_register.py --nickname "MyBot"
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `--nickname` / `-n` | string | yes | Agent display name, max 16 characters |
| `--api-base` | string | no | API base URL, default `https://www.aoment.com` |

Or register via API directly:

```bash
curl -X POST https://www.aoment.com/api/skills/aoment-image-video/register-agent \
  -H "Content-Type: application/json" \
  -d '{"nickname": "MyBot"}'
```

Registration response:

```json
{
  "success": true,
  "data": {
    "username": "agent_a1b2c3d4...",
    "nickname": "MyBot",
    "api_key": "<your-aoment-api-key>"
  }
}
```

Save the returned `api_key`; it is used for all subsequent skill calls. Store this API Key in a suitable secure location for long-term use.

## Tools

## Available Models

Use the model ID exactly as shown in the `--model` parameter.

### Image Models

| Model ID | Description |
|----------|-------------|
| `image-n2-fast` | Default image model. Faster N2-Fast image generation and editing, no watermark. |
| `image-n2` | N2 image generation and editing, fast, stricter single-reference image size limit, no watermark. |
| `image-n1-fast` | Faster N1-Fast image generation and editing, no watermark. |
| `image-n1` | N1 image generation and editing, slower, looser single-reference image size limit, no watermark. |
| `image-o2` | Image generation and editing with stronger aesthetics, good Chinese-language rendering, newer knowledge data, no watermark, and currently limited clarity near 1.5K. |
| `image-o2-pro` | O2-Pro high-resolution image generation and editing with precise size output support. |

Tip: N-series models use Nano Banana Pro, N-Fast-series models use Nano Banana 2, and O-series models use GPT Image 2.

### Image Recognition Models

| Model ID | Description |
|----------|-------------|
| `image-recognition-g1` | G1 image recognition and visual analysis powered by Gemini 3.1 Pro. |
| `image-recognition-g2` | G2 image recognition and visual analysis powered by Gemini 3.5 Flash. |

### Video Models

| Model ID | Description |
|----------|-------------|
| `video-v1-fast` | Default faster Veo 3.1 video generation model with 4/6/8 second duration options and one optional reference image. |
| `video-seedance-2` | Seedance 2.0 video generation with up to 9 reference images, 3 reference videos, 3 reference audio clips, 4-15 second duration, and 480p/720p/1080p output. This is the only video model that requires whitelist access; contact Aoment customer service to apply before use. |

### text-to-image

Generate images from a text prompt. The default model is `image-n2-fast` (N2-Fast).

```bash
uv run {baseDir}/scripts/aoment_image_video.py \
  --api-key <your-api-key> \
  --tool-type text-to-image \
  --prompt "a cinematic robot painter in a bright studio" \
  --aspect-ratio 1:1 \
  --image-size 1K
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `--api-key` / `-k` | string | yes | - | Agent API Key |
| `--tool-type` / `-t` | enum | yes | - | `text-to-image` |
| `--prompt` / `-p` | string | yes | - | Text prompt |
| `--model` | string | no | `image-n2-fast` | Image model ID. Available values: `image-n2-fast`, `image-n2`, `image-n1-fast`, `image-n1`, `image-o2`, `image-o2-pro` |
| `--aspect-ratio` | string | no | `auto` | `auto`, `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`, `5:4`, `4:5`, `21:9` |
| `--image-size` | enum | no | `1K` | `1K`, `2K`, `4K` |

### image-to-image

Generate a new image from a prompt and a reference image. The reference image can be a URL or base64 image data.

```bash
uv run {baseDir}/scripts/aoment_image_video.py \
  --api-key <your-api-key> \
  --tool-type image-to-image \
  --prompt "change the background to a beach" \
  --reference-image "https://example.com/photo.jpg"
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `--api-key` / `-k` | string | yes | - | Agent API Key |
| `--tool-type` / `-t` | enum | yes | - | `image-to-image` |
| `--prompt` / `-p` | string | yes | - | Transformation prompt |
| `--reference-image` | string | yes | - | Reference image as URL or base64 data |
| `--model` | string | no | `image-n2-fast` | Image model ID. Available values: `image-n2-fast`, `image-n2`, `image-n1-fast`, `image-n1`, `image-o2`, `image-o2-pro` |
| `--aspect-ratio` | string | no | `auto` | Output aspect ratio |
| `--image-size` | enum | no | `1K` | `1K`, `2K`, `4K` |

### video-generation

Generate a video from a prompt. The default video model is `video-v1-fast`. The CLI chooses a model-specific skill endpoint based on `--model`.

Dedicated skill HTTP endpoints:

| Model | Endpoint |
|-------|----------|
| `video-v1-fast` | `POST /api/skills/aoment-image-video/video-v1-fast` |
| `video-seedance-2` | `POST /api/skills/aoment-image-video/video-seedance-2` |

The old `POST /api/skills/aoment-image-video/video-generation` endpoint is removed and no longer accepts a `model` switch.

`video-seedance-2` is the only video model with a whitelist requirement. If the Agent API Key user is not whitelisted, the API returns `403 model_access_denied`; contact Aoment customer service to apply for whitelist access.

```bash
uv run {baseDir}/scripts/aoment_image_video.py \
  --api-key <your-api-key> \
  --tool-type video-generation \
  --prompt "sunset beach timelapse" \
  --orientation landscape \
  --resolution 720p
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `--api-key` / `-k` | string | yes | - | Agent API Key |
| `--tool-type` / `-t` | enum | yes | - | `video-generation` |
| `--prompt` / `-p` | string | text-to-video yes | - | Video prompt; optional for `video-seedance-2` when reference media is provided |
| `--model` | string | no | `video-v1-fast` | Video model ID. Available values: `video-v1-fast`, `video-seedance-2` |
| `--orientation` | enum | no | `portrait` | `portrait` or `landscape` |
| `--aspect-ratio` | string | no | `auto` | For `video-seedance-2`: `adaptive`, `16:9`, `9:16`, `4:3`, `3:4`, `1:1`, or `21:9` |
| `--resolution` | enum | no | `720p` | For `video-v1-fast`: `720p`, `1080p`, `4k`; for `video-seedance-2`: `480p`, `720p`, `1080p` |
| `--duration` | enum | no | `8` | For `video-v1-fast`: `4`, `6`, or `8`; for `video-seedance-2`: `4`-`15` or `-1`; 1080p/4k uses `8` on `video-v1-fast` |
| `--seedance-reference-mode` | enum | no | `multimodal` | For `video-seedance-2`: `multimodal`, `first_frame`, or `first_last_frame` |
| `--reference-image` | string | no | - | Reference image as URL or base64 data; Seedance2.0 supports up to 9 images |
| `--reference-video` | string | no | - | Reference video as URL or base64 data; only `video-seedance-2`, up to 3 videos |
| `--reference-audio` | string | no | - | Reference audio as local path or base64 data; only `video-seedance-2`, up to 3 clips and must be paired with image/video |

### image-recognition

Analyze one or more images with a text prompt. The default recognition model is `image-recognition-g2` (Gemini 3.5 Flash). Images can be local paths, URLs, or base64 image data.

```bash
uv run {baseDir}/scripts/aoment_image_video.py \
  --api-key <your-api-key> \
  --tool-type image-recognition \
  --prompt "List the visible objects and summarize the scene" \
  --image ./input.png
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `--api-key` / `-k` | string | yes | - | Agent API Key |
| `--tool-type` / `-t` | enum | yes | - | `image-recognition` |
| `--prompt` / `-p` | string | yes | - | Recognition or analysis instruction |
| `--image` / `-i` | string | yes | - | Image as local path, URL, or base64 data; can be passed multiple times |
| `--reference-image` | string | no | - | Compatibility alias for image input; can be passed multiple times |
| `--model` | string | no | `image-recognition-g2` | Recognition model ID. Available values: `image-recognition-g1`, `image-recognition-g2` |

### hd-repair

Repair and upscale an image. This is provided by a separate script:

```bash
uv run {baseDir}/scripts/aoment_hd_repair.py \
  --api-key <your-api-key> \
  --image ./input.png \
  --resolution 4K
```

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `--api-key` / `-k` | string | yes | - | Agent API Key |
| `--image` / `-i` | string | yes | - | Local path, URL, or base64 image data |
| `--resolution` | enum | no | `4K` | `2K`, `4K`, `8K` |
| `--model` | string | no | `image-hd-repair` | Only `image-hd-repair` is supported |

## Quota

Query remaining daily generation quota:

```bash
uv run {baseDir}/scripts/aoment_quota.py --api-key <your-api-key>
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `--api-key` / `-k` | string | yes | Agent API Key |

If your daily quota is used up and you need more, join the community:

- Discord: [https://discord.gg/3BMzRd7bJx](https://discord.gg/3BMzRd7bJx)
- QQ Group: 474397920 ([Join via link](https://qm.qq.com/q/9VGyXeMfUk))

## Response Format

All scripts print JSON to stdout.

Successful text-to-image or image-to-image:

```json
{
  "success": true,
  "tool_type": "text-to-image",
  "data": {
    "image_url": "https://cos.example.com/result.jpg?..."
  }
}
```

Successful video generation:

```json
{
  "success": true,
  "tool_type": "video-generation",
  "data": {
    "video_url": "https://cos.example.com/result.mp4?..."
  }
}
```

Successful HD repair:

```json
{
  "success": true,
  "tool_type": "hd-repair",
  "data": {
    "image_url": "https://cos.example.com/hd-repair-result.png?..."
  }
}
```

Successful image recognition:

```json
{
  "success": true,
  "tool_type": "image-recognition",
  "data": {
    "result_text": "The image shows..."
  }
}
```

Successful quota query:

```json
{
  "success": true,
  "data": {
    "remaining": 12,
    "quota": 15,
    "used": 3
  }
}
```

Error response:

```json
{
  "success": false,
  "error": "error description"
}
```

## Downloading Results

Returned `image_url` and `video_url` values are pre-signed COS URLs. Use the complete URL exactly as returned, including all query parameters. Do not strip the query string.

Example:

```bash
uv run {baseDir}/scripts/aoment_image_video.py \
  -k <your-api-key> \
  -t text-to-image \
  -p "prompt" > result.json

curl -L -o output.jpg "$(python3 -c "import json; print(json.load(open('result.json'))['data']['image_url'])")"
```

## Troubleshooting

1. If a request fails because of content policy, revise the prompt or reference image and retry.
2. If the script returns `update_required`, download and install the latest skill package.
3. If a generated URL cannot be opened, make sure your application preserves the full signed URL.
4. For help, join the Discord or QQ community listed above.
