# 微信搜一搜技能 更新日志

## 1.1.2

- 新增 `references/faq.md`；SKILL 写入 Windows cmd/PowerShell 双壳例与「cmd 只用双引号」。
- CLI 支持 `--json-args`（与传统 flag 互斥；键名用 `keyword`/`sort`/`limit` 等）；`parseCliArgs` 统一入口；SKILL/faq 补例。
- stdout 信封顶层可选 `cost`（透传取数接口花费估算；错误省略）。
- 成功结果默认不落盘；`--save` 或 `GUAIKEI_ENABLE_LOG=1` 时写入系统临时目录 `wechat-guaikei/logs/`（不再写技能目录 `logs/`）。
- `backendCodes`：在余额判断之后将裸 `errcode === 14` 稳定映射为 `PLAN_LIMIT`。
- 补全 `requestApi` 创建重试注释：以 `noRetry` 为准（频控等稳定业务码不重试）。

## 1.1.1

- 错误码 errmsg 优先：`PLAN_LIMIT` / `INSUFFICIENT_BALANCE` / `RATE_LIMITED` / `DAILY_LIMIT`（日限 errcode 18）。

## 1.1.0

- 对照抖音技能统一 JSON 信封、退出码、Header TOKEN、轮询分类与 fail-fast 参数校验。
