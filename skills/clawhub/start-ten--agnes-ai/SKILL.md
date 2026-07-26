---
name: agnes-ai
description: "Free image & video generation via Agnes AI API - text-to-image, image-to-image, text-to-video, image-to-video"
openclaw:
  emoji: "🖼️"
  requires:
    env:
      - AGNES_API_KEY
---

# Agnes AI

Free multimodal AI generation using [Agnes AI](https://agnes-ai.com) API.

## Available Models

| Model | Type | Price |
|-------|------|-------|
| `agnes-image-2.1-flash` | Image generation (text-to-image & image-to-image) | Free |
| `agnes-video-v2.0` | Video generation (text-to-video & image-to-video) | Free |

## Text-to-Image

```bash
curl -X POST https://apihub.agnes-ai.com/v1/images/generations \
  -H "Authorization: Bearer *** \
  -H "Content-Type: application/json" \
  -d '{"model": "agnes-image-2.1-flash", "prompt": "a cat on a desk", "size": "1024x1024", "extra_body": {"response_format": "url"}}'
```

## Text-to-Video

```bash
# Create task
curl -X POST https://apihub.agnes-ai.com/v1/videos \
  -H "Authorization: Bearer *** \
  -H "Content-Type: application/json" \
  -d '{"model": "agnes-video-v2.0", "prompt": "a cat walking", "width": 1152, "height": 768, "num_frames": 121, "frame_rate": 24}'

# Poll result
curl "https://apihub.agnes-ai.com/agnesapi?video_id=<ID>&model_name=agnes-video-v2.0" \
  -H "Authorization: Bearer $AGNES...
```

## Setup

1. Get free API key: [platform.agnes-ai.com](https://platform.agnes-ai.com)
2. `export AGNES_API_KEY=*** Run the commands

## Links

- GitHub: https://github.com/Start-Ten/agnes-ai-hermes-plugins
- API Docs: https://agnes-ai.com/doc
