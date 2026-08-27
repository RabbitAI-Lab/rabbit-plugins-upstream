---
name: finxdata
description: 当用户需要查询 FinXData 金融数据 API 时使用本技能，包括按代码或名称搜索股票、股票行情、股票图谱、财务报表、市场新闻、龙虎榜、限售解禁、宏观经济、FRED、异动追踪、额度、更新频率、请求限速与重试、API Key 配置、错误处理或服务健康状态。本技能调用与 FinXData MCP 工具相同的公开 HTTP 接口。
---

# FinXData

FinXData 用于金融数据查询，支持无需鉴权、API Key 和 Agent 来源标识三种访问方式。可调用的数据接口与 MCP 工具表面一致，包括 `/health`、`/api/quota/api-key`，以及 `/api/v1/summary` 中列出的当前 `GET /api/v1/http/*` 接口。

## 配置

```bash
export FINXDATA_API_KEY="sk-..."
export FINXDATA_BASE_URL="https://api.finxdata.ai"
# 仅调用 agent 免费接口时：
export FINXDATA_AGENT_TYPE="openclaw"  # 可用 openclaw / hermes / claude / codex / opencode / workbuddy / qoder 等 agent 类型
```

`FINXDATA_BASE_URL` 是可选项。

如果没有设置 `FINXDATA_API_KEY`，先提示用户需要登录 `www.finxdata.ai` 申请免费的 API Key，再继续调用需要鉴权的数据接口。`health` 和 `summary` 可在没有 API Key 时调用。

`agent` 命令不需要 API Key，但必须通过 `--agent-type` 或 `FINXDATA_AGENT_TYPE` / `AGENT_TYPE` 指定来源 agent 类型，例如 `openclaw`、`hermes`、`opencode`。
`agent` 命令当前支持获取的数据包括：
| 命令 | 接口 | 参数 | 内容 |
|---|---|---|---|
| `agent market-price` | `/api/v1/http/agent/market/price` | `code`，支持多个；另需 `--agent-type` | 指数或板块行情。 |
| `agent stock-quote` | `/api/v1/http/agent/stock/quote` | `code`，支持多个；另需 `--agent-type` | 股票最新行情。 |
| `agent hot-sectors` | `/api/v1/http/agent/market/hot_sectors` | 另需 `--agent-type` | 热门题材/概念榜。 |
| `agent hot-sector` | `/api/v1/http/agent/market/hot_sector` | `name` 或 `theme_id`，`days`，`track_date`；另需 `--agent-type` | 热门题材详情。 |
| `agent hot-reason` | `/api/v1/http/agent/stock/hot_reason` | `code`，`days`；另需 `--agent-type` | 个股题材归因历史。 |
| `agent dragon-tiger` | `/api/v1/http/agent/market/dragon_tiger` | `trade_date`、`min_net_buy`、`limit`、`refresh`；另需 `--agent-type` | 全市场龙虎榜。 |
| `agent track-news` | `/api/v1/http/agent/track/news` | 另需 `--agent-type` | 新闻跟踪快照。 |
| `agent track-market` | `/api/v1/http/agent/track/market` | 另需 `--agent-type` | 市场跟踪快照。 |
| `agent track-notice` | `/api/v1/http/agent/track/notice` | 另需 `--agent-type` | 公告跟踪快照。 |
| `agent economy-china` | `/api/v1/http/agent/economy/china` | `type`；另需 `--agent-type` | 中国宏观经济报表。 |
| `agent economy-calendar` | `/api/v1/http/agent/economy/calendar` | `year`、`month`、`months`；另需 `--agent-type` | 国内宏观数据发布日历。 |
| `agent ontology-abstract` | `/api/v1/http/agent/ontology/abstract` | `code`；另需 `--agent-type` | 股票图谱摘要，不返回实体和关系明细。 |
| `agent financial` | `/api/v1/http/agent/financial` | `code`；另需 `--agent-type` | 股票业绩报表简版。 |

## 调用流程

优先使用内置封装脚本：

```bash
python3 scripts/finxdata.py summary
python3 scripts/finxdata.py quota
python3 scripts/finxdata.py stock search --query 贵州茅台
python3 scripts/finxdata.py stock quote --code 600519
python3 scripts/finxdata.py stock financial --code 600519 --sections reports,mainops
python3 scripts/finxdata.py stock ontology --code 600519
python3 scripts/finxdata.py stock forecast --code 600519
python3 scripts/finxdata.py market price --code 000001 BK0477
python3 scripts/finxdata.py agent market-price --code 000001 BK0477 --agent-type openclaw
python3 scripts/finxdata.py agent stock-quote --code 600519 000001 --agent-type openclaw
python3 scripts/finxdata.py agent hot-sectors --agent-type openclaw
python3 scripts/finxdata.py agent hot-sector --name 人形机器人 --agent-type hermes
python3 scripts/finxdata.py agent hot-reason --code 688017 --days 7 --agent-type openclaw
python3 scripts/finxdata.py agent dragon-tiger --trade-date 2026-06-12 --limit 50 --agent-type hermes
python3 scripts/finxdata.py agent track-news --agent-type hermes
python3 scripts/finxdata.py agent track-market --agent-type hermes
python3 scripts/finxdata.py agent track-notice --agent-type hermes
python3 scripts/finxdata.py agent economy-china --type cpi --agent-type opencode
python3 scripts/finxdata.py agent economy-calendar --year 2026 --month 6 --months 1 --agent-type opencode
python3 scripts/finxdata.py agent ontology-abstract --code 600519 --agent-type openclaw
python3 scripts/finxdata.py agent financial --code 300223 --agent-type openclaw
python3 scripts/finxdata.py market hot-stocks --limit 100
```

封装脚本会输出 API 返回的 JSON；数据接口通常返回 `{"code": 200, "confidence": "高|中高|中", "data": "<字符串、对象或数组>"}`。脚本已内置网络重试、超时控制和常见 HTTP 错误的友好提示。

按这个顺序处理用户请求：

1. 需要确认接口能力时，先运行 `summary`，再选择具体命令。
2. 需要查询数据时，调用最窄的接口和参数；多股票报价或指数价格优先一次传多个 `code`。
3. 查询失败时，先读脚本返回的 `code` 和 `message`，不要把 curl 或堆栈错误直接抛给用户。
4. 返回给普通用户时，优先总结关键字段、日期范围、是否有数据和下一步建议；不要只贴原始 JSON。

## 请求限速

把每一次 HTTP 请求都视为有限资源；Agent 免费接口不扣账户额度，但仍受单 IP 每日限额和服务端频率保护约束，不能当作无限接口使用。

- 执行前先列出完成请求所需的最少接口。默认每个用户问题最多调用 3 个数据接口；没有用户明确授权时不得超过 5 个。达到上限仍无法完成时，停止调用并说明还缺什么。
- 同一任务内不重复请求相同接口和相同参数；复用已经取得的结果。不要为了“确认”结果而再次调用。
- 串行调用接口，不并发轰炸。连续请求之间至少间隔 3 秒；支持多个 `code` 的报价/价格接口必须合并为一次批量请求。
- `summary` 仅在接口能力不确定时调用，`quota` 仅在用户询问额度或 API Key 接口返回 429 时调用；不要把二者作为每次查询的固定前置步骤。
- 不主动使用 `refresh`。仅当用户明确要求刷新，或返回数据明显过期且刷新对回答必不可少时使用；同一数据在一次任务中最多刷新一次。
- 单次脚本调用已由 curl 对暂时性失败最多自动重试 3 次。脚本返回失败后，Agent 不得立即再次运行相同命令，以免把一次失败放大为多轮请求。
- 脚本重试后仍收到 429 时，立即停止该接口的后续调用，不通过切换命令、代码或 `agent-type` 规避限制。优先遵守脚本错误信息中的 `Retry-After`；没有该字段时，本轮不再自动调用，向用户说明稍后再试。
- 收到超时、网络错误或 5xx 且脚本重试仍失败后，本轮最多只报告失败，不再追加探测性 `health`、`summary` 或相邻接口调用。仅在用户明确要求诊断服务状态时调用 `health`。
- 结果已经足以回答用户时立即停止，不为补齐非必要字段继续请求。

## 参考资料

- 精简接口列表：读取 `references/api.md`。
- 场景示例、更新节奏、配额处理、示例结果和 FAQ：读取 `references/usage.md`。

## 规则

- 普通数据接口需要 `X-API-Key`；`stock search` 也需要 API Key，但不消耗账户额度；`agent` 免费接口需要 `x-agent-type`，不扣账户额度。
- 不确定某个接口是否可用时，先查询 `/api/v1/summary`。
- 不描述上游数据源，只描述接口内容、参数、更新时间口径和返回结果。
- 不把金融数据解释成投资建议；需要判断时说明数据来源于接口返回，结论仅供信息整理。
- 如果 API Key 接口配额不足，先运行 `quota`，用 `daily_remaining`、`daily_used`、`daily_max`、`prepaid_balance`、`gift_remaining` 和 `retry_after_seconds` 给出可理解的处理建议。Agent 免费接口的 429 不运行 `quota`。
- 对网络、超时、5xx、429 这类暂时性问题，说明脚本已重试；建议稍后重试、缩小查询范围或检查额度/网络。
