---
name: pollinations-image
description: "Free AI image generation via Pollinations.ai. No API key required. Use when the user asks to generate an image from text."
metadata: {"openclaw": {"emoji": "🎨", "requires": {"bins": ["curl"]}}}
---

# Pollinations Image Generation

Free text-to-image generation via Pollinations.ai. No API key, no signup.

## Usage

```bash
python3 scripts/pollinations-image.py "a sunset over mountains" --width 1024 --height 768
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt` | (required) | Text description of the image |
| `--width` | 1024 | Image width (max 2048) |
| `--height` | 1024 | Image height (max 2048) |
| `--nologo` | true | Remove Pollinations watermark |
| `--seed` | random | Fixed seed for reproducibility |

## Output

Saves to `~/.openclaw/media/pollinations-image/` and prints the file path.

## Example

```bash
python3 scripts/pollinations-image.py "a cyberpunk city at night with neon lights" --width 1024 --height 576
```

Output: `/home/user/.openclaw/media/pollinations-image/img_1234567890.jpg`

MEDIA:/home/user/.openclaw/media/pollinations-image/img_1234567890.jpg
