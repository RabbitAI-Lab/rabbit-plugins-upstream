# HTTP 请求与任务轮询

每个新逻辑 POST 生成不同 UUID；相同请求超时重试复用原 JSON 与原键。禁止对 POST 使用
curl 自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
FILINGS_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/investment-research/filing.search" \
  -H "Authorization: Bearer $INVESTMENT_RESEARCH_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $FILINGS_KEY" \
  -d '{"cik":"320193","forms":["10-K","10-Q"],"limit":20}' > filings-response.json
```

公司事实使用新 UUID：

```bash
FACTS_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/investment-research/company.facts" \
  -H "Authorization: Bearer $INVESTMENT_RESEARCH_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $FACTS_KEY" \
  -d '{"cik":"320193","taxonomies":["us-gaap"],"tags":["Revenue","NetIncomeLoss"],"units":["USD"],"limit":20}' \
  > facts-response.json
```

只在两个来源达到 `succeeded` 或有真实证据的 `partial` 后，用真实 task ID 构造本地请求：

```bash
jq -n --slurpfile filings filings-response.json --slurpfile facts facts-response.json \
  '{source_task_ids:[$filings[0].task_id,$facts[0].task_id]}' > source-tasks.json

RISK_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/investment-research/risk.analyze" \
  -H "Authorization: Bearer $INVESTMENT_RESEARCH_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $RISK_KEY" --data-binary @source-tasks.json

REPORT_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/investment-research/report.create" \
  -H "Authorization: Bearer $INVESTMENT_RESEARCH_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $REPORT_KEY" --data-binary @source-tasks.json
```

四个 operation 通常同步。若返回 HTTP `202`，读取 `task_id` 并查询相同 operation：

- `/api/v1/investment-research/filing.search/tasks/{task_id}`
- `/api/v1/investment-research/company.facts/tasks/{task_id}`
- `/api/v1/investment-research/risk.analyze/tasks/{task_id}`
- `/api/v1/investment-research/report.create/tasks/{task_id}`

GET 只需 Bearer 鉴权。`queued`、`processing` 从约 2 秒开始指数退避到最长约 30 秒，并限制
总次数与总时长；`succeeded`、`partial`、`failed`、`cancelled` 为终态。达到上限只报告
`task_id` 和当前状态，不新建 POST。

读取 `result.version` 与 operation 对应 structured 字段；`artifacts[]` 只作为平台返回元数据，
不猜下载 URL。计费只读取 `X-AI-Skills-Billing-Currency`、
`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`；同键重放可能返回首次计费头，
不得重复相加。
