# 文档翻译

接口：

- DOCX：`POST /api/v1/tibetan-ai/word/translation`
- PDF：`POST /api/v1/tibetan-ai/pdf/translation`

使用 multipart/form-data，字段为：

| 字段 | 约束 |
|---|---|
| `file` | 必填；DOCX 或 PDF；最大 5 MB |
| `from` | 必填，`zh` 或 `bo` |
| `to` | 必填，`zh` 或 `bo` |
| `mode` | 可选，`all_text`（默认）或 `tibetan_only` |

`all_text` 翻译提取出的全部文字；`tibetan_only` 只保留并处理藏文相关文本。接口提取文字
后调用翻译服务，返回文本翻译结果，不生成保留原排版的新 DOCX/PDF。

PDF 必须带可提取文字层，本技能不执行 OCR。空文档、损坏文件、扫描件或解析失败会返回
HTTP 422 `document_extraction_failed`。遇到该错误时请用户提供可复制文本或可解析文件，
不要无限重试。
