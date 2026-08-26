# 行为与错误规则

## 幂等与重试

- 每个新逻辑 POST 使用唯一 UUID `Idempotency-Key`；同一逻辑重试复用原值。
- 参数改变后视为新请求，生成新 UUID。连接超时后不知道 POST 是否被接收时，仍复用原键。
- HTTP `409` 且 POST 的 `errors.idempotency_key` 有内容：该键已用于不同请求；停止重发。
  只有用户确实发起新逻辑请求时才换键，不能用换键绕过冲突。
- GET 的 `error.code` 为 `reconciliation_required`：停止自动重发，核对任务历史和账单后
  再行动。
- 只对明确临时的读取失败做有限指数退避；禁止 curl 自动重试 POST。

## HTTP 与错误结构

- HTTP `422`：POST 的 `status` 为 `validation_failed`，字段问题在 `errors`；修正输入后
  作为新请求提交。
- HTTP `402`：余额不足，提示充值，不自动重发。
- HTTP `409`：POST 的 `status` 为 `conflict` 时从 `errors.idempotency_key` 读取幂等冲突；
  GET 的任务状态为 `cancelled` 时从 `error` 读取原因。不要把这两种结构混淆。
- HTTP `503`：若 POST 的 `errors.code` 为 `provider_not_configured`，停止请求并提示用户在
  平台控制台配置 Commerce Radar Provider；不要发送 `provider:auto`，不要绕过平台直连。
- GET 终态失败从 `error.code` 与 `error.message` 读取；POST 的连接错误使用
  `errors.code`，两者不能混淆。
- `failed`、`cancelled` 为失败终态；`partial` 是带部分结果的终态，只交付实际返回内容并
  明示缺失项。错误码或字段缺失时失败关闭，不伪造商品或报告。

## 数据与安全边界

- 只把 `source_url`、观察时间和 Provider 返回字段作为证据；不推断库存、销量或长期价格。
- URL 仅接受公开 HTTP(S) 目标；拒绝环回、私网、localhost、带用户名密码及非 Web 协议。
- 平台负责调用 Provider；禁止从 Skill 直连第三方 endpoint、提交第三方凭证或自行抓站。
- 店铺分析和报告属于读取与汇总，不会修改店铺。发布报告、发送给外部人员或写入其他系统
  前另行取得用户确认。
- 不保证固定价格、固定条数、数据实时或上游成功；以终态响应和计费头为准。
