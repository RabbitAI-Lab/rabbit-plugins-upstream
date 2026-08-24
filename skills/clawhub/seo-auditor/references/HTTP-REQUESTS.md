# HTTP 请求与任务轮询

每个新逻辑 POST 生成 UUID；相同请求超时重试复用原 JSON 与原键。禁止对 POST 使用 curl
自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
REQUEST_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/seo-auditor/page.audit" \
  -H "Authorization: Bearer $SEO_AUDITOR_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REQUEST_KEY" \
  -d '{"url":"https://example.com"}'
```

`page.audit` 成功受理通常返回 HTTP `202`、`task_id`、`status`、`operation`。查询：

```bash
TASK_ID="POST_RESPONSE_TASK_ID"

curl --fail-with-body \
  "$API_ROOT/seo-auditor/page.audit/tasks/$TASK_ID" \
  -H "Authorization: Bearer $SEO_AUDITOR_API_KEY"
```

全部模板：

- `/api/v1/seo-auditor/keyword.research/tasks/{task_id}`
- `/api/v1/seo-auditor/page.audit/tasks/{task_id}`
- `/api/v1/seo-auditor/competitor.gap/tasks/{task_id}`
- `/api/v1/seo-auditor/report.create/tasks/{task_id}`

`queued`、`processing` 继续等待；从约 2 秒开始指数退避到最长约 30 秒，限制总次数与总
时长。`succeeded`、`partial`、`failed`、`cancelled` 为终态。达到上限只报告任务 ID 和
当前状态，不新建 POST。

读取 `result.version` 以及 `metrics`、`findings` 或 `report`；`artifacts[]` 只作为平台返回
元数据，不猜下载 URL。计费只读取 `X-AI-Skills-Billing-Currency`、
`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。幂等重放可能返回首次计费头，
不能重复相加。
