# pdf-reader

![AI Skill](https://img.shields.io/badge/AI-Skill-111111?style=flat-square)
![PDF](https://img.shields.io/badge/PDF-Markdown-B91C1C?style=flat-square)
![OCR](https://img.shields.io/badge/OCR-tesseract-2563EB?style=flat-square)
![License](https://img.shields.io/badge/License-MIT--0-111111?style=flat-square)

`pdf-reader` 是一个把 PDF 稳定转换成 Markdown 的 AI Skill。它优先使用 `pdftotext -layout` 保留表格列对齐，必要时切换到 `markitdown`，扫描件则走 `pdftoppm + tesseract` OCR。转换结果会写入 Markdown，并在 stdout 输出 JSON 质量指标。

## 适合

- 读 PDF、提取 PDF 内容、PDF 转 Markdown
- 财报、公告、论文、问询函等带文字层的 PDF
- 扫描件或图片型 PDF 的中文/英文 OCR
- 下游 research/report workflow 需要先把 PDF 材料落盘为可检索文本

## 不适合

- 网页、视频、社交媒体内容提取
- 需要复原复杂版式的排版任务
- 未经人工复核就引用 OCR 里的关键金额、比例或日期

## 安装

Codex 用户可安装到默认 skills 目录：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Jiaranbb/pdf-reader \
  --path . \
  --name pdf-reader
```

也可以手动复制仓库到任意支持 AI Skill 的运行目录。

## 依赖

macOS:

```bash
brew install poppler
brew install tesseract tesseract-lang
uv tool install "markitdown[pdf]"
```

Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-eng
pipx install "markitdown[pdf]"
```

`markitdown` 是备选引擎；如果只使用 `pdftotext` 和 OCR，可以暂不安装。

## 使用

```bash
python3 scripts/pdf2md.py input.pdf -o output.md
```

常用参数：

```bash
# 只转换指定页码范围
python3 scripts/pdf2md.py input.pdf -o output.md --first 1 --last 5

# 强制 OCR
python3 scripts/pdf2md.py input.pdf -o output.md --engine ocr

# 繁体中文 + 英文
python3 scripts/pdf2md.py input.pdf -o output.md --engine ocr --lang chi_tra+eng
```

stdout 会输出一行 JSON：

```json
{
  "output": "/path/output.md",
  "engine": "pdftotext",
  "pages": 12,
  "ocr": false,
  "chars_per_page": 850.4,
  "garbage_ratio": 0.0,
  "warnings": []
}
```

Markdown 正文会包含页码标记：

```markdown
<!-- 第 1 页 -->
```

## 质量规则

- `chars_per_page >= 40` 且 `garbage_ratio <= 0.03` 视为基本合格。
- `warnings` 必须读；它会提示扫描页、OCR 风险或引擎失败原因。
- `ocr: true` 时，引用关键数字前必须回到原 PDF 对应页视觉复核。

## 安全边界

- 只读取用户指定的本地 PDF。
- 只写入用户指定的 Markdown 输出路径。
- 不读取浏览器凭据、账号密钥或系统密钥。
- 不联网下载、安装依赖或执行远程代码。
- `--lang` 只允许本机 tesseract 已安装的语言代码组合。

## License

MIT-0
