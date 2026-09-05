# API 密钥配置

在 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通 PDF 分析，然后在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

所有请求使用：

```http
Authorization: Bearer ${PDF_ANALYSIS_API_KEY}
Idempotency-Key: 每次新任务使用新的唯一值
Content-Type: application/json
```

响应计费信息位于 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged` 和 `X-AI-Skills-Billing-Balance`。不要记录、展示或提交 API 密钥。
