---
name: pdf-watermark
description: "Convert PPT/PPTX to PDF and add customizable watermarks. Supports diagonal/grid/center layouts, adjustable font size, opacity, rotation, and color. Trigger words: 加水印、转PDF、PDF水印、导出PDF、水印工具、add watermark、convert to PDF、PDF watermark. Includes a mobile-friendly web UI for real-time parameter tuning."
---

# PDF Watermark / PDF 水印工具

Convert PPTX → PDF and add customizable diagonal watermarks to every page.
将 PPT/PPTX 转为 PDF 并添加自定义水印。

## Dependencies / 依赖

- **LibreOffice** (`soffice`, headless mode for PPTX→PDF conversion)
  - macOS: `brew install --cask libreoffice`
  - Linux: `sudo apt install libreoffice`
  - Windows: Download from [libreoffice.org](https://www.libreoffice.org/download/)
- **Python 3**: `PyPDF2`, `reportlab`
  ```bash
  pip3 install PyPDF2 reportlab
  ```
- **Fonts**: Auto-detected per platform
  - macOS: STHeiti (built-in)
  - Linux: Noto Sans CJK / WenQuanYi (install `fonts-noto-cjk` or `fonts-wqy-zenhei` if missing)
  - Windows: SimSun (built-in)
  - Fallback: Helvetica (ASCII only, CJK characters will not render)

## Usage / 用法

### Method 1: PPTX → PDF + Watermark (one step) / 一步到位

```bash
python3 {baseDir}/scripts/pptx_to_pdf_watermark.py input.pptx output.pdf [config.json]
```

### Method 2: Add watermark to existing PDF / 给已有 PDF 加水印

```bash
python3 {baseDir}/scripts/pptx_to_pdf_watermark.py input.pdf output.pdf [config.json]
```

### Method 3: Preview watermark layout / 预览水印效果

```bash
python3 {baseDir}/scripts/pptx_to_pdf_watermark.py --preview [config.json] preview.pdf
```

### Method 4: Convert PPTX to PDF only (no watermark) / 仅转 PDF

```bash
soffice --headless --convert-to pdf --outdir <output_dir> <input.pptx>
```

## Configuration / 配置参数

All parameters are optional. Without a config file, defaults are used.
所有参数可选，不提供 config.json 则使用默认值。

```json
{
  "text": "内部资料 请勿外传",
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

| Parameter | Description | Default |
|-----------|-------------|---------|
| `text` | Watermark text / 水印文字 | `"内部资料 请勿外传"` |
| `fontSize` | Font size in pt / 字号 | `60` |
| `opacity` | Transparency 0-1 / 透明度 | `0.15` |
| `rotation` | Rotation in degrees / 旋转角度 | `45` |
| `color` | RGB values 0-1 / 颜色 | `[0.5, 0.5, 0.5]` |
| `pattern` | Layout: `diagonal` / `grid` / `center` / 布局模式 | `"diagonal"` |
| `repeatX` | Grid horizontal count / 网格水平重复 | `3` |
| `repeatY` | Grid vertical count / 网格垂直重复 | `3` |
| `offsetX` | Diagonal spacing X / 对角线间距 | `200` |
| `offsetY` | Diagonal spacing Y / 对角线间距 | `200` |

### Layout Patterns / 布局模式

- **`diagonal`**: Center + 4 offset copies (5 total). Best for standard pages.
- **`grid`**: Uniform X×Y grid across the page. Best for dense coverage.
- **`center`**: Single centered watermark. Best for minimalist style.

## Web UI (Optional) / 调参界面（可选）

A mobile-friendly web UI is included for real-time parameter tuning:
内置手机端调参界面，支持实时预览：

```bash
# Start local server
cd {baseDir} && python3 -m http.server 8088

# Open in browser
# Mobile UI: http://localhost:8088/watermark-mobile.html
# Desktop UI: http://localhost:8088/watermark-ui.html
```

Tune parameters in the UI, copy the generated JSON config, and pass it to the script.
在界面中调好参数，复制 JSON 配置，传给脚本即可。

### Remote Access (Optional) / 远程访问（可选）

To tune parameters from a phone outside localhost, use a tunnel service like `cloudflared`:
如需手机远程访问调参界面，可使用隧道工具：

```bash
brew install cloudflared  # macOS
cloudflared tunnel --url http://127.0.0.1:8088
```

This is entirely optional. The script works standalone without the web UI.
此为可选功能，脚本本身无需 Web UI 即可独立运行。

## How It Works / 工作原理

1. **PPTX → PDF**: LibreOffice headless mode converts the presentation.
2. **Watermark PDF**: reportlab generates a watermark overlay page with the configured parameters.
3. **Merge**: PyPDF2 merges the watermark onto every page of the source PDF.
4. **Output**: Final watermarked PDF is written to the specified path.

## Principles / 原则

- **Non-destructive**: Never modifies the input file / 不修改原始文件
- **Cross-platform**: Auto-detects OS-appropriate fonts / 自动适配各平台字体
- **Configurable**: All parameters have sensible defaults / 所有参数有合理默认值
- **Standalone**: Script runs without the web UI / 脚本独立运行，不依赖 Web UI
