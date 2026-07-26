---
name: "trading-journal"
description: "交易日志+决策清单+影子盘：每笔记录/买入前清单/业绩报告/模式识别/影子盘管理"
user-invocable: true
metadata:
  openclaw:
    emoji: "📓"
    tags: ["trading", "journal", "checklist", "performance"]
---

# Trading Journal v2.0

## 1. 交易记录
开仓: symbol/direction/entry/size/thesis/catalyst/stop_loss/take_profit
平仓: exit_price/date/pnl/pnl_pct/emotion/lesson

## 2. 决策清单
买入前: 商业模式/护城河/财务/估值/仓位 ≤20%
卖出前: 买入理由/是否恐惧/更好机会/重新买入条件

## 3. 业绩报告
周报(胜率/盈亏/最大单笔) | 月报(收益率/对比沪深300/情绪-结果关联)

## 4. 模式识别
自动分析: 最优时段/亏钱类型/最佳策略/持仓时长vs盈亏

## 5. 影子盘
虚拟跟踪未实盘标的，验证选股逻辑。

## 存储
`~/.openclaw/workspace/trading/journal.json` / `shadow.json` / `reports/`
