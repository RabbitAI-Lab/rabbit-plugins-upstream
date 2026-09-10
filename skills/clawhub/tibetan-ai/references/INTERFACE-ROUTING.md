# 接口路由

所有路径都基于 `/api/v1/tibetan-ai`。

| 用户意图 | 方法与路径 | 说明 |
|---|---|---|
| 中文与藏语严格互译 | `POST /translation` | JSON，语言代码为 `zh` 与 `bo` |
| DOCX 翻译 | `POST /word/translation` | multipart，提取文字后翻译 |
| PDF 翻译 | `POST /pdf/translation` | multipart，仅支持可提取文字层 |
| 藏语问答、解释、改写或创作 | `POST /chat/completions` | OpenAI 风格消息数组 |

选择原则：

- 用户要求“翻译”且不需要解释时使用 `/translation`，不要用对话接口扩写。
- 用户上传 `.docx` 或 `.pdf` 时使用对应文档接口。
- 用户要求回答问题、润色、总结、续写或创作时使用 `/chat/completions`。
- 图片或扫描 PDF 不做 OCR；应请用户提供可复制文本或带文字层的文件。
