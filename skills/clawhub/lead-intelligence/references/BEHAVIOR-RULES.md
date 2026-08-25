# 隐私、评分与错误规则

## 隐私边界

- 禁止发送 `linkedin_cookie`、`cookie`、`linkedin_username`、`linkedin_password`、
  `username`、`password`、`session`、`payload`、`provider_payload`、`apollo_payload`；所有
  operation 都拒绝这些字段。
- 不登录、抓取或自动操作 LinkedIn。用户主动提供 Cookie、密码或 session 时拒绝接收并
  建议撤销已暴露凭证。
- `people.search` 不调用联系方式 enrichment，不返回邮箱或电话号码。只原样报告
  `email_available`、`direct_phone_available`，且不推断邮箱、不推断电话。
- 企业或联系人为空、姓名被遮蔽、时间字段缺失时保持未知，不拼接或购买个人信息。

## 确定性评分

`lead.score` 只使用提交字段，最高 6 points：

| 可观察信号 | points |
|---|---:|
| `latest_funding_date` 在执行日之前（含当天）365 天内 | +2 |
| `active_job_count` 大于 0 | +1 |
| `title` 与任一 `target_titles` 去空白、忽略大小写后完全匹配 | +2 |
| `technologies` 与 `target_technologies` 存在去空白、忽略大小写的交集 | +1 |

`score = points × 100 ÷ 6`，使用 half-up 四舍五入为 0–100 整数。未来融资日期不加分。
`reasons` 逐项解释实际加分。不要用 LLM、搜索结果或主观判断改变分数，也不把 100 分称为
真实、有意向或保证转化。

## 幂等与错误

- 新逻辑 POST 使用唯一 UUID `Idempotency-Key`；同一逻辑重试复用原值和 JSON。
- HTTP `422`：POST `status=validation_failed`，问题读取 `errors`；修正后用新 UUID。
- HTTP `402`：余额不足，提示充值，不自动重发。
- HTTP `409`：POST `status=conflict` 时读取 `errors.idempotency_key`；停止重发且不换键绕过。
  GET 的 `cancelled` 原因从 `error` 读取。
- 搜索接口 HTTP `503` 时优先读取 `error.code`；若该字段不存在，再读取 `errors.code`。
  任一字段为 `provider_not_configured` 时停止并引导用户在平台配置 Lead Intelligence
  Provider。禁止添加 `provider:auto`、使用 LinkedIn Cookie 或直连第三方；本地
  `lead.score`、`report.create` 不需要 Provider，可按用户原意独立执行。
- GET 失败读取 `error.code`、`error.message`；POST 在任务已建立后的终态错误同样使用
  `error`，只有提交阶段直接拒绝时才可能使用 `errors`。
  `error.code=reconciliation_required` 时停止自动重发并核对任务与账单。
- `partial` 只交付有效记录并说明逐项问题；`failed`、`cancelled` 或结构缺失时失败关闭。

## 外部动作

搜索、评分和本地报告都是读取/计算。把联系人数据或报告发送给第三方、写入 CRM、发起外联、
购买联系方式或扩大批次前，必须另行获得用户确认并遵守适用隐私与营销规则。
