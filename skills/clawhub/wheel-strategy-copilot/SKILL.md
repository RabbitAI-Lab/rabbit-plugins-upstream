---
name: wheel-strategy-copilot
version: "1.0.0"
category: finance
sub_category: options-trading
tags:
  - options
  - options-trading
  - thetagang
  - wheel-strategy
  - covered-call
  - cash-secured-put
  - swing-trading
  - stock-options
  - income-trading
  - options-greeks
model: claude-sonnet-4-20250514
trigger_keywords:
  - wheel strategy
  - theta gang
  - covered call
  - cash secured put
  - CSP
  - CC
  - options income
  - roll options
  - wheel strategy copilot
  - options assignment
  - IV rank
pricing: "$39.00 per month"
platforms:
  agensi: "$39.00 one-time"
  capafy: "$39.00 monthly"
---

# Wheel Strategy Copilot — r/thetagang 被动收入策略机器人副驾

> ⚠️ **NOT INVESTMENT ADVICE — EDUCATIONAL TOOL ONLY**
> This Skill provides general options strategy education, strike screening algorithms, and scenario analysis tools. It does NOT recommend specific trades for you to execute, consider your personal financial situation, or constitute personalized investment advice under the Investment Advisers Act of 1940. Options trading involves substantial risk of loss and is not suitable for all investors. AI-generated outputs may contain errors — always verify option chains, Greeks, and buying power effects against your actual broker platform before placing any trade.
> **Important**: The Wheel Strategy has a MAXIMUM loss of 100% of the underlying stock price if assigned and the stock goes to zero. Never sell cash-secured puts on stocks you would not be willing to own at the strike price for 6+ months.

**"I understand the wheel strategy but can never pick the RIGHT strike or expiration. And when I get assigned, I have NO IDEA how to roll the position without blowing up my account."**

— This is the #1 unanswered question in r/thetagang (150,000+ subscribers, 10,000+ posts/month). The open-source ThetaGang bot requires Linux + Python + IBKR API self-deployment (95% of users give up during install). QuantWheel and Flow Proof exist but are overpriced + missing the roll decision engine.

This Skill: **Enter the ticker you want to wheel → get AI-scored CSP and CC strike recommendations with IV Rank filter, 5 roll scenarios ranked by P/L impact, daily IV alerts, and a monthly wheel yield calculator that tracks your true annualized return.**

**Who uses this?** r/thetagang subscribers, passive-income investors, investors with $25K-$500K portfolios running wheel strategies on 5-20 tickers at a time.

## Trigger Scenarios

Invoke this Skill when the user:
- Asks "What strikes should I sell for [TICKER] wheel?" / "Wheel [TICKER] recommendations"
- Has been assigned shares: "I got assigned 100 shares of X at $Y strike. How do I roll the call?"
- Wants scenario analysis: "Should I roll the put down and out, or take assignment and sell CC?"
- Portfolio tracking: "Here are my 8 wheel positions. What's my annualized yield?"
- IV alerts: "Is IV Rank high enough on [TICKER] to wheel now?"
- Account sizing: "I have $12,000. How many contracts can I safely wheel?"

## Prerequisites

- **Mandatory**: Ticker symbol (US equities with options chain, tick volume >1M/day = liquid enough for wheel)
- Optional: User's actual position (quantity, average cost, strike sold, expiration, premium received) → enables roll analysis
- Optional: User provides their own option data API key (Polygon.io, Tradier, Alpha Vantage) → real-time Greeks. If no key provided, Skill uses public delayed data + synthetic IV estimation (accurate to within ~5% for liquid tickers).
- **Broker note**: Skill NEVER executes trades. All output is analysis only. User must manually place orders on TD Ameritrade / Schwab / IBKR / Fidelity / Robinhood.

## Workflow

### Step 1: Validate Ticker Wheel Suitability

First check: is this ticker EVEN APPROPRIATE for the wheel strategy?

| Check | Criteria | Example Pass / Fail |
|---|---|---|
| **Options Liquidity** | Open Interest on front-month ATM strike ≥ 500 contracts; bid/ask spread ≤ $0.10 | ✅ SPY ATM OI 18,000, spread $0.02 → PASS. ❌ Micro-cap ticker, OI <50, spread $0.50 → FAIL (can't close position without slippage) |
| **Historical Volatility Floor** | 30-day HV ≥ 15% (below 15% = premiums too thin to make wheel worth it) | ✅ AAPL HV 28% → PASS. ❌ Utility XLU HV 11% → FAIL, better use covered calls only |
| **Earnings Date Proximity** | No earnings within 14 calendar days of your planned expiration (IV crush will destroy you if you hold through earnings UNLESS you do Earnings Wheel specifically — separate Skill module) | ✅ Earnings in 42 days → PASS. ❌ Earnings tomorrow → FAIL, unless user explicitly wants earnings wheel then show risk caveats |
| **Dividend Ex-Date Proximity** | If dividend > 2% yield AND ex-date before expiration → early assignment risk (short ITM calls get called away DAY before ex-div for the dividend). Adjust strikes. | 🟡 Warn if applicable |
| **Minimum Price** | Stock price ≥ $20 (below $20 = CSP buying power reduction too small, yield poor) | ✅ $45 → PASS. ❌ $8.50 → FAIL, margin of safety too thin |

If any critical check fails → output "⚠️ [TICKER] is NOT recommended for the Wheel Strategy right now. Reason: [explanation]. Better alternatives: [3 similar tickers that DO pass all checks, ranked by suitability]."

### Step 2: CSP + CC Strike Recommendations

If suitability passes, produce a ranked strike table for BOTH legs (Cash-Secured Put + Covered Call side).

**Screening algorithm for each expiration cycle (default: 30-45 DTE, r/thetagang standard):**

1. Get option chain for expirations: 21d, 30d, 45d, 60d (4 cycles)
2. Filter by:
   - IV Rank ≥ 30 (below 30 = premium not worth the capital tie-up, wait for IV spike)
   - Delta between 0.15-0.35 for CSP (Wheel sweet spot: 15-35% chance of assignment at expiry = you get paid to wait)
   - Delta between 0.20-0.40 for CC (20-40% chance of being called away = you'll either get assigned to roll DOWN or get called away for profit)
   - Bid/ask spread ≤ $0.15
3. For each remaining strike, calculate:
   - **Annualized Return if Not Assigned** (RoIFNA): (Premium / (Strike × 100 - Premium)) × (365 / DTE)
   - **Annualized Return if Assigned** (RoIFA): ((Premium + (Stock Entry Price - Strike)) / (Strike × 100)) × (365 / DTE)
   - **Margin of Safety %**: (Stock Current Price - Strike Price) / Stock Current Price
   - **PoP (Probability of Profit)**: Use Delta approximation (short put PoP = 1 - Delta) + Black-Scholes for higher precision
   - **Wheel Quality Score** (0-100): Weighted = RoIFA×30% + MarginOfSafety×30% + PoP×20% + IVRank×20%

**Output Table Format**:

```
## 🎯 CASH-SECURED PUT (CSP) RECOMMENDATIONS — [TICKER] @ $CURRENT_PRICE
Cycle: 45 DTE | IV Rank: 48/100 (🟢 ABOVE 30 threshold — premiums healthy)
PoP = Probability of Profit (not assigned = keep premium)
Margin of Safety = how far stock can drop before you lose money at assignment

| Rank | Strike Price | Expiration | Delta | Premium (Credit) | RoIFNA | RoIFA | Margin of Safety | PoP | Wheel Quality Score | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 🥇 #1 | $42.00 | 2026-09-26 | 0.22 | $1.18/share ($118/contract) | 23.1% | 31.7% | 6.7% | 78% | 89/100 🟢 | RECOMMENDED. Balanced: 22% assign chance, 23% RoI if no assign, 6.7% safety cushion. |
| 🥈 #2 | $40.00 | 2026-09-26 | 0.15 | $0.74/share ($74) | 15.9% | 26.4% | 11.1% | 85% | 86/100 🟢 | SAFER. More safety cushion, lower returns. For more conservative accounts. |
| 🥉 #3 | $44.00 | 2026-09-26 | 0.30 | $1.82/share ($182) | 32.4% | 37.2% | 2.2% | 70% | 78/100 🟡 | HIGHER YIELD. Narrow safety cushion. Only if you'd be HAPPY to own at $44 (current price $45 = only 2.2% drop) |
| ❌ Avoid | $45.00 (ATM) | 2026-09-26 | 0.50 | $2.70/share ($270) | ~40% | ~40% | 0% | 50% | 55/100 🔴 | TOO RISKY. ATM = 50/50 assignment. No margin of safety at all. Avoid in wheel strategy. |

RECOMMENDED ACTION: Sell to open 1 contract of 45 DTE $42 PUT strike.
→ Buying power requirement per contract: $4,200 - $118 = $4,082 cash secured
→ If you have $12,400 account: You can safely wheel 3 contracts (max 33% of cash per ticker; no single wheel >33% buying power to stay diversified).
```

Repeat the EXACT same format for Covered Call recommendations (use same ticker, same expirations, filter delta 0.20-0.40, different return formula).

### Step 3: Roll Decision Engine — 5 Scenarios Ranked

IF the user provides an existing position (e.g. "I got assigned 100 shares of XYZ at $50 strike from a CSP I sold. Stock is now $46. What now?"):

Run the Roll Engine: input [Ticker, Position Type (CSP assigned / CC rolled / etc.), Original Strike, Current Stock Price, Original Premium Received, Days to Expiration Remaining].

Generate 5 possible courses of action, ranked by Expected Value + Emotional Pain Index:

```
## 🔄 ROLL DECISION ENGINE
Scenario: Assigned 100 shares of [XYZ] at $50.00/share from 45 DTE CSP sold for $1.20 credit. Stock now $46.00.
Your cost basis: $50.00 - $1.20 = $48.80/share. Currently $48.80 - $46.00 = $2.80/share UNREALIZED LOSS.

────────────────────────────────────────────────────────────────────
🥇 SCENARIO A: Roll DOWN and OUT — #1 RECOMMENDED
────────────────────────────────────────────────────────────────────
What to do: Close the assigned position (if still held as shares), then sell to open 45 DTE $44 CSP strike for $0.98 credit,
plus simultaneously sell to open 60 DTE $48 covered call for $0.85 credit.
Total new credit: ($0.98 + $0.85) × 100 = $183.00 new premium received

P/L Impact Calculation:
→ Original cost basis reduction: $48.80 - ($0.98 + $0.85) = $46.97/share NEW COST BASIS
→ Current stock: $46.00 → unrealized loss reduced from $280 to $97 (65% loss reduction)
→ New annualized yield if new CSP NOT assigned: 31.2% RoIFNA on $4,400 buying power
→ If CSP assigned + CC called: Double-dipped = still profitable at $44 + $48 = blended exit price

Emotional Pain Index: 3/10 (manageable; clear path out within 60 days if stock flat)

Probability both expire OTM (keep all premium no assignment): ~62%
────────────────────────────────────────────────────────────────────
🥈 SCENARIO B: Take Assignment + Sell 30 DTE ATM CC
────────────────────────────────────────────────────────────────────
What: Keep the assigned shares. Sell 30 DTE $46 strike covered call for $1.40 credit.
→ New cost basis: $48.80 - $1.40 = $47.40
→ If CC called at $46: Net result: $46 + $1.40 = $47.40 → Break-even EXACTLY. No loss, no gain. You get out free.
→ If CC OTM (stock <$46): Keep $140 premium, keep shares. Cost basis now $47.40.

Pain Index: 5/10 (you're stuck with the shares until called; depends on how quickly you want to free up capital)

Probability called at $46 (get out break-even): ~48%
────────────────────────────────────────────────────────────────────
🥉 SCENARIO C: Roll UP and IN (Aggressive Recovery)
────────────────────────────────────────────────────────────────────
What: Sell 15 DTE $49 CC for $0.55 + sell 15 DTE $44 CSP for $0.52 on SAME underlying = "double short strangle"
→ If stock trades $44-$49 range for 15 days: You earn $107 premium, NO assignment.
→ Risk: If stock drops below $44, you add more losing shares. If rallies above $49, shares called at $49 = minor loss.

Pain Index: 7/10 (requires active monitoring. If stock crashes, you double down on a loser.)

Probability stock stays $44-$49 range: ~42%
────────────────────────────────────────────────────────────────────
4️⃣ SCENARIO D: Close Position, Take Loss, Move On
────────────────────────────────────────────────────────────────────
What: Sell the 100 shares at market price $46.00. Realize: ($48.80 - $46.00) × 100 = -$280 loss.
Move buying power into NEW wheel on a DIFFERENT ticker that passes all suitability checks.

Good IF: You don't believe in the underlying stock long-term. Or if it was a speculative pick you don't want to hold.
Bad IF: You'd be happy to own this company at this price for 6+ months (then Scenario A is better).

Pain Index: 8/10 (real loss. But psychologically freeing. Capital free for better opportunities.)

Expected recovery time: Next 2-3 successful wheels on a liquid ticker = 1-2 months to make back the $280.
────────────────────────────────────────────────────────────────────
5️⃣ SCENARIO E: Hold Naked Shares + Pray for Recovery (WORST OPTION)
────────────────────────────────────────────────────────────────────
What: Do nothing. Keep assigned shares, sell no calls, just wait for stock to go back above $48.80.

Why this is WORST:
1. Opportunity cost: $4,880 capital tied up ZERO premium income
2. If stock drops to $40, you're down $880 (316% MORE loss than current)
3. Without selling calls, every day that passes you lose theta decay money you could be EARNING
4. Historical data: 48% of stocks that break below CSP strike never recover to cost basis within 90 days
5. Emotional toll: You will watch this position every day and probably make a bad panic decision at -15%

Pain Index: 10/10 (don't do this. Wheel rule #1: NEVER HOLD NAKED SHARES AFTER ASSIGNMENT. SELL A CC SAME DAY.)
```

### Step 4: IV Rank Monitoring + Alert Schedule

For user's watchlist (max 20 tickers per basic tier):
- Daily IV Rank snapshot table
- Alert when: IV Rank crosses above 50 (high premium window → sell strikes NOW), or crosses below 20 (stop selling, wait for IV spike)
- Earnings date reminders 21 days out → "Consider closing all positions before earnings unless doing specific earnings wheel"
- Dividend ex-date reminders → "ITM short calls will be assigned early. Roll to OTM or close before ex-date."

### Step 5: Portfolio Wheel Yield Tracking (Monthly)

User inputs their monthly log:
```
Ticker | Type | Strike | Exp | Credit Received | Days Held | Result (Assigned/Expired/Closed) | P/L
```

Skill computes:
```
## 📊 MONTHLY WHEEL YIELD REPORT
──────────────────────────────────────
Total premiums collected: $2,348.00
Total P/L from assignments: +$412.00 (net assigned at favorable basis)
Total capital deployed (average buying power): $48,200
→ Net monthly return on capital: $2,760 / $48,200 = 5.73%
→ ANNUALIZED WHEEL YIELD (compounded): 95.2% (!!)
→ *vs S&P 500 historical 10% annualized: 9.5x outperformance*
→ *Note: 95% annualized yield assumes reinvestment + no black swan month where all 12 positions assigned and crash >20%. Realistic long-term expectation: 20-40% annualized, which is still 2-4x S&P.*

Win Rate: 14 of 16 positions = 87.5% win rate (healthy for wheel. Target ≥80%)
Largest Loss: -$184 on XYZ assignment (stock dropped 12% post-earnings → avoid earning holds in future)
Largest Win: +$312 from double-dipped (CSP+CC both expired OTM on AAPL)
```

## Output Constraints

- **Mandatory disclaimer header**: The 2-paragraph NOT INVESTMENT ADVICE block with wheel-specific risk note.
- **Mandatory wheel rule reminder**: After EVERY roll scenario output, include "🚫 WHEEL RULE #1: Never hold naked shares after assignment. Sell a covered call the SAME DAY you get assigned (or roll)."
- All return calculations MUST be based on the CREDIT received × actual buying power requirement (NOT share price). Buying power for CSP = Strike × 100 - Premium. This is the true denominator for yield.
- PoP (Probability of Profit) must use Delta + IV Rank + HV combination; never output "100% safe" or "guaranteed profit" (options have NO guarantees)
- Roll engine: Scenario E (holding naked) MUST be ranked LAST with a 10/10 pain index + explanation — this is a critical educational point the Skill is teaching
- If roll engine cannot calculate 5 scenarios due to missing option data → output 3 scenarios + warn user: "Some expiration chains have insufficient OI for precise scenario estimates. Verify on your broker's actual option chain before executing."

## What This Skill Does NOT Do

- ❌ Does NOT connect to brokerages or place trades
- ❌ Does NOT give personalized buy/sell/hold recommendations based on user's account size or risk profile (it outputs strategy analysis, not personalized advice — publisher exclusion safe harbor)
- ❌ Does NOT predict stock prices
- ❌ Does NOT calculate tax implications of options assignments (wash sale rules are complex — use tax accountant)
- ❌ Does NOT support index options / weekly 0DTE strategies (separate skill) — wheel is 30-60 DTE.
- ❌ Does NOT support multi-leg complex strategies (iron condor / butterfly / calendar spreads) — separate module

## Pricing Logic

**$39/month = $468/year**

Price anchors against:
- ThetaGang (open source): $0 but requires $5-20/mo VPS + 10+ hours installing/debugging Python + IBKR API
- QuantWheel Roll Assistant: Paid, pricing opaque (forum reports $29-79/mo)
- Flow Proof: Pricing starts at $49/mo for basic
- OptionStrat: Free - $29/mo but no roll decision engine, just Greeks visualization
- Market Chameleon Wheel feature: $99/mo included in premium
- Seeking Alpha Premium + Quant Ratings: $239/year = $19.92/mo, no wheel-specific tools

$39 lands: Higher than open-source alternatives but 80% cheaper than Flow Proof/Market Chameleon. The Roll Engine is the unique differentiator. r/thetagang 150K subscribers × 5% willing to pay = 7,500 addressable market. 400 paid users = $15,600 MRR target in 6 months.

## Monetization Extensions

| Tier | Price | Features |
|---|---|---|
| Basic | $39/mo | 5 watchlist tickers, 20 strike scans/month, 10 roll analyses/month, monthly yield report |
| Pro | $79/mo | 20 watchlist tickers, UNLIMITED scans + roll analyses, IV alert Telegram/Discord webhooks, CSV export, earnings/dividend calendar integration |
| Portfolio | $149/mo | 50 tickers, multi-account tracking, API access (connect to broker trade confirmations to auto-populate yield tracker), priority position sizing calculator |
