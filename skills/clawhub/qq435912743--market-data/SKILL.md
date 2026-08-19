---
name: market-data
description: |
  A股行情与财报数据获取技能。基于 westock-data（腾讯自选股）数据源，覆盖实时行情、K线、财报、板块、资金流、龙虎榜等维度；给出 FastAPI 后端 + React/AntD/ECharts 前端的接入范式。适用于量化交易、自选股看板、分时图、复盘分析。
version: 1.0.0
author: WorkBuddy
agent_created: true
visibility: "public"
tags:
  - 股票
  - A股
  - 行情
  - 财报
  - 量化
  - westock
---

# market-data — A股行情·财报数据台

_为量化交易系统提供稳定、实时的行情与基本面数据接入。_

## 数据源
- **westock-data**（腾讯自选股）：本机可直接调用的结构化行情接口，覆盖股票/ETF/指数/板块/期货/可转债。
- 维度：实时价、K线、分时、财报、新闻公告、资金流、龙虎榜、北向资金、新股日历。

## 接入范式（贴合用户技术栈）
**后端 FastAPI**：
```python
# 封装 westock-data 为 REST 接口，供前端轮询/推送
from fastapi import FastAPI
import westock_data as wd  # 伪名，按实际包名

app = FastAPI()

@app.get("/quote/{code}")
def quote(code: str):
    return wd.realtime(code)        # 实时价/涨跌/换手

@app.get("/kline/{code}")
def kline(code: str, period: str = "day"):
    return wd.kline(code, period)   # 历史K线
```
**前端 React + AntD + ECharts**：
- 自选股看板：表格轮询 `/quote`，红涨绿跌（A股惯例）。
- 分时/K线：ECharts `candlestick` + `line`，定时刷新。
- 实时推送：WebSocket 服务端订阅 → 前端订阅更新。

## 常用查询维度
- 实时行情：`realtime(code)` → 现价、涨跌幅、换手、量比、市盈率
- K线：`kline(code, period)` → OHLCV
- 财报：`f10(code)` / 业绩预告 / 分红
- 板块：行业/概念板块涨跌幅排行
- 资金流：主力净流入、北向资金
- 龙虎榜：上榜原因、买卖席位

## 实时性要点（用户已明确要求"实时行情"）
1. 后端定时任务拉取 → 写缓存（如 Redis/内存）；前端短轮询或 WS 推送。
2. K线/分时低频刷新（秒级~分钟级），盘口高频（亚秒级需 WS）。
3. 限流与重试：行情接口失败要退避重试，避免雪崩。

## 自我进化学习系统
```bash
python scripts/learner.py record <技能目录> --capability 实时行情 --note "WS推送比轮询更稳"
python scripts/learner.py record <技能目录> --capability 财报解析 --fail --error 字段缺失 --note "某些股票F10字段不全"
python scripts/learner.py insight <技能目录>
python scripts/learner.py reflect <技能目录>
```
记忆落盘 `learned_patterns.json`。

## 安全边界
- 仅用于本人模拟盘/量化研究；实盘交易需独立风控与合规性确认。
- 不越权访问账户、不代客理财。
- 行情数据注意版权与用量限制。
