# 本地 PDF 文字提取

使用 Skill 包中的 `scripts/extract_pdf.py`：

```sh
python3 scripts/extract_pdf.py "/绝对路径/报告.pdf" --output "/安全临时目录/report.json"
```

脚本输出可直接作为 API 中的 `document` 对象，包含 `name`、`page_count`、`total_characters` 和 `pages`。每个页面包含真实 `page` 和对应 `text`。

限制：单份最多 10 MB、50 页、120000 个字符。脚本会在打开 PDF 前检查文件大小，不会 OCR；无文字层、加密或损坏的 PDF 会返回错误。若缺少依赖，在独立虚拟环境中安装：

```sh
python3 -m venv .venv-pdf-analysis
.venv-pdf-analysis/bin/pip install PyMuPDF
```

分析完成后删除临时 JSON。原始 PDF 不需要上传，但提取后的文字会发送到用户配置的 AI Skills 平台进行模型分析，因此处理敏感资料前应取得用户同意。
