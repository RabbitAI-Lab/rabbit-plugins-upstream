# 行为、错误与重试规则

- 只上传完成请求所需的内容；文件或敏感长文本上传前取得同意。
- 同一逻辑请求复用 `Idempotency-Key`，内容改变时使用新值。
- 不回显 Key、完整原始响应或无关内部诊断。
- 翻译读取 `data.tgtText`，对话读取 `choices[0].message.content`；缺失则失败关闭。
- `validation_failed`：修正字段、语言代码或长度。
- `insufficient_balance`：提示充值，不自动重发。
- `rate_limited`：遵循 `Retry-After` 或有限指数退避。
- `upstream_unavailable`：短暂退避并复用原幂等键，限制重试次数。
- `idempotency_in_progress`：等待原请求，不换 Key 并发提交。
- `idempotency_key_reused`：仅请求内容确实不同才换新 Key。
- `idempotency_indeterminate`：停止自动重试，先核对原请求和账单。
- `document_extraction_failed`：更换可解析文件或改用纯文本。

幂等重放返回首次响应与首次计费头。统一计费头为
`X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、
`X-AI-Skills-Billing-Balance`。
