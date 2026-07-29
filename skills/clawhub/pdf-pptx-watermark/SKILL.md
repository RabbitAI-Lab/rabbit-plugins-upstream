---
name: pdf-watermark
description: "PPTX→PDF watermark tool with real-time mobile parameter tuning. Convert PPT/PPTX to PDF, add custom watermarks (diagonal/grid/center), adjust text/size/opacity/rotation/color — all tunable live from your phone. Trigger: 加水印、转PDF、PDF水印、水印工具、add watermark, convert to PDF, PDF watermark."
---

# PDF Watermark

> **📱 Core Highlight: Mobile Parameter Tuning**
> Tune every watermark parameter in real-time from your phone — no config file editing, no guessing. Adjust, preview, export.

Convert PPT/PPTX to PDF and add custom watermarks with live mobile preview.
将 PPT/PPTX 转为 PDF，支持手机实时调参加水印。

## Quick Start / 快速开始

```bash
# One-liner: PPTX → watermarked PDF
python3 {baseDir}/scripts/pptx_to_pdf_watermark.py input.pptx output.pdf

# With custom config
python3 {baseDir}/scripts/pptx_to_pdf_watermark.py input.pdf output.pdf config.json
```

## Features / 功能

- 📱 **Mobile parameter tuning** — live preview on phone, copy JSON, done
- 📐 **3 layout modes** — diagonal / grid / center
- 🎨 **Full customization** — text, size, opacity, rotation, color
- 🌍 **Cross-platform** — auto-detects CJK fonts (macOS/Linux/Windows)
- 📦 **PPTX support** — one step from PPTX to watermarked PDF
- 🔒 **Local & safe** — no network, no credentials, input never modified

## Configuration / 配置

```json
{
  "text": "CONFIDENTIAL",
  "fontSize": 60,
  "opacity": 0.15,
  "rotation": 45,
  "color": [0.5, 0.5, 0.5],
  "pattern": "diagonal",
  "repeatX": 3,
  "repeatY": 3,
  "offsetX": 200,
  "offsetY": 200
}
```

All parameters optional — sensible defaults provided.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `text` | `"内部资料 请勿外传"` | Watermark text |
| `fontSize` | `60` | Font size (pt) |
| `opacity` | `0.15` | Transparency (0–1) |
| `rotation` | `45` | Rotation (degrees) |
| `color` | `[0.5, 0.5, 0.5]` | RGB (0–1) |
| `pattern` | `"diagonal"` | `diagonal` / `grid` / `center` |
| `repeatX` | `3` | Grid horizontal count |
| `repeatY` | `3` | Grid vertical count |

## Dependencies / 依赖

- **LibreOffice** (PPTX→PDF): `brew install --cask libreoffice` (macOS) / `apt install libreoffice` (Linux)
- **Python 3**: `pip3 install PyPDF2 reportlab`

## Principles

- **Non-destructive** — input file is never modified
- **Cross-platform** — auto-detects OS-appropriate fonts
- **No network required** — all processing is local
- **No credentials** — no API keys, nothing to leak
