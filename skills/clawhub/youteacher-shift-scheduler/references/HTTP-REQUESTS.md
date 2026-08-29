# HTTP 请求、幂等与任务轮询

默认 `BASE=${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net/api/v1}`。每个新业务动作生成 UUID `Idempotency-Key`；不确定的网络结果只能用相同 operation、body 和键重放。不要修改 body 后复用旧键，注意 `errors.idempotency_key`。

- `/api/v1/shift-scheduler/schedule.generate`；`/api/v1/shift-scheduler/schedule.generate/tasks/{task_id}`
- `/api/v1/shift-scheduler/schedule.read`；`/api/v1/shift-scheduler/schedule.read/tasks/{task_id}`
- `/api/v1/shift-scheduler/schedule.update`；`/api/v1/shift-scheduler/schedule.update/tasks/{task_id}`
- `/api/v1/shift-scheduler/schedule.export`；`/api/v1/shift-scheduler/schedule.export/tasks/{task_id}`

```sh
curl -sS -X POST "$BASE/shift-scheduler/schedule.read" \
  -H "Authorization: Bearer $SHIFT_SCHEDULER_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_UUID" \
  --data '{"schedule_id":"实际 UUID"}'
```

`200` 为完成；`202` 后按 task ID 轮询对应 `/tasks/{task_id}`，用 1、2、4、8 秒的有界退避，约 60 秒后仍未终结则让用户稍后查询，不能重复生成。终态为 `succeeded`、`partial`、`failed`。读取 `structured`、`artifacts`，并保留 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。错误优先读取 `errors.code`，兼容 `error.code`。
