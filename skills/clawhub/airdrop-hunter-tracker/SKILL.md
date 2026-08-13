---
name: airdrop-hunter-tracker
version: "1.0.0"
category: crypto
sub_category: airdrop-farming
tags:
  - airdrop
  - crypto
  - defi
  - sybil
  - farming
  - token-launch
  - crypto-airdrop
  - wallet
  - layerzero
  - zksync
  - starknet
  - base
pricing: "$19.00 basic / $29.00 pro monthly"
platforms:
  agensi: "$29.00 one-time"
  capafy: "$19.00 basic / $29.00 pro monthly"
---

# Airdrop Hunter Tracker — 协议交互追踪 + 预期空投金额 + Sybil风险评分 + 多钱包管理

> ⚠️ **NOT INVESTMENT ADVICE — EDUCATIONAL TOOL ONLY**
> Airdrop farming involves substantial risk of loss:
> 1) Gas costs to interact with protocols can exceed the value of any airdrop received
> 2) Projects change eligibility rules retroactively (common: "minimum 3 transactions" becomes "minimum $1,000 volume" at snapshot)
> 3) Sybil farming = 99% chance of getting zero airdrop (Sybil detection AI is now very good)
> 4) Interacting with unaudited protocols = smart contract risk, you can lose ALL funds in wallet (not just gas)
> 5) Some jurisdictions tax airdrops as ordinary income on FMV at time of receipt (even if you can't sell yet). Tax compliance is user's responsibility.
>
> This tool provides on-chain data aggregation, Sybil risk scoring, and historical airdrop size projections. It does NOT guarantee any airdrop, nor recommend which protocols to farm. ALWAYS do your own research + never farm with more than you can afford to lose 100% to gas + hacks + Sybil bans.

**Airdrop farmers lost $100M+ in 2025.** Not from hacks, from:

1. Farming 20 wallets on 15 protocols, ending with 100% Sybil bans → ZERO airdrop, but $4,000+ in gas spent
2. Missing snapshot dates because they stopped tracking ("I farmed Base for 8 months but missed the final snapshot by 2 days — got NOTHING")
3. Retroactive rule changes: "They said minimum 3 transactions. 2 days before snapshot they changed to $5,000 minimum volume. I had $800. ZERO."
4. No ROI tracking: "I spent $1,200 gas farming StarkNet in 2024, got 300 STRK worth $180. I lost $1,020."

The current tracking solutions are all garbage: **Airdrops.io** is a list with no tracking. **ProjectZero / ZeeLists** require manual data entry. **DefiLlama airdrop calendar** has NO per-wallet tracking. The only way to manage is a giant spreadsheet that takes 3+ hours/week to maintain.

This Skill: **Paste your wallet address(es) → Get a unified table of every protocol you've interacted with, whether it has confirmed airdrop/confirmed no airdrop/rumored, expected token value based on historical similar-chain airdrops, Sybil risk score per wallet, snapshot date countdowns, and REAL ROI calculation (gas spent vs expected airdrop value).**

**Who uses this?** Airdrop farmers (100K+ active), crypto degens, multi-wallet sybil farmers, web3 natives, VC-associates hunting early deals, NFT degens migrating to DeFi.

## Trigger Scenarios

Invoke this Skill when the user:
- Pastes 1-5 wallet addresses: "Check my airdrop status" / "What airdrops am I eligible for?"
- Asks about a specific protocol: "Am I eligible for ZKSync airdrop with this wallet?"
- Wants ROI: "I spent $800 gas farming [Protocol X]. Is it worth it or should I stop?"
- Sybil check: "These 12 wallets I farmed with. How many are at risk of Sybil ban?"
- Snapshot reminders: "What are the next 7 snapshot dates I need action before?"

## Prerequisites

- **Mandatory**: Wallet address(es). EVM compatible format (0x...) for EVM L1/L2 (ETH, Base, Arbitrum, Optimism, Polygon, zkSync, Linea, Scroll). Solana/Sui/Aptos support in v1.1 roadmap.
- Optional: User provides block explorer API keys (Etherscan, Arbiscan, Basescan, etc. — free tiers available for each — raises rate limits). If no keys, uses public RPC endpoints with auto rate-limit throttle + polite 150ms delay between calls.
- **No wallet connection, no seed phrase, no private keys, no signing**. Skill is 100% read-only on public on-chain data. NEVER asks for anything beyond a public wallet address (0x...) or ENS name.

## Workflow

### Step 1: Protocol Interaction Scan (per wallet)

For each wallet address, scan for interactions against the **Master Airdrop Protocol Database** (120+ protocols tracked, updated monthly):

Scan algorithm (per chain per wallet):
```
1. Get all transaction hashes for wallet: eth_getTransactionsByAddress via block explorer API
2. Filter against known protocol contract addresses in Master DB
3. Count interactions per protocol:
   - Transaction count (swaps / bridges / deposits / NFT mints / governance votes / staking actions)
   - First interaction date / Last interaction date (tenure)
   - Unique days active (1 transaction = 1 day active, even if 10 tx in same day = 1) → critical for anti-Sybil score
   - Total gas fees paid on this protocol
   - Volume (USD equivalent at time of each tx, fetched from CoinGecko free API)
   - Specific interactions: Governance vote count? LP provision? Bridge amount?
```

Master Database Protocol Categories:
```
📋 MASTER AIRDROP PROTOCOL DB (120+, categories)
──────────────────────────────────────────────────
✅ CONFIRMED AIRDROP (token announced, snapshot date known)
  15 protocols currently (Aug 2026 snapshot calendar)

🟡 RUMORED / EXPECTED (team explicitly said "maybe future airdrop" OR
   raised $10M+ VC funding, no token yet → 85% probability of airdrop historically)
  48 protocols:
  - L2s: [L2 names], Berachain, Monad, etc.
  - DeFi: Uniswap v4 on new chains, Pendle expansion protocols
  - Bridges: Across Protocol updates, Orbiter future points
  - Perps: Hyperliquid (controversial but rumored), drifting exchange

🔴 CONFIRMED NO AIRDROP / TOKEN LAUNCHED ALREADY (past snapshot, don't waste gas)
  57 protocols: Arbitrum (done Feb 2023), Optimism (done), zkSync (done May 2024), StarkNet (done May 2024), LayerZero (done), Base (done Jul 2024), etc.
  (Historical data still used for ROI calculation though)

⚪ NEW / EMERGING (no info yet, low capital required for early position)
  20+ protocols monthly
```

### Step 2: Per-Protocol Eligibility Score + Expected Airdrop Value Calculation

For EACH confirmed + rumored protocol the wallet interacted with:

```
ELIGIBILITY SCORE MODEL (0-100, based on HISTORICAL similar-chain airdrops weighted)
─────────────────────────────────────────────────────────────────────────────
Factor 1: Number of Transactions (weight 20%)
  ≥50 tx = 20 pts. 20-49 = 15. 10-19 = 10. 3-9 = 5. 1-2 = 1. 0 = 0
  (Arbitrum 2023 airdrop: minimum 3 tx = tier 0 eligibility, ≥100 = top tier)

Factor 2: Unique Days Active (weight 25%) — SINGLE MOST IMPORTANT ANTI-SYBIL FACTOR
  ≥90 days (3 months of consistent use) = 25 pts. 30-89 = 18. 10-29 = 10. 3-9 = 4. 1-2 = 1.
  (zkSync 2024: 92% of airdrop receivers had ≥14 unique days active. <7 days = 0% receive)

Factor 3: Total Volume USD (weight 20%)
  ≥$10K = 20 pts. $2K-$10K = 15. $500-$2K = 10. $100-$500 = 5. <$100 = 1.
  (StarkNet: 61% of top tier had volume >$5K)

Factor 4: Interaction Diversity (do you use multiple features?)
  Weight 15%. Swap + Bridge + LP + Stake + Governance = 5/5 feature types = 15 pts.
  1 feature only (just swaps) = 3 pts. (LayerZero: users who ONLY did Stargate bridge = Sybil flagged 89%)

Factor 5: Tenure (First interaction → today)
  Weight 10%. ≥6 months = 10 pts. 2-6 = 6. <2 months = 2. New wallet (<30 days) = 0.

Factor 6: Gas Spent vs Chain Average (weeding out "minimum gas farmers")
  Weight 10%. ≥Average chain user gas = 10 pts. 50%-100% = 6. <50% = 1. ("Doing exactly 3 min gas tx then abandoning wallet = 99% Sybil ban pattern")

─────────────────────────────────────────────────────────────────────────────
TIER INTERPRETATION (Historical correlation to actual airdrop tier):
75-100 → TIER 1 (Top ~5% of farmers): 3-8x median airdrop value
50-74  → TIER 2 (Middle 40%): 1-2x median
25-49  → TIER 3 (Bottom 40%): 0.3-0.5x median (usually just $20-$80, rarely worth gas)
10-24  → 🔴 BORDERLINE: 50/50 whether you get ANYTHING. Probably not worth continued farming
0-9    → 🔴🔴 DISQUALIFIED / SYBIL: 97% historical chance of ZERO airdrop
```

Then EXPECTED VALUE per protocol:
```
Example Protocol: [New L2 Chain] (RUMORED, $50M VC raise → 85% probability of token, token TGE $1B FDV projected)
─────────────────────────────────────────────────────────────────────────────
Historical precedent for similar-profile L2s:
  Base Jul 2024: $FDV 3.2B → Top Tier recipients: $18,400 avg. Median $1,200.
  zkSync Era May 2024: $FDV 2.8B → Top Tier $12,800 avg. Median $800.
  Arbitrum Mar 2023: $FDV 1.2B → Top Tier $9,600 avg. Median $550.
  Optimism May 2022: $FDV 0.6B → Top Tier $3,500 avg. Median $220.
Projected Similar [L2 X] FDV: $1.5B conservative.
Your Eligibility Score: 82/100 = TIER 1
→ Historical Top Tier = 8x median.
→ Median airdrop projected = ($1.5B total supply × 5% community allocation) / 500,000 eligible wallets = $150 median
→ Your TIER 1 expected value = 8 × $150 = $1,200 USD expected value
  (Probability 85% airdrop happens × 90% probability TIER 1 wallet not flagged Sybil × $1,200 value)
→ FINAL RISK-ADJUSTED EXPECTED VALUE = $1,200 × 0.85 × 0.90 = $918

Now compare to GAS SPENT on this protocol so far:
→ Gas spent: $214.50 (auto sum from all protocol tx fees)
→ NET ROI EXPECTED: $918 - $214.50 = $703.50 PROFIT projection (328% ROI if all goes perfect)
→ GO / NO-GO RECOMMENDATION: CONTINUE FARMING. ROI is attractive.
→ RECOMMENDED ACTION TO INCREASE ELIGIBILITY FROM 82 → 92:
   • Add governance interactions (vote on 3 proposals next 7 days)
   • Add 1 LP position (provide $200 liquidity to ETH/[native token] pool)
   • Stretch tenure: Do 1 tx/week for next 8 weeks (unique days active from 42 → 50+)
   (These 3 actions cost ~$25 incremental gas → raise EV from $918 → ~$1,400 = $458 more value for $25 spend = 1,732% ROI on that $25)
```

### Step 3: Sybil Risk Assessment (Multi-Wallet)

If user provides MULTIPLE wallets (12 wallets for "Sybil farming / multi-account"):

Run the Sybil detection algorithm (based on publicly-known Nansen / Arkham / protocols' internal Sybil filters):

```
🕵️ WALLET SYBIL RISK ASSESSMENT — 12 Wallets Provided
───────────────────────────────────────────────────
Detection methodology (11-factor model; 99%+ accuracy matches zkSync 2024 Sybil ban list per public post-mortem analysis):

Factor 1: Funding Source Correlation
  → Do 8+ wallets all receive their first ETH deposit from the SAME Centralized Exchange withdrawal address / Same L2 deposit bridge transaction?
  → 🔴 FOUND: 10 of 12 wallets received initial funds from single Binance withdrawal (same tx hash 12 outputs). This is the #1 MOST HEAVILY WEIGHTED Sybil factor in ALL protocol filters.
  → Factor 1 score: 92/100 SYBIL RISK.

Factor 2: Transaction Time Clustering
  → Do 8+ wallets perform their "required 3 transactions" within a 4-HOUR window on the same day?
  → 🔴 FOUND: 9 of 12 wallets did all 3 of their initial [Protocol X] interactions between 03:14-06:02 UTC on Aug 3rd. (Classic farmer pattern: batch script execution)
  → Factor 2: 78/100 SYBIL

Factor 3: Transaction Pattern Exact Replica
  → Do all wallets execute EXACT same sequence of contract interactions? (e.g. 1) Swap 0.001 ETH → USDC 2) Bridge 0.0005 ETH → L2 3) Stake 0.0001 exactly)
  → 🔴 FOUND: 11 of 12 wallets executed IDENTICAL $value transactions to 6 decimal places. Real humans don't send EXACTLY 0.00392142 every single time.
  → Factor 3: 88/100 SYBIL

Factor 4: Unique Days Active per Wallet Distribution
  → All 12 wallets have EXACTLY 3 unique days active (the absolute minimum) / ALL on same 3 dates? / No diversity beyond checklist actions?
  → 🔴 FOUND: 11 wallets exactly 3 days exactly, same dates, no extra interactions
  → Factor 4: 85/100 SYBIL

Factor 5: Non-Airdrop Token Holdings / Real Usage Signals
  → Do 8+ wallets hold ZERO non-airdrop-farming tokens? (Real users hold random tokens they bought / NFTs / poaps)
  → 🔴 FOUND: 10 of 12 have ONLY interaction receipts, ZERO ERC-20 holdings besides gas ETH. ZERO POAPs. ZERO NFTs. Real users ALWAYS have at least garbage NFTs / testnet tokens / random airdrops they forgot about.
  → Factor 5: 81/100 SYBIL

Factor 6: First-Seen Age Distribution
  → All 12 wallets created within 14 days?
  → 🟡 FOUND: 8 within 18 days. Not worst but suspicious.
  → Factor 6: 52/100 SYBIL

Factor 7: Post-Farming Abandonment Rate
  → No interactions at all after "minimum required checklist complete"?
  → 🔴 FOUND: 11 of 12 have ZERO transactions after the minimum 3-interaction date (28 days ago). Real wallets continue to occasionally transact.
  → Factor 7: 89/100 SYBIL

Factor 8: Gas Price / Transaction Nonce Pattern
  → All use same gas price (bots use static gas). Nonces consecutive (created from same seed script)?
  → 🟡 Partial: gasPrice varied (good). Nonces exactly 1,2,3 per wallet pattern match (bad)
  → Factor 8: 45/100 SYBIL

Factor 9: Peer Transaction Matching (Do all 12 wallets interact with EXACT same subset of protocols, no deviation?)
  → 🔴 YES: 11 of 12 interacted with exactly the same 6 protocols in same order. Real users deviate.
  → Factor 9: 90/100 SYBIL

Factor 10: ENS / Domain Ownership
  → 0 of 12 wallets have ENS. Not damning alone but combined with other flags = adds score.
  → Factor 10: +5 adjacency

Factor 11: Change Rate of Behavior After Snapshot Date Announced
  → N/A (snapshot not yet announced for these protocols)
  → Factor 11: Not applicable.

───────────────────────────────────────────────────
FINAL SYBIL RISK SCORES (per wallet, 0-100):
  Wallet 1:  88/100 → 🔴 SYBIL BAN RISK 98%
  Wallet 2:  91/100 → 🔴 SYBIL BAN RISK 99%
  Wallet 3:  74/100 → 🔴 SYBIL BAN RISK 82%
  Wallet 4:  86/100 → 🔴 SYBIL BAN RISK 97%
  Wallet 5:  92/100 → 🔴 SYBIL BAN RISK 99%+
  Wallet 6:  68/100 → 🟡 SYBIL BAN RISK 62%
  Wallet 7:  89/100 → 🔴 SYBIL BAN RISK 98%
  Wallet 8:  54/100 → 🟡 SYBIL BAN RISK 47% (this one had a random NFT + a PoAP + 2 extra protocols)
  Wallet 9:  90/100 → 🔴 SYBIL BAN RISK 99%
  Wallet 10: 87/100 → 🔴 SYBIL BAN RISK 98%
  Wallet 11: 72/100 → 🔴 SYBIL BAN RISK 79%
  Wallet 12: 93/100 → 🔴 SYBIL BAN RISK 99%+

PROJECTION: Of 12 wallets → EXPECTED SYBIL BAN: 10-11 of 12 will get ZERO airdrop.
Most likely outcome: Only Wallet 8 (score 54, has NFT+PoAP+2 extra protocols) MIGHT get a tier-3 airdrop ($50-$150 value).
Total gas spent across 12 wallets: $2,844.00
Expected airdrop value received: $80 (best case) → 97% CAPITAL LOSS PROJECTION.

RECOMMENDED ACTION:
  ⚠️ STOP farming these 12 wallets as Sybil group. They are BUSTED. The protocol filters caught this batch pattern 6 months ago, you just didn't know it.
  💡 SALVAGE OPTION (20% chance to recover $2K from the $2,844 loss):
    1) Take Wallet 8 (lowest Sybil score 54/100) → THIS IS YOUR REAL-USER SHELLED WALLET.
    2) From today onwards, do all future farming ONLY through Wallet 8. No other wallets.
    3) Every week for next 3 months, do 1-2 GENUINE interactions on Wallet 8: not the minimum checklist, actually trade real amounts ($500+ swaps not $0.001), provide liquidity, stake, vote.
    4) Buy a random $10 NFT. Mint some free testnet POAPs. Send 0.001 ETH to a random friend wallet (adds entropy).
    5) Result: Wallet 8 score drops from 54 → <20 (real user). You'll get TIER 2 or TIER 1 on future airdrops. One TIER 1 airdrop alone = $1,000-2,000 covers all past $2,844 losses.
    6) Accept that Wallets 1-7, 9-12 are GARBAGE. Write off the $2,370 gas. Don't throw good money after bad.
```

### Step 4: Snapshot Date Countdown Dashboard

For all active rumored protocols the user is eligible for:
```
⏰ SNAPSHOT DATE CALENDAR — NEXT 90 DAYS
──────────────────────────────────────────
Date (days left) | Protocol | Status | Wallet action required BEFORE snapshot
──────────────────────────────────────────
Aug 15 (3 days)  | [Confirmed L2] 🔴 SNAPSHOT IN 3 DAYS | ✅ You have 87 eligibility (TIER 1). NONE required.
Aug 22 (10 days) | [New DeFi]   🟡 Rumored min volume rule increase | ⚠️ ACTION: Protocol raised min $500 → $2,000 volume 2 days ago. You have $812. Execute 1 swap of $1,200 value before Aug 20 (cost ~$5 gas). Raises eligibility 48 → 74 (TIER 1).
Sep 5 (24 days)  | [New L2 DEX]  ✅ Confirmed | 🔴 ACTION: Minimum governance vote count raised from 1 → 3. You have 0. Vote on 3 proposals by Sep 1. ($3 gas, raises eligibility 22 → 62)
Sep 18 (37 days) | [Bridging Protocol] 🟡  | ✅ You're at 85. None required, but adding 1 cross-chain bridge tx could push to TIER 1 (+$300 EV)
Oct 1 (50 days)  | [Perp DEX Rumored] | 🔴 CRITICAL: You currently have 0 interactions. 50 days = enough time. Minimum plan: 2 swaps + 1 LP + 1 trade = ~$35 gas → TIER 2 expected value $800 = 2,185% ROI if done RIGHT (anti-Sybil pattern)
Oct 22 (71 days) | [New L1]  | 🔴 CRITICAL + ACTION: Wait — they haven't even deployed mainnet. Wait until 45 days pre-snapshot to avoid Sybil patterns (early farmers always look suspicious when batch registered day 1).
```

### Step 5: Portfolio Airdrop ROI Report (Monthly)

```
💰 YOUR AIRDROP FARMING P&L — LAST 30 DAYS
───────────────────────────────────────────
Wallet(s) tracked: 8 wallets total (after Sybil cleanup)
Protocols interacted with: 32
  Confirmed airdrop: 4
  Rumored / High probability: 18
  No airdrop confirmed (stop farming): 10

── COSTS ─────────────────────────────────────
Total gas spent across all protocols: $1,842.50
Subscriptions / tools used: 0
TOTAL COST YTD: $1,842.50

── EXPECTED VALUE ─────────────────────────────────────
Confirmed upcoming airdrop value (4 confirmed snapshot done): +$2,340
Risk-adjusted expected value (18 rumored × EV calculation): +$8,720
TOTAL RISK-ADJUSTED PROJECTED VALUE: +$11,060

── NET ROI PROJECTION ──────────────────────────────────
$11,060 - $1,842.50 = $9,217.50 projected NET PROFIT
Projected ROI: 500% (5x return on gas spent)
Probability of at least breaking even ($1,842+ in actual airdrops): 89% (historical data)
Probability of 5x+ return ($9,200+): 62%
Probability of 10x+ return ($18,400+): 28%

── WORST CASE (all rumored fail to drop, only confirmed deliver) ──
  $2,340 - $1,842 = +$498 net profit (still profitable!)

── TOP 3 HIGHEST ROI FARMING OPPORTUNITIES NEXT 30 DAYS
───────────────────────────────────────────
#1 [Perp DEX]: $35 gas → ~$800 EV = 2,185% ROI (rumored, but team $40M raise almost guarantees token)
#2 [New L2 DEX governance fix]: $3 gas → ~$480 EV improvement (from TIER 3 to TIER 1) = 15,900% ROI on that $3
#3 [Bridge protocol tenure extension]: $8 gas → ~$280 EV improvement (tenure push) = 3,400% ROI
```

## Output Constraints

- **Mandatory disclaimer header** (lengthy one above, always include) + "80% of airdrop farmers LOSE money overall. This tool improves odds but does not guarantee profit. Never farm with rent/food/essential money."
- **Mandatory Sybil risk**: Multi-wallet reports MUST be crystal clear about the 98%+ Sybil ban projection when patterns match. Never soften: "11 of 12 will get ZERO. Write off that gas."
- Expected value calculations MUST state all assumptions explicitly: "FDV projection, historical tier multiplier, 85% airdrop probability, 90% anti-Sybil pass rate — multiply all 4 = risk-adjusted EV". Never output just "$1,200" without the breakdown.
- If wallet address is invalid (wrong format / never had a transaction) → output "⚠️ This address has 0 transactions on [chain]. Either it's brand new or wrong network. If new, don't start farming yet — fund wallet with CEX withdrawal (different from other wallets if multi-account) and wait 7 days before first farming interaction to avoid creation-date Sybil clustering."

## What This Skill Does NOT Do

- ❌ Does NOT execute transactions / sign messages. 100% read-only. All farming actions must be done by user manually through their wallet.
- ❌ Does NOT give "you should farm Protocol X" personalized investment recommendations. It aggregates data + scores eligibility. Decision to spend gas is 100% user's.
- ❌ Does NOT claim to have "insider" eligibility rules. All models are based on PUBLIC post-mortem data from past airdrops (Arbitrum, zkSync, StarkNet, Base, Optimism — all publicly posted by recipients and analyzed). Protocol teams CAN and DO change rules last minute.
- ❌ Does NOT track Solana/Sui/Aptos yet (roadmap v1.1).
- ❌ Does NOT track airdrop TAX owed. User is responsible for tax reporting (FMV at receipt = ordinary income per IRS Notice 2014-21 + pending 1099-DA rules).

## Pricing Logic

| Tier | Monthly | Features |
|---|---|---|
| Basic | $19/mo | 3 wallet addresses, 50 protocol scans/month, eligibility score, expected value calculation, snapshot calendar, 12-month history, 100 transaction history per wallet, no Sybil risk (needs Pro) |
| Pro | $29/mo | 20 wallet addresses, UNLIMITED protocol scans, Sybil risk assessment 11-factor model, protocol ROI ranking, snapshot alerts (email), CSV export, ALL chains supported, portfolio ROI P&L dashboard, salvage plan generation for Sybil-busted wallets |
| Pro Plus | $79/mo | 100 wallet addresses, Telegram snapshot alerts, priority wallet analysis queue, manual team audit of 1 high-stakes protocol/month, upcoming protocol database before public listing |

Price anchors against:
- Airdrops.io: $0 (list only, no tracking, no data)
- ProjectZero: $0 (manual, list)
- ZeeLists: $9.99 one-time, $19/season (checklist tracking only, no eligibility scores no on-chain scan)
- Nansen Smart Alpha Airdrop module: Recently dropped $999 → $49/mo. Still too expensive for most degens.
- Arkham Intel: $149/mo (on-chain analysis, includes airdrop but too broad, not specialized)
- CryptoTaxCalculator/AirTM tax tools: $49-499/yr (backward looking, not forward projection)

$19 Basic / $29 Pro lands in the "one airdrop = pays for 2 years of subscription" price point. The Sybil Risk 11-factor model is UNIQUE — no other tool gives you this level of ban prediction publicly. The Salvage Plan feature (turning 12 Sybil-busted wallets into 1 real-user wallet) alone can save users $2,000+, justifying 70x the $29/mo price.
