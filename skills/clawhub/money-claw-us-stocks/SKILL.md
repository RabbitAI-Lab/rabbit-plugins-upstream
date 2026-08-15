---
name: money-claw-us-stocks
description: Screen and rank U.S.-listed common stocks, ordinary shares, and ADR/ADS securities for extreme low-float squeeze moves, including potential +500% intraday events. Use for 美股暴涨策略、盘前或盘后涨幅榜筛选、低流通盘/低价股/妖股 squeeze、ELPW/TDIC/SKK/CPOP/RGNT/CPHI/CYCU/FGI/GXAI 类案例、盘前到开盘及停牌复牌执行清单、5分钟量价阶段识别、抛物线加速与放量派发、暴涨因子回测、候选股评分，以及判断盘前、盘中或盘后异动股是否符合暴涨因子。 Evaluate point-in-time price, baseline liquidity, float/share supply, premarket, official-open, and after-hours gaps, turnover, spread, VWAP, earnings/news catalysts, splits, dilution, halts, and data quality. Do not use for long-term valuation or for ETFs, warrants, rights, units, preferred shares, or bonds.
---

# 美股极端暴涨候选筛选

## 决策原则

严格区分三个层级：

1. **结构候选**：低价、低基线流动性、低股本或低 float。
2. **事件确认**：盘前、正式开盘或盘后榜出现强 gap 与供给周转，并有可核验的事件或低供给证据。
3. **可执行交易**：开盘后保持 VWAP、价差可控、结构确认且供应风险已排查。

不要把盘前涨幅、盘前最高价或上一常规时段的 `last price` 当作正式开盘 `Gap`。不要把 evidence score 当成上涨概率。

按需读取：

- 引用命中率、odds ratio、分位数或回撤统计前，读取 [references/factor-model.md](references/factor-model.md)。
- 解释模型来源、历史案例或样本外验证时，读取 [references/case-studies-2026.md](references/case-studies-2026.md)。
- 分析 5 分钟图、设计日内入场/减仓/退出或识别末端派发时，读取 [references/intraday-500pct-playbook.md](references/intraday-500pct-playbook.md)。
- 讨论 CYCU 2026-07-30 的量价阶段、消息发酵或供应冲突时，读取 [references/cycu-2026-07-30.md](references/cycu-2026-07-30.md)。

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
regular_close, after_price, after_high, after_volume, after_bid, after_ask
market_cap, total_shares, float_shares
median_dollar_volume_20, avg_volume_20, pre_return_20d_pct
split_today, post_split, last_split_date, dilution_overhang, halted
premarket_supply_risk, supply_risk_type, supply_risk_source, supply_risk_checked_at
open_price, last_price, regular_volume, vwap, first_5m_structure
prior_abnormal_volume_warmup, turnover_expanding
catalyst, catalyst_source
after_hours_catalyst_quality, after_hours_supply_thesis
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
- 在评分前完成盘前消息供给核验：检查 registered resale、ATM、可转换证券、
  warrants、PIPE/equity line、lock-up release 和新增发行；确认存在时直接 `EXCLUDE`。
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
AND premarket_supply_risk == false
```

### 5. 盘后榜发现层

盘后榜只用于发现下一交易时段的候选，不把盘后上涨直接解释成可执行信号。计算：

```text
after_gap_pct       = (after_price / regular_close - 1) * 100
after_turnover      = after_volume / supply_shares
after_spread_pct    = (after_ask - after_bid) / ((after_ask + after_bid) / 2) * 100
after_high_fade_pct = (after_price / after_high - 1) * 100
```

盘后质量门槛：

```text
after_gap_pct >= 15.00
AND after_turnover >= 0.25
AND after_spread_pct <= 3.50
AND after_high_fade_pct >= -20.00
AND premarket_supply_risk == false
```

只接受两条可核验路径：

- `AFTER_HOURS_EARNINGS`：财报、业绩预告或正式监管文件支持，GXAI 属于该类研究原型。
- `AFTER_HOURS_LOW_SUPPLY`：经来源核验的低 float/低总股本或极紧供给结构，FGI 属于该类研究原型。

合格盘后候选最高只能输出 `WATCH`。下一交易时段必须重新核验供给风险、spread、
VWAP、开盘周转和首个 5 分钟结构，完成后才允许进入既有开盘执行路径。任何 confirmed
ATM、registered resale、warrant、PIPE、equity line 或其他即时供给风险直接 `EXCLUDE`。

### 6. 判断开盘路径

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
AND premarket_supply_risk == false
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
AND premarket_supply_risk == false
AND halted != true
```

不要把常规 `Gap >= 100%` 模型的命中率套用到 CPHI subtype。

### 7. 运行 5 分钟状态机

上游只有 `EXECUTE` 才能进入日内执行模块。逐个完成的 5 分钟 bar 更新：

```text
last_price, high_price, vwap, bid, ask
ma5, ma10, ma20, current_bar_volume, bar_volume_ma5, macd_hist
turnover_expanding, retest_confirmed, halted, dilution_overhang
official_primary_source, catalyst_age_minutes
```

批量或单票快照使用：

```powershell
python scripts/classify_intraday_phase.py snapshots.json --format markdown
```

只使用以下阶段：

| 阶段 | 执行 |
|---|---|
| `OPEN_CONFIRMATION` | 等待 VWAP、均线和周转确认 |
| `TREND_EXPANSION` | 只做突破后的首次或二次缩量回踩 |
| `CONTROLLED_PULLBACK` | 回踩确认后才允许入场；已有仓位减为 core |
| `PARABOLIC_EXTENSION` | 禁止追涨；已有仓位减仓 50–80% |
| `BLOW_OFF_DISTRIBUTION` | 禁止新开；退出 runner |
| `FAILED_TREND` | 退出 |
| `HALTED` | 禁止新开；复牌后重算 |
| `WAIT_DATA` | 修复数据 |

以下组合定义末端派发，而不是新突破：

```text
day_gain_pct >= 250%
AND high_fade_pct <= -10%
AND current_bar_volume / bar_volume_ma5 >= 2.00
AND (last_price < MA5 OR macd_hist <= 0)
```

消息发酵按 `UNVERIFIED / FRESH / FERMENTING / CROWDED` 分层。未验证消息不交易；
消息越拥挤，越不能用题材强度替代回踩、spread 和供应检查。完整规则见
[references/intraday-500pct-playbook.md](references/intraday-500pct-playbook.md)。

### 8. 处理停牌和供应风险

- `halted=true` 时输出 `WATCH`，禁止新开仓；复牌后重新确认 VWAP、spread、周转和价格结构。
- 每只候选必须核验当日盘前消息和最新 SEC/交易所/发行人正式公告，并记录
  `supply_risk_source` 与 `supply_risk_checked_at`。优先核验 `424B5/424B3`、
  `S-1/S-3`、`EFFECT`、`8-K Item 1.01/3.02`、发行公告及定价公告。
- 以下任一风险确认存在且未解除，设置 `premarket_supply_risk=true` 并直接输出
  `EXCLUDE`：active ATM、public/registered direct offering、可立即出售的 registered
  resale、PIPE/equity line、warrant exercise/inducement/repricing、可转债转股、解禁或
  其他会在当前事件窗口增加可售股份的安排。
- 只有 shelf capacity 但尚未确认 takedown，或消息仅来自社媒/聊天室时，不得直接
  判断为无风险；设置 `premarket_supply_risk=UNKNOWN`，输出 `WAIT_DATA` 并继续核验。
- `dilution_overhang` 为旧字段。新数据以 `premarket_supply_risk` 为准；旧数据缺少新字段时
  可回退到 `dilution_overhang`，但必须标记 `SUPPLY_RISK_LEGACY_FALLBACK`。
- 无新增显性催化时写明“暂未发现新增显性驱动”，不得用题材猜测填空。

### 9. 输出决策

只使用以下机器状态：

| 状态 | 含义 |
|---|---|
| `EXECUTE` | 结构、路径、VWAP、周转、流动性和供应风险全部确认 |
| `WAIT_OPEN` | 强盘前候选，等待正式开盘确认 |
| `WAIT_DATA` | 关键字段缺失 |
| `WATCH` | 部分因子符合、盘后候选等待下一时段复核、执行门槛失败或正在停牌 |
| `EXCLUDE` | 证券类型、当日 split、结构/事件强度失败，或确认存在盘前供给风险 |

同时输出：

- `path_type`：`CONVENTIONAL_GAP`、`CPHI_SUBTYPE`、`AFTER_HOURS_EARNINGS`、
  `AFTER_HOURS_LOW_SUPPLY` 或 `NONE`。
- `risk_flags`：`HALTED`、`SUPPLY_RISK_CONFIRMED`、`PREMARKET_SUPPLY_RISK`、
  `SUPPLY_RISK_UNKNOWN`、`SUPPLY_RISK_LEGACY_FALLBACK`、`DILUTION_OVERHANG`、
  `POST_SPLIT`、`SUPPLY_PROXY`、`AFTER_HOURS_SIGNAL`、
  `AFTER_HOURS_UNVERIFIED_ROUTE`、`AFTER_HOURS_WIDE_SPREAD`、`MISSING_DATA`。

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
- 单票最多两次入场，单日已实现加浮动风险上限为账户权益的 0.50%。
- post-split 标的不做无保护裸空。
- 跌破 VWAP 且周转不再扩张时，优先视为供应释放。
- 进入 `PARABOLIC_EXTENSION` 时减仓 50–80%；进入 `BLOW_OFF_DISTRIBUTION` 时退出 runner。
- 除非另有经过验证的隔夜模型，15:55 ET 前清空日内仓位。
- 不承诺止损在 halt gap 中按计划价格成交。

## 数据完整性

- 数据冲突时，采用时间戳更新且字段定义更明确的来源。
- API 涨跌幅异常时，用 point-in-time 价格自行重算。
- 不用复权历史价格替代事件当时价格。
- 不把条件命中率解释成单只股票的确定概率。
