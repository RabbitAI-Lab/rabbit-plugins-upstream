# HTTP 请求与任务查询

## 同步请求示例

每个新逻辑 POST 使用新的 UUID；相同请求因网络超时重试时复用原请求体和原键。禁止给
POST 配置 curl 自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
REQUEST_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/ad-intelligence/creative.search" \
  -H "Authorization: Bearer $AD_INTELLIGENCE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_KEY" \
  -d '{"query":"example.com","location_code":2840,"depth":40,"platform":"youtube","format":"video"}'
```

同步成功或部分成功通常返回 HTTP `200`，响应含 `task_id`、`status`、`operation`、
`result` 与 `artifacts`。不要因为客户端超时就换键重发。

## 202 与任务查询

如果 POST 返回 `202`，以响应的 `task_id` 查询同 operation；不要创建新的 POST 代替查询：

```bash
TASK_ID="POST_RESPONSE_TASK_ID"

curl --fail-with-body \
  "$API_ROOT/ad-intelligence/creative.search/tasks/$TASK_ID" \
  -H "Authorization: Bearer $AD_INTELLIGENCE_API_KEY"
```

模板路径为：

- `/api/v1/ad-intelligence/creative.search/tasks/{task_id}`
- `/api/v1/ad-intelligence/advertiser.analyze/tasks/{task_id}`
- `/api/v1/ad-intelligence/trend.report/tasks/{task_id}`

`queued`、`processing` 继续等待；采用从约 2 秒开始、最长约 30 秒的有界指数退避。
`succeeded`、`partial`、`failed`、`cancelled` 为终态。达到等待上限时返回 `task_id` 和当前
状态，不误报失败。

## 结果与费用

读取 `result.version` 及 operation 对应的 `creatives`、`analysis`、`advertisers`、`report`。
`artifacts[]` 只作为平台返回的产物元数据，不猜测下载 URL。

计费只读取 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、
`X-AI-Skills-Billing-Balance`。幂等重放可能返回首次响应与首次计费头，不能将其相加或解释
为二次收费。
