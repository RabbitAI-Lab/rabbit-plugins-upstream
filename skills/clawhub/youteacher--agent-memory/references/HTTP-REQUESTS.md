# HTTP 请求、幂等与轮询

## POST 模板

为每个新的逻辑 POST 生成唯一 UUID，并在本地保存请求 JSON 与键：

```bash
IDEMPOTENCY_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body --silent --show-error \
  -X POST "$API_ROOT/agent-memory/memory.write" \
  -H "Authorization: Bearer $AGENT_MEMORY_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $IDEMPOTENCY_KEY" \
  --data-binary '{"type":"preference","scope":"project:alpha","content":"此项目使用 pnpm","confidence":0.9,"metadata":{"source":"user_confirmed"}}'
```

不要给写 POST 使用 `curl --retry`。首次请求超时或连接中断时，结果未知；同一逻辑重试必须复用完全相同的 `Idempotency-Key` 和 JSON。改变字段就是新逻辑请求，应生成新 UUID。

`409 conflict` 时检查 `errors.idempotency_key`；不要换新键绕过冲突，也不要把同一键用于不同 JSON。

## Endpoint

每个操作都使用固定 POST 与任务 GET：

| 操作 | POST | 任务 GET |
|---|---|---|
| `memory.write` | `/api/v1/agent-memory/memory.write` | `/api/v1/agent-memory/memory.write/tasks/{task_id}` |
| `memory.search` | `/api/v1/agent-memory/memory.search` | `/api/v1/agent-memory/memory.search/tasks/{task_id}` |
| `memory.consolidate` | `/api/v1/agent-memory/memory.consolidate` | `/api/v1/agent-memory/memory.consolidate/tasks/{task_id}` |
| `memory.archive` | `/api/v1/agent-memory/memory.archive` | `/api/v1/agent-memory/memory.archive/tasks/{task_id}` |
| `memory.delete` | `/api/v1/agent-memory/memory.delete` | `/api/v1/agent-memory/memory.delete/tasks/{task_id}` |

不要改成 REST 风格自造路径，也不要直接请求任何 Provider endpoint。

## `202` 轮询

五个操作在当前产品定义中都是本地同步操作，但客户端仍必须兼容平台返回 `202`。读取 `task_id` 后，只 GET 同一 operation 的任务地址。使用有界指数退避，例如 1、2、4、8、16 秒，总等待最多 31 秒；不要在客户端假设 worker sleep，也不要自动重复 POST。

终态为 `succeeded`、`partial`、`failed` 或 `reconciliation_required`。到达等待上限时返回 `task_id`、最后状态和可继续查询的路径，不宣称成功或失败。

## 响应提取

成功时提取响应中的 structured `result`/`data`、`artifacts`、`task_id` 与状态。任务 GET 失败读取 `error.code`；POST 验证失败通常读取 `errors.code`，同步执行故障也可能使用 `error.code`，因此先读 `error.code`，再回退 `errors.code`。

逐次记录这三个响应头，不猜价格，不把幂等重放重复累计为新收费：

- `X-AI-Skills-Billing-Currency`
- `X-AI-Skills-Billing-Charged`
- `X-AI-Skills-Billing-Balance`
