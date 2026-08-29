# 行为、安全与错误

- 不猜测员工身份、可用性、工时偏好或法定限制；用户应审核后使用排班。
- 始终把 unfilled 和 `partial` 明确告知用户，原因 `no_eligible_member` 表示当前约束下没有可用人员。
- 人工调整前展示变化并取得用户同意；发生 `conflict` 时读取新 version，不静默覆盖。
- 排班数据按用户隔离、加密存储；只向当前用户展示 artifacts，避免在公开消息暴露人员信息。
- 网络状态无法确认时用原 Idempotency-Key 对账；仍无法确定则报告 `reconciliation_required`，不创建重复排班。
- 输入或权限失败时显示 `errors.code` 或 `error.code` 的安全摘要，不泄露 API Key、内部路径和堆栈。

本 Skill 是平台本地确定性工具，不调用第三方付费服务；但 AI Skills 平台自身会按成功操作扣费。本 Skill 不替代劳动法规、合同或人事专业审查。
