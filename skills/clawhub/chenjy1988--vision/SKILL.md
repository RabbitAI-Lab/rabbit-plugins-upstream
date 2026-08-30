---
name: vision
description: "Image analysis using Google Gemini vision models. Use when user needs to: (1) Describe what's in an image, (2) Extract text from images (OCR), (3) Analyze visual content, (4) Compare images, (5) Answer questions about images. Supports JPG, PNG, GIF, WebP formats."
---

# vision — 让无视觉模型"看图"的 Skill

模型本身看不了图片时（用户发截图/报错图/UI 图/设计稿），用本项目脚本把图片
交给 Google Vertex AI 视觉模型（Gemini），把文字描述/分析结果带回对话。

## 触发场景

- 用户发了截图/图片路径，但主模型无法直接读取图像内容
- 需要分析 UI 截图、错误弹窗、棋盘画面、日志截图、图表、设计稿等
- 模型需要"看到"某张图才能继续任务

## 用法

```bash
python3 ~/.claude/skills/vision/scripts/see.py <图片路径或URL> "<要问的问题>"
```

例：
```bash
python3 ~/.claude/skills/vision/scripts/see.py shot.png "这是游戏棋盘截图，描述你看到的内容，棋盘边缘是否有虚空/空洞？"
```

## 环境要求（复用项目已有配置）

- `GOOGLE_API_KEY`（gen-image 工具链同款，已在用）
- `GOOGLE_CLOUD_PROJECT`（Vertex project id）
- 可选 `VISION_MODEL`：默认 `gemini-2.5-flash`
- 可选 `VISION_LOCATION`：默认 `global`

无需额外安装（纯标准库 urllib + base64；图片用 PNG 重编码，不依赖 pillow 时可跳过重编码）。

## 注意

- 输出是模型的文字回复，直接转述给用户即可，不要声称"自己看到了图"。
- 一次只发一张图；多图就多次调用。