---
name: stock-screener
description: 股票量化与 AI 投研一体化全能 MCP 插件。全景覆盖：1) A股全市场秒级多策略选股；2) 实时问股与技术面诊断；3) 历史K线量化策略回测；4) 宏观大盘指数行情与复盘；5) 自选股/持仓盈亏管理；6) 价格突破/止损与异动预警；7) 深度 AI 投研报告；8) ML 未来5日方向预测（walk-forward RF+GB，免 Token）。
metadata:
  openclaw:
    primaryEnv: THS_REFRESH_TOKEN
---

# stock-screener (股票全能 Copilot)

基于高性能量化分析引擎与本地 DSA 深度投研系统的全功能股票 MCP 插件。当前本地加固版支持同花顺 iFinD 官方 HTTP QuantAPI，并在未配置授权时回退至公开行情源。

## 运行要求

- Python `>=3.11,<3.14`
- Python 包：`fastmcp`、`scikit-learn`、`pandas`、`numpy`
- MCP 启动命令：`python3 server.py`

## 数据源配置

- `STOCK_DATA_PROVIDER=auto`（默认）：配置同花顺凭据后优先使用 iFinD，否则回退公开行情源。
- `STOCK_DATA_PROVIDER=ths`：只允许同花顺数据；没有凭据或请求失败时直接报错，不回退。
- `STOCK_DATA_PROVIDER=tencent`：只使用原有公开行情源。
- `THS_REFRESH_TOKEN`：从同花顺超级命令客户端或网页版账号详情获取。服务只把它发送到固定官方地址 `https://quantapi.51ifind.com`。
- `THS_ACCESS_TOKEN`：可选，适合短期测试；长期运行优先使用 refresh token。

同花顺实时行情与历史 K 线走官方 QuantAPI。`auto` 模式下，实时接口不提供的 PE/PB/总市值字段会由原公开行情源补齐，便于保持多因子选股兼容性。

DSA 仅允许 `localhost`、`127.0.0.1` 或 `::1`。分发版不会向远程 DSA 发送会话或密码。

## 安全与数据边界

- 行情请求只会发往固定的同花顺 QuantAPI (`https://quantapi.51ifind.com`) 或腾讯公开行情 HTTPS 地址；同花顺凭据不会发送到其他主机。
- `DSA_ADMIN_PASSWORD` 只会用于回环地址的本地 DSA 登录，且不会被返回、记录或写入文件。
- `manage_portfolio` 和 `manage_alerts` 会修改本机 SQLite 中的自选、持仓或提醒规则。仅在用户明确要求新增、更新或删除相应记录时调用；不执行任何券商下单。
- `generate_ai_report` 会将股票代码和报告选项发送给本机 DSA 服务。远程报告服务不受此 Skill 支持。
- 未配置同花顺凭据时可使用腾讯公开行情回退；公开行情源不接收任何同花顺或 DSA 凭据。

## 适用场景与意图匹配

1. **宏观大盘与全市场复盘**：
   - 「今天大盘走势怎么样？」
   - 「查看上证指数、深成指、创业板指最新点位与两市成交额」
   👉 *自动调用 `get_market_review`*

2. **自选股与持仓盈亏管理**：
   - 「把贵州茅台加入自选股」
   - 「记录持仓：比亚迪 200股，成本价 85 元」
   - 「查看我的自选股和当前持仓总盈亏」
   👉 *自动调用 `manage_portfolio`*

3. **价格预警与异动监控**：
   - 「帮我设置茅台跌破 1300 元提醒」
   - 「设置比亚迪涨幅超过 5% 预警」
   - 「查看当前的所有监控预警状态」
   👉 *自动调用 `manage_alerts`*

4. **智能量化选股**：
   - 「帮我用多头突破策略选 5 只股票」
   - 「筛选市值>500亿、市盈率<30的白马股」
   👉 *自动调用 `screen_stocks`*

5. **实时问股与量化技术诊断**：
   - 「帮我看看贵州茅台 / 600519 行情」
   - 「宁德时代的趋势和支撑压力位是多少？」
   👉 *自动调用 `ask_stock`*

6. **历史数据策略回测**：
   - 「回测一下 600519 过去半年的均线金叉策略收益」
   👉 *自动调用 `backtest_strategy`*

7. **深度 AI 决策研报**：
   - 「生成 600519 的完整 AI 投研报告」
   👉 *自动调用 `generate_ai_report`*

8. **ML 短期方向预测**：
   - 「预测贵州茅台未来 5 天涨跌方向」
   - 「600519 和 300750 的机器学习方向信号」
   👉 *自动调用 `predict_stock`*

## 工具列表

### 1. `get_market_review`（宏观大盘复盘）
- 返回主要大盘指数点位、涨跌幅、两市成交额合计、全市场涨跌家数与多空情绪。

### 2. `manage_portfolio`（自选股与持仓管理）
- `action`：`list_all` (查看自选与持仓盈亏), `add_watchlist`, `remove_watchlist`, `add_position`, `remove_position`
- `stock_code`：股票代码
- `cost_price` / `shares`：成本价与股数（持仓时需要）
- `group_name`：自选/持仓分组名

### 3. `manage_alerts`（价格与异动预警监控）
- `action`：`list` (查看所有规则与触发状态), `create` (新增预警), `delete` (删除规则)
- `stock_code`：股票代码
- `rule_type`：`price_above` (突破目标价), `price_below` (跌破止损价), `pct_chg_above` (涨超百分比), `pct_chg_below` (跌超百分比)
- `threshold`：触发阈值数值

### 4. `screen_stocks`（全市场量化智能选股）
- `strategy`：选股策略（`bull_momentum`, `low_valuation_value`, `volume_breakout`, `growth_tech`, `oversold_rebound`）
- `market_cap_min_yi` / `pe_max` / `turnover_min` 等多因子过滤。

### 5. `ask_stock`（实时问股与技术面诊断）
- `stock_code_or_name`：股票代码或名称。返回均线多空组、RSI(14)、20日支撑阻力位。

### 6. `backtest_strategy`（策略历史回测）
- `stock_code`：股票代码。支持 `sma_cross`, `momentum_breakout`, `rsi_mean_reversion`，输出 Alpha、最大回撤与胜率。

### 7. `generate_ai_report`（深度 AI 决策研报）
- `stock_code`：股票代码。调用本地 DSA 生成深度投研报告。

### 8. `predict_stock`（ML 未来 5 日方向预测）
- `codes`：股票代码列表（支持 `600519`、`600519.SH` 等）
- `force`：是否强制重新训练（默认 false，命中内存缓存）
- 返回上涨概率、walk-forward 样本外准确率与偏多/偏空/方向不明判断。首次约 1-2 分钟/股，建议工具超时 ≥300s。

### 9. `predict_cache_status`（预测缓存查询）
- 列出当前已缓存的 ML 预测结果，无网络请求。

### 10. `get_strategies`（策略清单查询）

### 11. `get_data_provider_status`（数据源状态）
- 显示当前数据源、同花顺凭据是否配置以及 DSA 地址安全状态，不返回任何密钥。
- `verify_connection=true` 时只验证同花顺授权，不拉取行情数据。
