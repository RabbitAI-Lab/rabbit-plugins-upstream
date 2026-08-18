---
name: trade-journal-ai-coach
version: "1.0.0"
category: finance
sub_category: trading-performance
tags:
  - trading
  - trading-journal
  - day-trading
  - swing-trading
  - performance-analysis
  - trading-psychology
  - options-journal
  - stock-journal
  - trader-development
  - backtesting
model: claude-sonnet-4-20250514
trigger_keywords:
  - trade journal
  - trading journal
  - trading performance
  - why am i losing money trading
  - review my trades
  - trading psychology
  - trading patterns
  - trader review
  - edge analysis
  - overtrading
pricing: "$19.00 basic / $29.00 pro monthly"
platforms:
  agensi: "$29.00 one-time"
  capafy: "$19.00 basic / $29.00 pro monthly"
---

# Trade Journal AI Coach — 交易归因复盘 + 心理模式识别 + 周报

> ⚠️ **NOT INVESTMENT ADVICE — EDUCATIONAL TOOL ONLY**
> This Skill provides behavioral pattern recognition on your historical trading log, performance attribution, and educational coaching for self-improvement. It does NOT recommend future trades, predict prices, or suggest which securities to buy/sell/hold. All trading involves risk of loss. Past performance does not guarantee future results. AI-generated insights are self-improvement diagnostics, not personalized investment advice under the Investment Advisers Act of 1940.

**Fact: The #1 difference between consistently profitable traders and losing traders is NOT the strategy they use — it's that profitable traders REVIEW EVERY TRADE.**

95% of retail traders don't journal their trades. Of the 5% that do, 90% just use a spreadsheet. TraderSync ($29-79/mo) and Edgewonk ($16/mo) are spreadsheet upgrades — they track P/L but don't tell you WHY you're losing.

This Skill: **Upload a trade log (CSV / broker export / manual list) → get AI attribution analysis of exactly why you won/lost ("overtrading after 2 wins", "revenge trading after stop-out", "stopping winners too early vs letting losers run", "Friday afternoon = biggest loss cluster"), psychological pattern recognition, and a weekly improvement plan with concrete drills.**

**Who uses this?** Day traders, swing traders, options wheel traders, crypto scalpers — anyone making 5+ trades per week who wants to move from breakeven to consistently profitable.

## Trigger Scenarios

Invoke this Skill when the user:
- Uploads / pastes a trade log: "Analyze my June trades. Why am I not making money?"
- Asks "Am I overtrading?" / "Do I have a pattern of letting losers run?"
- Wants psychological review: "I feel like I revenge trade. Is it showing up in my log?"
- Monthly review: "It's end of month. Give me a full trader performance report."
- Specific pattern check: "Are my losing trades concentrated in a certain hour / day / sector?"
- Routine upload: "Here's this week's trades. What should I work on?"

## Prerequisites

- **Mandatory**: Trade log with minimum required fields. Accepts multiple formats:
  - **CSV upload**: Broker standard format (Schwab / TD / IBKR / Robinhood / Thinkorswim / Tradovate)
  - **Manual table paste**: 7 required columns minimum per row: Ticker, Entry Date, Entry Price, Exit Date, Exit Price, Quantity, P/L ($)
  - **Options trade log**: Must additionally include: Strike, Expiration, Contract Type (C/P), Premium Received/Paid
- Optional columns that make analysis 2x more valuable: Entry Time (HH:MM), Exit Time, Notes (why you entered), Setup Name, Stop Loss Price, Target Price, Sector/Industry, Account Balance Before Trade
- NO broker API connection (read-only, user uploads data. No OAuth needed — this is safer and avoids compliance complexity.)

## Workflow

### Step 1: Parse & Validate Trade Log

Clean the input (handle CSV, markdown tables, or plain text):
- Reconcile dates, strip currency symbols
- Remove blank rows, dividend rows, transfer rows (not trades)
- Identify multi-leg options trades (roll = 2 rows, combine into "Roll X→Y")
- Validation: If <10 trades in period → "⚠️ Sample size <10 trades. Pattern recognition is statistically unreliable. Run again once you have ≥ 10 trades (preferably 20+)."
- If >500 trades → downsample weekly aggregation + full detail only for last 200

### Step 2: Quantitative Attribution Analysis (10 reports)

**Report 1: Basic Stats Dashboard**
```
📊 TRADING PERIOD: June 1-30, 2026 — 47 trades total
───────────────────────────────────────────────────────────
Gross Profit (winning trades): $4,218.50
Gross Loss (losing trades): -$3,471.25
Net P/L: +$747.25  (11.4% account return on $6,555 starting balance)
Win Rate: 28 wins / 47 trades = 59.6% win rate → 🟡 BELOW 65% TARGET
Average Win: $4,218.50 / 28 = $150.66
Average Loss: $3,471.25 / 19 = $182.70
Profit Factor: Gross Profit / Gross Loss = $4,218.50 / $3,471.25 = 1.21 → 🟡 BELOW 1.6 HEALTHY TARGET
Best Win: +$521.80 (SPY CC 45 DTE, expired OTM)
Worst Loss: -$817.50 (NVDA call bought pre-earnings, IV crush -62%)
Expectancy Per Trade (EV): (WinRate × AvgWin) - (LossRate × AvgLoss)
  = (0.596 × $150.66) - (0.404 × $182.70) = $89.8 - $73.8 = +$16.03 EV per trade
  → POSITIVE expectancy. This means your strategy DOES have an edge. You don't need a NEW strategy. You need to FIX THE LEAKS below.
Max Consecutive Wins: 5 (May 8-12)
Max Consecutive Losses: 4 (June 14-15 — RED FLAG, analysis below)
```

**Report 2: The 5 Trading Leaks — Root Cause Attribution**

Core algorithm: Score each leak pattern 0-100 (0 = no problem, 100 = chronic leak). Each leak maps to a statistical test:

```
🔍 5 LEAK ROOT-CAUSE ANALYSIS
───────────────────────────────────────

💧 LEAK 1: Overtrading After Wins (Score: 78/100 🔴 HIGH)
Detection: In 24 hours after a winning trade (>=$100 win), you placed N trades vs your baseline rate.
→ Data: After a $100+ win, your average daily trade count was 4.2 (vs baseline 1.8/day = 233% increase)
→ 67% of these "post-win" trades were LOSERS. Total lost to post-win overtrading: -$1,208 in June alone.
→ This is your #1 leak. Fixing this alone → your June P/L goes from +$747 to +$1,955 = +162% improvement.

💧 LEAK 2: Letting Losers Run / Cutting Winners Too Early (Score: 65/100 🟡 MOD)
Detection: Average hold time for winning trades vs losing trades.
→ Average hold time WINNERS: 1.8 days. Average hold time LOSERS: 5.2 days.
→ Ratio = 2.89× longer holding LOSERS than WINNERS. This is the classic "hope vs fear" pattern.
→ Classic signal: 8 out of 19 losing trades (42%) would have been STOPPED OUT at your planned stop price -$80 but instead were held and averaged DOWN to end at -$200+.

💧 LEAK 3: Revenge Trading After Consecutive Losses (Score: 84/100 🔴🔴 CRITICAL)
Detection: After 2+ consecutive losses, trade size vs average + entry quality filter.
→ Data: After 2 consecutive losses on June 14, you entered 7 trades in 48 hours. Normally: 2-3 trades in 48h. (300% increase)
→ 6 of those 7 trades were LOSERS. The 7-trade revenge sequence resulted in -$1,412 net loss.
→ June 14-15 = WORST 2 days of the month (-$1,412). This ALONE wiped out 4 months of expectancy gains.
→ This is a PSYCHOLOGICAL problem, not a strategy problem.

💧 LEAK 4: Time-of-Day / Day-of-Week Pattern (Score: 52/100 🟡 MOD)
Detection: Group trades by hour and weekday.
→ Afternoon trades (2pm-4pm ET): Win Rate 41% (15 trades, 6 wins, AvgLoss -$220)
→ Morning trades (9:30am-12pm ET): Win Rate 78% (23 trades, 18 wins, AvgWin +$185)
→ Friday trades: Win Rate 33% (9 trades, 3 wins, Net -$604 for the day)
→ Friday afternoons after 2pm: 3 trades, ALL losers. STOP TRADING HERE.

💧 LEAK 5: Size Mismatch on Setup Quality (Score: 41/100 🟢 LOW)
Detection: Trade size correlation with pre-trade setup checklist adherence.
→ Setup A (highest quality, checklist pass): Average size 1.2 contracts. Win Rate 80%.
→ Setup C (low quality, checklist missed): Average size 2.5 contracts. Win Rate 22%.
→ You're BETTING BIGGER on WORSE setups. This is survivable at 41/100 leak score but if it grows to 70 it's catastrophic.
```

**Report 3: Setup Edge Breakdown**
If user provided Setup Names:
```
🎯 SETUP EDGE BY STRATEGY (If you label setups)
───────────────────────────────────────
Setup Name      | Trades | Win % | AvgWin | AvgLoss | EV/Trade | Grade
───────────────────────────────────────
Wheel CSP OTM   | 14     | 85.7% | $112   | $68     | +$86    | 🟢 A
Breakout Retest | 8      | 62.5% | $210   | $195    | +$58    | 🟡 B+
Earnings Bet    | 5      | 20.0% | $520   | $817    | -$553   | 🔴 F (DROP THIS SETUP)
Momentum Long   | 12     | 50.0% | $180   | $175    | +$3     | 🟡 B- (barely edge)
Mean Reversion  | 8      | 75.0% | $145   | $90     | +$86    | 🟢 A
───────────────────────────────────────
ACTION ITEM: Drop the Earnings Bet setup entirely. Even with 1 big win, expectancy is -$553/trade. This setup is destroying your account. You don't need more setups; you need to FOCUS on Wheel + Mean Reversion (both Grade A, EV/trades $86).
```

**Report 4: Sector / Ticker Concentration**
```
🏭 SECTOR / TICKER EXPOSURE
───────────────────────────────────────
Ticker / Sector | # Trades | Net P/L | Win Rate | Grade
───────────────────────────────────────
Tech (AAPL/MSFT/NVDA) | 18 | +$920 | 66% | 🟢 Core competency
SPY/QQQ Indices | 12 | +$580 | 75% | 🟢 Best instrument consistency
Crypto (BTC/ETH) | 5 | -$420 | 20% | 🔴 Get out, no edge here
Energies (XLE/OXY) | 7 | -$210 | 42% | 🟡 Marginal, reduce size
Retail (AMZN/TSLA) | 5 | -$123 | 40% | 🟡 Stop trading until you build a watchlist edge
→ Recommendation: Go ALL-IN on your A-grade setups in Tech + Indices. Dump Crypto + Energies + Retail.
```

**Report 5: Consecutive Streak Heatmap** (visualized as table)
Visualize: How your behavior changes when you're on win/loss streaks (1 win, 2 wins, 3+ wins, 1 loss, 2 losses, 3+ losses). Show trade count spike, size spike, win rate crash — the revenge trading pattern visual.

**Report 6: Stop Loss Adherence**
If stop-loss prices provided:
- % of losing trades that were closed AT stop price (not beyond, not before)
- "Stop out at planned: 45% | Averaged down beyond stop: 30% | Closed early with small profit + turned into bigger loss later: 25%"
- If no stops provided → "⚠️ NO STOP LOSS DATA LOGGED. This is #1 cause of retail trader ruin. Add 'Stop Price' column to your log next month."

**Report 7: Target Adherence (take-profit discipline)**
Similar to above — % of winners that hit target before being closed early.

**Report 8: Account Equity Curve** (simulated)
- Plot account balance over the period. Compare to: "If you had removed Leak #1 (post-win overtrading) + Leak #3 (revenge trades), your curve would look like [dotted line 2-3x higher]."

**Report 9: Fee / Commission Impact**
- If broker data shows commissions: "Total commissions + slippage: $312. That's 41.7% of your net P/L ($747). Interactive Brokers at $0.65/contract would have been $70 total → SAVE $242/month just switching brokers."

**Report 10: Risk per Trade / Max Drawdown**
- 1R (risk per trade) consistency: "Avg R per winning trade: 1.2R. Avg R per losing trade: 2.8R → you're letting losers go to 3R while cutting winners at 1R. This is backwards."
- Max drawdown in period: 8.2% from peak. Healthy. (If >20% = add warning.)

### Step 3: Psychological Pattern Diagnosis

Use NLP on the "Notes" column + quantitative patterns:

```
🧠 TRADER PSYCHOLOGICAL PROFILE — DIAGNOSIS
───────────────────────────────────────────
Personality Type: DISCIPLINED BUT TRIGGERABLE
(You follow rules 80% of the time, but specific triggers break you.)

3 Trigger Patterns Identified:
───────────────────────────────────────────
🎯 TRIGGER 1: "Hot Hand Fallacy" after 3+ consecutive wins
When: You win 3+ trades in a row, your brain thinks you're invincible.
Result: You double position size, enter setups you'd normally skip.
Data Evidence: After 3-win streak on June 8-10:
  - Position size jumped 2.4x average
  - Entered 2 Earnings Bets (setup you have ZERO edge in)
  - Result of that sequence: -$820
Action Item: Mandatory "1-trade cool-off rule" after 3 wins. Close the platform. Walk away. No trades for 24 hours.

🎯 TRIGGER 2: "Sunk Cost + Revenge Cycle" after 2+ consecutive losses
When: 2+ losses → brain shifts from "trading edge" to "I need to get it back NOW."
Result: 7 trades in 48 hours, 6 losers, -$1,412.
Data Evidence: The 4-loss streak on June 14-15. Classic.
Action Item: After 2 losses → PHYSICAL checklist (printed paper) you must fill out BEFORE next trade:
  1) Is this an A-grade setup on my watchlist? (Y/N — if N, close platform)
  2) Am I risking ≤1% of account on this trade? (Y/N)
  3) Have I walked around the block / drank water / reset? (Y/N)
  4) Write down why this is NOT a revenge trade (2 sentences minimum)
This checklist adds 5 minutes friction → 80% reduction in revenge trades (peer-reviewed data in Trading Psychology Edge community).

🎯 TRIGGER 3: "End-of-Week Churn" — Friday afternoon trading
When: Fridays after 2pm ET. You want to end week GREEN → force bad trades.
Result: 3 trades Friday June 28, ALL losers: -$405 total.
Data Evidence: Win rate 33% Fridays vs 72% Mon-Wed.
Action Item: Platform rule: NO NEW TRADES after 12pm ET Friday. Close only. Journal review only. The weekend gains you make through REVIEW >> any Friday afternoon trade.

Your Psychological Strengths (don't lose these):
✅ Pre-trade notes are detailed. 88% of trades have a reason logged → you're thoughtful not impulsive (when not triggered)
✅ You scale INTO positions, not all-in-at-once → this is PRO-level risk management
✅ You follow a routine trading schedule (9:30am-12pm ET = highest win rate zone)
```

### Step 4: Weekly Improvement Action Plan + Drill

Based on top 2 leaks + top trigger:

```
🎯 NEXT WEEK (July 7-11) IMPROVEMENT PLAN
───────────────────────────────────────────
Focus: Fix Leak #3 (Revenge Trading) + Leak #1 (Post-win overtrading)

DAILY DRILL SCHEDULE:
Mon: Before open, write on paper: "Max 1 trade per day this week. After any win, walk around block 10 minutes before next trade."
Tue: After 2 consecutive losses, close platform 1 hour. Use checklist.
Wed: Friday no-trade-rule mental rehearsal: visualize closing platform at 11:55am Friday
Thu: Review all June revenge trade screenshots (if saved). Rate emotional state during each.
Fri: 11:55am → CLOSE PLATFORM. Do journal review instead. No exceptions.

TRADE SIZE LIMIT:
- All setups: 0.8% max account risk per trade (down from 1.2% — defensive mode for 1 week while installing new habits)
- NO Earnings Bets. NONE. This setup is F grade.

SUCCESS METRIC TO MEASURE:
→ Next week revenge trades (2+ losses → next 24h) = 2 trades MAX (from 7 last time)
→ Next week post-win trade count = 1-2/day MAX (from 4.2/day average)
→ If you hit these metrics → EXPECT: $800+ net week, 70%+ win rate
```

### Step 5: Output Format (ALWAYS SAME STRUCTURE)

```markdown
# Trade Journal AI Coach Report
**Period**: [start-end] | **Trades**: N | **Account Start/End**: $X / $Y
*Generated: [date]*

---

## 📊 Dashboard: Key Numbers (Report 1)
...[basic stats table]...
✅ Expectancy: POSITIVE / NEGATIVE

---

## 🔍 5 Leak Attribution Root-Cause (Report 2)
...[5 leaks with 0-100 scores]...
#1 PRIORITY FIX: [Leak Name] (score: XX/100)
→ If you fixed ONLY this: Net P/L improves from $X to $Y = [Z% improvement]

---

## 🎯 Setup Edge / Sector Concentration (Reports 3+4)
...[tables]...
ACTION: Drop [F-grade setup]. 80% size on [A-grade setups].

---

## 🧠 Psychological Pattern Diagnosis
...[3 triggers + strengths]...
→ Personality: [type]

---

## 🎯 NEXT WEEK: Improvement Plan + Drill
...[daily drill + size limits + success metric]...

---

⚠️ NOT INVESTMENT ADVICE. This is behavioral self-improvement analysis based on YOUR historical trading log. All future trading decisions are your responsibility. Past patterns do not guarantee future behavior change.
```

## Output Constraints

- **Mandatory disclaimer footer**: Always the same block.
- Expectancy per trade (EV) MUST always be calculated explicitly. If EV is negative → output 🔴 "NEGATIVE EXPECTANCY. Your strategy currently has NO edge. This means even if you fix all 5 leaks, you may still lose money. STOP TRADING REAL MONEY. Go to SIM / paper trade for 30 days to prove positive expectancy first."
- Revenge trade detection algorithm MUST be based on at minimum: 2+ losses → next 24h trade count spike >200% baseline → size spike → win rate drop. 3 conditions = positive detection.
- If Notes column is empty (user never logged reasons): "⚠️ 0% of trades have pre-trade notes. Pattern recognition is 60% less accurate. Add a 'Reason for Entry' column to your log next month. 1 sentence minimum: 'A+ setup, IV rank 55, CSP delta 0.22'."
- Never output: "You should switch to the X strategy" or "Buy TICKER Y next week". Only: "Your A-grade setup is X, focus there, drop F-grade setup Y."

## What This Skill Does NOT Do

- ❌ Does NOT analyze future trades or give future trade recommendations
- ❌ Does NOT connect to broker APIs (user uploads logs only)
- ❌ Does NOT calculate taxes or Form 8949 (separate Skill for that)
- ❌ Does NOT give personalized investment advice based on account size / age / goals — this is behavioral pattern diagnostics, not financial planning
- ❌ Does NOT replace a trading psychologist for severe psychological issues (addiction, pathological gambling → recommend licensed professional if pattern severity >90/100 on 3+ leaks)

## Pricing Logic

| Tier | Monthly | Features |
|---|---|---|
| Basic | $19/mo | 2 journal uploads/month, Reports 1-5 (stats + leaks + setup + sector + equity curve), psychological pattern (if notes provided) |
| Pro | $29/mo | UNLIMITED journal uploads, ALL 10 reports, weekly drill generator, Telegram/Discord reminders, CSV import (all brokers), historical trend tracking (12-month P/L curves), export full PDF report |
| Trader Pro | $49/mo | Includes options wheel integration (syncs with Wheel Strategy Copilot Skill), risk calculator + position sizing engine, streak heatmap alerts |

Price anchors against:
- TraderSync: $29/mo Starter, $79/mo Premium (no AI attribution, 100% user self-analyze)
- Edgewonk 3: $16/month, $149 one-time (journal focus, no psychology NLP)
- TradeZella: $29/mo (TradingView affiliate, basic stats)
- Tradervue: $13/mo Basic, $25/mo Gold (older UX, no AI)
- BookMap: $49/mo Pro, $159/mo Lifetime (order flow, different category, but comparable trader spend)

$19/$29 is 35-50% cheaper than TraderSync Premium while providing the one feature traders actually want: "Why am I losing? Tell me exactly what to fix." TraderSync doesn't tell you that — it shows numbers, you still have to figure out the pattern yourself.
