---
name: "a-share-trading"
description: "A股交易层：自选股管理/实时监控/大盘情绪/热点板块/买卖策略/止盈止损/仓位管理/价格预警"
user-invocable: true
metadata:
  openclaw:
    emoji: "🎯"
    tags: ["a-share", "trading", "monitoring", "portfolio"]
---

# A-Share Trading v2.0

## 定位

A 股**唯一交易执行层**。数据→`a-share-data`，分析→`a-share-analysis`。

---

## 1. 自选股管理

纯文本存储，无数据库依赖：

### 文件
- 自选股：`~/.openclaw/a_share/watchlist.txt`（`代码|名称`）
- 交易记录：`~/.openclaw/a_share/transactions.txt`（`日期|代码|买卖|价格|数量|备注`）
- 预警：`~/.openclaw/a_share/alerts.txt`（`代码|类型|目标价|当前价|日期`）

### 操作
```bash
python3 scripts/add_stock.py <代码> [名称]
python3 scripts/remove_stock.py <代码>
python3 scripts/list_stocks.py
python3 scripts/summarize_performance.py
```

---

## 2. 行情监控

- 自选股汇总：每票价格/涨跌幅/来源
- 大盘指数：上证/深证/沪深300/创业板/科创50
- 大盘情绪：涨跌比+成交量+板块轮动 → 风险等级(低/中/高)

---

## 3. 热点板块

- 行业/概念板块涨幅排行
- 主线(连续强势) vs 情绪(单日爆发)
- 每个热点列龙头股

---

## 4. 交易策略

### 代码识别
60xxxx(沪) / 00xxxx(深) / 30xxxx(创业板) / 68xxxx(科创板)

### 操作模板
```
【操作建议】XX股(XXXXXX)
方向：做多/观望/回避
入场区间：XX-XX元 | 止损：XX元 | 止盈：XX元
仓位：XX% | 逻辑：[2-3条] | 风险：[1-2条]
```

### 时间维度
- 短线(1-5天)：催化剂+严格止损
- 中线(1-3月)：趋势+分批建仓

---

## 5. 仓位管理

- 单票 ≤20% | 单行业 ≤40%
- 总仓位随情绪调整：高风险≤30% 中风险≤60% 低风险≤90%
- 永留现金

---

## 6. 价格预警

预警类型：突破/跌破/放量/金叉死叉
记录到 alerts.txt，定时检查

---

## 7. 定时任务

```bash
25 9 * * 1-5  market_open.py       # 开盘准备
30 10,13,14 * * 1-5 intraday_check.py  # 盘中检查
30 15 * * 1-5  summarize_performance.py # 收盘汇总
```

---

## 安全

- 数据标注来源和时间
- 避免绝对化表述
- 不构成投资建议
