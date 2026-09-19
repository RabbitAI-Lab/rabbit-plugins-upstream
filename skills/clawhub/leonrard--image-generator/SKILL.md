---
name: image-generator
description: AI image generation using GrusAI API (支持 nano-banana 和 gpt-image-2 模型). Generate images from text prompts.
version: 2.0.0
---

# Image Generator Skill

Generate AI images using GrusAI API (支持 nano-banana 和 gpt-image-2 模型).

## Supported Models

| 模型 | 端点 | 说明 |
|------|------|------|
| `nano-banana-fast` (默认) | `https://grsaiapi.com/v1/draw/nano-banana` | 快速生成 |
| `gpt-image-2` | `https://grsaiapi.com/v1/draw/completions` | 更高质量，中文渲染更强 |

## Setup

No additional setup required. API key is passed via headers.

## Usage

### Generate Image (nano-banana)

```bash
python3 generate.py "一只可爱的猫咪在草地上玩耍" --model nano-banana-fast --aspect-ratio 1:1 --output image.png
```

### Generate Image (gpt-image-2)

```bash
python3 generate.py "一只可爱的猫咪在草地上玩耍" --model gpt-image-2 --aspect-ratio 16:9 --output image.png --api-key YOUR_API_KEY
```

## Parameters

- `prompt` (required): Image description / 图片描述
- `--model`: Model name — `nano-banana-fast` (默认) 或 `gpt-image-2`
- `--aspect-ratio`: 图片比例 — `auto`, `1:1`, `16:9`, `9:16`, `3:2`, `2:3`
- `--size`: 图片尺寸 — `1K`, `2K`, `4K` (gpt-image-2 支持更高分辨率)
- `--output`: 输出文件名
- `--api-key`: API密钥 (gpt-image-2 必须提供)
- `--urls`: 参考图 URL / data URL / 本地文件路径(本地文件自动 base64 编码为 data URL)。支持图生图,逗号分隔多张
- `--image-prompt`: 图生图提示词

## Example Prompts

- "一只可爱的猫咪在草地上玩耍"
- "未来城市的高楼大厦，赛博朋克风格，写实摄影风格"
- "A luxurious modern swimming pool, crystal clear blue water, tropical landscaping, photorealistic"
- "中环麓岛小区整体效果图，现代简约风格，高端住宅"

## API

Uses GrusAI API:
- **nano-banana**: `https://grsaiapi.com/v1/draw/nano-banana`
- **gpt-image-2**: `https://grsaiapi.com/v1/draw/completions`
- Headers: `Authorization: Bearer {apikey}`

## Notes

- `nano-banana-fast`: 生成速度快，免费额度内可用
- `gpt-image-2`: 效果更好，文字渲染更准确，生成时间约30秒
- gpt-image-2 需要有效的 API Key才能使用
