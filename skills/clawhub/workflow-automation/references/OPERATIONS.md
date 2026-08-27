# Operations 契约

| operation | POST 路径 | 行为 | 主要结果 |
|---|---|---|---|
| `workflow.validate` | `/api/v1/workflow-automation/workflow.validate` | 通常同步、只读校验 | `result.workflow`、`result.approval` |
| `workflow.trigger` | `/api/v1/workflow-automation/workflow.trigger` | 通常同步、高风险外部动作 | `result.execution` |
| `execution.read` | `/api/v1/workflow-automation/execution.read` | 通常同步、只读 | `result.execution` |
| `execution.history` | `/api/v1/workflow-automation/execution.history` | 通常同步、只读分页 | `result.executions` |

对应任务 GET 为 `/api/v1/workflow-automation/{operation}/tasks/{task_id}`。四个 operation/ability
都需要已配置连接，均返回 structured 结果。

## workflow.validate

只接受允许列表中的 `workflow_id`，1–100 位字母、数字、下划线或连字符。

```json
{"workflow_id":"order_sync"}
```

读取 `workflow` 的 `workflow_id`、`name`、`active`、`version`、`content_hash`、`updated_at`、
`source`、`observed_at`，以及 `approval.workflow_id`、`version`、`content_hash`、
`approval_nonce`、`action=trigger_n8n_production_webhook`、`expires_at`。审批有效期 15 分钟，
nonce 一次性使用；校验不等于批准或触发。

## workflow.trigger

必填 `workflow_id`、`approved=true`、校验返回的 `version`、64 位小写十六进制
`content_hash` 与 `approval_nonce`。可选 `input` 必须是 JSON object。

```json
{"workflow_id":"order_sync","approved":true,"version":"version-7","content_hash":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","approval_nonce":"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb","input":{"order_id":"o-42","dry_run":false}}
```

示例 hash/nonce 只说明格式，真实触发必须用刚才 validate 返回的值。input 最大 32 KiB、最多
64 个 key、嵌套深度最多 4、字符串最多 4096 字节；递归禁止 `headers`、`header`、
`credentials`、`credential`、`binary`、`url`、`host`、`authorization`、`cookie`、`secret`、
`token`、`_ai_skills_request_id`。不要传 webhook URL、认证或 workflow_id 到 input。

成功读取 `execution_id`、`workflow_id`、`status=accepted`、`platform_request_id`、
`approved_version`、`approved_content_hash`、`source`、`observed_at`。accepted 不是最终成功。

## execution.read

只接受允许列表中的 `workflow_id` 与 1–100 位 `execution_id`。

```json
{"workflow_id":"order_sync","execution_id":"9001"}
```

读取 `execution_id`、`workflow_id`、`status`、`started_at`、`stopped_at`、`source`、
`observed_at`，并核对结果仍属于请求的 workflow。

## execution.history

必填 `workflow_id`；可选 `status` 为 `canceled|crashed|error|new|running|success|unknown|waiting`，
`limit` 1–100（默认 20），`cursor` 最多 2048 位且只含字母、数字、下划线、连字符。

```json
{"workflow_id":"order_sync","status":"success","limit":20}
```

读取 `executions[]` 的同一受限执行字段及 `pagination.next_cursor`；不要请求或声称返回完整执行
数据、任意凭证或工作流内部 secret。
