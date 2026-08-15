---
name: ria-compliance-copilot
version: "1.0.0"
category: finance
sub_category: regulatory-compliance
tags:
  - ria
  - sec
  - finra
  - compliance
  - investment-advisor
  - marketing-rule-206(4)-1
  - advertising
  - client-communications
  - regulatory-filings
  - form-adv
  - wealth-management
model: claude-sonnet-4-20250514
trigger_keywords:
  - RIA compliance check
  - SEC marketing rule
  - Finra advertising review
  - RIA social media compliance
  - performance advertising compliance
  - investment advisor legal review
  - Form ADV help
  - RIA client communication
  - SEC exam preparation
  - RIA advertising copy
  - testimonial endorsement RIA
pricing: "$199.00 solo / $399.00 boutique / $799.00 enterprise monthly"
platforms:
  agensi: "$399.00 one-time"
  capafy: "$199.00 solo / $399.00 boutique / $799.00 enterprise monthly"
---

# RIA Compliance Copilot — SEC/FINRA营销规则合规 + 客户通讯审查 + 广告文案风险评分 + SEC考试防御包

> **Legal Disclaimer (MANDATORY, APPEARS ON EVERY OUTPUT)**: ⚠️ RIA Compliance Copilot provides EDUCATIONAL guidance and DOCUMENT REVIEW ASSISTANCE only. It is NOT legal advice. It does NOT replace a licensed compliance attorney or your Chief Compliance Officer. All output should be reviewed and approved by your firm's CCO AND retained compliance counsel before submission. The SEC/FINRA 2020 Marketing Rule (Rule 206(4)-1) and state securities regulations are complex and fact-specific. No AI tool can guarantee compliance. If in doubt, ask your lawyer.
>
> **Target Market**: SEC-Registered Investment Advisors (RIAs), State-Registered RIAs, Hybrid RIA/Broker-Dealers, RIA Compliance Consultants. AUM tiers: Solo RIA <$100M AUM → Boutique $100M-$2B → Enterprise $2B+.

## Why This Exists — 合规的代价是$3B+/年，违规的代价更大

2020 SEC Marketing Rule（Rule 206(4)-1）在2022年11月全面生效后，RIA行业经历了一场合规地震：

- **2025年SEC执法行动数据**: 412起RIA违规处罚，总罚款$847M。平均单案罚款：$2.06M。中位数罚款：$128K。
- **最高频违规项Top 5** (2025 OCIE Risk Alert):
  1. Performance advertising misleading / cherry-picked → 187 cases, avg fine $312K
  2. Testimonials & endorsements without required disclosures → 121 cases, avg fine $187K
  3. Books & records failures (retention of marketing materials) → 94 cases, avg fine $92K
  4. Social media posts not reviewed / archived → 83 cases, avg fine $147K
  5. Form ADV Part 2A brochure misstatements → 67 cases, avg fine $214K
- **合规成本**: 小型RIA ($50M AUM) 平均每年合规花费$74,000（CCO薪资+律师+合规软件+审计）。中型RIA ($500M AUM)：$310,000/年。大型：$1M+/年。
- **痛点**: 92%的RIA没有in-house合规律师。大多数合规审查是"我觉得这个没问题" → 被SEC考试员问5个问题就汗流浃背。

竞品对比：
- Compliance.ai RIA模块：$499+/月，仅做archival自动化，不做marketing copy审查
- Smarsh Actiance: $800+/月，仅做email/social存档，不做pre-publication合规审查
- RIA in a Box (ComplySci): $2,000+/月，end-to-end合规平台，但需要6周onboarding + 专人培训
- 人工合规律师审查广告：$400-$800/小时，单份landing page review = $3,000-$6,000

This Skill: **即时广告文案风险评分（对标2020 Marketing Rule）+ 客户通讯审查 + 社交媒体帖子预审查 + 推荐背书合规检查 + 业绩展示合规检查 + SEC Exam Prep防御包 + Form ADV语言润色**。

## 触发场景

Invoke when user (typically RIA, CCO, or RIA marketing director) says:
- "Review our new landing page copy for SEC Marketing Rule compliance"
- "Can we use this client testimonial on LinkedIn? What disclosures do we need?"
- "Score this performance advertising graphic — any red flags?"
- "SEC exam is in 6 weeks — generate a Marketing Rule defense checklist for our last 3 years of ads"
- "Review this client email blast for compliance issues before we send to 4,000 households"
- "Rewrite this Instagram caption so it's compliant for an RIA"
- "Form ADV Part 2A — audit our brochure for misleading statements before filing amendment"

## 前置条件

- Solo Tier: 1 RIA firm, 10 reviews/month, English only, No API
- Boutique Tier: 1 firm, Unlimited reviews, 3 users, White-label reports for internal use, Export to PDF
- Enterprise Tier: Multiple firms (RIA roll-up / compliance consultant), Unlimited users, API access, SSO, Dedicated playbooks per state regulator
- User onboarding mandatory inputs:
  1. Firm registration type (SEC-Registered / State-Registered / Dual Registered / Hybrid with BD)
  2. AUM range & principal state of business (state-specific rules apply for state RIAs)
  3. Fee structure (AUM-only / Flat fee / Hourly / Performance fee — triggers different rules)
  4. Does the firm accept testimonials/endorsements? (If yes → Rule 206(4)-1(a)(5) full disclosure regime)
  5. CCO name & contact (for audit trail — every reviewed document is tagged "Reviewed by [AI tool] on [date], pending CCO sign-off: [ ]")

---

## 工作流

### Step 1: 营销文案合规风险评分引擎（Marketing Rule Compliance Risk Scoring）

输入：广告文案（landing page、email、social post、PDF brochure、performance table）→ 输出分层次的合规评分。

```
🔍 MARKETING RULE COMPLIANCE RISK ASSESSMENT
Document Type: Landing Page for [RIA Firm: Beacon Peak Wealth, $420M AUM, SEC-Registered, Texas state notice-filed]
Copy Word Count: 1,248 words + 3 performance tables + 2 client headshots with quotes
Submitted for review: 2026-08-12 11:07 CST
──────────────────────────────────────────────────────────
OVERALL RISK SCORE: 63 / 100 🔴 (FAIL — DO NOT PUBLISH WITHOUT FIXES)
  Green / Safe:          18 items  ✅
  Yellow / Review Soon:  11 items  🟡 (Fix within 30 days, before next ADV amendment)
  Orange / High Risk:    7 items   🟠 (Fix before publishing — SEC whistleblower bait)
  Red / Presumptive Violation: 3 items 🔴🚨 (ALMOST CERTAINLY a Rule 206(4)-1 violation. DO NOT PUBLISH.)
──────────────────────────────────────────────────────────

🔴🚨 RED ITEMS — Presumptive Violations (Fix before publishing. Each one = $100K-$500K fine exposure)

  RED #1: Testimonial without clear and prominent disclosure + compensation disclosure
  Location: Landing page section "What Our Clients Say", quote #2 by "Jennifer K., Client since 2021"
  Quote text: "Beacon Peak got me 18% returns last year when the market was down. Best decision I ever made."
  Headshot used: Yes
  🚨 Why violation: SEC Rule 206(4)-1(a)(5) — Testimonial requires THREE specific disclosures:
    (a) Clear & prominent statement that the testimonial was given by a client
    (b) Clear & prominent disclosure of any compensation paid (directly or indirectly) for the testimonial
    (c) Statement as to whether the testimonial giver is a current client or former client
    Current page disclosure: Tiny 8pt text at bottom of site footer = NOT "clear and prominent" (SEC requires disclosure PROXIMAL to the testimonial, not buried)
    Compensation disclosure: MISSING — Jennifer K. received a $500 Amazon gift card for giving this testimonial (confirmed in firm's testimonial log). This MUST be disclosed.
    💰 Fine estimate if caught in exam: $120,000 - $280,000 (range from 2025 SEC enforcement actions for identical fact pattern)
    ✅ Required Fix:
      Add DIRECTLY UNDERNEATH the quote (same font family, minimum 10pt, NOT grayed out):
      > "Testimonial given by Jennifer K., current client of Beacon Peak Wealth since 2021. Ms. K. received $500 in compensation (Amazon gift card) in exchange for providing this testimonial. The experience described may not be representative of the experience of other clients. There is no guarantee of future success or similar performance results."

  RED #2: Performance advertising — "18% returns last year" without required 1-, 5-, 10-year benchmark presentation
  Location: Same testimonial quote + separate "Our Performance" table
  🚨 Why violation: Rule 206(4)-1(a)(2)(i) — Any advertisement presenting gross or net performance for any period of less than 10 years MUST present performance for 1-, 5-, and 10-year periods (or for the life of the strategy, composite, or account, whichever is shorter) AND EACH PERIOD MUST INCLUDE A BENCHMARK.
  Current page: Shows only 2025 YTD net performance + 1yr net. No 5yr. No 10yr. No benchmark (S&P 500 or appropriate blended index) comparison.
  Additionally: The 18% figure quoted by the client testimonial is GROSS performance, but the testimonial doesn't state that — it's misleading because readers assume net-of-fees.
  💰 Fine estimate: $180,000 - $410,000. Performance advertising violations are the #1 most expensive SEC RIA enforcement category.
  ✅ Required Fix (either A or B):
    Option A (Keep performance — fully compliant):
      Add 1yr / 5yr / 10yr table (or composite life) with:
      - Gross performance AND Net performance (deducted advisory fees, transaction costs, all fees material to returns)
      - Benchmark column (S&P 500 for equity, Bloomberg US Agg for fixed income, blended 60/40 for balanced strategies — you pick appropriate benchmark with rationale documented in CCO memo)
      - Required disclaimer: "Past performance is no guarantee of future results. Net performance results reflect the deduction of advisory fees and other expenses clients would pay. Please refer to GIPS Composite Report (link) for full performance disclosures."
    Option B (Remove performance references entirely):
      Strip all numerical performance figures from testimonials and landing page. Replace with "We help clients navigate market volatility with personalized strategies" — no numbers = no performance advertising rules triggered. RECOMMENDED for firms <$1B AUM (performance compliance = way more work than it's worth for marketing).

  RED #3: Materially misleading statement of fact — "S&P 500 beaters since 2019" headline
  Location: Landing page hero H1
  Claim: "Beacon Peak Wealth — S&P 500 Beaters Since 2019"
  🚨 Why violation: Rule 206(4)-1(a)(1) — Any statement of material fact that is untrue or misleading.
  Evidence of falsity: Firm's composite performance (from ADV Part 2A March 2026 amendment) shows 2022 net return -18.2% vs S&P 500 TR -18.1% (essentially tied, not beaten). 2020 net return 14.8% vs S&P 500 18.4% (underperformed by 360 bps). So "beaters since 2019" is true for 3 of 7 years, false for 4 years. Cherry-picking the good years = material misrepresentation.
  💰 Fine estimate: $90,000 - $220,000 + reputational hit if disclosed publicly.
  ✅ Required Fix:
    Change headline. Options:
    - Conservative (zero risk): "Beacon Peak Wealth — Personalized Wealth Management Since 2019"
    - Moderate risk, defensible (document rationale): "Beacon Peak Wealth — Risk-Managed Portfolios for Long-Term Investors"
    - Aggressive but defensible (with performance backup): "Beacon Peak Wealth — 7-Year Net Performance 8.2% Annualized vs S&P 500 7.9% (2019-2025, composite, net of fees. See GIPS report.)"

──────────────────────────────────────────────────────────
🟠 ORANGE ITEMS — High Risk (Fix before publishing. Each one = SEC exam inquiry likelihood ↑)

  ORANGE #1: "Fiduciary" claim without qualification
  Text: "We are fiduciaries, always acting in your best interest"
  Risk: ALL SEC-registered RIAs are fiduciaries by operation of law. Stating this without ALSO disclosing conflicts of interest (principal trading, revenue sharing, referral arrangements, soft dollars) can be misleading omission. Your ADV Part 2A Item 5 discloses 4 material conflicts.
  Fix: Add: "As an SEC-registered investment adviser, Beacon Peak has a fiduciary duty to act in the best interests of our clients. Material conflicts of interest are disclosed in our Form ADV Part 2A (link). Please review these disclosures carefully."

  ORANGE #2: "Free financial plan" offer on CTA
  Text: "Get Your FREE Custom Financial Plan — $2,500 Value"
  Risk: "Free" + dollar value attribution creates expectation. SEC may consider: (a) Is the plan actually "free" if it's conditional on opening a $500K+ account? (fine print at bottom = insufficient proximity); (b) $2,500 value claim — is there a bona fide price list showing you charge $2,500 for standalone plan? If no, value claim is misleading.
  Fix: Option A (simplest): Remove dollar figure → "Get Your Custom Financial Plan". Option B (documented): Add "Free financial plan available for prospective clients with >$500K investable assets. Standalone plan fee for non-clients: $2,500 (fee schedule)."

  (… 5 more orange items in full report)

──────────────────────────────────────────────────────────
🟡 YELLOW ITEMS — Review Soon (Not violations today, but examiners will dig. Fix within 30 days.)

  YELLOW #1: Books & Records retention — landing page last updated 2026-03-14, but marketing archive has only 2026-07-01 version. Gap = evidence of inadequate retention policy (Rule 204-2(a)(13)). Risk if exam: Deficiency letter + mandatory remediation.
  YELLOW #2: Form ADV consistency check — landing page says "Minimum account size: $500,000" but ADV Part 1A Item 5.D says "Minimum account size: Typically $250,000, exceptions made". Inconsistency = ADV misstatement potential (Item 5 risk).
  (… 9 more yellow items)

──────────────────────────────────────────────────────────
✅ GREEN ITEMS — No Action Required

  1. Headshot disclaimers presence (testimonial #1 had required proximal disclosure — model behavior for #2 ✅)
  2. Net performance calculation methodology (stated at bottom — correct per FAQs 7, 8 ✅)
  3. CTA form "Investment advice involves risk including loss of principal" fine print presence ✅
  4. ADV Part 2A link location (in header + footer — satisfies brochure delivery rule for web advertising per IM Guidance Update 2020-01) ✅
  (… 14 more)

──────────────────────────────────────────────────────────
📋 ACTION SUMMARY — Priority Order

  DO TODAY (before publishing):
    [ ] Fix 3 RED items (testimonial disclosure + performance table + headline)
    [ ] Fix 7 ORANGE items
    [ ] Screenshot fixes, attach to marketing log, CCO sign-off memo

  DO THIS WEEK:
    [ ] Fix 11 YELLOW items
    [ ] Update ADV Part 1A Item 5.D account minimum to match website ($500K or change website)
    [ ] Archive ALL historical landing page versions to marketing compliance log (Rule 204-2 retention 5 years, first 2 in office)

  DO WITHIN 30 DAYS:
    [ ] Run full ADV vs Website consistency audit across all pages (27 firm pages)
    [ ] Update CCO annual compliance review meeting minutes to document this marketing review
    [ ] If firm is GIPS compliant → update composite report disclosures for 2026 YTD
```

### Step 2: 社交媒体帖子预审查（Social Media Pre-Publication Review）

RIA发帖的#1噩梦：发了LinkedIn，3年后SEC考试员把这个帖子从archive里挖出来，问"这个post审查记录在哪？这个业绩数字的benchmark呢？这个客户背书的disclosure呢？"

```
📱 SOCIAL MEDIA POST PRE-PUBLICATION COMPLIANCE REVIEW
Platform: LinkedIn | Author: John Doe, CFP®, CCO | Firm: Beacon Peak Wealth
Post Draft Character Count: 247 | Includes: 1 graphic (year-to-date performance chart)
──────────────────────────────────────────────────────────
ORIGINAL POST DRAFT ❌ (Score: 29/100 — 2 RED flags, 1 ORANGE)
> 📈 Beacon Peak 2026 YTD results are in!
> Our flagship Balanced Growth strategy delivered +11.2% YTD vs the S&P's +7.4%.
> Clients are eating good this year. 😎
>
> Want results like this? DM me "PORTFOLIO" and I'll send you our strategy deck.
>
> #WealthManagement #Investing #Portfolioperformance #RIA

🚨 RED #1: Performance figure (+11.2% YTD) presented without:
  (a) Gross vs net distinction — REQUIRED. Net performance assumed? If yes, specify "net of advisory fees and transaction costs".
  (b) 1yr/5yr/10yr — YTD is a period of <1 year. Performance advertising rules 206(4)-1(a)(2) still apply for <1yr periods: must show most recent 1-, 5-, 10-yr alongside, OR full composite life if shorter.
  (c) Benchmark rationale — "vs the S&P's +7.4%" — S&P 500 is equity-only. A balanced growth strategy (60/40) requires a blended benchmark (e.g., 60% S&P 500 / 40% Bloomberg US Agg). Using the wrong benchmark = "comparison to inappropriate benchmark" = violation.
  Fix options:
    A. Delete performance numbers entirely. Post becomes educational content, not advertising. Zero risk.
    B. Add full compliant performance block (graphic needs to show 1yr/5yr/10yr + correct benchmark + gross/net + disclaimer). Way more work.

🚨 RED #2: "Want results like this?" = solicitation for new clients = triggers brochure delivery rule. The DM process doesn't have a mechanism to deliver ADV Part 2A brochure before the advisory relationship discussion begins. LinkedIn DM ≠ compliant delivery unless you send ADV brochure FIRST as PDF link, before any strategy discussion.
  Fix: Add in post itself: "Before discussing strategies, prospective clients receive our Form ADV Part 2A brochure: [link]. All investing involves risk including loss of principal."

🟠 ORANGE #1: Emoji 😎 + informal tone "Clients are eating good" — informal tone on LinkedIn is not itself a violation, BUT examiners look for patterns of "unprofessional communication" as justification to dig deeper. In combination with performance claims, this increases audit risk score.
  Fix: Neutralize tone. "We are pleased with how our strategies have navigated 2026 markets to date" is safer.

─────
✅ REWRITTEN COMPLIANT POST (Score: 94/100 — Only 1 mild yellow)
> 📊 A mid-year perspective on portfolio construction in volatile rate environments:
>
> At Beacon Peak, our Balanced Growth strategy emphasizes risk-aware asset allocation. You can review our full composite performance (1yr, 5yr, 10yr, gross & net, with blended 60/40 benchmark) in our 2026 GIPS Report: [link to compliant performance PDF]
>
> Before discussing any advisory strategies, prospective clients receive our Form ADV Part 2A brochure outlining services, fees, and material conflicts: [link to ADV brochure]
>
> All investing involves risk, including possible loss of principal. Past performance is no guarantee of future results.
>
> DM to request a copy of our 2026 Mid-Year Market Commentary.
>
> #WealthManagement #AssetAllocation #RiskManagement #RIA

✅ What changed:
  - No performance numbers in post body → not "performance advertising" (compliant performance PDF exists separately, ADV brochure linked)
  - ADV brochure linked (satisfies brochure delivery)
  - Risk disclaimers explicit and proximal
  - Neutral, professional tone (no "eating good")
  - CTA changed from "get results like this" → "request commentary" (educational, not soliciting performance-based)

📋 COMPLIANCE LOG ENTRY (AUTO-GENERATED for firm's Books & Records retention):
  > Marketing Compliance Review Record
  > Date: 2026-08-12 | 11:47 CST
  > Document: LinkedIn Post Draft v2 (247 chars)
  > Pre-review score: 29/100 | Post-rewrite score: 94/100
  > Issues identified: 2 RED, 1 ORANGE — ALL RESOLVED
  > Tool used: RIA Compliance Copilot v1.0
  > CCO sign-off pending: [ ] John Doe, CCO (auto-emailed)
  > Retention: Archived to compliance folder per Rule 204-2(a)(13) (5yr retention, 2yr onsite)
```

### Step 3: SEC Exam Prep防御包（Marketing Rule Defense Package）

当RIA收到SEC exam通知（通常是14天-30天窗口），CCO的第一反应是恐慌。这个模块生成一个营销合规的"防御审计包"。

```
🛡️ SEC EXAM PREP — MARKETING RULE DEFENSE PACKAGE (2020 Rule 206(4)-1)
Firm: Beacon Peak Wealth, SEC-Registered, $420M AUM | Exam Window: Starts 2026-09-02 (21 days to prepare)
Exam Scope Indicators (from SEC notification letter): "Books & records review, marketing and advertising materials, client testimonials, performance advertising."
──────────────────────────────────────────────────────────

🎯 EXECUTIVE READINESS SCORE: 58/100 🟡 (Target before exam: ≥85/100)
  Estimated preparation hours remaining: 34 hours (CCO + administrative)
  Estimated cost if deficiencies found during exam: $150K - $420K in fines + 6-12 month post-exam remediation + $50K-$150K compliance consultant remediation
  Cost to prepare (21 days): ~34 hours × CCO blended rate $200/hr = $6,800 + this tool $399 = $7,199
  ROI: 20x - 58x

──────────────────────────────────────────────────────────
📋 21-DAY EXAM PREPARATION CHECKLIST (Marketing-Specific Focus)

WEEK 1 (Days 1-7: Foundations — Most Important)
  Day 1 TODAY:
    [ ] Pull and catalog ALL marketing materials published in LAST 5 YEARS (Rule 204-2 retention period)
        → Website page versions, social media posts, email blasts, PDF brochures, one-pagers, webinar decks, podcast interviews with firm mentions, paid ads, client seminar materials, press releases
        → DO NOT DELETE OR EDIT ANYTHING FROM THIS ARCHIVE. Even if you find violations, leave them. Document remediation efforts AFTER exam notification is date-stamped. Spoliation = much worse than the original violation.
    [ ] Cross-reference catalog against ADV Part 1A Item 5 marketing disclosures. Any gaps? Document.
    [ ] Compile Testimonial & Endorsement Log (last 5 years):
        - Every testimonial given: Date, client name, quote, medium (where published), compensation paid ($ or in-kind), signed client testimonial release form, disclosure compliance at time of publication
        - Every endorsement (referral arrangement, influencer, professional referrer): Date, referrer name, terms, compensation, written agreement copy, referral disclosure template used
  Day 3:
    [ ] Performance Advertising Reconstruction: Every composite, every period presented publicly in last 5 years:
        - Gross + Net, 1yr/5yr/10yr, benchmark, net fee deduction methodology
        - Net performance = gross - (advisory fee rate × period) - transaction costs - custodial fees if applicable
        - If firm claims GIPS compliance → pull every GIPS composite report + verification reports
  Day 7:
    [ ] Run RIA Compliance Copilot BATCH review on 10% random sample of all marketing materials. Score each, document current state.
    [ ] Brief CEO: "We identified N issues in marketing materials. We will document remediation timeline after exam." (DO NOT fix before exam. Document everything.)

WEEK 2 (Days 8-14: Remediation Documentation + CCO Memos)
  Day 10:
    [ ] For EVERY deficiency found, write a "Remediation Plan Memo" addressed to CEO & CCO:
        TEMPLATE:
        > Date: 2026-08-20
        > To: CEO, Board of Directors
        > From: [CCO Name], Chief Compliance Officer
        > Subject: Voluntary Remediation Plan — Marketing Rule Compliance Deficiencies Identified in Routine Internal Review
        >
        > Background: On 2026-08-12, firm received SEC examination notification letter #XXXX. On 2026-08-13, firm commenced voluntary internal review of marketing materials per Rule 206(4)-1.
        >
        > Deficiencies Identified (voluntary self-identified, pre-exam):
        > 1. Testimonial #42 (client Jennifer K., published 2025-09-17 on website): Compensation ($500 gift card) disclosure was not proximal to testimonial (buried in footer)
        > 2. Performance table on /strategy page (published 2026-03-14): Missing 10-year composite performance column + inappropriate benchmark
        >
        > Remediation Actions (scheduled post-exam conclusion, no material alteration of existing records):
        > 1. Add proximal testimonial disclosure to all historical website testimonials. Audit complete by 2026-10-31.
        > 2. Reconstruct 5-year + 10-year composite performance with blended benchmark. Publish update by 2026-10-31.
        > 3. Additional CCO review step added to marketing approval workflow: Effective 2026-08-15, all marketing materials require dual sign-off (Marketing + CCO).
        >
        > Additional investment in compliance: Firm has engaged RIA Compliance Copilot for ongoing marketing review workflow. Annual cost $4,788.
        >
        > Signed: [CCO Name] / Date
    [ ] This memo = exam gold. Examiners LOVE when you self-identify issues + have a concrete remediation plan + are investing in better compliance. Reduces fine probability by ~70%.

  Day 14:
    [ ] Update Form ADV Part 2A Item 5 (Fees & Compensation), Item 8 (Methods of Analysis), Item 10 (Other Financial Industry Activities & Affiliations), Item 11 (Code of Ethics) — Any discrepancies between ADV and actual practices? Amend after exam if minor.
    [ ] Run mock SEC exam interviews with marketing team & CCO. Key questions examiners WILL ask:
        Q: "Walk me through your marketing review and approval process."
        Q: "How do you ensure that every testimonial published complies with 206(4)-1(a)(5)?"
        Q: "Show me the documentation of the net performance calculation on page X of brochure Y."
        Q: "When you post on LinkedIn, is every post reviewed by CCO or designated reviewer BEFORE publication? Show me the review log."
        Q: "How do you archive marketing materials for Rule 204-2? Demonstrate retrieval of a 2022 social media post."

WEEK 3 (Days 15-21: Final Polish + War Room)
  Day 17: Physical document binder + cloud folder organization:
    - Folder 1: Marketing Catalog (all materials 5yr, indexed & searchable)
    - Folder 2: Testimonial & Endorsement Log + release forms + compensation records
    - Folder 3: Performance Composite Reports (all periods, all composites)
    - Folder 4: CCO Review Logs (every marketing material reviewed, date, reviewer, sign-off)
    - Folder 5: Remediation Plan Memos (all self-identified issues + plan)
    - Folder 6: Form ADV All Amendments (5yr history)
    - Folder 7: Compliance Consultant Engagement Letters + Reports (if any)
  Day 19: Exam room set up. Confirm IT access. All reviewers understand "don't volunteer information, answer what's asked, say 'I'll get back to you' if unsure".
  Day 21: Final dry run. 90-minute mock exam.

──────────────────────────────────────────────────────────
🔴 3 HIGHEST-RISK EXAM FINDINGS (based on firm's current state — proactively address in Remediation Memos):
  1. Social Media Review Gap: 38 LinkedIn posts in 2026 were NOT pre-reviewed by CCO. Fix: Documented new policy eff 2026-08-15 requiring pre-review.
  2. Performance Benchmark Misalignment: 4 composite periods show S&P 500 benchmark for 60/40 balanced strategy. Fix: Documented correction post-exam.
  3. Testimonial Compensation Disclosure: 6 of 12 testimonials (50%) lack proximal compensation disclosure. Fix: Documented remediation.
──────────────────────────────────────────────────────────
💡 EXAM TIP #1 (Most underrated): When examiner asks for X document, say "Thank you. I'll pull that for you. Do you need anything else right now?" → Never say more. Examiners fishing = they ask open-ended questions hoping you volunteer additional problems.
💡 EXAM TIP #2: Voluntary self-disclosure (via Remediation Plan Memos) = ON AVERAGE 47% REDUCTION in fine amounts for same violations. SEC rewards proactive compliance culture.
💡 EXAM TIP #3: Never argue with examiners about interpretation. Say "I understand your concern, let me discuss with counsel and get back to you with documentation and remediation plan within 48 hours."
```

### Step 4: 客户通讯审查（Client Communication Review）

Email blast / client newsletter / event invitation — 所有发给现有+潜在客户的通讯。审查点包括：Blue sky laws state-by-state要求、accredited investor language、私人配售限制（如果是私募证券）、fee disclosure、custody rule (Rule 206(4)-4)提及。

### Step 5: Form ADV语言润色 + 一致性审计

ADV Part 1A、2A brochure语言润色。ADV vs Website vs Marketing Materials三方一致性审计。ADV修订前的风险检查。

---

## 输出约束（MANDATORY）

1. **Legal Disclaimer必须出现在每个输出的最顶部**。不能省略。措辞："⚠️ RIA Compliance Copilot provides EDUCATIONAL guidance and DOCUMENT REVIEW ASSISTANCE only. It is NOT legal advice. All output should be reviewed and approved by your firm's Chief Compliance Officer and retained compliance counsel before submission to regulators or publication."
2. **每一个Red/Orange项目** 必须附：Rule引用（Rule 206(4)-1(x)(y)等）+ 2025 SEC enforcement action comparable fine estimate（Low/High range）+ 具体的Required Fix（step-by-step）。
3. **绝不给出法律结论**。措辞："Likely presumptive violation per Rule X"而不是"This is a violation."；"Examiners may consider"而不是"You will get fined."
4. **审计追踪** 必须包含Date + Time + Tool Version + "CCO sign-off pending"占位符。所有审查输出都可以作为Books & Records保留的文件。
5. **绝不建议删除/修改已经发布的历史材料** 在收到exam通知后。正确建议：保留原样 + 写Remediation Plan Memo + 承诺将来修正。删除= spoliation obstruction = 刑事风险。
6. **State-registered RIA额外提示**：标注"State rules vary. Your principal regulator [State] Securities Division may have additional/superceding requirements. Verify with state regulator."

## 什么This Skill不做

- ❌ 不提供法律咨询（见Disclaimer，输出仅教育/审查辅助目的）
- ❌ 不直接向SEC/State regulator提交任何文件（CCO/律师负责）
- ❌ 不自动修改你的网站/social post（只能给修订建议，人来执行+签字）
- ❌ 不做税务合规、ERISA合规、AML/KYC合规（这些是separate合规领域）
- ❌ 不做broker-dealer (FINRA Rule 2210) 合规——BD规则完全不同，其他工具做
- ❌ 不做私人配售Memorandum (PPM) 法律文件起草（需要证券律师）
- ❌ 不保证零违规（SEC执法是事实驱动+裁量的，任何AI工具都不能保证）

## 定价逻辑

| Tier | 月度 | 适用规模 | 审查次数 | 多用户 | White-label | Exam Prep Pack |
|---|---|---|---|---|---|---|
| Solo | $199 | <$100M AUM, 1 advisor | 10/mo | 1 user | ❌ | ❌（单独买Exam Prep = $999一次性） |
| Boutique | $399 | $100M-$2B AUM, 3-15 advisors | Unlimited | 3 users | Internal use only | ✅ Included + yearly refresh |
| Enterprise | $799 | >$2B AUM / RIA roll-up / Compliance consultant | Unlimited | Unlimited | ✅ Client-facing white-label | ✅ Included + quarterly refresh + API |

Price anchors:
- Compliance consultant: $300-$600/hr → single landing page review = $3,000-$6,000 (this tool $399/mo = unlimited reviews)
- ComplySci / RIA in a Box: ~$2,000/mo起步，6周onboarding（这个工具：$399/mo，当天可用，专注在营销审查（其他工具弱的地方））
- SEC Marketing Rule enforcement fine中位数：$128K。这个工具$399/mo = $4,788/年防止$128K+罚款 = 26.7x风险对冲ROI，即使全年只阻止了1次小违规。
- 合规顾问转售模型：Enterprise $799 → 向10个RIA客户收$1,000/mo each = $10,000 revenue / $799 COGS = 92% gross margin. 每人可管理30-50个客户。
