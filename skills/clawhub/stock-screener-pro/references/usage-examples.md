# 使用用例

以下示例均为研究、模拟或本地记录用途；不连接券商，也不会发送真实订单。飞书中可直接使用自然语言；若 Agent 需要工具参数，按每个示例的调用填写。

## 1. 每日盘前/盘后市场检查

飞书可直接说：

```text
查看今天 A 股大盘、成交额、涨跌家数和市场情绪。
```

对应工具：

```text
get_market_review()
```

适合用于快速了解市场环境。行情默认来自腾讯公开数据；配置同花顺凭据后，`STOCK_DATA_PROVIDER=auto` 会优先使用 iFinD。

## 2. 诊断一只股票的技术面

飞书可直接说：

```text
分析 600519 的最新行情、均线、RSI、支撑位和压力位，只做研究，不给买卖指令。
```

对应工具：

```text
ask_stock(stock_code_or_name="600519")
```

股票代码可使用 `600519`、`600519.SH`、`000001.SZ` 等形式。输出是指标快照，需要结合基本面、公告和个人风险承受能力判断。

## 3. 用策略筛选候选股

飞书可直接说：

```text
用放量突破策略，从 A 股中筛出 10 只候选股，市值不低于 100 亿；给出筛选条件和结果，不要声称收益保证。
```

对应工具：

```text
screen_stocks(
  strategy="volume_breakout",
  market_cap_min_yi=100,
  top_n=10
)
```

可用策略：`bull_momentum`、`low_valuation_value`、`volume_breakout`、`growth_tech`、`oversold_rebound`。筛选结果只是候选清单，不能直接等同于交易建议。

## 4. 对单只股票做轻量回测

飞书可直接说：

```text
对 600519 做 180 根日线的均线交叉策略回测，初始资金 10 万，解释收益、回撤和交易次数的局限。
```

对应工具：

```text
backtest_strategy(
  stock_code="600519",
  strategy="sma_cross",
  lookback_bars=180,
  initial_cash=100000
)
```

策略可选 `sma_cross`、`momentum_breakout`、`rsi_mean_reversion`。回测不包含滑点、全部税费和未来数据不可得等现实因素，历史结果不代表未来表现。

## 5. 建立本地自选与价格提醒

添加自选：

```text
manage_portfolio(
  action="add_watchlist",
  target_type="watchlist",
  stock_code="600519",
  group_name="消费观察"
)
```

创建价格上穿提醒：

```text
manage_alerts(
  action="create",
  stock_code="600519",
  rule_type="price_above",
  threshold=1600
)
```

查看和删除：

```text
manage_portfolio(action="list_all")
manage_alerts(action="list")
manage_alerts(action="delete", rule_id=1)
```

这些操作只写入本机 SQLite 记录和本地提醒规则，不会向券商发单。

## 6. 运行五日方向预测

飞书可直接说：

```text
对 600519 和 000001 做五日方向预测，说明这是 walk-forward 模型输出，并列出不确定性。
```

对应工具：

```text
predict_stock(codes=["600519", "000001"], force=false)
```

`force=true` 会忽略可用缓存重新计算。预测是模型信号，不是价格目标或收益承诺。

## 7. 检查同花顺、DSA 与 AI4Trade 状态

```text
get_skill_status(
  verify_tonghuashun=true,
  include_details=true
)
```

该调用会验证同花顺授权状态，并返回行情源、DSA、AI4Trade、OpenClaw 模型桥接和 TradingAgents 后端状态。不会返回任何 Token、密码或密钥。

## 8. 获取 AI4Trade 信息，或进行受确认操作

查看公开信号：

```text
get_ai4trade(resource="signals", symbol="BTC", limit=10)
```

查看账户和模拟持仓：

```text
get_ai4trade(resource="account")
get_ai4trade(resource="positions")
```

例如关注一位 AI4Trade 交易员时，必须先获得用户对该次操作的明确同意，再调用：

```text
manage_ai4trade(action="follow", leader_id=123, confirm=true)
```

`confirm=true` 仅确认 AI4Trade 平台内的对应状态变更；它不构成券商交易授权。

## 9. 用 OpenClaw 默认模型进行多角色投研

飞书可直接说：

```text
用多角色投研框架研究 600519，截至 2026-08-22，做一轮牛熊讨论和风险复核；我同意本次调用 OpenClaw 模型和行情服务。
```

对应工具：

```text
run_agent_research(
  engine="tradingagents",
  stock_code="600519",
  analysis_date="2026-08-22",
  max_debate_rounds=1,
  confirm_external_ai=true
)
```

默认 `llm_provider=openclaw`，使用 OpenClaw 当前默认模型，不需要单独填写 LLM API Key。该调用可能产生模型费用，也可能将股票代码、研究提示和行情请求发送到已配置服务；每次都要单独传 `confirm_external_ai=true`。

## 10. 使用 Vibe 的研究团队预设

```text
run_agent_research(
  engine="vibe_swarm",
  preset="investment_committee",
  prompt="研究贵州茅台的估值、核心风险与需要继续核验的事实；仅研究和模拟。",
  confirm_external_ai=true,
  timeout_seconds=900
)
```

Vibe 需要先完成自己的 `vibe-trading init` 提供商配置。含有实盘买卖、下单、委托等意图的 Vibe 提示会被拒绝。
