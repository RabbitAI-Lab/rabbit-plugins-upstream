# HTTP 请求、幂等与任务轮询

令 `BASE=${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net/api/v1}`。每个新业务动作生成 UUID `Idempotency-Key`；请求携带 `Authorization: Bearer ${PRESENTATION_GENERATION_API_KEY:-$AI_SKILLS_API_KEY}`。

- `POST /api/v1/presentation-generation/presentation.inspect`；`GET /api/v1/presentation-generation/presentation.inspect/tasks/{task_id}`
- `POST /api/v1/presentation-generation/presentation.outline`；`GET /api/v1/presentation-generation/presentation.outline/tasks/{task_id}`
- `POST /api/v1/presentation-generation/presentation.generate`；`GET /api/v1/presentation-generation/presentation.generate/tasks/{task_id}`

```sh
curl -sS -X POST "$BASE/presentation-generation/presentation.inspect" \
  -H "Authorization: Bearer ${PRESENTATION_GENERATION_API_KEY:-$AI_SKILLS_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_UUID" \
  --data '{"brief":"为管理层准备季度复盘，收入数字需保留来源。"}'
```

`202` 后有限退避轮询，读取 `succeeded`、`partial`、`failed` 和 `artifacts`。错误优先读取 `errors.code`，兼容 `error.code`。结果不确定时只重放相同输入和原键；`conflict` 时读取 `errors.idempotency_key` 并停止改键重试。计费以 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged` 和 `X-AI-Skills-Billing-Balance` 响应头为准。
