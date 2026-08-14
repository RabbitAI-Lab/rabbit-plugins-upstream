---
name: earnings-call-ai-analyst
version: "1.0.0"
category: finance
sub_category: equity-research
tags:
  - earnings
  - earnings-call
  - stock-analysis
  - 10-k
  - sec-filings
  - sentiment-analysis
  - swing-trading
model: claude-sonnet-4-20250514
trigger_keywords:
  - earnings call
  - earnings transcript
  - quarterly results
  - Q1 Q2 Q3 Q4 results
  - guidance analysis
  - earnings sentiment
  - conference call
  - CEO tone analysis
  - earnings summary
  - SEC filing summary
pricing: "$29.00 per month"
platforms:
  agensi: "$29.00 one-time"
  capafy: "$29.00 monthly"
---

# EarningsCall AI Analyst — 财报电话会议情绪与指南解读

> ⚠️ **NOT INVESTMENT ADVICE — EDUCATIONAL TOOL ONLY**
> This Skill provides general market information and analytical summaries. It does NOT recommend specific securities for you to buy or sell, consider your personal financial situation, or constitute personalized investment advice under the Investment Advisers Act of 1940. All investment decisions are solely your responsibility. AI-generated outputs may contain errors. Always verify against primary sources (SEC EDGAR filings, exchange data) before acting.

**Earnings season is every quarter. Reading 5+ earnings call transcripts (80-150 pages each) in a week is impossible for most investors.**

This Skill turns a full earnings call transcript / 10-K / 10-Q / 8-K filing into a **30-second digest + management sentiment score + guidance diff vs prior quarter + Q&A highlights + red flags checklist** — exactly what Seeking Alpha Premium ($239/year) and AlphaSense ($500+/month enterprise) charge you for, at 1/8 the price.

**Who uses this?** Swing traders tracking 20-50 stocks, long-term investors with concentrated portfolios, finance students learning how to read earnings.

## Trigger Scenarios

Invoke this Skill when the user:
- Asks "summarize Q3 NVDA earnings call" / "what did AAPL say about guidance?"
- Uploads / pastes an earnings transcript (text/PDF) or SEC filing link
- Says "analyze management tone in MSFT earnings"
- Compares "Q2 vs Q3 guidance for META"
- Asks "any red flags in TSLA earnings call?"

## Prerequisites

- Inputs work with: **Pasted text transcript** (preferred), **PDF upload**, or **URL to SEC EDGAR / earnings site (factiva / seekingalpha transcript)**
- No API Key required for SEC EDGAR (rate-limited 10 req/sec)
- For live calls: user provides YouTube link → Whisper transcript (user's own API key)

## Workflow

### Step 1: Parse Input

Detect input type:
- **Pasted text** → direct ingestion
- **PDF** → extract text (handle SEC multi-document PDFs)
- **EDGAR URL (sec.gov/Archives/edgar/data/...)** → fetch with `urllib` (no key needed, respect 10 req/sec)
- **YouTube URL** → prompt user to provide their Whisper/Transcript API key or paste transcript

**Validation**: If filing is <5 pages or transcript <3000 words, warn user: "Input looks short — this may be a press release not the full transcript. The full call transcript typically has the Q&A section."

### Step 2: Structured NLP Extraction

Extract the following structured fields (each as bullet points):

**A. 5-Paragraph Executive Summary**
1. **Headline Numbers**: Revenue, EPS (GAAP vs Non-GAAP), YoY growth rates, beat/miss vs consensus by how much
2. **Segment Breakdown**: Revenue by segment/geography/division, which segments accelerated vs decelerated
3. **Management Guidance**: Forward guidance for next quarter / FY (revenue, EPS, margins, capex)
4. **Q&A Highlights**: 3 most important exchanges (write verbatim question + 1-sentence paraphrase of answer)
5. **Sentence That Mattered**: ONE single quote from CEO/CFO that actually changed the stock price (marked with 🔴 if negative, 🟢 if positive)

**B. Management Sentiment Score (0-100)**

Calculate using weighted scoring:

| Factor | Weight | Scoring |
|---|---|---|
| Forward-looking words ("expect", "optimistic", "strong") | 30% | Count vs baseline of 1800 earnings calls |
| Backward-looking / defensive words ("challenging", "uncertain", "headwinds") | 25% | Count vs baseline |
| Guidance revisions (raised / lowered) | 20% | Raised = +20 pts / Lowered = -20 pts / Flat = 0 |
| CEO vs CFO tone divergence | 10% | CEO positive but CFO cautious = -10 |
| Hedging language ("may", "could", "might", "potentially") frequency | 15% | Above median = -10 per sigma |

Output format:
```
Management Sentiment Score: 72/100
→ Tone: Cautiously optimistic
→ This ranks in the 68th percentile of 1800 S&P 500 Q2 earnings calls
→ 1 quarter ago: 65/100 (Δ +7, improving)
```

**C. Guidance Diff vs Prior Quarter**

Table format comparing this quarter's explicit guidance vs the prior quarter the same company issued:

| Metric | Q2 Guidance (3 months ago) | Q3 Actual / New Q4 Guidance | Δ Direction | Significance |
|---|---|---|---|---|
| Q4 Revenue | $12.8B-$13.2B | $13.4B-$13.7B raised | 🟢 Beat & Raise | Material (>$400M upward revision) |
| FY EPS | $4.50-$4.65 | $4.62-$4.72 raised | 🟢 Raised 3% | Will move consensus estimates |
| Gross Margin | 72%±1% | 73.5%±0.5% | 🟢 Raised materially | Priced into stock immediately |
| Capex | $4.5B FY | $4.8B-$5.0B FY | 🔴 Raised (may compress FCF) | FCF miss risk next quarter |

If the company did NOT give guidance: explicitly state "Company does not provide explicit forward guidance. This is a data point in itself — more common in cyclical / volatile sectors (energy, biotech)."

**D. Q&A Highlights (Top 3 Exchanges)**

Format:
```
🟢 Q&A 1 [Analyst Name — Firm]: "You guided gross margin up but your capex plan went up. What's driving that?"
CEO Reply (paraphrase): "We're front-loading AI infrastructure spend this quarter but see it as ROI-positive within 4 quarters. GM expands because pricing on [Product X] moved up faster than we modeled."
Signal: Neutral-to-positive — they've thought through the ROI math.

🔴 Q&A 2 [Analyst — Firm]: "Retention was 118% down from 124%. Is it stabilizing?"
CFO Reply (paraphrase): "It was primarily 2 very large logo churns from the financial sector, organic mid-market retention was actually flat sequentially."
Signal: NEGATIVE — blame "2 large customers" ALWAYS = more churn coming next quarter. This is a red flag.

🟡 Q&A 3 [Analyst — Firm]: "FX impact was +3% this quarter. What's Q4 FX assuming?"
CFO Reply (paraphrase): "We assume spot rates, so ~2% FX tailwind in Q4 at current levels."
Signal: Neutral — transparent, no hidden risk.
```

**E. Red Flags Checklist (must run every time)**

Scan for ALL of the following, flag each with severity:

| Red Flag | Scan Method | Severity if Found |
|---|---|---|
| Non-GAAP reconciliation EXCLUDES stock comp (SBC) | Check "Reconciliation of GAAP to Non-GAAP" table — if SBC added back, flag | 🔴 CRITICAL (overstating profitability) |
| DSO (Days Sales Outstanding) increased >5 days YoY | Revenue / (AR x 365) calculation | 🟡 WARNING (channel stuffing possible) |
| Inventory grew >2x revenue growth rate | Compare inventory growth % vs revenue growth % | 🟡 WARNING (demand miss next quarter) |
| Management says "pipeline is strong" but bookings guidance soft | Search transcript for "pipeline" count + compare to implied bookings | 🟡 WARNING (pipeline is a fluff metric) |
| CFO mentions "we're taking a look at our cost structure" | Search exact phrase | 🔴 CRITICAL (layoffs coming in next 2 quarters) |
| Revenue was "record" but operating cash flow was negative | Compare income statement to cash flow statement | 🔴 CRITICAL (quality of earnings issue) |
| CEO speaks for <20% of call time / delegates to CFO 80%+ | Count words by speaker | 🟡 WARNING (CEO may be checked out / preparing exit) |
| Guidance uses "approximately" + "subject to" + 3+ hedging words within one paragraph | Hedging language density scan | 🟡 WARNING (guidance is weak, likely to miss) |
| Key management personnel change mentioned in passing | Search "stepping down", "transition", "leave to pursue" | 🔴 CRITICAL (unexpected executive change) |

### Step 3: Output Format — Always the Same Structure

```markdown
# [TICKER] Q[X] [YEAR] Earnings Call — AI Digest
*Generated: [date]*

---

## 🔢 Headline Numbers
Revenue: $XX.XB (XX% YoY) → BEAT by $XXM / MISS by $XXM
EPS (Non-GAAP): $X.XX → BEAT by $X.XX / MISS by $X.XX
Gross Margin: XX.X% → EXPANDED [X.X bps] / COMPRESSED [X.X bps]
Operating Cash Flow: $XX.XM (vs Q[X-1] $XX.XM)
Free Cash Flow: $XX.XM (FCF Margin XX.X%)

## 📊 Segment Breakdown
...[segment table]...

## 🎯 Guidance vs. Consensus / Prior
...[guidance diff table]...

## 💬 Management Sentiment Score
**[SCORE]/100** — [One-word description: Bullish / Cautiously Optimistic / Neutral / Cautious / Bearish]
→ Ranks in the [X]th percentile of 1800 S&P 500 Q[X] earnings calls
→ Δ vs [prior quarter]: [+/- X pts, direction]

## ❓ Q&A Top 3 Exchanges
...[3 exchanges with signals]...

## 🚩 Red Flags Checklist
| Flag | Status | Severity |
|---|---|---|
| Non-GAAP excludes SBC | ✅ Clean / 🔴 FLAG | Low / High |
| DSO >5 days YoY increase | ✅ / 🟡 | — |
| ...all 9 flags... | ... | ... |

## 🎙️ The ONE Sentence That Mattered
> "[verbatim quote from management]"
> → [Why it matters: 1 sentence interpretation + typical stock reaction pattern]

---

⚠️ This is an AI-generated summary for educational use. It may contain errors. ALWAYS verify key numbers against the OFFICIAL 10-Q/8-K filing on SEC.gov before acting. NOT investment advice.
```

### Step 4: Cross-Company Comparison (Optional)

If user mentions 2+ tickers (e.g., "Compare NVDA and AMD Q3 earnings"), append a comparison table:

| Metric | NVDA | AMD | Spread (NVDA - AMD) |
|---|---|---|---|
| Revenue YoY | XX% | XX% | +X.X% |
| GM% | XX.X% | XX.X% | +X.X% |
| FY Guidance Direction | Raise | Flat | — |
| Sentiment Score | 78 | 62 | +16 |
| Red Flags Count | 1 | 3 | -2 |

## Output Constraints

- **Mandatory disclaimer footer** on every output (the 3-line block above). Never omit.
- Never say "Buy / Sell / Hold" anywhere — only factual descriptions.
- If a data point cannot be extracted, write "N/A — Not disclosed in transcript" instead of estimating.
- Sentiment score must always be compared to a percentile baseline ("68th percentile of 1800 S&P500 calls").
- The "One Sentence That Mattered" must be a verbatim quote, not paraphrased.
- Guidance Diff table requires BOTH directions (prior vs new). If no prior guidance, state that explicitly.

## What This Skill Does NOT Do

- ❌ Does NOT fetch live stock prices or real-time market data (use a data API Skill for that)
- ❌ Does NOT give personalized buy/sell recommendations based on user's portfolio
- ❌ Does NOT predict future stock price movement ("will go up X%")
- ❌ Does NOT perform technical analysis, charting, or options Greeks
- ❌ Does NOT store filings or build a historical database

## Pricing Logic

**$29/month = $348/year**

Price anchors against:
- Seeking Alpha Premium: $239/year = $19.92/month (but it's a broad news platform, not a deep earnings digest tool)
- AlphaSense: $500+/month (enterprise-only, needs sales rep)
- TraderSync Earnings feature: $49/month add-on
- Earnings Whispers: $39/month

$29 lands in the "worth trying for one earnings season" sweet spot. 500 paid users = $14,500 MRR in 6 months with basic content marketing.

## Monetization Extensions (Roadmap)

| Tier | Price | What's Included |
|---|---|---|
| Basic | $29/mo | 30 watchlist alerts, 10 full digests/day, weekly summary PDF |
| Pro | $49/mo | 100 watchlist, 50 digests/day, management score history + trends, Q&A sentiment CSV export |
| Enterprise | $199/mo | Team seats, Slack/Discord webhook alerts, API access, custom ticker universe |
