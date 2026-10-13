# HTTP 请求、幂等与任务轮询

令 `BASE=${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net/api/v1}`。每个新业务动作生成 UUID `Idempotency-Key`；所有请求携带 `Authorization: Bearer $DIAGRAM_GENERATION_API_KEY` 和 `Content-Type: application/json`。

- `POST /api/v1/diagram-generation/diagram.plan`；`GET /api/v1/diagram-generation/diagram.plan/tasks/{task_id}`
- `POST /api/v1/diagram-generation/diagram.render`；`GET /api/v1/diagram-generation/diagram.render/tasks/{task_id}`

```sh
curl -sS -X POST "$BASE/diagram-generation/diagram.plan" \
  -H "Authorization: Bearer $DIAGRAM_GENERATION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_UUID" \
  --data '{"prompt":"用户提交订单后经过库存检查和支付，成功后发货","type":"flowchart","direction":"TB","theme":"light"}'
```

`200` 表示同步完成，`202` 表示任务已接收。收到 `202` 后有限退避轮询对应 `/tasks/{task_id}`，读取 `succeeded`、`partial`、`failed` 与 `artifacts`。优先读取 `errors.code`，兼容 `error.code`。结果不确定时只重放相同输入和原键；`conflict` 时检查 `errors.idempotency_key`，不得自动换键创建重复付费任务。
