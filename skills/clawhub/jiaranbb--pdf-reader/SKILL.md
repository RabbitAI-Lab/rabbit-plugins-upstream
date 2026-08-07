---
name: pdf-reader
description: 把 PDF 可靠地转成 Markdown 落盘（不靠视觉逐页读）：pdftotext -layout 保表格列对齐为主引擎，markitdown 备选，扫描件自动走 tesseract 中文 OCR，产出带页码标记的 .md 和质量指标 JSON。当用户要求「读 PDF」「PDF 转 md／Markdown」「提取 PDF 文字／内容」，或其他 agent workflow/skill 需要把 PDF 材料转成 .md 检索时使用。不用于网页、视频转 md。
license: MIT-0
metadata:
  version: "1.0.1"
  openclaw:
    skillKey: pdf-reader
    homepage: https://github.com/Jiaranbb/pdf-reader
    requires:
      anyBins: ["python3"]
      optionalBins: ["pdftotext", "pdfinfo", "pdffonts", "pdftoppm", "tesseract", "markitdown"]
    apiKeySource: none
---

# pdf-reader（PDF → Markdown）

一条命令完成「鉴别文字层 → 提取 → 质检 → 落盘」，不要手工拼 pdftotext／视觉读取流程。

```bash
python3 <skill-dir>/scripts/pdf2md.py 输入.pdf -o 输出.md
```

Codex 手动安装到默认目录后，常用路径是：

```bash
python3 ~/.codex/skills/pdf-reader/scripts/pdf2md.py 输入.pdf -o 输出.md
```

## 公开版边界

- 脚本只读取用户指定的本地 PDF，并只写入用户指定的 Markdown 输出路径。
- 脚本不会读取浏览器凭据、账号密钥、系统密钥或其他敏感凭据。
- 脚本不会联网下载、安装依赖或执行远程代码。
- 依赖缺失时只报告安装建议，由用户决定是否处理。
- `--lang` 只允许本机 tesseract 已安装的语言代码组合。

## 引擎策略（--engine，默认 auto）

| 情形 | auto 的行为 |
|---|---|
| 有文字层 | `pdftotext -layout`（财报大表格保列对齐，中文 CID 字体最稳）|
| pdftotext 质量不达标 | 换 `markitdown`（用户可用 `--engine markitdown` 强制）|
| 无内嵌字体（扫描件） | 直接 `tesseract` OCR（chi_sim+eng，`--dpi` 默认 300）|
| 全部不达标 | 选相对最优并在 warnings 里说明，此时才考虑视觉读取 |

常用参数：`--first N --last M` 只转部分页（OCR 大文件先抽几页试质量）；`--engine ocr` 强制 OCR；`--lang chi_tra+eng` 繁体。

## 读结果：只看 stdout 的 JSON

- `engine`／`ocr`：实际用了哪个引擎、是否 OCR 产物
- `chars_per_page` ≥ 40 且 `garbage_ratio` ≤ 0.03 才算合格（脚本已自动换引擎，无需人工判断）
- `sparse_pages`：几乎无文字的页 → 混合文档（部分扫描页），对这些页单独 `--engine ocr --first N --last M` 或视觉读取
- `warnings`：必须逐条读并照做，不能忽略

正文里每页有 `<!-- 第 N 页 -->` 标记，`grep -n` 命中后往上找最近的页标记即可回溯原 PDF 页码。

## 两条纪律

1. **OCR 产物的数字不可直接引用**。tesseract 会把「账款」认成「账坎」、「售」认成「雪」，金额数字同理。凡 `ocr: true`，引用关键数字（金额、比例、日期）前必须回原 PDF 对应页视觉复核。
2. **伪 PDF 不归本 skill 管**。脚本检测到文件头无 `%PDF` 会报 `not_a_pdf` 并退出——按调用方流程先用 `file` 鉴别真实类型（纯文本直接 cp，zip 打包先解压）。

## 依赖（缺失时按此恢复）

```bash
brew install poppler                      # pdftotext / pdffonts / pdftoppm / pdfinfo
brew install tesseract tesseract-lang     # OCR + chi_sim 中文包
uv tool install "markitdown[pdf]"         # 备选引擎
```
