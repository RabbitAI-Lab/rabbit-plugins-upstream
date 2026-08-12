---
name: dataquant-connector
description: >-
  对接 DataQuant 量化数据平台，为回测与选股提供 REST API 取数通道，覆盖 A股/港股/美股/加密货币/指数/ETF 六大市场，支持 K线、估值快照、条件筛选与宏观数据。
  当用户需要从 DataQuant 查询行情、K线、估值快照、条件选股或宏观数据，或消息中出现 "DataQuant" / "dataquant kline" / "dataquant screen" 等取数指令时启用本 Skill。
---

# DataQuant Connector

## 触发条件

当用户消息包含以下任一模式时启动本 Skill：

| 类别 | 触发词（含中文/英文） |
|------|----------------------|
| 取数指令 | "用 DataQuant 取"、"DataQuant 查"、"dataquant kline"、"dataquant batch"、"dataquant detail"、"dataquant screen"、"dataquant search"、"dataquant macro"、"dataquant quota" |
| API Key 提供 | "DataQuant API Key 是"、"DQ_API_KEY="、"DATAQUANT_API_KEY" |

## 前置依赖

- **必装**：Python 3.8+，`requests`（`pip install requests`）
- **必填**：DataQuant API Key（注册地址：https://app.dataquant.trade）。优先读环境变量 `DATAQUANT_API_KEY`，缺失时向用户索取，不要自己编造。
- **Base URL**：`https://api.dataquant.trade`，认证方式 `X-API-Key` Header（CLI 已封装）。

## 市场代码（固定 6 个）

```
ashare     A 股
hkstock    港股
usstock    美股
crypto     加密货币
indices    全球指数
etfs       ETF
```

Coverage：A 股 ~3000 / 港股 ~1000 / 美股 ~2000 / 加密 ~100 / 指数 15 / ETF 11。

## 端点总览

| 命令 | 方法 + 路径 | CLI 子命令 |
|------|------------|-----------|
| 单标的日线 | `GET /{market}/klines/{symbol}` | `kline` |
| 批量日线 | `GET /{market}/klines`（`symbols=` 逗号分隔，必填） | `batch` |
| 单标的最新快照 | `GET /{market}/detail/{symbol}` | `detail`（单代码） |
| 批量最新快照 | `GET /{market}/detail`（`symbols=` 逗号分隔） | `detail`（多代码） |
| 条件筛选 | `GET /{market}/screen` | `screen` |
| 标的搜索 | `GET /{market}/symbols` | `search` |
| 宏观数据 | `GET /macro` | `macro` |
| 配额查询 | `GET /quota` | `quota` |

## 参数与默认值

**K 线 fields**
- 单标的 `/klines/{symbol}`：默认 `*`（全字段）。
- 批量 `/klines`：默认 `close,volume`。
- `fields` 支持短码或全名：`o,h,l,c,v,a` / `open,high,low,close,volume,amount`；非法列返回 400。
- `adj`：`bfq`（不复权，默认）/ `qfq` / `hfq`。
- `limit`：单标的默认 100；批量默认 100。服务端按套餐 `max_single_rows` 截断（free=100，pro/ent=500）。
- `offset`：默认 0。
- 批量额外支持 `date=YYYY-MM-DD`（与 `start`/`end` 互斥，取该日快照）。

**detail fields**：默认 `*` 全字段。`symbol`、`date` 始终返回，不受 `fields` 过滤。detail 接口不含 `adj_factor`。

**screen**
- `sort` 默认 `change_percent`；`order` 默认 `desc`。
- `limit` 默认 50；`offset` 默认 0。返回列固定为服务端 `_SCREEN_COLUMNS`（23 列：symbol/name/market_name/date/close + 估值/规模/动量/均线 等）。
- 过滤语法：`min_<列>` / `max_<列>`，列名必须在白名单内（见 `references/api-reference.md`）；不在白名单的列被服务端静默忽略。

**search（`/{market}/symbols`）**
- `search`：对 symbol 代码做子串匹配（例如 `600519`、`sh600519`、`BTC`）。不支持中文名称搜索——服务端仅按代码匹配，传 `贵州茅台`/`茅台` 返回空。
- `limit` 默认 50，最大 100；`offset` 默认 0。
- 返回结构：`{"market","total","count","offset","symbols":[...]}`，`symbols` 是代码字符串列表（不含名称）。

**macro**
- `indicator`：`gdp` / `cpi_ppi` / `pmi`，不传返回全部。
- `start` / `end`：年份 `YYYY`（可选）。⚠️ 服务端按字符串比较 `date`，若想包含末年数据，建议 `end` 用年末日期（如 `2025-12-31`）或省略 `end`。
- `limit` 默认 100；`offset` 默认 0。返回 `data[]` 中 `data` 字段已由服务端解析为对象，调用方无需二次 `json.loads`。

## /screen 可筛选 / 可排序字段

完整白名单（分组）见 **`references/api-reference.md` → 「/screen 字段白名单」**。筛选/排序的列名必须取自该表，否则被服务端静默忽略。

## 常用 detail 字段

完整字段（分组）见 **`references/api-reference.md` → 「常用 detail 字段」**。响应示例与完整定义以线上 api-docs 为准。

## K 线复权（adj_factor）

- 每行 K 线始终返回 `symbol`、`date`、`adj_factor`。
- `adj_factor = hfq_close / bfq_close`（恒正，首日 ≈ 1.0）。
- `bfq_price` = 原始不复权价（默认）。
- `hfq_price = bfq_price × adj_factor`。
- `qfq_price = bfq_price × adj_factor / 最新日 adj_factor`。
- 仅缩放 `open/high/low/close`；`volume/amount` 不缩放。
- 取 K 线用于计算指标时建议 `--adj qfq`，避免除权除息跳空。

## 套餐与配额

- 配额按「返回行数」计：kline 按行数、detail 按标的数、screen 按 `limit`。
- 速率：api-docs 文档值 30/120/600 rpm（免费/专业/企业）；**服务端另设全局 `200/min` 硬上限**，超限返回 429。
- 建议：批量请求之间留 ≥ 0.5s 间隔；先用 `/quota` 看剩余再决定分批或缩减时间跨度。
- 完整套餐表（日配额 / 批量标的 / 单次行数）见 **`references/api-reference.md` → 「套餐与配额」**。

## 错误处理

HTTP 状态含义与处理见 **`references/api-reference.md` → 「错误码」**。要点：401 让用户检查 Key；429/503 退避后重试；403 仅 dashboard 写操作会触发，本 Skill 只做 GET 不会遇到。

## Agent 工作流

### 1. 获取 API Key
`os.environ.get("DATAQUANT_API_KEY")` → 不存在则问用户要，禁止自造。

### 2. 选命令（示例均为真实可跑）

```bash
# 单标的日线（前复权）
python scripts/dataquant.py kline ashare sh600519 --start 2020-01-01 --end 2025-12-31 --adj qfq --api-key KEY
# 批量日线（默认 close,volume）
python scripts/dataquant.py batch ashare sh600519,sz000858 --start 2025-01-01 --adj bfq --api-key KEY
# 最新快照（单 / 多）
python scripts/dataquant.py detail ashare sh600519 --api-key KEY
python scripts/dataquant.py detail ashare sh600519,sz000858 --api-key KEY
# 条件筛选（列名取白名单）
python scripts/dataquant.py screen ashare --min-pe-ratio 0 --max-pe-ratio 30 --min-total-market-cap 1000 --sort chg_20d --api-key KEY
# 标的搜索（按代码子串，非名称！）
python scripts/dataquant.py search ashare 600519 --api-key KEY
# 宏观
python scripts/dataquant.py macro gdp --start 2020 --end 2025 --api-key KEY
# 配额
python scripts/dataquant.py quota --api-key KEY
```

### 3. 解析响应
CLI 输出 JSON 到 stdout；用 `raise_for_status()` 检查 HTTP 状态。字段含义见上方「常用 detail 字段」「K 线复权」；完整字段与响应示例见 `references/api-reference.md` 与线上 api-docs。

## 文件清单与角色

| 文件 | 必须 |
|------|------|
| `SKILL.md` | ✅ |
| `skill.json` | ✅ |
| `scripts/dataquant.py` | ✅ |
| `references/api-reference.md` | ✅ |
| `README.md` | — |
| `LICENSE` | — |

字段定义与响应示例以 https://app.dataquant.trade/api-docs 为准，本 Skill 只做精确摘要，不替代 api-docs。
