# HTTP 请求与任务轮询

## 创建任务

下面是完整可运行的商品搜索示例。每个新逻辑请求生成新 UUID；同一请求因超时或临时错误
重试时必须复用原请求体和原 `REQUEST_KEY`。不要对 POST 使用 curl 自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
REQUEST_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/commerce-radar/product.search" \
  -H "Authorization: Bearer $COMMERCE_RADAR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_KEY" \
  -d '{"query":"无线耳机","location_code":2840,"language_code":"en","limit":20}'
```

POST 响应含 `task_id`、`status`、`operation`，异步结果尚未产生时没有 `result`。

## 轮询

以 POST 返回的 `task_id` 原样替换示例值，并查询同一 operation：

```bash
TASK_ID="POST_RESPONSE_TASK_ID"

curl --fail-with-body \
  "$API_ROOT/commerce-radar/product.search/tasks/$TASK_ID" \
  -H "Authorization: Bearer $COMMERCE_RADAR_API_KEY"
```

`queued`、`processing` 继续等待；从约 2 秒开始指数退避到最长约 30 秒，限制总次数与总等待
时长。不要创建新的 POST 代替轮询。`succeeded`、`partial`、`failed`、`cancelled` 都是终态。
达到本地等待上限时返回 `task_id` 和当前状态，不能声称任务失败。

模板路径为：

- `/api/v1/commerce-radar/product.search/tasks/{task_id}`
- `/api/v1/commerce-radar/product.detail/tasks/{task_id}`
- `/api/v1/commerce-radar/store.analyze/tasks/{task_id}`
- `/api/v1/commerce-radar/report.create/tasks/{task_id}`

## 结果与费用

终态响应读取 `result.version` 和相应的 `result.products`、`result.product`、`result.store`、
`result.report`；逐项问题可能出现在 structured 结果中。`artifacts[]` 只包含平台返回的产物
元数据，不猜测下载地址。

费用只读取三个响应头：`X-AI-Skills-Billing-Currency`、
`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。幂等重放可能返回首次响应与
首次计费头，不能把它解释为二次收费，也不能自行改写金额。
