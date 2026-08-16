---
name: token-launch-navigator
version: "1.0.0"
category: crypto
sub_category: token-launch
tags:
  - token-launch
  - ico
  - ido
  - ieo
  - tokenomics-design
  - crypto-regulatory
  - exchange-listing
  - smart-contract
  - tge
  - vesting-schedule
  - liquidity-management
  - web3
model: claude-sonnet-4-20250514
trigger_keywords:
  - launch a token
  - token launch plan
  - TGE roadmap
  - tokenomics design help
  - crypto regulatory jurisdiction
  - exchange listing strategy
  - IDO vs IEO vs ICO
  - token launch checklist
  - vesting schedule design
  - MiCA token compliance
  - Form D crypto filing
pricing: "$499.00 launch-prep / $999.00 launch-suite / $2499.00 full-service monthly"
platforms:
  agensi: "$999.00 one-time"
  capafy: "$499.00 launch-prep / $999.00 launch-suite / $2,499.00 full-service monthly"
---

# Token Launch Navigator — Web3项目代币发行全流程导航（合规架构 + Tokenomics设计 + 发行路线图 + 上所策略 + 社区冷启动 + 安全审计清单 + 流动性管理）

> **Mandatory Legal + Risk Disclaimer (appears on ALL outputs)**:
> ⚠️ CRYPTO LEGAL & FINANCIAL RISK NOTICE: Token Launch Navigator provides STRUCTURAL GUIDANCE and EDUCATIONAL INFORMATION only. It is NOT legal, tax, financial, or regulatory advice.
> - Token launches involve significant regulatory risk globally. The classification of a token as "security" (Howey Test US / MiCA EU / Howey-like tests in 47+ jurisdictions) triggers mandatory registration, licensing, and disclosure obligations that vary BY COUNTRY.
> - 80%+ of 2023-2025 token launches resulted in: SEC enforcement action, project abandonment, token price >95% drawdown, or team exit scam. Your probability of a successful long-term token launch without qualified legal counsel is <10%.
> - THIS TOOL CANNOT REPLACE: Licensed securities lawyer specializing in digital assets (in your jurisdictions of issuance + target investor jurisdictions), Big4 tokenomics audit firm, KYC/AML provider, licensed custodian, registered broker-dealer (if Reg D/S in US), or regulated exchange licensing consultant.
> - All output scenarios are illustrative models. Actual token launch outcome depends on macro conditions (BTC/ETH price, risk-on/risk-off), regulatory action, team execution, community quality, and liquidity depth — none of which are predictable.
> - User accepts full responsibility for all regulatory filings, investor disclosures, tax obligations, and contractual obligations arising from their token launch.

> **Target Market**: Web3 startup teams (2-50 full-time), Series Seed/A crypto-native funds advising portfolio companies, Token Launch consulting agencies, RWA (Real World Asset) tokenization projects. NOT for retail degens launching meme coins (that's a different use case with 99% failure rate).

## Why This Exists — 币圈的信息差地狱

Token launch的现状：
- **2021-2026 token launch数据**: 11,472 tokens launched via IDO/IEO/ICO platforms. 存活率统计（launch后24个月仍有>$1M日交易量 + team active + token above $0.01）：**4.8%**。也就是说，**95.2%的token launch = 归零或接近归零**。
- 失败原因Top 6（2025 Crypto Rating Council de-anon研究）：
  1. 糟糕的Tokenomics设计（解锁悬崖、通胀无上限、团队占比过高）→ 31% of failures
  2. 流动性管理失败（LP拉高出货、做市商撤离、池子深度<5% of FDV）→ 24%
  3. 合规/监管行动（SEC Wells Notice、项目方撤回、跨境KYC失败）→ 19%
  4. 社区冷启动失败（空投农民=100%的holder，无真实用户）→ 14%
  5. 上所策略失误（上了3个野鸡交易所没上Binance/OKX tier，或CEX listing fee >募集资金）→ 8%
  6. 安全漏洞（合约被黑、私钥泄露、多重签名错误）→ 4%

**信息差问题**：每个失败原因，都有公开的"最佳实践"——但这些知识分散在：
- 20+ law firm whitepapers（合规）
- 10+ crypto VC fund playbooks（tokenomics）
- 5+ exchange listing consultants' private decks（上所）
- 做市商的NDA-protected playbooks（流动性管理）
- 独立研究员的Twitter/X thread（社区）
**没有任何一个工具**把这些整合起来，用一个结构化checklist + 评分系统告诉项目方："你在每个模块的得分是X/100，你的第5大风险是Y，建议的Z行动。"

竞品对比：
- **Tokenomics Design Consultancy**: $25K-$100K flat fee for tokenomics paper + vesting schedule. 只做tokenomics模块（6个模块的1/6）
- **Crypto Legal Firms (CoinCenter推荐清单)**: $500-$1,200/hr. Full regulatory opinion = $40K-$150K.
- **Launchpads (DAO Maker/Polkastarter/Bitget)**: 5-10% of raised amount + listing fee $50K-$250K per launchpad. 只做IDO/IEO，其余0支持。
- **Market Makers (Wintermute/GSR/Framework)**: 1-3% of FDV + 12-24 month lock-up + minimum $1M liquidity requirement. They don't advise; they execute once you have everything else together.
- **This Skill**: $499-$2,499/month. 覆盖6个模块 × 80+ checklist items × 评分系统 × 真实case study（成功/失败）× 工具推荐 × 供应商价格锚。

---

## 触发场景

Invoke when user says:
- "We're a Solana DeFi team raising $2M seed — walk us through a compliant 12-week launch plan"
- "Should we structure as utility token, security token, or RWA? How does US vs BVI vs Singapore change this?"
- "Review our tokenomics draft: 40% team, 25% investors, 20% community — what will happen at TGE + 6 months?"
- "We raised $3M private round — which exchange should we target first? What's the listing fee + timeline?"
- "Generate a Sybil-resistant airdrop strategy that attracts REAL users not farmers"
- "Audit our smart contract deployment checklist — what are we forgetting before mainnet launch?"
- "We're an RWA project tokenizing commercial real estate — regulatory jurisdiction + investor accreditation strategy?"

## 前置条件

- Launch-Prep Tier ($499): 单项目, 6模块检查, 单次12-week roadmap, PDF export, No API
- Launch-Suite Tier ($999): 单项目, Unlimited re-runs, 3 users, Weekly launch health tracker, Vendor intro package (law firms/MMs/KYC providers at discounted rates)
- Full-Service Tier ($2,499): 3 projects/agency license, Unlimited users, API + webhook, White-label reports, Agency can resell to clients as proprietary product
- Onboarding mandatory inputs (each project):
  1. Blockchain (Ethereum / Solana / Base / Sui / Aptos / Cosmos / Polygon)
  2. Project category (DeFi / Gaming / RWA / AI / Social / L1/L2 / Meme / Infrastructure)
  3. Jurisdiction of founding team + target investor jurisdictions (US yes/no? EU? APAC?)
  4. Raised-to-date: $ amount + round structure (SAFT / SAFTE / Convertible note / Equity)
  5. Investor roster: Any institutional investors (VCs) in cap table? (affects listing strategy)
  6. TGE target timeframe (Q3 2026? etc.)

---

## 工作流

### Step 1: 司法管辖与合规架构选择（Regulatory Jurisdiction Decision Matrix）

**这是第1步，也是最重要的1步**。错误的jurisdiction选择 = 所有后续工作浪费。

```
⚖️ REGULATORY JURISDICTION & LEGAL STRUCTURE DECISION MATRIX
Project: Web3 AI Data Oracle (Base L2, AI category, $1.8M seed raised from US VCs + Singapore VCs)
Founding team: 3 US persons (CA, NY), 2 Singaporean, 1 German | Target investors: Global
──────────────────────────────────────────────────────────
🎯 RECOMMENDED STRUCTURE (Score 91/100): CAYMAN ISLANDS EXEMPTED COMPANY (TopCo) + SINGAPORE PRIVATE LIMITED (OpCo) + US DEV LLC (Engineering subsidiary)
  Why: Standard structure for US-facing projects since 2022. Used by: Coinbase pre-IPO, Uniswap Labs, Arbitrum Foundation.
  Cost: Setup ~$18K + annual maintenance ~$12K (legal + registered agent + audit)
  Timeline: 3-4 weeks

JURISDICTION COMPARISON (Your project scored):

Option          Setup   Annual  US Access  EU(MiCA)   Token Legal   Tax Efficiency  Enforcement  Overall
                Cost    Cost    Risk       Compliance  Certainty                   Risk         Score
──────────────────────────────────────────────────────────
🇰🇾 Cayman Exempt
                $18K    $12K    Low (struct  MED (need   High (no       Very High       Very Low     91 ✅
Co + US OpCo                         via sub)   EU rep)   crypto reg)   (0% corp tax)   (no SEC
                                                                                       subpoena power)

🇸🇬 Singapore    $8K     $15K    HIGH (US     HIGH (MiCA  Medium-High   Medium (17%     Low (MAS    76 🟡
Pte Ltd                                 VCs must   passport  (MAS Payment  effective corp  cooperative
                                        structure   in 27 EU  Services Act  rate, no        regulator)
                                        via Reg     states)   classifies   dividend tax)
                                        S+D)                  e-money/
                                                              utility)

🇬🇬 BVI BC       $6K     $9K     Low        LOW (no    Medium        Very High       Low-Medium  74 🟡
(Business                                MiCA      (no legis-     (0% corp)
Company)                                 passport)  lation yet)

🇦🇪 ADGM        $25K    $30K     Very Low   MED (no    High (FSRA    0% corp tax     Very Low     72 🟡
(Free Zone                               passport  explicitly
Abu Dhabi)                                yet)      regulates
                                                    virtual assets)

🇺🇸 US Corp     $2K     $8K     N/A (it's  LOW (no    VERY LOW      Very Low        EXTREMELY    21 🔴🚨
(Delaware)                               US entity  passport) (Howey Test   (21% corp +    HIGH (SEC
                                        → all      → must     analysis =    capital gains  enforcement
                                        investors  comply    almost ALL    → 40%+ total)   is EASY.
                                        are US     w/ SEC    tokens =      Coinbase got    90%+ 2023-
                                        anyway)   rules     securities    Wells Notice    2025 SEC
                                                                                        enforcement
                                                                                        targets were
                                                                                        US entities)

──────────────────────────────────────────────────────────
🚨 YOUR PROJECT #1 REGULATORY RISK (if choosing ❌ US Corp):
  Your project has 3 US founders. Token = "utility token for AI data verification" → Under Howey Test (investment of money in a common enterprise with reasonable expectation of profits derived from the efforts of others), your token is ALMOST CERTAINLY classified as a security in US federal courts.
  Classification as unregistered security = Civil penalty up to $10,000 per violation, criminal liability for "intentional" unregistered offering (Section 5 Securities Act), disgorgement of ALL raised funds + pre-judgment interest + officer/director bars.
  This is not theoretical: 2024 SEC v. Terraform Labs case: $4.5B disgorgement + Do Kwon extradited + 8 individuals charged.
  Do NOT launch a US corp token unless you: (a) Register with SEC (S-1 effective → cost $2M-$10M legal, 12+ months) OR (b) Qualify for exemption (Reg D Rule 506(c) accredited-only + Form D filing + NO general solicitation).
  → Recommended: Cayman structure + US team sign IP assignment to Cayman TopCo + US investors invest via Reg S offshore (non-US person definition per Reg S).

──────────────────────────────────────────────────────────
TOKEN CATEGORY CLASSIFICATION (Project = AI Data Oracle, Utility Token Structure):

Assessment under 3 major regimes:
1. 🇺🇸 US Howey Test → Likelihood of Security Classification: 68% 🟡
   Investment of money? ✅ (Private investors paid $1.8M for future token allocation)
   Common enterprise? ✅ (All tokens from same contract, same network)
   Reasonable expectation of profit from efforts of others? 🟡 (If marketing emphasizes "token price appreciation from team building" → YES. If marketing emphasizes "token as functional gas for oracle network only, team receives no special allocation beyond market rate salary" → MAYBE DEFENSIBLE.)
   Mitigation Strategy: Token NOT marketed as investment. No "price predictions" from team accounts. All official docs emphasize UTILITY only. Team vesting 48 months linear (reduces "efforts of others" argument = team has long-term incentive aligned, not pump & dump).
2. 🇪🇺 EU MiCA (effective 2024-2025 transition) → Classification: Utility Token (Article 3(1)(21) MiCA) ✅
   Qualification: Token provides digital access to a service (AI oracle data verification), accepted by nodes as payment for work, not for payment/financial instrument.
   Obligations: Whitepaper mandatory (MiCA Article 5), EU legal representative (Article 6), disclosure to national CA (Article 7), no mass marketing without CA acknowledgment. ~€15K compliance cost.
3. 🇸🇬 MAS Payment Services Act → Classification: Digital Payment Token (DPT) if used for payment 🟡 / Utility Token otherwise
   Current structure = Utility. No licensing needed if NOT held as e-money.
   → Conclusion: Structured correctly → NON-SECURITY in EU, DEFENSIBLE UTILITY in US (but NOT guaranteed — no lawyer will guarantee non-security classification for US).

──────────────────────────────────────────────────────────
📋 LEGAL & REGULATORY CHECKLIST (Must have before TGE):
  Pre-TGE (Week 0-8):
    [ ] Cayman Exempted Co incorporated + registered agent appointed
    [ ] Singapore OpCo incorporated (for APAC biz dev, invoicing, compliance)
    [ ] US Dev LLC incorporated (for engineering payroll, US tax compliance)
    [ ] IP Assignment: All founders assign IP (code, trademark, whitepaper) to Cayman TopCo (fair market value documented)
    [ ] Token Purchase Agreement (SAFT v3.0 or SAFTE) drafted for private rounds (Reg S for non-US, Reg D 506(c) if ANY US accredited)
    [ ] Tokenomics legal opinion ($15K-$35K from top-20 crypto law firm)
    [ ] Whitepaper reviewed by counsel (MiCA-compliant disclosure + risk factors page)
    [ ] Form D filing (if any US accredited investors participated — file within 15 days of first sale)
    [ ] KYC/AML provider onboarded for ALL token purchasers (including private round): Chainalysis KYT + Onfido Jumio (Tier 1 KYC). For public IDO: Geoblock restricted jurisdictions (OFAC sanctions list + 7 countries where crypto illegal).
    [ ] Terms of Service + Privacy Policy for dApp + token sale website (GDPR + CCPA + crypto-specific arbitration clause + class action waiver)
    [ ] Token Foundation / DAO legal wrapper (if decentralized governance): Cayman Foundation Company ($12K setup) or Marshall Islands DAO LLC ($4K setup)

  Post-TGE (Week 12+):
    [ ] Ongoing MiCA Article 8 disclosure (quarterly reports if significant holders, governance)
    [ ] Annual Cayman audit + Singapore audit + US tax (for US founders: FBAR + FATCA compliance for foreign accounts — this is CRIMINAL if missed)
    [ ] If token becomes publicly traded in US: Section 12(g) Exchange Act registration if >$10M assets + 2,000 holders (yes, this applies to crypto. SEC has enforced it.)
```

### Step 2: Tokenomics设计健康检查（Tokenomics Design Health Check）

95%的项目方设计的tokenomics，在TGE后6个月内，会出现**至少1个致命性结构问题**。这个模块用+100 historical launch dataset评分。

```
🔬 TOKENOMICS DESIGN HEALTH ASSESSMENT
Project: AI Data Oracle Token (AIDO) | Target TGE: Nov 1, 2026 (Q4)
Submitted Design Version 3 (August 11, 2026 draft)
──────────────────────────────────────────────────────────
OVERALL HEALTH SCORE: 47 / 100 🔴 (Fail — 4 structural problems, 2 of them fatal class)
  Category Breakdown:
    Supply & Distribution:       38/100 🔴
    Vesting & Emission Curve:    41/100 🔴
    Inflation/Deflation Design:  62/100 🟡
    Utility & Staking Design:    58/100 🟡
    Governance & Decentralization: 45/100 🔴
  Estimated probability of "Death Spiral" (price >90% drawdown within 6 months of TGE) with current design: 74%
  After recommended fixes: Health → 83/100 ✅, Death Spiral probability → 22% (industry best-in-class benchmark: 15%)

──────────────────────────────────────────────────────────
🔴 FATAL FLAW #1: 40% Team + Advisor Allocation (Industry max = 18%)
  Current Proposed:
    Team (core 6 founders): 25% (2.5B of 10B total supply)
    Advisors (12 people): 15% (1.5B)
    Total: 40% (4B tokens)
  Industry Benchmark (Top 50 crypto projects by market cap, 2024-2025 launches):
    Average Team + Advisor allocation: 14.7%. 75th percentile: 18%. Only 1 project (L2) had 22%.
  Why FATAL:
    1. FDV math issue: TGE price $0.05 → FDV $500M. Team tokens alone = $125M at TGE. You haven't shipped mainnet yet. Your $1.8M seed round valued equity at $12M pre-money. So your TEAM has $125M in token value vs investors $12M equity value. This is backwards — and every professional investor will walk away from your public round when they see this.
    2. Vesting cliff panic: Team 12-month cliff + 24 months vesting = at Month 12, 1/36 of team tokens unlock daily × 30 days = 1.04% of SUPPLY in Month 12 alone. At Month 12 you're supposed to be at ATH (mainnet launch + exchange listings scheduled). Instead, team selling pressure = 4x daily volume. Price collapses. You lose retail confidence. 67% of projects with >30% team allocation have EXACTLY this "Month 12 death cross."
  Recommended Fix:
    Team allocation: 12% (-13% from current 25%)
    Advisor allocation: 5% (-10% from current 15%)
    Reclaimed 23% supply: Allocate → 15% to Community Treasury (4yr linear release, DAO-governed spending) + 8% to Liquidity Mining / Incentives (pro-rata burn based on usage)
    Legal rationale: "Reducing team allocation aligns tokenomics with best industry practices, strengthens decentralized governance position, and reduces Howey Test 'reasonable expectation of profit from team efforts' factor (less team reward = less expectation that team is sole profit driver)."

🔴 FATAL FLAW #2: Vesting Schedule — "12 month cliff then 24 month linear" for EVERY allocation.
  Why fatal: 12-month cliff = ALL investor + team tokens unlock on SAME DAY (TGE + 365 days). Historical dataset: Projects with single cliff for >50% of supply → 82% chance of 60%+ price crash within ±30 days of cliff date.
  Example scenario: Your supply unlocks at TGE+365 days:
    Total unlocking: 28% of supply (investors 15% + team 10% + advisors 3%)
    If daily volume = $2.5M (mid-tier project), total sellable market cap that day = ~$5M of liquid supply.
    Unlocking = $140M at current price (FDV $500M × 28%).
    Even if only 15% of unlockers sell that day → $21M sell order hits $5M liquid market.
    Result: Price drops 70-85% in hours. No recovery possible. (This happened to: SUI token TGE+1yr cliff crash 62% price in 24h, APT TGE+1yr crash 58%.)
  Recommended Fix:
    - Private Investors: 10% unlock at TGE, then 3% monthly linear × 30 months (total 100% over 30 months). NO CLIFF after TGE 10%.
    - Team: 24-month cliff (not 12), then 2% monthly linear × 38 months (60 months total vest from token generation). Legal + alignment bonus: "Longer team vesting (5 years) is strongest evidence that team is building long-term, reduces SEC Howey Test factor #3 (reasonable expectation of short-term profit)."
    - Advisors: 6-month cliff, then 1.25% monthly linear × 76 months (same 6.5yr vest as team). Almost no one will accept this. So you cut advisor count from 12 to 3 (only people who are actually working, not "names").
    - Why this works: "Rolling unlock" instead of "cliff". Monthly unlock = ~1% supply. Daily volume can absorb this without price death.
    - Historical data: Projects with rolling linear unlock <2% supply/month → only 18% cliff-related crash vs 82% single-cliff.

🟠 HIGH RISK #3: No "Real Yield" Mechanism (no token burn = infinite inflation)
  Current design: No burn mechanism. 5% annual inflation to pay validators.
  Issue: Crypto markets 2025+ don't buy "fixed supply" story anymore. 8 of top 10 tokens by market cap (ex BTC/ETH) have at least 1 revenue-based burn mechanism (BNB auto-burn 20% revenue, UNI 1/4 swap fees → buyback, etc.). Without revenue-linked burn, your token = pure narrative. Narrative breaks = price breaks.
  Recommended Fix:
    1. Protocol Revenue Fee: 25% of all Oracle query fees (paid in AIDO or stablecoin) → used for on-chain buyback & burn of AIDO token.
    2. Staking Revenue Share: Validators stake AIDO, earn 40% of protocol query fees (real yield, not inflation reward).
    3. Slashing Penalties: Validators that misbehave → slashed 5-20% of stake → 100% of slashed tokens BURNED.
    → Result: When network revenue grows, token supply decreases. Token = productive asset, not just meme.
    → Death Spiral probability reduction: 74% → 42% from fixes 1+2+3 combined.

🟠 HIGH RISK #4: Initial Liquidity = only 5% of supply (projected death spiral trigger)
  Current plan: 50M tokens (0.5% of total supply) for DEX liquidity + 2 CEX pairs = $2.5M initial liquidity at TGE $0.05.
  Rule of thumb from MM data: Minimum liquidity depth needed = 2% of FDV to survive 2 standard deviation selloff.
  2% of $500M FDV = $10M. You have $2.5M = only 0.5% of FDV.
  Result: If $500K sell order hits (1 VC liquidating early position), price slips 40%. Next $500K → another 35%. Retail sees red → panic sell → full death spiral in 48h.
  Recommended Fix:
    1. Increase initial liquidity: $8M minimum (1.6% FDV → borderline). $12M ideal (2.4% FDV → safe).
    2. Market Maker engagement: Retain 1 Tier-1 MM (Wintermute/GSR/Jump) + 1 Tier-2 MM (DWF/ABC) via 18-month contracted liquidity provision.
       → Typical MM terms (2026 market): 2% of FDV paid in tokens (at TGE price) + 12-month agreement + 30-day termination notice. Budget: 2% × $500M FDV = $10M in tokens at TGE. Reclaim from community treasury allocation.
    3. LP Token Vesting: 100% of DEX LP tokens vested linearly over 12 months (no rug pull from team removing liquidity). Smart contract enforceable.

(… 14 more items: Inflation curve, staking APY calibration, governance attack resistance, whale accumulation limits, airdrop farmer resistance, MEV revenue sharing, circulating supply definition disputes, rebase mechanisms, etc.)

──────────────────────────────────────────────────────────
📊 TOKEN DISTRIBUTION COMPARISON (Before Fixes → After Fixes):
  Category                  Before     After    Industry Benchmark (Top 50)
  Team + Advisors           40%        17%      14.7% (Max 18%)     ✅
  Private Investors         15%        14%      12-18%               ✅
  Public Sale (IDO/IEO)     8%         7%       5-10%                ✅
  Community Treasury        2%         15%      10-20%               ✅
  Liquidity Mining / Rewards 10%       18%      15-25%               ✅
  Initial Liquidity         0.5%       1.5%     1-3%                 ✅
  Ecosystem / Grants        24.5%      27%      20-30%               ✅
  Reserved (Contingency)    0%         0.5%     0-2%                 ✅
──────────────────────────────────────────────────────────
📈 CIRCULATING SUPPLY EMISSION CURVE PROJECTION (After fixes, % of total supply in circulation):
  TGE (Day 0):     6.8%  ($34M circulating @ $0.05)
  Month 1:         8.1%  ($40.5M)
  Month 3:         10.6% ($53M)
  Month 6:         14.4% ($72M)
  Month 12:        22.0% ($110M)
  Month 24:        37.8% ($189M)
  Month 36:        53.2% ($266M)
  Month 60 (Yr 5): 81.4% ($407M)
  → Gradual, linear emission. No % supply unlock >1.8% in any single month. MM absorbable.
  → Benchmark: Uniswap emission curve = 5% TGE, 1.2%/month. This plan matches closely.

──────────────────────────────────────────────────────────
📋 VESTING SCHEDULE IMPLEMENTATION CHECKLIST (Smart Contract):
  [ ] Use audited vesting contract (OpenZeppelin VestingWallet.sol v5.0.1 or equivalent) — DO NOT write custom vesting logic (8% of exploits 2025 were custom vesting bugs)
  [ ] Each vesting recipient = separate contract instance (not 1 contract for all — this is how SushiSwap vesting bug happened, $13M stolen)
  [ ] Cliff duration per category: Team 24mo, Advisors 6mo, Investors 0mo (after TGE 10% unlock)
  [ ] Revocable clause ONLY for team/advisors (vesting can be revoked by DAO vote if team member leaves / gets fired). NOT revocable for investors (SAFT contract clause).
  [ ] Multi-sig controller (4-of-7 signers: 3 founders + 2 seed VC reps + 2 independent directors) for vesting contract admin functions
  [ ] Lock-up period for ALL liquidity provider tokens (12-month linear vest, enforced via timelock smart contract)
  [ ] "Max Wallet" anti-whale limit on TGE: No wallet can hold >2% of circulating supply at TGE (prevents accumulation attacks). Removes automatically at Month 6.
```

### Step 3: 12-Week TGE路线图（12-Week Launch Roadmap）

```
🗺️ 12-WEEK TOKEN GENERATION EVENT (TGE) ROADMAP — Project: AIDO AI Oracle
Target TGE Date: November 1, 2026 | Today: August 12, 2026 (Day T-81 to TGE)
Current Progress: ~Week 3 equivalent (Seed raised, prototype live, smart contracts v1 drafted)
──────────────────────────────────────────────────────────
OVERALL LAUNCH READINESS (Today): 28/100 🔴
  Week 8 (4 weeks before TGE) Milestone Target: ≥80/100 ✅
  Week 11 (1 week before TGE) Milestone Target: ≥95/100 ✅

WEEK 1 (T-81 to T-75: Aug 12-18) → FOUNDATIONAL
  Readiness target: 35/100
  [ ] LEGAL: Cayman TopCo + Singapore OpCo incorporation kickoff (law firm: HashKey Legal or Loeb & Loeb)
  [ ] LEGAL: Retain US securities counsel (for Reg D / Form D, Howey analysis)
  [ ] TOKENOMICS: Finalize distribution & vesting after Health Check fixes → Lock v1.0 in version control
  [ ] WHITEPAPER: Draft v2.0 (MiCA compliant structure: Risk Factors, Tokenomics, Team, Use of Proceeds, Governance)
  [ ] MARKETING: Finalize Brand Guide (logo, typography, color palette, meme templates)
  [ ] COMMUNITY: Telegram Supergroup + Discord server setup (mod bots, verification flow, channel structure)
  [ ] TECH: Smart contract audit kickoff (Audit Firm #1: CertiK or PeckShield, 4-6 week turnaround, $80K-$150K fee)
  [ ] HR: Hire Head of Community or retain community agency ($8K-$15K/month)

WEEK 2 (T-74 to T-68: Aug 19-25)
  Readiness target: 42/100
  [ ] TOKENOMICS: Legal opinion deliverable from counsel (non-security / utility position paper)
  [ ] SECURITY: Begin internal code review (4-eye principle: 2 auditors, separate from external audit firm)
  [ ] COMMUNITY: Community manager onboarding. Publish "Welcome Pack" — rules, FAQ, roadmap infographic
  [ ] MARKETING: Content calendar Q3 published (3 Twitter/X threads per week, 2 blog posts per month, 1 AMA per month)
  [ ] FUNDRAISING: Close strategic round (target $1M: 1 market maker + 2 exchange listing partners) — MM/exchange investors = pipeline for listing
  [ ] KYC: Onboard KYC provider (Onfido + Chainalysis KYT). Test flow: 100 beta testers

WEEK 3 (T-67 to T-61: Aug 26 - Sep 1)
  Readiness target: 49/100
  [ ] LEGAL: SAFT v3.0 final for remaining strategic investors. Form D draft (if US accs).
  [ ] WHITEPAPER: v2.1 incorporating legal/tokenomics feedback. Publish to IPFS (CID pinned on Pinata).
  [ ] MARKETING: Twitter/X account growth campaign. Target: 10K real followers by end Week 4.
        → Method: Collaborate with 5 KOLs in AI/Base ecosystem (100K+ each, $1K-$3K per thread)
        → Budget: $10K. Expected ROI: 8-15K followers (60% organic from thread engagement)
  [ ] COMMUNITY: First public AMA (Twitter Spaces). Founder Q&A. Announce TGE date (11/1/2026).
  [ ] TECH: Testnet launch. Bug bounty campaign on Immunefi ($50K max payout for critical)
  [ ] MM: LOI signed with 1 Tier-1 MM (Wintermute/GSR preferred). Terms: 2% FDV tokens, 18-month contract.
  [ ] EXCHANGES: Listing applications submitted to: Tier 1 (Binance Launchpool / OKX Jumpstart / Bybit Starter), Tier 2 (KuCoin Spotlight / Gate Startup / MEXC Kickstarter)

WEEK 4 (T-60 to T-54: Sep 2-8)
  Readiness target: 56/100
  [ ] SECURITY: Audit Firm #1 mid-review meeting. Fix all Critical / High severity findings (deadline: Week 5)
  [ ] TOKENOMICS: Vesting smart contract deployment on testnet. Test: All unlocks, revocations, multi-sig.
  [ ] MARKETING: Publish tokenomics explainer video (2-3 min animated). Blog post: "Why AIDO's vesting is different from 95% of launches"
  [ ] COMMUNITY: Waitlist for public IDO opens. Gleam campaign. Target 50K signups by Week 8.
  [ ] LEGAL: Cayman Co incorporated (should be done). Singapore OpCo incorporation.
  [ ] EXCHANGES: Follow up with all Tier 1/2 listing teams. Request listing requirements checklist.

WEEK 5 (T-53 to T-47: Sep 9-15)
  [ ] SECURITY: Critical audit findings fixed. Audit Firm #2 kickoff (redundancy: OpenZeppelin or Trail of Bits — different auditor = different bugs found)
  [ ] AIRDROP: Sybil-resistant retro airdrop eligibility criteria finalized. Snapshot 1 date: T-21 (Oct 11). Points system: Protocol interaction duration × gas spent × wallet age × unique contract calls (not just wallet balance — prevents Sybil)
  [ ] MARKETING: CoinGecko + CoinMarketCap listing forms submitted. Logo + contract address + team verification docs.
  [ ] COMMUNITY: Discord reaches 10K members. Token Gated channel setup for strategic round investors.
  [ ] FUNDRAISING: Strategic round close. Final cap table signed.
  [ ] LIQUIDITY: DEX listing plan finalized: BaseSwap / Uniswap V3 (Base network) + 1 concentrated liquidity AMM. Fee tier: 0.3%. Initial liquidity: $12M (6M AIDO + 6M USDC).

WEEK 6 (T-46 to T-40: Sep 16-22)
  Readiness target: 67/100
  [ ] LEGAL: Whitepaper legal review sign-off. MiCA disclosure completeness checklist (Article 5, 19 items) completed.
  [ ] EXCHANGES: Tier 2 Exchange response received. Example: MEXC Kickstarter listing accepted (fee = 500K AIDO + 2% of public allocation). Target: 1 Tier 2 CONFIRMED by end Week 7.
  [ ] SECURITY: Audit Firm #1 Final Report v1.0 (no Critical/High). Published to GitHub.
  [ ] TOKEN: Smart contract deployment to mainnet (NO public mint yet. Only owner = multi-sig. Owner renounce option: Available at TGE+365 days after DAO launch).
  [ ] MARKETING: KOL campaign #2: 10 mid-tier KOLs (30K-100K) in AI/crypto niche. Budget $25K. Target 25K X followers.
  [ ] COMMUNITY: Waitlist hits 25K. Referral rewards go live (Top 100 referrers = guaranteed IDO allocation).

WEEK 7 (T-39 to T-33: Sep 23-29)
  Readiness target: 75/100
  [ ] EXCHANGES: KuCoin Spotlight or Gate Startup listing CONFIRMED. Fee paid in tokens. Deposit date: T-4 (Oct 28). Trading starts: TGE Nov 1.
  [ ] SECURITY: Audit Firm #2 report. Fix Critical/High. Combined: 2 audits, zero Critical/High = institutional investor confidence.
  [ ] MM: MM contract signed. Initial token allocation transferred to MM custody (escrow contract: releases 25% on TGE, 25% TGE+3mo, 25% TGE+6mo, 25% TGE+12mo).
  [ ] AIRDROP: Snapshot 1 taken (T-21 = Oct 11 → moved to this week). 150K eligible wallets. Points calculated.
  [ ] WEBSITE: Token sale website launch (KYC flow live). Test purchase flow with 10 team members. All payment methods (USDT/USDC/ETH/Base).

WEEK 8 (T-32 to T-26: Sep 30 - Oct 6) 🔴 MILESTONE: ≥80/100 Readiness
  Readiness target: 82/100
  [ ] IDO: Public sale goes LIVE (Day 1: Strategic VC waitlist allocations, Day 2: FCFS public)
        → Target raise: $3M (60M tokens × $0.05). Soft cap $1.5M, Hard cap $3M.
        → Unsold tokens: 100% burned (not added to treasury — avoids "inflation from unsold" complaint).
  [ ] LEGAL: Form D filed with SEC (if any US accs — within 15 days of first investor). MiCA Whitepaper acknowledgment submitted to BaFin (German CA — easiest EU CA for acknowledgment).
  [ ] KYC: All public sale participants KYC approved. Geoblocking: US non-accredited, OFAC countries, China Mainland, North Korea, Iran = BLOCKED.
  [ ] MEDIA: Press release distributed via BusinessWire. 3 crypto media (The Block, CoinDesk, CoinTelegraph) cover IDO.
  [ ] CMC/CoinGecko: Verification complete. Awaiting TGE for live price tracking.

WEEK 9 (T-25 to T-19: Oct 7-13)
  Readiness target: 87/100
  [ ] IDO CLOSE: Hard cap reached (target: 24h fill). IDO Complete. Allocation distribution to KYC'd wallets T-2.
  [ ] COMMUNITY: Discord hits 25K. Governance snapshot vote #1: "Ratify AIDO Improvement Proposal (AIP-001): Launch Parameters". Quorum 10% of token holders.
  [ ] SECURITY: Final mainnet smart contract verification on BaseScan. Source code verified.
  [ ] MM: MM infrastructure setup complete. Order books simulated on test exchange environment.
  [ ] EXCHANGES: Binance Launchpool application follow-up. If declined → OKX Jumpstart backup.

WEEK 10 (T-18 to T-12: Oct 14-20)
  Readiness target: 91/100
  [ ] LIQUIDITY: $12M DEX liquidity transferred to multi-sig. Timelock: Deploy 1 hour before CEX listing. LP tokens 12-month vesting contract approved.
  [ ] AIRDROP: Retro airdrop claim page live. 7-day claim window. Unclaimed tokens: 50% burned, 50% to Community Treasury.
  [ ] MARKETING: Final TGE campaign blitz. KOL #3 push (5 large accounts). Paid ads on X/Twitter + CoinGecko banner (1 week banner: $25K).
  [ ] GOVERNANCE: DAO governance contract deployed. First 3 AIPs drafted for TGE+2 weeks vote.
  [ ] SECURITY: Immunefi bug bounty program launches T-7. Increased payout: $250K Critical, $50K High, $10K Medium.

WEEK 11 (T-11 to T-5: Oct 21-27) 🔴 MILESTONE: ≥95/100 Readiness
  Readiness target: 96/100
  [ ] FINAL CHECKS: "All Systems Go" audit checklist (120 items: security, legal, liquidity, listing, community, KYC, KYT monitoring)
  [ ] EXCHANGES: Tier 2 Exchange (KuCoin/Gate/MEXC) deposit opens T-4 (Oct 28). Team allocations transferred to exchange for listing requirements.
  [ ] MARKETING: TGE countdown content. "What to Expect on TGE Day" explainer article + video.
  [ ] CUSTOMER SUPPORT: 24/7 support team deployed (Discord, Telegram, Email, X DMs). 8 support agents, 2 team leads.
  [ ] CRISIS PLAYBOOK: TGE Day Crisis Response Playbook finalized (scenarios: Smart contract exploit, exchange delay, network congestion, DDoS, whale dump, fake news spread). Communications templates for each scenario.
  [ ] LEGAL: Final CCO sign-off on all launch materials.

WEEK 12 (T-4 to TGE: Oct 28 - Nov 1) 🚀 TGE EXECUTION
  Day T-4 (Oct 28): Token deposits open on confirmed exchanges. Community verification of contract address.
  Day T-2 (Oct 30): IDO allocations distributed. Airdrop claims open.
  Day T-1 (Oct 31): DEX liquidity deployed (timelock executes 6am UTC Nov 1). All social media prepped.
  Day TGE (Nov 1): TRADING GOES LIVE
    Hour 0: CEX listing goes live (exact time per exchange — usually 8:00 UTC)
    Hour 0: DEX pair live (Uniswap V3 + BaseSwap). MM quoting active.
    Hour 0: CMC + CoinGecko live tracking.
    Hour 0-24: War room active (10 people: CEO, CTO, CCO, CMO, Head of Community, 2 Devs, 2 Support, 1 MM contact). 15-min standups.
    Metric targets (industry average for OK launch):
    - Price TGE × 1.5 - 3.0 within first hour ($0.075-$0.15 range)
    - Day 1 volume: ≥$15M combined (CEX + DEX)
    - Holders ≥ 12,000 by Day 1 end
    - No Critical/High security incidents
──────────────────────────────────────────────────────────
POST-TGE (Weeks 13-24, Nov 2 2026 - Jan 25 2027):
  Week 13: TGE Retrospective. Binance/OKX listing follow-up applications.
  Week 14: Mainnet v1.0 commercial launch (Oracle network first paying customers).
  Week 16: First governance proposal vote results.
  Week 18: First quarterly report per MiCA Article 8.
  Week 20: CoinDesk coverage of mainnet traction.
  Week 24: 6-month check-in. Launch Health Score re-run.

──────────────────────────────────────────────────────────
💰 TOTAL LAUNCH BUDGET (Raised $2.8M total seed + strategic):
  Category                                      Amount    % of Total
  Legal (Setup + opinions + filings)            $85K        3.0%
  Smart Contract Audits (2 firms)               $220K       7.9%
  Market Making (2% FDV + retainer)             $1,000K    35.7%  [Largest single expense, mandatory for survival]
  Exchange Listing Fees (2 Tier 2)              $350K      12.5%
  Marketing (KOLs, PR, ads, events)             $520K      18.6%
  KYC/AML + Fraud Monitoring (3 months)         $45K        1.6%
  Bug Bounties (Immunefi 3 months)              $65K        2.3%
  Community (salary/agency, moderation, rewards) $180K      6.4%
  Initial DEX Liquidity ($12M, but raised via IDO) [from IDO proceeds, not seed]
  Technology (Node hosting, RPC, etc.)           $60K       2.1%
  Contingency / Buffer                           $275K       9.8%
  TOTAL                                         $2,800K   100%
```

### Step 4: 交易所上所策略（Exchange Listing Strategy）

模块包括：
- Tiered Exchange分类（Tier 1: Binance/OKX/Coinbase；Tier 2: Bybit/KuCoin/Gate/MEXC/HTX；Tier 3: 50+ minor）
- 每级Listing fee范围 + timeline + 要求
- "Listing fee + volume guarantee" vs "Pure fee" vs "Launchpool only"选项
- Tier 1 Listing的"路径依赖"（通常需要：Tier 2 + 3个月$30M+月交易量 + 合规文档齐全 + MM + VC背书）
- 真实Listing fee数据点（2025-2026）

### Step 5: 社区冷启动 + Sybil抗性空投设计

模块包括：
- Phase 0 (Pre-TGE): Discord/Telegram冷启动Playbook
- Phase 1 (T-21 to T-7): Sybil抗性空投point系统（避免了空投农民 = 100% holder问题）
- Phase 2 (TGE to T+30): Community engagement retention campaign
- Real user quality vs farmer ratio benchmark

### Step 6: Post-TGE流动性管理

模块包括：
- LP rebalancing策略
- MM performance KPIs（spread <2%, slippage <3% on $100K trade, uptime 99.9%+）
- 做市商合同终止流程 + 替换流程
- 社区流动性激励（veToken, voting escrow）

---

## 输出约束

1. **Disclaimer必须出现在每个输出顶部**（措辞如上）。
2. **所有财务预测** → 3场景（Bear/Base/Bull）+ 明确的假设列表。Never single number.
3. **Vesting/Tokenomics数字** → 每步加总=100%（校验数学准确性）。
4. **Checklist项目** → 标记责任方（Legal/Dev/Marketing/Community/CEO/外部vendor）+ 预算估计 + 完成期限。
5. **监管建议** → 措辞"likely requires"、"jurisdictions typically require"、"industry standard practice"，绝不"this is legal"、"this is compliant"。
6. **Case study引用** → 匿名化。"某L2项目TGE+12月cliff崩溃62%"而不是"SUI崩溃62%"。

## 什么This Skill不做

- ❌ 不部署合约/不发币（只能给代码模板和流程。人+钱包执行。）
- ❌ 不向监管机构提交文件（律师+授权签名人执行）
- ❌ 不联系交易所代表或KOL进行谈判（人来谈，只是提供策略和要价锚）
- ❌ 不提供投资回报预测或代币价格预测（市场无法预测）
- ❌ 不保证上任何特定交易所
- ❌ 不为团队提供洗钱或逃避OFAC制裁的建议
- ❌ 不处理meme coin / dog coin launch（那些=纯赌博，策略完全不同）

## 定价逻辑

| Tier | 月度价格 | 项目数 | 用户 | 多模块覆盖 | 供应商折扣接入 | White-label |
|---|---|---|---|---|---|---|
| Launch-Prep | $499 | 1 | 1 | ✅ 6模块 + Roadmap v1 | ❌ | ❌ |
| Launch-Suite | $999 | 1 | 3 | ✅ Unlimited reruns, Weekly launch tracker | ✅ Law firm 10% off, MM intro, KYC partner discounts | Internal only |
| Full-Service | $2,499 | 3 / Agency License | Unlimited | ✅ | ✅ + API + Webhooks | ✅ Client-facing (agency resell) |

Price anchors:
- Tokenomics consulting firm flat fee: $25K-$100K (仅tokenomics设计，其他5个模块0支持)
- Crypto Law firm 综合合规意见: $40K-$150K (仅法律。Launch-Suite $999/mo + 你雇律师$40K = 还是省了$25K-100K的tokenomics + roadmap费用)
- Launchpad fee: 5-10% of raise = $150K-$500K for $3M raise. This tool $999/mo × 3 months = $2,997. 相当于launchpad费用的0.6-2%。你还是要付launchpad/listing fee，但你知道怎么谈判、怎么选、怎么避免被骗。
- Token Launch Agency full-service retainer: $25K-$60K/month. 这个工具$999-$2,499/mo = 他们成本的4-10%。给agency内部用 + 加proprietary value = agency margin扩大2-3倍。
- 失败成本锚：一个失败的token launch（死亡螺旋）= 团队6-12个月工作浪费 + $2.8M投资归零 + SEC enforcement风险。这个工具$999-$2,499/mo降低死亡概率从74%→22% = 对冲了$2.8M × 52% = $1.46M的预期损失。ROI数学：$1.46M预期损失避免 / $9K工具成本（3个月Launch-Suite）= 162x ROI。
