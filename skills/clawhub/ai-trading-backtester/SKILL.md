---
name: "AI Trading Strategy Backtester"
description: "AI-powered quantitative trading strategy backtesting assistant. Designs, codes, and evaluates trading strategies across historical market data. Supports A-share (China), Hong Kong, US equity markets. Covers mean reversion, momentum, breakout, pairs trading, and machine learning-based strategies. Built for quantitative analysts and retail traders. Keywords: trading backtest, quantitative strategy, algorithmic trading, Python backtesting, backtrader, vectorbt, trading strategy, momentum, mean reversion, pairs trading, A-share strategy, financial data, technical indicators."
version: "5.0.1"
---

# AI Trading Strategy Backtester

## Overview

An AI-powered quantitative trading strategy design and backtesting assistant that helps you transform trading ideas into fully-coded, backtested strategies. It guides you through strategy design (mean reversion, momentum, breakout, pairs trading, ML-based), implements them in Python (backtrader, vectorbt, pandas), evaluates performance across historical data for A-share, HK, and US markets, and produces risk-adjusted performance reports.

## Market & Regulatory Context (as of 2026-09-14)

| 事项 | 对回测的直接影响 |
|------|----------------|
| **程序化交易管理要求** | 高频类策略需自行计入报备、流速与异常交易约束，回测中不能假设"无限报单" |
| **A股 T+1 与涨跌幅限制** | 当日买入不可卖出、涨跌停无法成交，回测必须对不可成交信号做剔除或顺延处理 |
| **停牌与流动性** | 停牌期间的"信号"不可成交；小市值标的需按实际成交量限制下单规模 |
| **交易成本口径** | 佣金、印花税、滑点合计常被低估，年换手率高时成本可吞掉全部超额收益 |
| **数据复权与幸存者偏差** | 使用不复权价格或仅含现存标的历史，会系统性高估策略表现 |

**新动态（截至 2026-09-14）：**
- **程序化交易监管常态化**：境内市场对程序化交易的报备、交易行为监测与异常交易认定持续细化，高频与日内回转类策略的合规成本上升。回测时应把"报单频率上限""撤单率约束"纳入假设，而非只追求收益最大化。
- **AI 选股与因子挖掘的合规关注上升**：以大模型或机器学习生成交易信号时，监管与机构风控普遍要求可解释、可复现、留痕，纯黑箱信号在实盘落地时面临额外审核成本。
- **数据要素与另类数据应用扩展**：产业、舆情、供应链等另类数据被更广泛用于因子构建，但数据可得性的时点（point-in-time）问题更突出，回测中须严格避免引入未来信息。
- 以上为公开信息综述，**具体规则、费率与执行口径以交易所、中国证监会及券商官方最新发布为准**。

---

## Triggers

- "backtest my trading strategy"
- "design a momentum strategy for [stock/market]"
- "test mean reversion on [symbol]"
- "pairs trading strategy example"
- "Python backtrader setup guide"
- "vectorbt tutorial"
- "trading strategy optimization"
- "量化回测策略"
- "技术指标择时策略"
- "A股量化策略设计"

## Workflow

### Step 1: Define the Strategy Brief

Collect the trading idea:
- **Strategy type**: Momentum, mean reversion, breakout, pairs trading, ML-based, event-driven
- **Market**: A-share (sh/sz), HK stock (hk), US equity (us)
- **Timeframe**: Intraday (1m/5m/15m), daily, weekly, monthly
- **Assets**: Single stock, ETF, index, portfolio
- **Entry/Exit signals**: Technical indicators, price patterns, fundamental signals, ML predictions
- **Position sizing**: Fixed, Kelly criterion, risk-parity, dynamic
- **Constraints**: Max position size, long-only/short, turnover limit, slippage model

**简报示例（合格）：**
> 策略类型：动量；市场：A股（沪深300成分股）；频率：日线；标的：成分股等权；信号：20日动量排名前20%；仓位：等权，最多10只；约束：仅做多、单边成本0.15%、单票上限10%、剔除ST与上市不足60日个股；回测区间：2019-01-01 至 2026-08-31。

**简报示例（不合格及原因）：**
> "帮我做个能稳定赚钱的量化策略。"
>
> 缺少市场、频率、成本、仓位与约束，任何回测结果都无法验证。更关键的缺失是**没有失败条件**——合格简报应写明"什么情况下判定策略不可用"（如样本外夏普<0.5 或最大回撤>25% 即放弃）。

### Step 2: Strategy Design & Code Generation

Based on the brief, generate production-quality Python code:

#### A. Momentum Strategy Template
```python
import pandas as pd
import numpy as np
import backtrader as bt

class MomentumStrategy(bt.Strategy):
    params = (
        ('lookback', 20),       # 回望期
        ('hold_period', 5),    # 持有期
        ('rank_percentile', 0.2),  # 选股分位数
    )

    def __init__(self):
        self.inds = {}
        for d in self.datas:
            self.inds[d] = {}
            self.inds[d]['momentum'] = bt.indicators.RateOfChange(
                d.close, period=self.params.lookback
            )

    def next(self):
        # 按动量排序，取前20%
        rankings = sorted(
            self.datas,
            key=lambda d: self.inds[d]['momentum'][0],
            reverse=True
        )[:int(len(self.datas) * self.params.rank_percentile)]

        # 平仓不在榜单的持仓
        for d in self.datas:
            if d not in rankings and self.getposition(d).size > 0:
                self.close(d)

        # 买入榜单中的标的
        for d in rankings:
            if self.getposition(d).size == 0:
                self.order_target_percent(d, 1.0 / len(rankings))
```

**调用示例与常见坑：**

```python
cerebro = bt.Cerebro()
cerebro.addstrategy(MomentumStrategy, lookback=20, hold_period=5, rank_percentile=0.2)
# 关键：传入的是"回望期内的动量"，必须剔除上市不足 lookback 天的新股，
# 否则新股会因为没有足够历史而产生极端 ROC 值，长期占据榜单前排。
```

- **坑一（未来函数）**：若在 `next()` 里用当收盘价排序并在同一根 K 线以收盘价成交，等于用到了收盘才可知的信息。A 股应改为**次日开盘或次日均价成交**。
- **坑二（涨跌停不可成交）**：榜单里的股票当日一字涨停时无法买入，回测若照单全收会高估收益。应对方式：当日涨停则跳过，顺延至下一交易日。
- **坑三（集中度过低）**：`1.0 / len(rankings)` 在 rankings 为空时会除零，需先判断 `if rankings:`。

#### B. Mean Reversion Strategy Template
```python
class MeanReversionStrategy(bt.Strategy):
    params = (
        ('bb_period', 20),
        ('bb_dev', 2.0),
        ('rsi_period', 14),
        ('rsi_oversold', 30),
        ('rsi_overbought', 70),
    )

    def __init__(self):
        self.bb = bt.indicators.BollingerBands(
            self.data.close, period=self.params.bb_period,
            devfactor=self.params.bb_dev
        )
        self.rsi = bt.indicators.RSI(
            self.data.close, period=self.params.rsi_period
        )

    def next(self):
        if self.position.size == 0:
            # 价格触及下轨且RSI超卖 → 买入
            if self.data.close < self.bb.lines.bot and \
               self.rsi < self.params.rsi_oversold:
                self.order_target_percent(self.data, 1.0)
        else:
            # 价格触及上轨或RSI超买 → 卖出
            if self.data.close > self.bb.lines.top or \
               self.rsi > self.params.rsi_overbought:
                self.close()
```

**调用示例与参数敏感度说明：**

```python
# rsi_oversold 从 30 调到 25，交易次数可能从 127 次降到 70 次以下，
# 而样本外夏普从 1.12 掉到 0.6 —— 这种"微调剧变"就是过拟合信号。
cerebro.addstrategy(MeanReversionStrategy, bb_period=20, bb_dev=2.0,
                    rsi_period=14, rsi_oversold=30, rsi_overbought=70)
```

- **适用场景**：震荡市中表现较好；单边下跌行情里"越跌越买"会连续触发买入信号，形成典型的**均值回归陷阱**——建议叠加趋势过滤（如仅在收盘价高于 MA60 时允许开仓）。
- **A 股注意**：T+1 制度下当日买入不能当日卖出，若策略在盘中触发卖出信号，回测中必须顺延到下一交易日，否则会虚增收益。

#### C. Pairs Trading Strategy
```python
import statsmodels.api as sm

def find_cointegrated_pairs(data_dict):
    """寻找协整配对"""
    n = len(data_dict)
    pairs = []
    symbols = list(data_dict.keys())

    for i in range(n):
        for j in range(i + 1, n):
            try:
                x = data_dict[symbols[i]]
                y = data_dict[symbols[j]]
                # OLS回归
                X = sm.add_constant(x)
                model = sm.OLS(y, X).fit()
                residuals = model.resid
                # ADF检验
                adf_result = sm.tsa.stattools.adfuller(residuals)
                if adf_result[0] < adf_result[4]['1%']:
                    pairs.append((symbols[i], symbols[j], adf_result[0]))
            except:
                continue
    return sorted(pairs, key=lambda x: x[2])

def pairs_trading_signals(spread, z_entry=2.0, z_exit=0.5):
    """配对交易信号"""
    signals = pd.Series(0, index=spread.index)
    z_score = (spread - spread.mean()) / spread.std()

    signals[z_score < -z_entry] = 1    # 做多价差
    signals[z_score > z_entry] = -1     # 做空价差
    signals[abs(z_score) < z_exit] = 0  # 平仓
    return signals
```

**调用示例：**

```python
pairs = find_cointegrated_pairs({"600036": s_a, "601318": s_b})
# => [("600036", "601318", -3.87)]   ADF 统计量 -3.87 < 1% 临界值，判定协整

spread = s_a - 1.24 * s_b           # 1.24 来自 OLS 回归系数
signals = pairs_trading_signals(spread, z_entry=2.0, z_exit=0.5)
```

- **关键提醒一**：`z_score` 用全样本 `mean()`/`std()` 计算会引入未来函数。实务中应使用**滚动窗口**（如过去 60 日）的均值与标准差。
- **关键提醒二**：协整关系会衰减。建议在回测中每 N 个月重新检验一次协整，关系破裂即停止交易该配对，而不是一路持有到止损。
- **关键提醒三**：A 股缺乏便捷的做空渠道，配对交易的"做空腿"往往无法实现，因此在 A 股使用时应明确标注为"仅做多腿的变体"，收益预期需相应下调。

### Step 3: Backtest Execution

Guide the user through running the backtest:

```python
import backtrader as bt
import pandas as pd

# 加载数据
data = bt.feeds.GenericCSVData(
    dataname='historical_data.csv',
    dtformat='%Y-%m-%d',
    datetime=0,
    open=1, high=2, low=3, close=4, volume=5,
    openinterest=-1
)

# 运行回测
cerebro = bt.Cerebro()
cerebro.addstrategy(MomentumStrategy)
cerebro.adddata(data)
cerebro.broker.setcash(1000000.0)  # 100万初始资金
cerebro.broker.setcommission(commission=0.001)  # 千一手续费
cerebro.addsizer(bt.sizers.PercentSizer, percents=95)

print(f'初始资金: {cerebro.broker.getvalue():,.2f}')
cerebro.run()
print(f'最终资金: {cerebro.broker.getvalue():,.2f}')
```

**A股成本设置的正确示范：**

```python
# 佣金双边 + 印花税（卖出单边）+ 滑点，缺一项都会高估收益
cerebro.broker.setcash(1_000_000.0)
cerebro.broker.setcommission(commission=0.0003, stocklike=True)   # 佣金万三
cerebro.broker.set_slippage_perc(perc=0.0005)                     # 滑点万五
# 印花税需在卖出侧单独计入（历史口径曾为卖出单边 0.1%，以最新官方口径为准）
```

**一次性跑完的最小检查清单：**
1. 初始资金与期末资金是否如预期变化（没变说明根本没有成交）
2. 成交笔数是否合理（为 0 说明信号从未触发；过多说明成本被低估）
3. 是否有信号落在停牌日或涨跌停日（有则说明缺少可交易性过滤）

### Step 4: Performance Analysis

Generate comprehensive performance metrics:

| Metric | Description | Target | Formula / 计算口径 | 常见误读 |
|--------|-------------|--------|-------------------|---------|
| Total Return | Cumulative return | > Benchmark | 期末权益/期初权益 - 1 | 忽略分红再投与复权方式差异 |
| Annualized Return | CAGR | > 10% (A-share), > 8% (HK/US) | (终值/初值)^(252/交易日数) - 1 | 回测期不足一年时年化会严重放大 |
| Sharpe Ratio | Risk-adjusted return | > 1.5 | (年化收益 - 无风险利率)/年化波动 | 用日收益简单乘√252 前需确认收益无自相关 |
| Max Drawdown | Peak-to-trough loss | < 20% | max((峰值 - 当前值)/峰值) | 只看数值不看持续天数，低估心理压力 |
| Win Rate | Percentage of profitable trades | > 50% | 盈利次数/总平仓次数 | 高胜率配低盈亏比仍可能整体亏损 |
| Profit Factor | Gross profit / Gross loss | > 1.5 | 总盈利/总亏损 | 不含成本时会被系统性高估 |
| Calmar Ratio | Annual return / Max DD | > 1.0 | 年化收益/最大回撤 | 回测期短时最大回撤尚未充分暴露 |
| Sortino Ratio | Return / Downside deviation | > 1.0 | (年化收益 - 无风险利率)/下行波动 | 与夏普混用会导致横向比较失真 |
| Turnover / 换手率 | 年化双边成交额/平均权益 | 视策略而定 | 年双边成交额/平均权益 | 常被忽略，却是成本吞噬的主因 |
| Exposure / 持仓暴露 | 有仓位时间占比 | 视策略而定 | 持仓交易日/总交易日 | 低暴露策略的年化收益不可直接对比满仓策略 |

### Step 5: Optimization & Stress Testing

```
A. 参数优化
   - Grid search over key parameters
   - Walk-forward analysis (in-sample / out-of-sample)
   - Avoid overfitting: use Information Coefficient (IC) analysis

B. 压力测试
   - Historical crises: 2008, 2015 A-share crash, COVID-19 (2020)
   - Monte Carlo simulation of equity curves
   - Sensitivity analysis: commission, slippage, spread assumptions

C. 风险分析
   - Position-level VaR (Value at Risk)
   - Factor exposure (momentum, size, volatility)
   - Tail risk: maximum loss scenarios
```

**压力测试示例（A股场景）：**

| 情景 | 假设 | 观察指标 |
|------|------|---------|
| 2015 年异常波动 | 指数快速回撤、流动性骤降、大面积停牌 | 策略最大回撤、停牌期间无法减仓的比例 |
| 2018 年单边下跌 | 全年趋势向下 | 均值回归类策略是否连续触发买入、资金是否耗尽 |
| 2020 年疫情冲击 | 短期急跌后快速反弹 | 止损是否被触发在最低点、反弹是否踏空 |
| 流动性收缩 | 成交额下降 50% | 冲击成本上升后的净收益变化 |
| 成本翻倍 | 佣金与印花税假设提高 100% | 净收益是否仍为正——若为负说明策略靠低成本存活 |

**参数优化示例（Walk-forward）：**
```
样本划分：2019-2023 为优化期，2024-2026 为样本外
滚动方式：每 12 个月重新优化一次参数，用下一年数据检验
判定规则：样本外夏普 / 样本内夏普 > 0.6 视为可接受；< 0.4 判定过拟合
```
若样本内夏普 1.8、样本外 0.5（比值 0.28），即使样本内指标漂亮，也应判定该策略不可用。

## Input/Output Examples

### Example 1: Strategy Design Request

**Input:**
```
Design a momentum strategy for A-share market.
Criteria:
- Daily timeframe
- Lookback: 20 days
- Hold for 5 days
- Long only
- Top 20% by momentum score
- Max 10 positions
- Trade AAPL, TSLA, NVDA, MSFT
```

**Output:**
```
Strategy Design Summary:

┌─────────────────────────────────────────┐
│ Strategy: Top-Momentum Long-Only        │
│ Market: US Equity (4 stocks)            │
│ Timeframe: Daily                        │
│ Backtest Period: 2020-01-01 to 2025-12-31 │
└─────────────────────────────────────────┘

Key Components:
1. Momentum ranking: ROC(close, period=20)
2. Selection: Top 20% by momentum score (max 10 stocks)
3. Position sizing: Equal weight (10% per position)
4. Hold period: 5 trading days
5. Rebalance: Daily at market open

Expected Performance (illustrative):
- Annualized Return: 18-25% (historical backtest)
- Sharpe Ratio: 0.8-1.2
- Max Drawdown: 30-40%
- Win Rate: 52-56%

Code generated at: strategy_momentum_us.py
```

### Example 2: Performance Report

**Input:**
```
Compare these two strategies: RSI mean reversion vs momentum breakout on CSI 300 (000300)
Period: 2020-2024
Initial capital: 1,000,000 CNY
```

**Output:**
```
Backtest Results: CSI 300 Strategies (2020-2024)

┌──────────────────────┬─────────────────────┬────────────────────┐
│ Metric               │ RSI Mean Reversion  │ Momentum Breakout  │
├──────────────────────┼─────────────────────┼────────────────────┤
│ Total Return         │ +68.3%              │ +124.7%            │
│ Annualized Return    │ +13.2%              │ +17.8%             │
│ Sharpe Ratio         │ 1.12               │ 1.45               │
│ Max Drawdown         │ -22.1%             │ -31.4%             │
│ Win Rate             │ 58.3%              │ 49.2%              │
│ Profit Factor        │ 1.82               │ 1.67               │
│ Calmar Ratio         │ 0.60               │ 0.57               │
│ Avg Holding Days     │ 8.2                │ 4.6                │
│ Total Trades         │ 127                │ 284                │
└──────────────────────┴─────────────────────┴────────────────────┘
Benchmark: CSI 300 Index (+42.1% over same period)

Recommendation:
- Risk-averse investors: RSI Mean Reversion (lower drawdown, higher win rate)
- Return-seeking investors: Momentum Breakout (higher return, more trades)

⚠️ Note: Past performance does not guarantee future results.
A-share markets are subject to significant regulatory and liquidity risks.
```

## Strategy Templates Library

| Strategy Type | Best For | Timeframe | Markets | 典型失效场景 | A股落地难点 |
|--------------|----------|-----------|---------|------------|------------|
| Momentum | Trending markets | Daily/Weekly | All | 急转弯行情（风格切换） | T+1 导致信号次日才可执行 |
| Mean Reversion | Range-bound markets | Intraday/Daily | All | 单边下跌（越跌越买） | 涨跌停无法成交、T+1 |
| Breakout | Volatile markets | Intraday/Daily | All | 假突破密集期 | 涨停排队难以建仓 |
| Pairs Trading | Market-neutral | Daily | US/HK | 协整关系破裂 | 做空腿难以实现 |
| Machine Learning | Alpha discovery | Daily | All |  regime 变化、特征漂移 | 可解释性与留痕要求高 |
| Event-Driven | Corporate actions | Daily | A-share/US | 事件被提前price-in | 事件数据 point-in-time 难保证 |

## Best Practices

1. **Always use out-of-sample testing** — split data 70/30 or use walk-forward
2. **Account for transaction costs** — A-share commission + stamp tax ≈ 0.15% per trade
3. **Include slippage** — assume 0.05-0.1% for liquid stocks, higher for illiquid
4. **Diversify across uncorrelated strategies** — don't rely on one strategy
5. **Stress test for A-share specifics** — T+1 trading, limit-up/limit-down, suspension risks
6. **Validate with paper trading** — run live for 1-3 months before real capital
7. **Beware of overfitting** — fewer parameters = more robust strategy

**举例说明第 2 条（交易成本）为何致命：** 某日频策略年换手 20 倍，单边成本按 0.15% 计，年化成本约 6%。若策略毛年化超额为 8%，扣费后仅剩 2%，再计入滑点后大概率归零。因此**高换手策略必须先算成本再算收益**。

**举例说明第 5 条（A股特性）：** 某策略在 2015 年 6-8 月期间发出减仓信号，但持仓标的中 40% 处于停牌状态，实际无法卖出。回测若假设全部成交，会把最大回撤从真实的 -45% 写成 -28%，严重低估风险。

**举例说明第 6 条（模拟盘）：** 正式投入资金前，建议先做 1-3 个月模拟或小额实盘，重点验证的不是收益，而是"信号能否按回测假设成交"——实盘中的成交价、可成交量、停牌与临停，往往与回测假设差距最大。

## Risk Disclaimer

This skill provides backtesting tools and historical analysis for educational and research purposes only. Backtested results are not indicative of future performance. Real trading involves significant risks including market volatility, liquidity constraints, regulatory changes, and model risk. Always consult with qualified financial advisors before making investment decisions.
## Appendix G. Alibaba Dianjin Fusion — ai-trading-backtester v5.0.1

> **Source**: Alibaba Dianjin Digital Employee — `investment-advisor` (AI投资顾问) & `quant-researcher` (AI量化研究员)  
> **Essence**: 策略回测、参数优化、风险控制、绩效评估  
> **Integrated**: 2026-05-31
> **Last reviewed**: 2026-09-14

---

### G.1 Core Workflow (Dianjin essence)

```
策略回测流程：
1. 策略定义：买入条件+卖出条件+止损条件
2. 数据准备：历史K线+成交量+因子数据
3. 回测执行：按时间顺序模拟交易
4. 绩效计算：收益率+夏普比率+最大回撤
5. 参数优化：网格搜索/贝叶斯优化
6. 风险分析：回撤期+胜率+盈亏比
```

---

### G.2 Backtest Metrics (Dianjin method)

**核心指标体系**：

| 指标 | 计算公式 | 优秀标准 | 及格标准 | 易被操纵的方式 | 交叉验证指标 |
|------|---------|---------|---------|--------------|------------|
| 年化收益率 | (终值/初值)^(252/交易日)-1 | >20% | >8% | 缩短回测期至强年份 | 分年度收益是否稳定 |
| 夏普比率 | (年化收益-无风险利率)/年化波动 | >1.5 | >0.5 | 剔除极端亏损交易日 | 与索提诺、Calmar 同时看 |
| 最大回撤 | max((历史最高-当前)/历史最高) | <15% | <30% | 只报告收盘价回撤 | 回撤持续天数与恢复天数 |
| 胜率 | 盈利次数/总次数 | >60% | >45% | 用极短止盈拉高胜率 | 盈亏比是否同步下降 |
| 盈亏比 | 平均盈利/平均亏损 | >2.0 | >1.5 | 放宽止损拉高盈亏比 | 最大回撤是否同步恶化 |
| 索提诺比率 | (年化收益-无风险利率)/下行波动 | >2.0 | >1.0 | 下行波动口径自行定义 | 与最大回撤交叉核对 |
| 换手率 | 年双边成交额/平均权益 | 视策略 | 视策略 | 常常干脆不报告 | 与净收益同时报告 |

**回测报告模板（Dianjin风格）**：

```
【策略回测报告】均线突破策略（5日+20日）

一、回测参数
- 标的：沪深300指数 (000300.SH)
- 周期：2019-01-01 至 2026-05-31
- 频率：日线
- 初始资金：100万
- 交易成本：单边0.1%（佣金0.03%+印花税0.07%）

二、绩效指标
✅ 年化收益率：18.5%（优秀）
✅ 夏普比率：1.62（优秀）
❌ 最大回撤：-28.3%（不及格，应<15%）
⚠️ 胜率：52.3%（及格）
⚠️ 盈亏比：1.85（及格）

三、分年度表现
| 年份 | 收益率 | 最大回撤 | 夏普比率 |
|------|--------|----------|----------|
| 2019 | +32.5% | -12.3% | 2.1 |
| 2020 | +28.7% | -15.8% | 1.8 |
| 2021 | -8.2% | -22.5% | -0.3 |
| 2022 | -15.3% | -28.3% | -0.8 |
| 2023 | +22.1% | -10.5% | 1.5 |
| 2024 | +12.8% | -8.7% | 1.2 |
| 2025 | +25.6% | -9.2% | 1.9 |

四、问题诊断
❌ 2022年回撤-28.3%（策略在熊市表现差）
❌ 胜率仅52.3%（信号质量不高）
⚠️ 交易成本年化-3.2%（高频交易成本高）

五、改进建议
1. 增加趋势过滤（仅在MA60向上时开仓）
2. 优化止损（当前-8%止损太宽，改为-5%）
3. 降低交易频率（当前年均交易45次，降至20次以下）
```

---

### G.3 Parameter Optimization (Dianjin essence)

**参数优化方法**：

```
方法1：网格搜索（Grid Search）
  - 优点：简单，保证找到全局最优
  - 缺点：计算量大（参数多时指数爆炸）
  - 适用：参数少（<5个），范围小

方法2：贝叶斯优化（Bayesian Optimization）
  - 优点：高效，用高斯过程建模目标函数
  - 缺点：实现复杂，可能陷入局部最优
  - 适用：参数多（>5个），计算资源有限

方法3：遗传算法（Genetic Algorithm）
  - 优点：全局搜索能力强，适合复杂目标
  - 缺点：收敛慢，参数调优难
  - 适用：非线性、多峰目标函数
```

**过拟合风险警示（Dianjin重点）**：

```
⚠️ 过拟合信号：
1. 样本内绩效远优于样本外（差距>50%）
2. 参数极度敏感（微调参数导致绩效剧变）
3. 交易次数过少（<20次，统计不显著）
4. 最大回撤发生在样本末端（未来函数嫌疑）

✅ 防过拟合措施：
1. 样本外测试（保留最近1-2年数据不参训）
2. 滚动窗口验证（Walk-forward，每N个月重新优化）
3. 参数稳定性检验（参数在合理范围内波动，绩效不剧变）
4. 经济逻辑检验（策略要有合理解释，不能纯数据挖掘）
```

---

### G.4 Risk Control & Position Management (Dianjin method)

**仓位管理模型**：

```
固定比例法（最简单）：
  - 单一策略：股票仓位≤30%
  - 组合策略：总仓位≤80%

凯利公式（Kelly Criterion）：
  仓位 = (胜率 × 盈亏比 - 败率) / 盈亏比
  例：胜率55%，盈亏比2.0 → 仓位 = (0.55×2-0.45)/2 = 32.5%

ATR仓位法（波动率调整）：
  仓位 = 账户资金 × 风险系数 / (ATR × 合约乘数)
  例：账户100万，风险系数0.02，ATR=2元，合约乘数100
  → 仓位 = 100万 × 0.02 / (2×100) = 100股（约占总资金2%）
```

**凯利公式的实操提醒：** 上例算出 32.5% 仓位，但凯利公式对胜率与盈亏比的估计误差极为敏感——若实际胜率是 50% 而非 55%，最优仓位会大幅下降。实务中普遍采用**半凯利或四分之一凯利**（上例取 16% 或 8%），以避免在参数高估时过度下注。

**ATR 仓位法举例（跨标的比较）：**

| 标的 | ATR | 单笔风险预算 2% 时的股数 | 占总资金 |
|------|-----|----------------------|---------|
| 高波动个股（ATR=2元，价格20元） | 2.0 | 100股 | 约2%名义，实际暴露高 |
| 低波动蓝筹（ATR=0.3元，价格20元） | 0.3 | 667股 | 约13%名义 |

同一风险预算下，低波动标的自然获得更高名义仓位，这正是波动率调整的目的：**让每笔交易的风险贡献相当，而不是让每笔交易的金额相当**。

---

### G.5 Test Case (Dianjin quality)

**Test Case: 策略回测+优化**

```
Input: "回测均线突破策略（5日+20日）在沪深300的表现，2019-2026"

Expected Output:
1. 回测参数（标的/周期/成本）
2. 绩效指标表（年化收益/夏普/最大回撤/胜率/盈亏比）
3. 分年度表现
4. 问题诊断（回撤过大/胜率过低）
5. 改进建议（增加过滤/优化止损）

Quality Check:
- ✅ 指标计算准确（公式正确）
- ✅ 问题诊断客观（不回避缺陷）
- ✅ 改进建议可行（有实操价值）
- ✅ 风险提示（过拟合风险）

Additional Cases:
- TC002: "策略回测夏普 1.9，但交易次数只有 18 次" → 判定统计不显著，要求延长样本或降低参数自由度
- TC003: "回测中未设置涨跌停过滤" → 判定存在可交易性缺陷，要求补过滤后重跑并对比差异
- TC004: "样本外夏普 0.5，样本内 1.8" → 判定过拟合，给出缩减参数与简化规则的改法
```

---

**End of Dianjin Fusion Content — ai-trading-backtester v5.0.1**
