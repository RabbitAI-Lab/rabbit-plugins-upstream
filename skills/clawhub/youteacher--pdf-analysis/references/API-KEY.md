# API 密钥配置

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `PDF_ANALYSIS_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。


在 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通 PDF 分析，然后在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建并复制 API 密钥。

所有请求使用：

```http
Authorization: Bearer ${PDF_ANALYSIS_API_KEY:-$AI_SKILLS_API_KEY}
Idempotency-Key: 每次新任务使用新的唯一值
Content-Type: application/json
```

响应计费信息位于 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged` 和 `X-AI-Skills-Billing-Balance`。不要记录、展示或提交 API 密钥。
