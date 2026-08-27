# 证据、安全与错误规则

## SSRF 与证据

- `page.audit` 只提交用户明确指定的公开 URL；拒绝非 HTTP(S)、用户信息、异常端口、
  localhost、IP 字面量，以及 DNS 解析到环回、私网、链路本地或保留地址的主机。
- 平台在校验与任务执行时分别解析精确 host 和适用的 apex host；结果变化视为 DNS 重绑定，
  任务失败。不要由 Skill 自行抓取页面或跟随重定向绕过检查。
- 每条 metric/finding 必须保留真实 `source` 与 `observed_at`。单页问题保留
  `evidence_url`；只有 Provider 明确给出聚合计数时才用 `affected_pages`。
- `partial` 只交付有证据的部分；空结果、缺失字段或未审计页面不能解释为“没有问题”。

## 幂等与错误

- 新逻辑请求使用唯一 UUID `Idempotency-Key`；相同逻辑重试复用原值与 JSON。
- HTTP `422`：POST `status=validation_failed`，字段问题读取 `errors`；修正后用新 UUID。
- HTTP `402`：余额不足，停止并提示充值。
- HTTP `409`：POST `status=conflict` 时读取 `errors.idempotency_key`，停止且不换键绕过。
- HTTP `503` 时优先读取 `error.code`，若不存在再读取 `errors.code`；
  `provider_not_configured` 表示 Provider operation 暂停并需平台内配置。禁止
  `provider:auto` 或第三方直连；本地 `report.create` 有合规输入时仍可独立执行。
- 终态错误读取 `error.code`、`error.message`；提交阶段直接拒绝才可能使用 `errors`。
  `reconciliation_required` 时停止自动重发并核对任务与账单。
- `failed`、`cancelled` 或结构缺失时失败关闭，不伪造 SEO 结果。

## 交付边界

页面、关键词与排名数据是特定来源的时间切片，不保证完整或持续有效。建议需区分数据证据与
分析意见；不保证排名、流量、收入或修复效果。发布报告、改写网站、执行 SEO 变更或写入
外部系统前另行取得用户确认。
