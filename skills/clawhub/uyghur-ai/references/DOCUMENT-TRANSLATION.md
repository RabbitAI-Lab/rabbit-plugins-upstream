# 文档翻译

- DOCX：`POST /api/v1/uyghur-ai/word/translation`
- PDF：`POST /api/v1/uyghur-ai/pdf/translation`

multipart/form-data 字段：

| 字段 | 约束 |
|---|---|
| `file` | 必填；DOCX 或 PDF；最大 5 MB |
| `from` | 必填，`zh` 或 `ug` |
| `to` | 必填，`zh` 或 `ug` |
| `mode` | 可选，`all_text`（默认）或 `uyghur_only` |

`all_text` 翻译提取出的全部文字；`uyghur_only` 只保留并处理维吾尔文相关文本。接口返回
提取文本的翻译结果，不生成保留原排版的新文件。

PDF 必须带可提取文字层，本技能不执行 OCR。空文档、损坏文件、扫描件或解析失败会返回
HTTP 422 `document_extraction_failed`。此时请用户提供可复制文本或可解析文件，不要无限重试。
