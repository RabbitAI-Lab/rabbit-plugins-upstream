# HTTP 请求与任务查询

## 请求示例

每个新逻辑请求生成 UUID；相同请求因超时重试时必须复用原 JSON 与原键。禁止对 POST 使用
curl 自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
REQUEST_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/lead-intelligence/company.search" \
  -H "Authorization: Bearer $LEAD_INTELLIGENCE_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_KEY" \
  -d '{"domains":["example.com"],"page":1,"per_page":20}'
```

同步成功/部分成功通常返回 HTTP `200`，包含 `task_id`、`status`、`operation`、structured
`result` 与 `artifacts`。

## 202 与任务查询

若 POST 返回 `202`，查询同 operation，不再创建 POST：

```bash
TASK_ID="POST_RESPONSE_TASK_ID"

curl --fail-with-body \
  "$API_ROOT/lead-intelligence/company.search/tasks/$TASK_ID" \
  -H "Authorization: Bearer $LEAD_INTELLIGENCE_API_KEY"
```

完整模板：

- `/api/v1/lead-intelligence/company.search/tasks/{task_id}`
- `/api/v1/lead-intelligence/people.search/tasks/{task_id}`
- `/api/v1/lead-intelligence/lead.score/tasks/{task_id}`
- `/api/v1/lead-intelligence/report.create/tasks/{task_id}`

`queued`、`processing` 继续等待；从约 2 秒开始指数退避到最长约 30 秒，并限制总次数与总
时长。`succeeded`、`partial`、`failed`、`cancelled` 是终态。达到上限只返回任务 ID 和
状态，不误报失败。

## 结果、产物与计费

读取 `result.version` 以及 operation 对应的 `companies`、`people`、`pagination`、`leads`、
`report`。`artifacts[]` 只作为平台返回元数据，不猜测下载 URL。

计费只读取 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、
`X-AI-Skills-Billing-Balance`。幂等重放可能返回首次响应与首次计费头，不将其相加或解释为
二次收费。企业/联系人按成功返回记录计费，空结果可为零单位；`lead.score` 免费，报告按一份
结算，但任何具体金额都只引用真实响应头。
