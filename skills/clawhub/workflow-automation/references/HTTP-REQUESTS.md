# HTTP 请求与任务轮询

每个新逻辑 POST 生成不同 UUID；同一请求超时恢复复用原 JSON 与原键。禁止对 POST 使用 curl
自动重试。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
VALIDATE_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"

curl --fail-with-body "$API_ROOT/workflow-automation/workflow.validate" \
  -H "Authorization: Bearer $WORKFLOW_AUTOMATION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $VALIDATE_KEY" \
  -d '{"workflow_id":"order_sync"}' > validate-response.json
```

向用户展示 workflow、审批过期时间、固定 Production Webhook 动作和确切 input。获得明确批准后，
只用真实审批证据构造触发体：

```bash
jq '{workflow_id:.result.approval.workflow_id,approved:true,version:.result.approval.version,content_hash:.result.approval.content_hash,approval_nonce:.result.approval.approval_nonce,input:{order_id:"o-42",dry_run:false}}' \
  validate-response.json > trigger-input.json
TRIGGER_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/workflow-automation/workflow.trigger" \
  -H "Authorization: Bearer $WORKFLOW_AUTOMATION_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $TRIGGER_KEY" --data-binary @trigger-input.json > trigger-response.json
```

读取单次执行与最近成功执行分别使用新 UUID：

```bash
READ_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/workflow-automation/execution.read" \
  -H "Authorization: Bearer $WORKFLOW_AUTOMATION_API_KEY" -H "Content-Type: application/json" \
  -H "Idempotency-Key: $READ_KEY" -d '{"workflow_id":"order_sync","execution_id":"9001"}'

HISTORY_KEY="$(uuidgen | tr '[:upper:]' '[:lower:]')"
curl --fail-with-body "$API_ROOT/workflow-automation/execution.history" \
  -H "Authorization: Bearer $WORKFLOW_AUTOMATION_API_KEY" -H "Content-Type: application/json" \
  -H "Idempotency-Key: $HISTORY_KEY" -d '{"workflow_id":"order_sync","status":"success","limit":20}'
```

四个 operation 通常同步。若返回 HTTP `202`，读取 `task_id` 并查询相同 operation：

- `/api/v1/workflow-automation/workflow.validate/tasks/{task_id}`
- `/api/v1/workflow-automation/workflow.trigger/tasks/{task_id}`
- `/api/v1/workflow-automation/execution.read/tasks/{task_id}`
- `/api/v1/workflow-automation/execution.history/tasks/{task_id}`

GET 只需 Bearer 鉴权。`queued`、`processing` 从约 2 秒开始指数退避到最长约 30 秒，并限制
总次数与总时长；`succeeded`、`partial`、`failed`、`cancelled` 为终态。但触发任务若为
`processing` 且 `error.code=reconciliation_required`，立即停止自动轮询和 POST 重发，转人工对账。

读取 `result.version`、operation 对应 structured 字段和 `artifacts[]` 元数据，不猜下载 URL。
计费只读取 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、
`X-AI-Skills-Billing-Balance`；同键重放可能返回首次计费头，不重复相加。
