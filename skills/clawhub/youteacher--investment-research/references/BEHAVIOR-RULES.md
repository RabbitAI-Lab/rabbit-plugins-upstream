# 来源、证据与投资安全规则

## 可信来源

- 只把真实查询响应的 `task_id` 放入 `source_task_ids`；禁止传手写 URL、filings/facts 数组、
  任意旧响应、其他用户/产品/operation 的任务，或随机生成 UUID 冒充来源。
- 来源任务必须为 `succeeded` 或有证据的 `partial`，结果版本有效且未截断；最多 2 个任务、
  合计最多 40 条 canonical 证据。平台会拒绝越权、重复、失败、篡改或无证据来源。
- 每项结论保留 accession、form、filed、period、unit、`source` 与 `observed_at`。不要自行抓取
  source URL，也不要允许用户控制 Provider host、path 或 User-Agent。
- 空结果或缺少某个 tag 只说明本次来源与筛选未返回数据，不证明该事实不存在。

## 投资安全

- `risk.analyze` 与 `report.create` 使用固定确定性模板，不接受自由文本结论，也不利用检索
  结果生成买入、卖出、持有、目标价、交易时机、保本或保证收益。
- 每次交付原样包含“仅供信息参考，不构成投资建议”。申报是特定时间的历史披露，不是实时
  股价、估值、市场共识或个性化财务建议。
- 用户追问“是否应买入并保证收益”时，明确拒绝保证或下交易指令；可以总结真实披露证据、
  局限与待核事项，但不能扩展成个性化投资决策。

## Provider、错误与恢复

- `filing.search`/`company.facts` 需要平台 Provider；HTTP `503` 优先读取 `error.code`，不存在
  时再读 `errors.code`。`provider_not_configured` 时停止上游查询，禁止第三方直连；已有真实、
  有权且有效的来源任务仍可供两个本地 operation 使用。
- HTTP `422` 普通字段问题读取 `errors`；HTTP `402` 停止并提示充值。
- HTTP `409` 的 POST `status=conflict` 读取 `errors.idempotency_key`，停止且不换键绕过。
- 终态失败读取 `error.code`、`error.message`；`reconciliation_required` 时停止自动重发，先核对
  任务与账单。`partial` 只交付真实证据并明确缺失项。
- 新逻辑 POST 使用新 UUID；同一请求超时只用原 JSON 和原键恢复。有 `task_id` 时只查询原任务，
  禁止 curl 自动重试 POST。

不保证数据完整、持续有效、固定价格或 Provider 成功；不得把该 Skill 用于自动交易、执行订单
或承诺投资回报。
