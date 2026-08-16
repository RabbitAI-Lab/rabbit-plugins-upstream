---
name: tokenomics-decoder
version: "1.0.0"
category: crypto
sub_category: token-analysis
tags:
  - crypto
  - tokenomics
  - defi
  - airdrop
  - token-unlock
  - blockchain
  - ethereum
  - solana
  - rug-pull
  - smart-contract
model: claude-sonnet-4-20250514
trigger_keywords:
  - tokenomics
  - token analysis
  - token unlock
  - tokenomics report
  - crypto analysis
  - rug pull check
  - contract audit
  - vesting schedule
  - crypto due diligence
  - FDV
  - circulating supply
pricing: "$24.00 per month"
platforms:
  agensi: "$24.00 one-time"
  capafy: "$24.00 monthly"
---

# Tokenomics Decoder — 链上 Token 经济尽调报告生成器

> ⚠️ **NOT INVESTMENT ADVICE — EDUCATIONAL TOOL ONLY**
> This Skill provides general tokenomics information and due-diligence checklists. It does NOT recommend specific tokens for you to buy or sell, consider your personal financial situation, or constitute personalized investment advice. Crypto tokens are highly volatile and many projects fail entirely. AI-generated outputs may contain errors — always verify against on-chain block explorers and official project documentation before acting.
> **Note**: Some tokens (e.g. SOL, ADA per SEC enforcement actions) may be classified as securities under U.S. law. This tool makes no determination regarding any token's regulatory status. Consult a licensed attorney for regulatory questions.

**60% of new crypto investors lose money because they don't check tokenomics before buying.**

*"This token has 2% of supply unlocked and 98% vesting over 2 years → it dumps 95% 6 months post-TGE."* — That pattern repeats every bull run. Token Terminal and Messari Pro charge $30-$1,000+/month for tokenomics data. Nansen just dropped from $999 → $49/month to try to stay relevant.

This Skill: **paste a contract address → 30 seconds later you get a full tokenomics report with unlock pressure score + rug pull risk matrix + comparison vs 50 peers in the same category.**

**Who uses this?** Degen traders hunting new DEX listings, airdrop farmers deciding whether to hold or dump, mid-term investors avoiding unlock bombs.

## Trigger Scenarios

Invoke this Skill when the user:
- Pastes a contract address: "0xAbCd... analyze tokenomics"
- Asks "is this token safe to buy?" / "rug pull check for 0x..."
- Wants "unlock schedule for [TOKEN]" / "when does team vest?"
- Asks "compare tokenomics of PEPE vs DOGE vs FLOKI"
- Says "what's the FDV / circulating ratio of this?"
- Requests "sybil risk assessment for this token I farmed"

## Supported Chains

| Chain | Block Explorer | Free API Status |
|---|---|---|
| Ethereum | etherscan.io | ✅ Free tier 5 req/sec |
| BNB Chain | bscscan.com | ✅ Free tier 5 req/sec |
| Polygon | polygonscan.com | ✅ Free tier 5 req/sec |
| Arbitrum | arbiscan.io | ✅ Free tier 5 req/sec |
| Optimism | optimistic.etherscan.io | ✅ Free |
| Base | basescan.org | ✅ Free |
| Solana | solscan.io / explorer.solana.com | ⚠️ Public RPC rate-limited, user can provide Helius/Shyft key |
| Avalanche | snowtrace.io | ✅ Free |
| Sui / Aptos / Sui | Respective explorers | 🔴 Not yet (roadmap v1.1) |

## Prerequisites

- **Mandatory input**: contract address + chain ID
- Optional: user provides their own Etherscan API key (raises rate limits)
- Solana RPC: user provides Helius / Shyft API key OR uses public RPC (slower)
- No key provided → use public APIs with automatic rate limiting + retry + polite delays
- Block explorer links are clickable verifications (critical: user must be able to check raw on-chain data themselves)

## Workflow

### Step 1: Validate Address & Chain

- Check address format matches chain (EVM: 42 hex chars starting 0x; Solana: base58 32-44 chars)
- Fetch contract creation transaction, deployer address, deployer balance change
- If address is invalid / no contract deployed there → output "⚠️ No contract found at this address on [chain]. Double-check the address and chain network."
- If contract is verified on explorer: note "✅ Contract source code VERIFIED on [explorer] — audit trail available"
- If contract NOT verified: note "🔴 CONTRACT SOURCE NOT VERIFIED on [explorer]. This means you CANNOT confirm what the contract actually does. Extreme caution warranted. Common rug pull pattern."

### Step 2: Structured Tokenomics Report (5 Core Sections)

**Section A: Token Basics Table**

| Field | Value | Source Link |
|---|---|---|
| Token Name | The Token | (etherscan link) |
| Symbol | TTKN | — |
| Decimals | 18 | — |
| Total Supply (Minted Ever) | 1,000,000,000 TTKN | (totalSupply() call) |
| Current Circulating Supply | 150,000,000 TTKN | (manual — burn addr + dead addr + team vesting excluded) |
| Circulating % of Total | 15.0% | — |
| Fully Diluted Valuation (FDV) | $2,400,000 | (price × total supply, from DEX spot) |
| Current Market Cap | $360,000 | (price × circulating) |
| FDV / MC Ratio | **6.67×** | ⚠️ Interpretation below |
| Deployer Token Holdings | 0 TTKN (0.00% of total) | 🔴🟢🟡 rating below |
| Deployer ETH/SOL Balance | 0.00 | (checking for dev rug exit liquidity) |

**FDV/MC Ratio Interpretation**:
```
1.0x = 100% circulating, 🟢 NO unlock risk
1.0x-2.0x = Mild unlock risk, manageable
2.0x-5.0x = 🟡 MODERATE — expect sell pressure as cliff dates approach
5.0x-10.0x = 🔴 HIGH — supply shock likely at unlock cliffs
10.0x+ = 🔴🔴 CRITICAL — token will almost certainly dump >80% unless demand is exponential (rare)
```

**Section B: Allocation & Vesting Pie Chart (Text + Numbers)**

Breakdown ALL initial allocations from docs + verified on-chain. If docs not available → infer from top holders (etherscan top 100 holders, tag addresses by known labels: Team, Treasury, VCs, Staking, LP, Community, Airdrop, Unknown).

Table format:

| Category | Tokens Allocated | % of Total | Vesting Pattern | Cliff Date | Tokens Unlocked / Remaining | Unlock Status |
|---|---|---|---|---|---|---|
| Team / Core Contributors | 150M | 15% | 2yr linear, 6mo cliff | 2025-06-15 | 0 / 150M | 🔴 100% LOCKED |
| Investors (Seed / Series A) | 200M | 20% | 3yr linear, 12mo cliff | 2026-02-01 | 0 / 200M | 🔴 100% LOCKED |
| Treasury | 100M | 10% | No vesting, team controls | — | 100M / 0 | 🟡 TEAM-CONTROLLED DUMP RISK |
| Liquidity (LP) | 50M | 5% | Permanent lock? → check LP lock contract | — | 50M locked for 2 years | 🟢 LP LOCKED |
| Community / Airdrop | 250M | 25% | TGE unlocked + 6mo vest | TGE | 250M fully unlocked | 🟢 NO RISK |
| Staking Rewards | 150M | 15% | 5yr emission schedule | Continuous | 12M / 138M | 🟡 MODERATE EMISSION |
| Eco-system / Grants | 100M | 10% | Controlled by multisig | — | 0 / 100M | 🟡 MULTISIG RISK |
| **TOTAL** | **1,000M** | **100%** | — | — | **412M / 588M (41.2% circulating)** | — |

Then compute:
```
Unlock Pressure Score (0-100): 72/100
→ This is HIGH. 58.8% of supply is still locked with multiple large cliff dates coming.
→ Next 90-day unlock: 2025-06-15 Team cliff = 150M = 23% of current supply entering market.
→ Expected supply expansion: +23% in one day. Historical pattern: -40% to -70% price crash unless sustained new demand.
```

**Section C: Smart Contract Rug Pull Risk Matrix**

Scan the verified contract source code OR for unverified, scan bytecode signatures + transaction patterns:

| Check | Status | Severity if FAIL |
|---|---|---|
| `mint()` function exists AND is callable by owner only | ✅ Owner only mint | 🟡 Warning if OWNER IS EOA not multisig |
| `mint()` is UNRESTRICTED (any wallet can mint) | 🔴 OPEN MINT FOUND | 🔴🔴 CRITICAL CERTAIN RUG — abandon project |
| `blacklist()` / `freeze()` function exists | 🔴 FOUND — owner can freeze any holder's funds | 🔴 CRITICAL (projects use this to "stop dumps" = rug) |
| Owner can upgrade proxy implementation | 🟡 Proxy upgradeable | 🟡 WARNING: Owner could change contract logic any time |
| Transfer tax >5% (or >10% sell only) | 🟡 6% buy / 10% sell tax | 🟡 MODERATE: Anti-whale mechanism but could be dev fee |
| LP tokens are NOT locked (check LP lock contract) | 🔴 LP NOT LOCKED — owner can pull LP at any time | 🔴🔴 CERTAIN RUG (honey pot pattern) |
| Max wallet limit exists <1% of supply | ✅ Anti-whale max 1% wallet | 🟢 Good (prevents accumulation attacks) |
| Top 10 holders = >40% of supply excluding burn | 🔴 Top 10 = 62% (3 team wallets = 45%) | 🔴 HIGH: coordinated dump possible |
| Owner can pause trading entirely | 🔴 pauseTrading() found | 🔴 CRITICAL: you may get trapped with untradeable tokens |
| Honeypot test (simulate buy + immediate sell via static call) | ✅ Sell succeeds with expected amount | 🔴🔴 CRITICAL if sell fails = 100% rug |
| Renounced ownership (owner = 0x0...dead) | ✅ Ownership renounced → NO rug possible | 🟢 SAFEST POSSIBLE STATE |

**Final Rug Risk Score (0-100)**:
```
Rug Pull Risk: 38/100
→ Risk Level: MODERATE
→ Reducing factors: LP locked, ownership partially renounced on mint, max wallet limit
→ Increasing factors: 6%/10% tax (unusual), proxy upgradeable, team holds 45% of supply in 3 wallets
→ Overall: NOT a guaranteed rug. But the 10% sell tax will destroy your PnL unless you hold >2 weeks.
```

**Section D: Sybil / Concentration Risk Assessment**

(for airdrop farmers / token purchasers):

- Scan top 1000 holders for clustering patterns (created same day, same funding source, similar nonce ranges, identical small token balances like exactly 99.9 tokens)
- Count: how many addresses appear to be sybil-controlled wallets vs genuine unique users
- Sybil score: 0-100, higher = more sybil concentration
- Interpretation table:
```
<10/100 → 🟢 Decentralized, real users
10-30 → 🟡 Moderate sybil (common in airdrops)
30-60 → 🔴 HIGH sybil: token distribution is fake; when team withdraws liquidity, it collapses
>60 → 🔴🔴 CERTAIN COLLAPSE: entire distribution is wash-traded sybils
```

Also identify if a single CEX hot wallet holds >10% (listing pump signal, CEX can dump anytime).

**Section E: Peer Comparison vs 50 Category Peers**

Take the top 50 tokens in the same category (e.g. "AI Agent tokens", "L2 tokens", "Memecoins on Solana", "DeFi DEX tokens") and produce percentile rankings:

| Metric | This Token | Median of 50 peers | Percentile Rank | Interpretation |
|---|---|---|---|---|
| FDV / MC Ratio | 6.67x | 3.2x | 88th percentile | 🔴 WORSE than 88% of peers — heavy unlock overhang |
| Team Allocation % | 15% | 12% | 68th percentile | 🟡 Slightly above median, not unusual |
| Circulating % | 41.2% | 62% | 22nd percentile | 🔴 WORSE than 78% — less circulating = more supply to dump |
| LP Lock Status | Locked 2yrs | 40% have NO lock | 90th percentile | 🟢 BETTER than 90% — strong LP safety |
| Rug Risk Score | 38/100 | 45/100 | 38th percentile | 🟢 BETTER than 62% — slightly safer than median project |
| Tax (buy/sell) | 6%/10% | 0%/0% (DeFi) | 98th percentile | 🔴 WORSE than 98% — unusual tax structure |

OVERALL PEER PERCENTILE: **48th percentile → MEDIAN PERFORMANCE vs peers. Nothing outstanding, nothing catastrophically bad.**

### Step 3: Output Format

ALWAYS output in this exact structure:

```markdown
# Tokenomics Decoder Report
**Contract**: `0xAbCd...Ef12`  **Chain**: Ethereum  **Explorer**: [etherscan.io/token/0x...](https://etherscan.io/token/0xAbCd...)
*Generated: 2026-08-12 | Price source: DexScreener spot $0.0024*

---

## 📋 Token Basics Summary
...[table A]...
**FDV/MC Ratio Interpretation**: [inline]

## 🧩 Allocation & Vesting
...[table B]...
**Unlock Pressure Score**: [X]/100 → [HIGH/MOD/LOW] + [90-day cliff summary]

## 🛡️ Rug Pull Risk Matrix
...[11 checks table C]...
**Final Rug Risk Score**: [X]/100 → [Level] + [2 sentence interpretation]

## 🎭 Sybil / Concentration Assessment
Top 10 holders hold [X]% of supply (excluding burn/dead addresses).
Clustered sybil wallets detected: [N] out of top 1000 → [Sybil Score XX/100]
**[Interpretation paragraph]**

## 🏆 Peer Comparison (vs 50 [category] tokens)
...[table E + overall percentile]...

---

## 🎯 Quick Decision Cheat Sheet
| Question | Answer |
|---|---|
| Can I daytrade this safely? | 🟢 Yes / 🟡 Tax >8% makes scalping hard / 🔴 Rug = NO |
| Safe to hold 30 days? | 🟢 No cliffs in 30d / 🟡 Cliff within 30d — caution / 🔴 Cliff next week = avoid |
| Airdrop farmer: hold or dump? | 🟢 Low sybil, strong peers → hold partial / 🟡 Mod sybil → dump 70% / 🔴 High sybil → dump ALL now |
| LP provider? | 🟢 LP locked 2yr+ → safe / 🔴 LP not locked → NEVER provide liquidity |

---

⚠️ NOT INVESTMENT ADVICE. This is an educational due-diligence tool only.
→ Always verify critical numbers DIRECTLY on the block explorer (links provided above).
→ Crypto tokens have extremely high failure rates (80%+ of projects go to zero). Never invest more than you can lose entirely.
→ Regulatory determination (security vs commodity) is not made by this tool.
```

### Step 4: Multi-Token Comparison

If user inputs 2+ addresses ("compare PEPE vs DOGE vs FLOKI tokenomics"), append a side-by-side table plus a "Tokenomics Quality Composite Score" (weighted: unlock pressure 30% + rug risk 30% + sybil 15% + peer percentile 15% + allocation fairness 10%).

## Output Constraints

- **Mandatory disclaimer footer** on every report. Never omit.
- Every critical data point must link BACK to the on-chain block explorer for user verification (this is trust-building AND CYA).
- Never use the word "buy" / "sell" / "hold" as a recommendation. Only output factual "rug risk X/100", "unlock pressure X/100". The Cheat Sheet column is a factual template from historical patterns, not a personalized recommendation.
- If allocation is undisclosed (no docs + holders unlabeled), write "⚠️ ALLOCATION NOT OFFICIALLY DISCLOSED. Numbers below are INFERRED from holder addresses and may be wrong."
- Honeypot test is mandatory: always attempt a static-call simulation of buy-then-sell. If it fails, flag 🔴🔴 CRITICAL.
- Rug Risk Score and Unlock Pressure Score must always give the 0-100 number AND a plain-English explanation.

## What This Skill Does NOT Do

- ❌ Does NOT execute trades (no wallet connectivity)
- ❌ Does NOT give personalized buy/sell recommendations based on user's portfolio or risk profile
- ❌ Does NOT check for legal/regulatory compliance of the token offering (Howey Test etc.)
- ❌ Does NOT predict future token prices
- ❌ Does NOT store contract states or build historical databases

## Pricing Logic

**$24/month = $288/year**

Price anchors against:
- Nansen Smart Money: recently dropped to $49/month from $999 (20x reduction = too many users left)
- Sonar Tracker Pro: $7.99/month (cheapest AI tool, but lite — doesn't do tokenomics reports)
- Messari Pro: $30/month minimum, enterprise "thousands/month"
- Token Terminal: requires enterprise quote for tokenomics data
- RugDoc / RugCheck: free, but only binary safe/unsafe, no 0-100 scoring or peer comparisons

$24 lands between the free rug checkers and the $30+ professional tools. The peer comparison feature is unique.

**User acquisition**: organic SEO landing pages targeting "[TOKEN NAME] tokenomics" (millions of monthly searches in bull markets) + TikTok/YouTube review snippets.

## Monetization Extensions (Roadmap)

| Tier | Price | Features |
|---|---|---|
| Basic | $24/mo | 100 reports/month, watchlist unlock alerts (50 tokens), all 5 report sections |
| Pro | $49/mo | 500 reports/month, 200-token watchlist, unlock alert webhooks (Telegram/Discord), CSV export, Solana/Sui/Aptos chains |
| Team | $149/mo | 5 team seats, 5000 reports/month, shared watchlists, priority email support |
| Project / Enterprise | $999/mo | White-label API, custom token universe (your project + competitors), investor reporting template |
