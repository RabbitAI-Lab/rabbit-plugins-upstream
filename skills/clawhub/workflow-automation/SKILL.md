---
name: workflow-automation
description: Use when 用户需要进行工作流自动化：校验允许列表中的工作流、在明确批准后触发其固定 Production Webhook，或读取限定工作流的执行状态与历史；需要 WORKFLOW_AUTOMATION_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"⚙️","homepage":"https://ai-skills.open-idea.net","primaryEnv":"WORKFLOW_AUTOMATION_API_KEY","requires":{"env":["WORKFLOW_AUTOMATION_API_KEY"]}}}
---

# Workflow Automation

通过 AI Skills 平台安全校验、触发和读取已配置的工作流。默认 API 根为
`https://ai-skills.open-idea.net/api/v1`；`AI_SKILLS_API_URL` 只能覆盖站点根。不要直连或
描述第三方 Provider endpoint。

## 执行流程

1. 按 [API Key 配置](references/API-KEY.md)读取产品专属 Key，不回显完整值。
2. 从 [Operations 契约](references/OPERATIONS.md)选择 operation，只发送白名单字段。
3. 按 [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)为每个新逻辑 POST 生成 UUID。
4. 触发前先 `workflow.validate`，展示固定 workflow、版本与输入，取得用户对当前审批证据的
   明确批准后才 `workflow.trigger`。
5. 按 [触发、对账与安全规则](references/BEHAVIOR-RULES.md)处理超时、structured 结果和计费。

## 核心边界

- 只使用连接允许列表中预先固定的 Production Webhook；不接受用户提供的 URL、host、headers
  或 credentials。
- `workflow.trigger` 必须绑定当前 `version`、`content_hash`、`approval_nonce` 且
  `approved=true`；审批 15 分钟后或工作流版本变化即失效。
- 触发超时或 `reconciliation_required` 时不自动重发；先对账。平台幂等不等于端到端
  exactly-once。
- 触发成功只表示 webhook 已接受，不代表工作流或其外部副作用成功；用执行读取验证状态。

## 参考资料

- [API Key 配置](references/API-KEY.md)
- [Operations 契约](references/OPERATIONS.md)
- [HTTP 请求与任务轮询](references/HTTP-REQUESTS.md)
- [触发、对账与安全规则](references/BEHAVIOR-RULES.md)
