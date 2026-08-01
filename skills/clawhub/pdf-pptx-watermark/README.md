# PDF Watermark

> 一句话钩子：PPT/PPTX 转 PDF + 自定义水印，一条命令搞定。

[![Agent Skills](https://img.shields.io/badge/Agent-Skills-blue)](https://clawhub.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)]()

**English** | [中文](README.md)

---

## When do you need it? / 你什么时候需要它？

1. **Exporting internal materials**: Convert PPT to PDF and stamp "Confidential" before sharing.
2. **Batch watermarking**: Add your company name or "Do Not Distribute" to existing PDFs.
3. **Client deliverables**: Add a subtle watermark to presentations before sending to clients.

---

## What does it deliver? / 它会交付什么？

- A watermarked PDF file (from PPTX or existing PDF)
- Three layout modes: diagonal (default), grid, or centered
- Full control over text, size, opacity, rotation, and color
- Optional web UI for real-time parameter tuning

---

## Quick Start / 快速开始

```bash
# Install dependencies
pip3 install PyPDF2 reportlab
brew install --cask libreoffice  # macOS; or apt install libreoffice on Linux

# One-step: PPTX → watermarked PDF
python3 scripts/pptx_to_pdf_watermark.py presentation.pptx output.pdf

# With custom config
python3 scripts/pptx_to_pdf_watermark.py presentation.pptx output.pdf config.json
```

---

## Trigger Words / 触发方式

**中文**：加水印、转PDF、PDF水印、导出PDF、水印工具
**English**：add watermark, convert to PDF, PDF watermark, stamp PDF

---

## Example / 示例

```json
{
  "text": "CONFIDENTIAL",
  "fontSize": 60,
  "opacity": 0.15,
  "rotation": 45,
  "pattern": "diagonal"
}
```

```bash
python3 scripts/pptx_to_pdf_watermark.py slides.pptx slides_watermarked.pdf config.json
# → Watermarked PDF saved: slides_watermarked.pdf
```

---

## How is it different? / 它和同类有什么不同？

| Feature | pdf-watermark | Online Tools | Python Scripts |
|---------|--------------|-------------|----------------|
| PPTX → PDF + Watermark | ✅ One step | ❌ Separate | ❌ PPTX only |
| Web UI for tuning | ✅ Included | ✅ Native | ❌ None |
| Cross-platform fonts | ✅ Auto-detect | N/A | ❌ Hardcoded |
| Works offline | ✅ | ❌ | ✅ |
| Config file support | ✅ JSON | ❌ GUI only | ❌ CLI args only |
| Batch / scriptable | ✅ | ❌ | ✅ |

---

## Safety / 安全边界

- ✅ Never modifies the input file
- ✅ No network access required (except optional `cloudflared` tunnel)
- ✅ No API keys or credentials needed
- ✅ All processing is local

---

## File Structure / 文件结构

```
pdf-watermark/
├── SKILL.md                    # Full documentation / 完整文档
├── README.md                   # This file
├── scripts/
│   └── pptx_to_pdf_watermark.py  # Main script / 主脚本
├── watermark-mobile.html       # Mobile web UI / 手机端调参界面
└── watermark-ui.html           # Desktop web UI / 桌面端调参界面
```

---

## License

MIT
