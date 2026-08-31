# 接口路由

所有路径都基于 `/api/v1/uyghur-ai`。

| 用户意图 | 方法与路径 | 说明 |
|---|---|---|
| 中文与维吾尔语严格互译 | `POST /translation` | JSON，语言代码为 `zh` 与 `ug` |
| DOCX 翻译 | `POST /word/translation` | multipart，提取文字后翻译 |
| PDF 翻译 | `POST /pdf/translation` | multipart，仅支持可提取文字层 |
| 维吾尔语问答、解释、改写或创作 | `POST /chat/completions` | OpenAI 风格消息数组 |

- 用户要求“翻译”且不需要解释时使用 `/translation`。
- 用户上传 `.docx` 或 `.pdf` 时使用对应文档接口。
- 用户要求问答、润色、总结、续写或创作时使用 `/chat/completions`。
- 维吾尔文通常使用阿拉伯字母；不要仅凭拉丁字母片段假定为维吾尔文。
- 图片或扫描 PDF 不做 OCR，应请用户提供可复制文本或带文字层的文件。
