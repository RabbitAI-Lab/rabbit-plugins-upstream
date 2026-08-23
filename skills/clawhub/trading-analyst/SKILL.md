---
name: trading-analyst
slug: trading-analyst
version: 1.3.0
homepage: https://github.com/pmuhammadagus-byte/openclaw-settings
description: "Trading analysis framework: multi-TF structure, liquidity concepts, entry checklist, trade review, and memory schema. Use when the user asks to analyze XAU/USD, forex, gold, or crypto charts, check market bias, build an entry plan, run a pre-trade checklist, review a trade, or fetch prices/calendar/correlation data (DXY, yields, SPX)."
changelog: "v1.3.0: Fix version drift, trigger-rich description, declare env/bin requirements. v1.2.0: ClawHub metadata, validation gates, skill-card"
metadata: {"clawdbot":{"emoji":"📈","requires":{"env":["TWELVE_DATA_API_KEY","FIRECRAWL_API_KEY"],"bins":["curl"]},"os":["linux","darwin","win32"]}}
---

# Trading Analyst Skill v1.3

A structured framework for trading analysis collaboration. Provides methodologies, checklists, and memory schemas for systematic market analysis.

## When to Use

User asks for market/chart analysis (gold, forex, crypto), daily bias, entry plans, pre-trade checklist validation, post-trade review, or market data (prices, economic calendar, DXY/yield/SPX correlation). Triggers: "analisa XAU", "checklist", "bias", "entry plan", "review trade", "calendar", "correlation".

**Never gives financial advice** — all output is framed as analysis and scenarios. Final decisions always belong to the user.

## Analisa Framework

### Multi-Timeframe Structure (Top-Down)
1. **HTF Bias (W/D/4H)** — Trend direction, key levels, market structure (HH/HL/LH/LL)
2. **ITF Structure (1H/15M)** — Pullback depth, liquidity pools, order blocks, FVG
3. **LTF Trigger (5M/1M)** — Entry pattern: BoS, CHoCH, rejection, sweep & reclaim

### Core Concepts (ICT/SMC/Quarters Theory)
- **Market Structure** — Break of Structure (BoS), Change of Character (CHoCH)
- **Liquidity** — Buy-side / Sell-side liquidity, equal highs/lows, swing points
- **Order Blocks** — Last up/down candle before impulsive move, mitigation rules
- **Fair Value Gaps (FVG)** — 3-candle imbalance, confluence with OB/liquidity
- **Quarters Theory** — LQ1-LQ4 ranges, Half Point, Over/Undershoot rules
- **Kill Zones** — Asian/London/NY open, London Close — optimal entry windows

### Intermarket Context
- **DXY** — Inverse correlation, key levels, trend
- **US 10Y Yield** — Real rates impact on non-yielding assets
- **SPX/Risk Assets** — Risk-on/off sentiment
- **Oil/Copper** — Inflation/growth proxies
- **Silver (XAG)** — Gold beta, GSR (Gold/Silver Ratio)

---

## Data Layer Integration (NEW v1.1)

### Primary APIs
| Provider | Purpose | Free Tier | Key Endpoints |
|---|---|---|---|
| **Twelve Data** | OHLCV, indicators, real-time | 800 req/day | `/time_series`, `/rsi`, `/macd`, `/ema`, `/price` |
| **Firecrawl** | Web scraping (JS rendering) | 500 credits/mo | `/v1/scrape`, `/v1/crawl` |
| **gold-api.com** | Precious metals spot | Unlimited | `/price/XAU`, `/price/XAG` |

### Symbol Formats (Twelve Data)
- Gold: `XAU/USD`
- Silver: `XAG/USD`
- DXY: `DXY` (may need paid tier)
- US10Y: `US10Y` (paid tier)
- SPX: `SPX` (paid tier)
- Forex: `EUR/USD`, `GBP/USD`, `USD/JPY`

### Correlation Data Sources (Fallback)
When API symbols unavailable:
1. **Firecrawl → TradingView technicals** — `/symbols/DXY/technicals/`, `/symbols/SPX/technicals/`
2. **Firecrawl → Investing.com** — Bonds/yields technical pages
3. **Manual** — User provides key levels from their chart

### Rate Limit Management
- Twelve Data: 8 req/sec burst, 800/day → cache responses, batch requests
- Firecrawl: 500/mo → prioritize high-value scrapes (calendar, correlation)
- Use `memory/trading/api_keys.md` for secure key storage

---

## Entry Checklist v1.1 (UPDATED)

| # | Criteria | Pass/Fail | Notes |
|---|---|---|---|
| 1 | **HTF Bias Clear** | ☐ | Trend + key level identified (accept conflict with size reduction) |
| 2 | **ITF Pullback to Value** | ☐ | OB / FVG / 50% / 61.8% / Liquidity / EMA confluence |
| 3 | **LTF Trigger Present** | ☐ | BoS/CHoCH/Rejection/Sweep on 5M/1M/15M |
| 4 | **R:R ≥ 1:2** | ☐ | Measured from entry to SL/TP |
| 5 | **Risk ≤ 1% Equity** | ☐ | Position size calculated |
| 6 | **No High-Impact News ±30min** | ☐ | Check economic calendar (ForexFactory/Investing.com) |
| 7 | **Session Timing Aligned** | ☐ | Kill zone / avoid lunch/rollover |
| 8 | **Correlation Confirmed** | ☐ | DXY/Yield/SPX support direction (partial OK with note) |
| 9 | **Journal Pre-filled** | ☐ | Plan written BEFORE entry |
| 10 | **Spread/Slippage Check** | ☐ | Spread < 0.5% ATR, liquidity adequate |

### Conflict Resolution Rules (NEW)
- **HTF Conflict** (e.g., Daily bearish, 4H bullish) → Reduce size to 0.5%, tighten SL, require stronger LTF trigger
- **Missing Correlation** (1 of 3 unknown) → Proceed if 2/3 align, flag in journal
- **No LTF Trigger** → Do not chase; set alerts at key levels instead

---

## Trade Management Rules

- **SL Placement** — Beyond invalidation (structure break), not arbitrary pips
- **TP1** — 1R (move SL to BE), **TP2** — 2R, **TP3** — 3R+ (trail)
- **Trailing** — 1H/4H structure: trail behind swing HL/HH
- **Max Drawdown** — Daily -2%, Weekly -5% → stop trading, review
- **Correlation Cap** — Max 2 correlated positions (e.g., XAU + XAG = 1 unit)
- **Time Stop** — Cancel unfilled limits after session kill zone ends

---

## Trade Review Template (Post-Trade)

```markdown
## Trade Review — [DATE] [SYMBOL] [LONG/SHORT]

**Setup:** [Which checklist item triggered]
**Entry:** [Price] | **SL:** [Price] | **TP:** [Price] | **R:R:** [x:y]
**Size:** [Lots/Contracts] | **Risk %:** [%] | **Result:** [Win/Loss/BE] | **P&L:** [R-multiple]

**What Went Well:**
- 
**What Didn't:**
- 
**Mistake Category:** [Setup / Execution / Management / Psychology / Risk / Data]
**Improvement Action:** [Specific, measurable]

**Chart:** [Attach screenshot with annotations]
**Data Sources Used:** [Twelve Data / Firecrawl / Manual / Chart]
```

---

## Memory Schema (Per Symbol) — UPDATED v1.1

```yaml
symbol: XAUUSD
bias: "bullish/bearish/neutral/conflicted"          # HTF bias with conflict flag
key_levels:                               # Price levels that matter
  - price: 4050
    type: "LQ3_top / OB / FVG / Swing / EMA"
    tf: "4H"
    status: "untested/tested/broken"
    source: "api/chart/firecrawl"
open_trades: []                           # Active positions
closed_trades: []                         # History (last 20)
notes: ""                                 # Free-form context
data_sources:                             # Track what informed analysis
  - twelve_data: true
  - firecrawl: ["DXY", "SPX"]
  - chart_screenshot: true
last_updated: "2026-07-30T01:14:00+07:00"
```

**Storage:** `memory/trading/<SYMBOL>.md` (one file per symbol)

---

## Assistant Behavior Rules (UPDATED)

1. **Never give financial advice** — Frame as "analysis," "setup," "candidate," "consider"
2. **Always ask for chart screenshot** before analyzing structure (FVG/OB/liquidity need visual)
3. **Require checklist completion** before discussing entry
4. **Log every analysis** to symbol memory file with data sources used
5. **Flag conflicts** (timeframe, correlation, news) explicitly
6. **Default to "no trade"** when ambiguous — cash is a position
7. **Track data source reliability** — API vs scrape vs visual, note gaps
8. **Pre-fill journal template** before any entry discussion

---

## Commands (Mental Shortcuts)

| User Says | Assistant Does |
|---|---|
| "analisa XAU" | Fetch price, check memory, ask for chart screenshot |
| "checklist" | Run through entry checklist interactively |
| "review" | Open last trade review template |
| "bias XAU" | Read/update symbol memory bias & key levels |
| "calendar" | Fetch high-impact events next 48h (Firecrawl ForexFactory) |
| "levels XAU" | List key levels from memory + current price context |
| "correlation" | Fetch DXY/SPX/US10Y via Firecrawl + Twelve Data |
| "entry plan" | Generate full plan with entry/SL/TP/size/rules |

---

## Practical Workflows (NEW v1.1)

### Daily Bias Brief (06:00 WIB)
```
1. Twelve Data: XAU/USD D/4H/1H/15M OHLCV
2. Twelve Data: RSI/MACD/EMA across TFs
3. Firecrawl: ForexFactory calendar (today + tomorrow)
4. Firecrawl: TradingView DXY/SPX technicals
5. Firecrawl: Investing.com US10Y if available
6. Synthesize: Multi-TF structure + indicators + correlation + events
7. Output: Bias, key levels, 3 scenarios, checklist status
```

### On-Demand Analysis (User sends chart)
```
1. Parse user chart: TF, structure, patterns, levels
2. Cross-reference with API data (price, indicators)
3. Run checklist with visual confirmation
4. Generate entry plan with specific levels
5. Save to memory with chart reference
```

### Correlation Check
```
1. Twelve Data: DXY/US10Y/SPX price (if tier allows)
2. Firecrawl: TradingView technicals for each
3. Synthesize: Direction + momentum + key levels
4. Map to Gold bias (inverse DXY, inverse Yield, inverse SPX risk-off)
```

---

## Known Constraints (Documented for Transparency)

| Limitation | Workaround |
|---|---|
| No real-time WebSocket feed | Poll REST API at intervals; use chart for LTF |
| No chart rendering/visual analysis | User provides screenshots; Alt+S text copy |
| No broker execution | Manual entry only; journal pre-fill |
| Twelve Data free tier: no DXY/US10Y/SPX | Firecrawl TradingView/Investing.com |
| Firecrawl: 500 credits/mo | Prioritize calendar + correlation; cache |
| No persistent position monitoring | User updates; memory tracks open trades |
| Session memory resets | All context saved to `memory/trading/` files |

---

## Version History
- **v1.0.0** — Initial framework
- **v1.1.0** — Added API integration patterns, correlation workflows, conflict resolution, data source tracking, practical constraints, daily brief workflow
- **v1.2.0** — Added ClawHub metadata, validation gates, and skill-card
- **v1.3.0** — Fixed title/frontmatter version drift, trigger-rich description, declared `requires.env` (TWELVE_DATA_API_KEY, FIRECRAWL_API_KEY) and `requires.bins` (curl)

---

*Evolve based on user feedback and live trading results.*
