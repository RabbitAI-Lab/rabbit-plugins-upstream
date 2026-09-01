---
name: hectorlee-global-risk-signal
slug: hectorlee-global-risk-signal
version: 1.0.0
displayName: 盘前雷达
category: finance
platforms:
  - WorkBuddy
  - ClawHub
description: "A股盘前外围风险信号雷达。聚合外围行情(A50期货/纳指期货/离岸人民币/美元指数/VIX/美债10Y)、地缘事件(GDELT)、财经日历(华尔街见闻)、中国资金面(两融/龙虎榜/沪深港通)、国内新闻(中新网/东财快讯/新浪滚动)、宏观数据(东财PMI/CPI/PPI+World Bank)六大维度，做多空情景推演打分，输出方向判断+1-5级风险分级+可分享信号卡，支持推送飞书群。MIT开源免费、零第三方依赖、无key开箱即用。触发词：盘前雷达、盘前信号、外围风险、全球风险、外围市场、今晚外围、盘前外围、风险信号、今日外围、外围异动。"
agent_created: true
metadata:
  author: hectorlee
  license: MIT
  tags: global-risk, premarket, market-signal, A-share, finance, open-source, zero-dependency
  compatibility: workbuddy
---

# 盘前雷达（Global Risk Signal）

A 股盘前外围风险信号。聚合六大维度数据，做**多空情景推演**（经验驱动、非机械打分），输出方向判断 + 1-5 级风险分级 + 可分享信号卡，并支持推送到飞书群。

## 核心定位

- **面向对象**：A 股散户，盘前 30 秒看懂"外围今天有没有雷/有没有催化"。
- **分析方法**：多头逻辑 vs 空头逻辑的情景推演，输出方向概率 + 反向风险条件，不做机械打分。
- **配色约定**：红 = 利多，绿 = 利空（A 股心智）；风险条用琥珀色 1-5 级，避免与多空色冲突。

## 红线

- **禁止编造数据**：所有指标必须来自脚本实时采集，标注来源与数值。
- **不确定就直说**：信号混乱时明确标"方向不明"，不强行给结论。
- **必须附免责声明**：每次输出末尾附：
  > 免责声明：以上内容基于公开信息的分析推演，仅供参考，不构成投资建议。市场有风险，投资需谨慎。

## 快速开始

```bash
cd scripts

# 一键：采集 → 打分 → 输出报告 + 生成信号卡
python3 score_and_report.py --pretty

# 渲染 HTML 信号卡（读 output 报告 + templates/card.html）
python3 render_card.py

# 推送飞书群（本机，走 notify-hub）
python3 push_feishu.py --send

# 推送飞书群（云端，走 webhook，需 FEISHU_WEBHOOK / FEISHU_SECRET）
python3 push_webhook.py
```

纯 Python 标准库（urllib / xml.etree / email.utils），**零第三方依赖、无 key 开箱即用**。

## 六大数据源

| 模块 | 脚本 | 内容 | key |
|---|---|---|---|
| A 外围行情 | `fetch_market.py` | A50 期货、纳指期货、标普期货、离岸/在岸人民币、美元指数、VIX、美债 10Y、黄金、原油、恒指（腾讯/新浪/东财，三级降级） | 否 |
| B 地缘事件 | `fetch_geopolitics.py` | GDELT DOC 2.0（conflict/trade/mideast 三主题，http 协议 + 重试） | 否 |
| C 财经日历 | `fetch_calendar.py` | 华尔街见闻日历（当日事件 + 重磅事件，Unix 时间戳参数） | 否 |
| C+ 国内新闻 | `fetch_news_cn.py` | 中新网 RSS（5 频道）+ 东财 7x24 快讯 + 新浪滚动 | 否 |
| D 宏观数据 | `fetch_macro.py` | 中国 PMI/CPI/PPI（东财）+ 美国/中国/全球 GDP·CPI·失业率（World Bank）+ FRED 高频（可选） | 否 |
| E 中国资金面 | `fetch_funds.py` | 两融余额、龙虎榜（去重）、沪深港通净流入、在岸人民币 | 否 |

## 打分与风险分级

- **多空方向**：七大外围指标（A50/纳指期货/离岸人民币/美元指数/VIX/美债10Y 等）逐项判利多/利空，加权得方向分与概率。
- **风险分级 1-5**：综合方向分歧度、VIX 位置、地缘异动、重磅事件密度得出，1=低风险 / 5=高风险。
- **宏观底色**：只作情景背景（如"中美 10Y 利差 +304bp 深度倒挂，人民币承压"），不进方向打分。

## 输出产物

- `output/report_YYYYMMDD.json` — 结构化报告（verdict / risk_level / 方向概率 / 各维度明细）
- `output/card_YYYYMMDD.html` — 可分享信号卡（品牌 footer + 风险条 + 结论区变色）
- `output/push_card_YYYYMMDD.json` — 飞书卡片 DSL

## 订阅推送（可选）

- **本机**：`push_feishu.py --send`，走 notify-hub 已配置通道。
- **云端**：`.github/workflows/daily-push.yml` 每天 UTC 0:30（北京 8:30，周一~五）自动跑 `push_webhook.py`，电脑关机也照常推。需在仓库 Secrets 配 `FEISHU_WEBHOOK`、`FEISHU_SECRET`。

## 目录结构

```
hectorlee-global-risk-signal/
├── SKILL.md
├── README.md
├── LICENSE
├── scripts/
│   ├── score_and_report.py      # 编排 + 打分 + 报告
│   ├── fetch_market.py          # 外围行情
│   ├── fetch_geopolitics.py     # 地缘事件
│   ├── fetch_calendar.py        # 财经日历
│   ├── fetch_news_cn.py         # 国内新闻
│   ├── fetch_macro.py           # 宏观数据
│   ├── fetch_funds.py           # 中国资金面
│   ├── render_card.py           # 信号卡渲染
│   ├── push_feishu.py           # 本机推送（notify-hub）
│   ├── push_webhook.py          # 云端推送（webhook 加签）
│   └── templates/card.html      # 信号卡模板
└── .github/workflows/daily-push.yml
```
