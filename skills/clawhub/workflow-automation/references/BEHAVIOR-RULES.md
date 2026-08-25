# 触发、对账与安全规则

## 审批与固定目标

- validate 只校验连接允许列表中已发布的 workflow，并签发绑定当前版本、内容 hash 的 15 分钟
  一次性审批证据。向用户展示 workflow 和确切 input；用户明确批准当前动作后才提交 trigger。
- 只能触发连接中固定的 Production Webhook。拒绝调用者提供的 URL、host、headers、
  credentials、authorization、cookie、secret、token 或 binary；不得修改目标或认证。
- 触发前平台重新检查已发布版本；`approval_stale` 表示版本、hash、nonce、时效或一次性资格
  已失效，必须重新 validate、重新展示并重新取得批准。
- `provider_connection_changed` 表示连接版本变化，旧任务失败关闭；不要让旧审批跨连接使用。

## 超时与对账

- workflow trigger 是高风险外部动作。超时或 `reconciliation_required` 表示 webhook 可能已
  接受，不自动重发、不换幂等键、不重新消费审批；保留原 JSON、UUID、task_id 和计费证据。
- 有 task_id 时只查原任务。无法确定时交付“待对账”，由人工核对平台任务、工作流执行历史及
  下游业务记录。不要把超时说成失败，也不要根据未出现 execution_id 推断未执行。
- Idempotency-Key 只约束平台请求受理；工作流内部及下游系统可能有独立副作用，因此不保证
  exactly-once。`status=accepted` 也不等于执行成功，使用 `execution.read` 核验。

## Provider 与错误

- HTTP `503` 优先读取 `error.code`，不存在时再读 `errors.code`；`provider_not_configured` 时在
  AI Skills 平台配置连接和允许列表，禁止第三方直连或索取 secret。
- HTTP `422` 普通字段问题读取 `errors`；HTTP `402` 停止并提示充值。
- HTTP `409` 的 POST `status=conflict` 读取 `errors.idempotency_key`，停止且不换键绕过。
- 终态错误读取 `error.code`、`error.message`；`partial` 只交付真实结果并说明缺失。
- 不承诺固定价格、Provider 可用性、工作流成功或下游效果。触发以外的新外部动作需要另行授权。
