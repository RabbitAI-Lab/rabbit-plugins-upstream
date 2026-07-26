---
name: money-claw-us-stocks
description: Screen and rank U.S.-listed common stocks, ordinary shares, and ADR/ADS securities for extreme low-float squeeze moves, including potential +500% intraday events. Use for 美股暴涨策略、盘前涨幅榜筛选、低流通盘/低价股/妖股 squeeze、ELPW/TDIC/SKK/CPOP/RGNT/CPHI 类案例、盘前到开盘及停牌复牌执行清单、暴涨因子回测、候选股评分，以及判断盘前或盘中异动股是否符合暴涨因子。 Evaluate point-in-time price, baseline liquidity, float/share supply, premarket and official-open gaps, turnover, spread, VWAP, catalysts, splits, dilution, halts, and data quality. Do not use for long-term valuation or for ETFs, warrants, rights, units, preferred shares, or bonds.
---

# 美股极端暴涨候选筛选

## 决策原则

严格区分三个层级：

1. **结构候选**：低价、低基线流动性、低股本或低 float。
2. **事件确认**：盘前或正式开盘出现强 gap 与供给周转。
3. **可执行交易**：开盘后保持 VWAP、价差可控、结构确认且供应风险已排查。

不要把盘前涨幅、盘前最高价或上一常规时段的 `last price` 当作正式开盘 `Gap`。不要把 evidence score 当成上涨概率。

按需读取：

- 引用命中率、odds ratio、分位数或回撤统计前，读取 [references/factor-model.md](references/factor-model.md)。
- 解释模型来源、历史案例或样本外验证时，读取 [references/case-studies-2026.md](references/case-studies-2026.md)。

## 工作流

### 1. 固定时间和证券口径

- 写明日期、ET 时间、市场状态和数据时间戳。
- 用户提供截图时，逐项识别 `盘前价/盘前量/最新价/昨收/今开/停牌`，不凭颜色猜字段。
- 无法验证的字段标记 `UNKNOWN`，不得当成 0。
- 仅保留 Common Stock、Common Shares、Ordinary Shares、ADR/ADS。
- 排除 ETF、leveraged ETF、warrant、right、unit、preferred、bond 和 note。
- 当日生效 split 直接排除；近期 reverse split 只标记 `POST_SPLIT` 风险。

### 2. 收集最小数据集

至少收集：

```text
symbol, timestamp, market_status, security_type, listed_days
prev_close, pre_price, pre_high, pre_volume, bid, ask
market_cap, total_shares, float_shares
median_dollar_volume_20, avg_volume_20, pre_return_20d_pct
split_today, post_split, last_split_date, dilution_overhang, halted
open_price, last_price, regular_volume, vwap, first_5m_structure
prior_abnormal_volume_warmup, turnover_expanding
catalyst, catalyst_source
```

若缺少真实 float，计算：

```text
implied_total_shares = market_cap / current_price
```

只能称为“估算总股数”，不得称为 float。批量候选使用：

```powershell
python scripts/score_candidates.py candidates.csv --format markdown
python scripts/score_candidates.py candidates.json --format json
```

字段定义见 [references/factor-model.md](references/factor-model.md)。

### 3. 判断结构候选

使用以下事件前硬门槛：

```text
security_type in {Common, Ordinary, ADR, ADS}
AND listed_days >= 20
AND split_today == false
AND 0.30 <= prev_close <= 5.00
AND median_dollar_volume_20 <= 1,000,000
AND (verified_float <= 15,000,000 OR total_shares <= 10,000,000)
```

- 把 `prev_close <= 5` 视为模型范围，不解释为独立有效因子。
- 把 float、总股本和 market-cap proxy 的来源分开记录。
- 检查 registered resale、ATM、可转换证券、warrants 和新增发行。
- 不得用发行人国家或地区单独推导上涨概率。

### 4. 判断盘前强度

计算：

```text
pre_gap_pct       = (pre_price / prev_close - 1) * 100
pre_turnover      = pre_volume / supply_shares
spread_pct        = (ask - bid) / ((ask + bid) / 2) * 100
pre_high_fade_pct = (pre_price / pre_high - 1) * 100
pre_dollar_volume = pre_price * pre_volume
pre_rv20          = pre_volume / avg_volume_20
```

分层：

- `pre_gap >= 100%`：强候选，等待正式开盘。
- `50% <= pre_gap < 100%`：观察。
- `20% <= pre_gap < 50%`：只在供应极紧且成交继续扩张时观察。
- `pre_gap < 20%`：不进入常规 gap squeeze。

只有以下质量条件全部通过，才输出 `WAIT_OPEN`：

```text
pre_turnover >= 0.50
AND spread_pct <= 2.50
AND pre_high_fade_pct >= -20.00
AND dilution_overhang == false
```

### 5. 判断开盘路径

始终使用正式开盘价计算：

```text
official_gap_pct = (open_price / prev_close - 1) * 100
```

#### 常规 gap squeeze

仅在以下条件全部满足时输出 `EXECUTE`：

```text
official_gap_pct >= 100
AND last_price >= VWAP
AND regular_volume / supply_shares >= 1.00
AND spread_pct <= 2.50
AND first_5m_structure == confirmed
AND dilution_overhang == false
AND halted != true
```

等待第一根 5 分钟 K 线，突破 `max(premarket_high, opening_range_high)` 后回踩不破再执行。

#### CPHI subtype

只在 `official_gap < 20%` 且以下条件全部满足时输出 `EXECUTE`：

```text
regular_volume / supply_shares >= 1.00 very early after open
AND last_price >= VWAP
AND turnover_expanding == true
AND prior_abnormal_volume_warmup == true
AND spread_pct <= 2.50
AND first_5m_structure == confirmed
AND dilution_overhang == false
AND halted != true
```

不要把常规 `Gap >= 100%` 模型的命中率套用到 CPHI subtype。

### 6. 处理停牌和供应风险

- `halted=true` 时输出 `WATCH`，禁止新开仓；复牌后重新确认 VWAP、spread、周转和价格结构。
- 明确存在未解除的 ATM、registered resale、warrant 或可转换证券时，不得输出 `EXECUTE`。
- `dilution_overhang=UNKNOWN` 时输出 `WAIT_DATA`，不得假设供应风险为零。
- 无新增显性催化时写明“暂未发现新增显性驱动”，不得用题材猜测填空。

### 7. 输出决策

只使用以下机器状态：

| 状态 | 含义 |
|---|---|
| `EXECUTE` | 结构、路径、VWAP、周转、流动性和供应风险全部确认 |
| `WAIT_OPEN` | 强盘前候选，等待正式开盘确认 |
| `WAIT_DATA` | 关键字段缺失 |
| `WATCH` | 部分因子符合、执行门槛失败或正在停牌 |
| `EXCLUDE` | 证券类型、当日 split、结构或事件强度明确失败 |

同时输出：

- `path_type`：`CONVENTIONAL_GAP`、`CPHI_SUBTYPE` 或 `NONE`。
- `risk_flags`：`HALTED`、`DILUTION_OVERHANG`、`DILUTION_UNKNOWN`、`POST_SPLIT`、`SUPPLY_PROXY`、`MISSING_DATA`。

先给30秒结论，再给候选排名、有效因子、缺失字段、风险、升级条件、失效条件和排除名单。所有百分比和金额保留两位小数。

## 风控

默认单笔风险：

```text
risk_budget = account_equity * 0.25%
shares = floor(risk_budget / abs(entry - stop))
```

- 不用市价单追盘前或复牌瞬间。
- 不补仓摊低成本。
- 不同时持有超过两个同类低流通盘 squeeze。
- post-split 标的不做无保护裸空。
- 跌破 VWAP 且周转不再扩张时，优先视为供应释放。
- 不承诺止损在 halt gap 中按计划价格成交。

## 数据完整性

- 数据冲突时，采用时间戳更新且字段定义更明确的来源。
- API 涨跌幅异常时，用 point-in-time 价格自行重算。
- 不用复权历史价格替代事件当时价格。
- 不把条件命中率解释成单只股票的确定概率。
