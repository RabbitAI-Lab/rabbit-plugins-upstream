# 行为、证据与错误规则

## 幂等与错误结构

- 每个新逻辑 POST 使用唯一 UUID `Idempotency-Key`；相同请求重试复用原值和相同 JSON。
- HTTP `422`：POST `status=validation_failed`，字段问题读取 `errors`；修正后用新 UUID。
- HTTP `402`：余额不足，提示充值，不自动重发。
- HTTP `409`：POST `status=conflict` 时读取 `errors.idempotency_key`，停止重发；只有新的逻辑
  请求才换键。GET 的 `cancelled` 原因从 `error` 读取。
- HTTP `503` 且 POST `errors.code=provider_not_configured`：停止并提示用户在平台配置 Ad
  Intelligence Provider。禁止添加 `provider:auto`、猜测 Provider 列表或绕过平台直连。
- GET 的失败原因读取 `error.code`、`error.message`；POST 连接错误读取 `errors.code`，不可
  混淆。`error.code=reconciliation_required` 时停止自动重发，先核对任务与账单。
- `partial` 只交付实际素材及错误说明；`failed`、`cancelled` 不得当作空成功。响应结构缺失
  时失败关闭。

## 证据与使用边界

- 保留每条素材/广告主的 `source_url`、`regions`、`first_seen_at`、`last_seen_at`；不存在的
  字段不推断。
- 来源记录表明公开数据在某时被观察到，不证明素材现在仍投放，也不证明广告表现或归因。
- 不从广告主名称推断公司身份，不把 `creative_text`、图片或视频链接当作再利用授权。
- 搜索、分析与报告都是读取操作。下载并再发布素材、发送报告、写入外部系统或扩大到用户
  未要求的地区/批次前，另行取得确认。
- 不承诺价格、条数、完整性、实时性或 Provider 成功；只报告实际结果和计费头。
