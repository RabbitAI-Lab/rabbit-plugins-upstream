# HTTP 请求、幂等与轮询

## 可执行 POST

每个新逻辑 POST 生成并保存唯一 UUID：

```bash
IDEMPOTENCY_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body --silent --show-error \
  -X POST "$API_ROOT/knowledge-graph/entity.upsert" \
  -H "Authorization: Bearer $KNOWLEDGE_GRAPH_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $IDEMPOTENCY_KEY" \
  --data-binary '{"type":"company","external_key":"acme-001","name":"阿克米公司","properties":{"industry":"software"}}'
```

不要对写 POST 使用 `curl --retry`。首次 POST 超时代表结果未知；同一逻辑重试必须复用原 `Idempotency-Key` 和完全相同的 JSON。字段变化属于新逻辑请求，使用新 UUID。`409 conflict` 时检查 `errors.idempotency_key`，不要换键绕过冲突。

## Endpoint

| 操作 | POST | 任务 GET |
|---|---|---|
| `entity.upsert` | `/api/v1/knowledge-graph/entity.upsert` | `/api/v1/knowledge-graph/entity.upsert/tasks/{task_id}` |
| `relation.upsert` | `/api/v1/knowledge-graph/relation.upsert` | `/api/v1/knowledge-graph/relation.upsert/tasks/{task_id}` |
| `graph.query` | `/api/v1/knowledge-graph/graph.query` | `/api/v1/knowledge-graph/graph.query/tasks/{task_id}` |
| `source.attach` | `/api/v1/knowledge-graph/source.attach` | `/api/v1/knowledge-graph/source.attach/tasks/{task_id}` |
| `graph.summarize` | `/api/v1/knowledge-graph/graph.summarize` | `/api/v1/knowledge-graph/graph.summarize/tasks/{task_id}` |

不要自造实体详情、可达性、预览或 REST 风格路径；不要请求第三方 Provider endpoint。

## `202` 与结果

五个操作当前均为平台本地同步操作，但客户端仍兼容统一任务层返回 `202`。读取 `task_id` 后，仅 GET 同一 operation 的任务地址；使用 1、2、4、8、16 秒的有界退避，总等待最多 31 秒。不要重复 POST，也不要假设 worker sleep。

轮询到 `succeeded`、`partial`、`failed` 时停止；若状态仍为 `processing` 但 `error.code` 是 `reconciliation_required`，也停止自动轮询与重放并转人工对账。超出等待预算时返回 `task_id`、最后状态与查询地址，不宣称成功或失败。

提取 structured `result`/`data`、`artifacts`、状态和 task ID。任务 GET 与同步执行失败读取 `error.code`。普通 POST 字段验证返回 `status:validation_failed` 和字段化 `errors`，没有 `errors.code`；平台绑定缺失等提交前服务错误才可能使用 `errors.code`。不要假定两个 envelope 相同。

逐次记录三个计费头，不猜价格，不把同一幂等响应累计两次：

- `X-AI-Skills-Billing-Currency`
- `X-AI-Skills-Billing-Charged`
- `X-AI-Skills-Billing-Balance`
