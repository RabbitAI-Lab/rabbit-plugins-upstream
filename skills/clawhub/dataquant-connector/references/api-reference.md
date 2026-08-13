# DataQuant Connector — 详细参考

> 本文件是 `SKILL.md` 的外置参考，承载篇幅较大的字段表与参数表，避免占满调用上下文（progressive disclosure）。
> 所有接口、参数、默认值、字段均核对自线上 api-docs（https://app.dataquant.trade/api-docs）及平台后端源码，确保与线上服务一致。

## 市场代码

| 代码 | 市场 |
|------|------|
| ashare | A 股 |
| hkstock | 港股 |
| usstock | 美股 |
| crypto | 加密货币 |
| indices | 全球指数 |
| etfs | ETF |

Coverage：A 股 ~3000 / 港股 ~1000 / 美股 ~2000 / 加密 ~100 / 指数 15 / ETF 11。

## /screen 字段白名单（后端 `DETAIL_FILTERABLE`，完整列表）

任意 `min_<列>` / `max_<列>` 或 `sort=<列>` 都必须是下列字段之一；不在白名单的列被服务端静默忽略。

| 分组 | 字段 |
|------|------|
| 估值 | `pe_ratio` `pe_lyr` `pb_ratio` `dividend_ratio_ttm` `eps_ttm` |
| 规模 | `total_market_cap` `circulating_market_cap` `total_shares` `float_shares` |
| 活跃度 | `turnover_rate` `volume_ratio` `range_pct` |
| 动量 | `change_percent` `chg_5d` `chg_10d` `chg_20d` `chg_60d` `chg_ytd` |
| 位置/均线 | `close_vs_ma20` `close_vs_52w_high` `ma5` `ma10` `ma20` `ma60` `high_52week` `low_52week` |
| 行情 | `volume` `amount` `open` `high` `low` `close` |

screen 返回列固定为服务端 `_SCREEN_COLUMNS`（23 列：symbol / name / market_name / date / close + 估值 / 规模 / 动量 / 均线 等）。

## 常用 detail 字段（后端 `DETAIL_COLUMNS`）

| 分组 | 字段 |
|------|------|
| 标识 | `symbol` `date` `name` `market_name` |
| 行情 | `open` `high` `low` `close` `pre_close` `avg_price` `volume` `amount` `change` `change_percent` |
| 估值 | `pe_ratio` `pe_fwd` `pe_lyr` `pb_ratio` `dividend_ratio_ttm` `dividend_ttm` `eps_ttm` `wb_ratio`(港股特有) |
| 规模 | `total_market_cap`(亿元·本币) `circulating_market_cap` `total_shares` `float_shares` |
| 动量 | `chg_5d` `chg_10d` `chg_20d` `chg_60d` `chg_ytd` |
| 52 周 | `high_52week` `low_52week` `close_vs_52w_high` |
| 均线 | `ma5` `ma10` `ma20` `ma60` `close_vs_ma20` |

`detail` 接口默认返回全部字段；`symbol`、`date` 始终返回，不受 `fields` 过滤；detail 不含 `adj_factor`。

## 套餐与配额（后端 `PLANS_DEFINITION`）

| | 免费版 | 专业版 | 企业版 |
|---|---|---|---|
| 日配额（行） | 5,000 | 200,000 | 2,000,000 |
| 速率（rpm，文档值） | 30 | 120 | 600 |
| 批量标的 | 5 | 50 | 50 |
| 单次行数 | 100 | 500 | 500 |

- 配额按「返回行数」计：kline 按行数、detail 按标的数、screen 按 `limit`。
- 速率：api-docs 文档值为上表；**服务端另设全局 `200/min` 硬上限**，超限返回 429。
- 建议：批量请求之间留 ≥ 0.5s 间隔；先用 `/quota` 看剩余再决定分批或缩减时间跨度。

## 错误码（HTTP 状态）

| HTTP | 含义 | 处理 |
|------|------|------|
| 400 | 参数错误 | `fields` 非法 / `symbols` 超套餐上限 / `market` 不存在 / `indicator` 未知 |
| 401 | 认证失败 | `X-API-Key` 缺失、无效或已禁用 → 让用户检查 Key |
| 403 | 禁止访问 | 仅 dashboard 写操作的 CSRF 校验；本 Skill 只做 GET 查询，正常不会触发 |
| 404 | 资源不存在 | 标的代码不存在 / `macro` 库未就绪 |
| 429 | 速率或配额耗尽 | 退避后重试；仍失败则告知用户配额用尽 |
| 503 | 服务暂不可用 | 优雅关闭中；稍后重试 |
