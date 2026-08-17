---
name: redditads-intelligence-suite
version: "1.0.0"
category: marketing
sub_category: paid-social-intelligence
tags:
  - reddit-ads
  - paid-social
  - ad-intelligence
  - competitor-ads
  - ad-spy
  - ppc
  - performance-marketing
  - agency
  - b2b-marketing
  - ad-copy
  - landing-page
model: claude-sonnet-4-20250514
trigger_keywords:
  - Reddit ads spy
  - Reddit competitor ads
  - Reddit ad intelligence
  - Reddit paid ads
  - Reddit ad copy examples
  - Reddit ads benchmark
  - Reddit CPM CPA
  - Reddit ad agency
  - Reddit ads A/B test
  - Reddit promoted posts
  - Reddit Ads Manager optimization
pricing: "$299.00 starter / $599.00 pro / $1199.00 agency monthly"
platforms:
  agensi: "$599.00 one-time"
  capafy: "$299.00 starter / $599.00 pro / $1,199.00 agency monthly"
---

# RedditAds Intelligence Suite — 竞争对手广告间谍 + 品类基准线 + 投放策略逆向工程 + 创意生成

> **定位**: B2B付费社情情报工具。服务对象：SaaS市场团队($2M+ ARR)、品牌DTC增长团队、Performance Marketing代理。如果您是月投放<$5K的独立开发者，请用Reddit Post Guardian + Subreddit Finder组合（$48/月），不要买这个。
>
> **合规声明**: 所有广告样本来自Reddit公开的Promoted Post展示数据、公共Ads Help Center文档、第三方ad spy API（Adbeat/SimilarWeb公开层）。不破解Reddit Ads Manager后台，不获取竞品账户数据，仅采集**公开可见**的广告展示样本。符合CFAA及Reddit Terms of Service。

## Why This Exists — Reddit Ads的信息差红利

Reddit Ads在2025-2026年成为增长最快的付费渠道：
- Reddit广告收入Q2 2026同比+41%（$520M/季度），Meta仅+6%，Google搜索仅+8%
- 品类平均CPM $5.8（vs Meta $14.2，LinkedIn $38），平均CPA SaaS类$56（vs LinkedIn $210）
- 但**90%的广告主浪费了40-60%预算**，因为：
  1. Reddit Ads Manager的报表极弱，没有品类基准线，你永远不知道你的表现是好是坏
  2. 没有官方ad spy工具，你不知道竞品在投什么创意、定向什么subreddit、出价多少
  3. Reddit的「社区语境」广告优化逻辑完全不同于Meta/Google，照搬其他渠道素材=死

竞品对比：
- Adbeat Reddit模块：$499/月，仅提供广告截图，没有基准线、没有逆向工程、没有创意生成
- SimilarWeb Paid Social：$299/月，仅显示广告主总投放估计，不提供reddit-specific的sub定向和创意分析
- Reddit官方Ads基准线报告：每年出一次PDF，品类粒度粗到没用（仅分"B2B" vs "DTC"）

This Skill: **实时竞品广告间谍 + 26个细分品类基准线 + 投放策略逆向工程 + AI创意生成 + 投放账户审计**。

## 目标客户

- SaaS: B2B SaaS（HR, Marketing, DevTools, AI SaaS）$2M-$200M ARR
- DTC: Gaming配件、Supplement、Tech Gadget（Reddit友好品类）
- Agency: Performance Marketing代理（管理客户Reddit Ads账户）
- Crypto: 合规的中心化交易所、硬件钱包（Reddit是crypto投放TOP3渠道）

## 触发场景

Invoke when user says:
- "Show me all ads our competitors are running on Reddit right now"
- "What's the average CPM/CTR/CPA for DevTools SaaS ads on Reddit?"
- "We're spending $15K/month on Reddit Ads with $82 CPA — is this good or bad? Audit our account"
- "Generate 20 ad copy + creative angle variations for our SaaS launch on r/sales and r/marketing"
- "Which subreddits are our competitors NOT targeting that we should grab first?"
- "逆向工程Competitor X的Reddit投放策略：他们在测试什么？什么在起作用？"

## 前置条件

- Starter Tier: 2个竞品品牌追踪、English only、10个subreddit范围
- Pro Tier: 10个竞品、5个品类基准线、Creative AI生成API、周度更新
- Agency Tier: Unlimited竞品、Unlimited品类、White-label报告、多客户Workspace、API导出
- User-provided data (onboarding):
  - 竞品名单（至少2-5个直接竞品）
  - 自身投放品类（SaaS DevTools / DTC Gaming / Crypto Exchange 等26个品类选择）
  - 自身Ads Manager导出的最近30天数据（CSV导出，无PII，聚合指标即可）
  - 自身目标CPA / 目标ROAS

---

## 工作流

### Step 1: 竞品广告间谍扫描（Competitive Ad Intel Scan）

输出格式——每个竞品一份1页AD INTEL CARD：

```
🎯 COMPETITOR AD INTEL CARD — [Competitor: Notion Calendar (formerly Cron)]
Scanned: 2026-08-12 09:17 UTC | Sample Window: Last 21 days | Total Ads Detected: 47
──────────────────────────────────────────────────────────
📊 SPEND ESTIMATE (21d)
  Low Estimate:    $42,000 - $58,000
  Best Estimate:   $51,200 (confidence 78%)
  High Estimate:   $62,000 - $74,000
  Impressions:     8.2M - 10.4M
  Frequency Cap:   Estimated 2.3-3.1 per user (standard Reddit frequency capping)

🎯 TARGETING — Subreddits
  RANK  Subreddit               Imps Share   CPM Bid Est   Avg Ad Age
  1.    r/productivity          28%           $6.8          14d (LIVE long-running = WINNING)
  2.    r/calendars             19%           $5.2          9d
  3.    r/Notion                15%           $8.4          3d (NEW test)
  4.    r/busy                  12%           $4.9          11d
  5.    r/freelanceWriters       8%           $4.1          5d
  6.    r/smallbusiness          7%           $5.6          7d
  7.    r/AdultADHD              6%           $6.1          2d (NEW test)
  8.    Long-tail (23 subs)      5%           Avg $3.8      Mixed
  → Key Insight: They're TESTING r/AdultADHD (only 2d old, $6.1 CPM) — this is a new angle nobody else has found. Intercept immediately at $5.9 CPM before they saturate.

🎯 TARGETING — Audience Layer
  - Interest targets detected: "Calendar apps", "Productivity software", "Project management"
  - Lookalike detected: YES — 2 separate LALs visible (1% LAL = 0.5M audience)
  - Remarketing visible: YES — abandoned cart ads in r/productivity (confirmed by 12h recency pattern)
  - Device: 68% Desktop / 32% Mobile (SaaS category norm = 56% Desktop → they're intentionally biasing desktop = signal that desktop conversion is 2.3x mobile for them)

🎯 CREATIVE BREAKDOWN — 47 Ads
  Format Split:
    - Single Image: 58% (27 ads)
    - Video <15s: 24% (11 ads)
    - Carousel 3-slide: 13% (6 ads)
    - Text-only promoted post: 5% (2 ads, high CTR signal)
  Tone Split:
    - Direct Response ("Start free trial"): 62%
    - Problem/Solution ("Tired of double-booking?"): 27%
    - Community/UGC ("Redditors tell us..."): 11%
  TOP 3 WINNING CREATIVES (longest-running = highest ROI proxy):
    1. Ad ID #NC-038 (RUNNING 14 DAYS STRAIGHT) 🏆
       Image: Side-by-side screenshot of Google Calendar vs Notion Calendar
       Headline: "I switched from Google Calendar after 8 years. Here's why."
       CTA: "See the difference →"
       Est CTR: 0.78% (category avg 0.41% → 1.9x overperformer)
       Est CPC: $3.10
       → Why it works: "X years user, switched" testimonial pattern is Reddit catnip. Authentic tone.

    2. Ad ID #NC-019 (RUNNING 11 DAYS)
       Video: 12s screen recording of Calendar AI scheduling assistant
       Headline: "The calendar that books YOUR meetings for you"
       CTA: "Try 30 days free"
       Est CTR: 0.61%
       Est CPC: $4.20

    3. Ad ID #NC-007 (RUNNING 9 DAYS)
       Text-only promoted post: u/notion (verified brand account)
       Title: "We built a calendar that actually respects your focus time. AMA."
       Body: "2026 update: Notion Calendar now blocks focus time automatically... [full copy 142 words]"
       Est CTR: 1.12% (🔥 TEXT-ONLY outperforming image ads on Reddit — always)
       Est CPC: $2.40

  BOTTOM 3 TESTS (recently killed = LOSERS — don't copy these):
    - "Unlimited meeting scheduling" generic headline → KILLED after 3d, <0.18% CTR
    - Influencer selfie style image → KILLED after 4d, $8.40 CPC
    - "AI Calendar" buzzword bingo → KILLED after 2d

🎯 LANDING PAGE AUDIT (all ads link to 4 variants):
  1. notion.so/product/calendar (direct product page) — 62% traffic
  2. notion.so/calendar-vs-google-calendar (comparison LP) — 23% traffic 🔥
  3. notion.so/blog/stop-double-booking (content LP) — 10% traffic
  4. notion.so/signup (direct signup) — 5% traffic
  → Key Insight: Comparison landing page (Notion vs Google Calendar) gets 23% of spend → high-intent. Competitor built a comparison LP and is sending ad traffic there. You need one too.

🎯 OFFER / PRICING ANGLE:
  - Dominant offer: "Try free for 30 days" (82% of ads)
  - Test offer: "Get $50 credit when you book 10 meetings" (15% of ads, NEW test)
  - No discount / % off detected (mature SaaS: Notion doesn't discount)

🎯 STRATEGY INFERENCE (逆向工程结论):
  → Notion Calendar's Reddit strategy: They're using a "HARVEST + DISRUPT" playbook.
     1. HARVEST: r/productivity + r/calendars (high-intent categories) with DR ads → proven winners, 60% of budget.
     2. DISRUPT: Testing 2-3 NEW subreddits each week with $500-$1,000 microtests → currently r/AdultADHD is the #1 emerging test. When one works, they scale it 10x.
     3. CREATIVE BET: Text-only promoted post (AMA format) is their #3 performer. Almost no one does this because ad platforms default to image/video. Reddit rewards text authenticity.
  → YOUR ACTIONABLE DIFFERENTIAL (where they're weak, where you attack):
     1. r/ExecutiveAssistants (300K subs) — Notion Calendar ISN'T here. 71% overlap with calendar purchasers. Your CPM est $3.2 → jump in now.
     2. Text-only "I switched from Notion Calendar after X months" attack ad format → use their own #1 winning pattern against them.
     3. Comparison LP "YourCalendar vs Notion Calendar" — send 25% of your Reddit traffic there just like they do for Google.
```

### Step 2: 26个细分品类基准线（Category Benchmark Database）

Reddit Ads Manager**不提供**任何品类基准线。你永远不知道自己的表现好不好——直到你用了这个。

```
📊 CATEGORY BENCHMARK REPORT — DevTools SaaS (B2B, $19-$99/month price point)
Benchmark Date: August 2026 | Sample: 147 active advertisers, $8.2M aggregate spend tracked
──────────────────────────────────────────────────────────

METRIC                      25th %ile     Median      75th %ile     90th %ile (Top 10%)
──────────────────────────────────────────────────────────
CPM (Cost per 1K Imps)      $3.80         $5.80       $7.90         $10.40
CPC (Cost per Click)        $2.10         $3.60       $5.40         $8.10
CTR (Click-Through Rate)    0.19%         0.34%       0.52%         0.81%
CVR (Visit → Signup)        4.2%          8.7%        13.1%         19.6%
CPA (Signup)                $28           $56         $92           $148
CVR (Signup → Paid)         6.1%          11.4%       17.8%         26.3%
CAC (Paid Customer)         $310          $612         $1,020         $1,940
ROAS (30-day LTV / CAC)     0.4x          0.9x         1.6x          2.8x
Frequency per User          1.8x          2.7x         3.6x          4.4x
Desktop Share               41%           56%          69%           82%
Video Creative Share        12%           28%          47%           66%

──────────────────────────────────────────────────────────
SUBREDDIT TIER RANKINGS (DevTools SaaS-specific)
Tier S (Highest ROI, most saturated):
  r/programming, r/webdev, r/javascript, r/SaaS, r/startups
  Avg CPM: $7.2 | Avg CPA: $78 | Saturation Index: 87/100

Tier A (Great ROI, moderate saturation — SWEET SPOT 2026):
  r/devops, r/kubernetes, r/reactjs, r/typescript, r/coding
  Avg CPM: $4.8 | Avg CPA: $49 | Saturation Index: 41/100
  → RECOMMENDED: 50% of new budget goes here before Tier S is saturated.

Tier B (Emerging, low competition, test carefully):
  r/dotnet, r/golang, r/rust, r/Python (wait r/Python is moving to A fast), r/vscode
  Avg CPM: $2.9 | Avg CPA: $31 | Saturation Index: 14/100
  → RECOMMENDED: $500 microtests per sub, scale winners.

Tier C (Cheap but low intent — avoid unless VERY specific):
  r/learnprogramming, r/csMajors, r/programmingcirclejerk
  Avg CPM: $1.4 | Avg CPA: $189 | Saturation Index: 3/100

──────────────────────────────────────────────────────────
CREATIVE PERFORMANCE PATTERNS (DevTools SaaS):
  #1 Format: Text-only promoted post → Avg CTR 0.68% (vs all-format avg 0.34%)
  #2 Format: Side-by-side screenshot "Before vs After using [Tool]" → CTR 0.51%
  #3 Format: Terminal/screen recording demo <15s → CTR 0.47%
  WORST Format: Stock photo with 3 people smiling at laptop → CTR 0.11% (DON'T)
  Winning Headline Pattern: "I replaced [Legacy Tool] with [YourTool]. Here's what changed."
  Winning CTA: No CTA button (text post) > "Learn More" > "Sign Up" > "Get Started"

──────────────────────────────────────────────────────────
YOUR ACCOUNT vs BENCHMARK (Sample: DevTools SaaS, $14,800/mo spend)
  Metric                  Your Value   Benchmark Median   Δ      Diagnosis
  CPM                     $6.40        $5.80              +10%   🟡 Slightly over (OK if CTR over too)
  CTR                     0.21%        0.34%              -38%   🔴 BIG PROBLEM #1 — CTR half of median
  CPC                     $6.90        $3.60              +92%   🔴 BIG PROBLEM #2 (caused by CTR)
  CVR (Visit→Signup)      9.1%         8.7%              +5%    ✅ Landing page OK
  CPA (Signup)            $76          $56                +36%   🟡 OK but could be $45 if CTR fixed
  Signup→Paid             10.2%        11.4%              -11%   🟡 Nurturing sequence slightly weak
  CAC                     $840         $612               +37%   🔴 FIX CTR → CAC drops to ~$500 overnight

  ROOT CAUSE ANALYSIS (why CTR 0.21% vs 0.34% median):
    → 100% of your ads are stock-photo image format (avg CTR 0.11%)
    → $0 spent on text-only promoted posts (category #1 performer: 0.68% CTR)
    → All ads use generic headline "The Best [X] Tool for Devs"
    → You're bidding into Tier S saturated subs 100% — 0% in Tier A/B sweet spot
  30-DAY FIX PLAN + PROJECTED IMPACT:
    Week 1: Launch 6 text-only posts + 4 screenshot ads → 20% of budget
    Week 2: Shift 50% budget from Tier S → Tier A subs (r/devops, r/kubernetes, r/reactjs)
    Week 3: Kill bottom 40% worst CTR ads (auto optimization insufficient, manual kill needed)
    Week 4: Scale top 20% winners 2x
    → Projected result: CTR → 0.42% (+100%), CPC → $3.80 (-45%), CPA → $48 (-37%), CAC → $520 (-38%)
    → Monthly savings on same volume: $14,800 → $9,200 = $5,600/mo SAVINGS (this tool $599 = 9.3x ROI in month 1)
```

### Step 3: 投放账户审计（Ads Manager Account Audit）

用户导出最近30天Ads Manager CSV数据 → 输出审计报告。

```
🔍 REDDIT ADS ACCOUNT AUDIT — [Client: HR SaaS "PeopleFlowPro"]
Period: Last 30 days | Spend: $47,208 | Signups: 812 | Paid Conversions: 94 | CAC: $502
Audited by: RedditAds Intelligence Suite | Date: 2026-08-12
──────────────────────────────────────────────────────────

🎯 EXECUTIVE SUMMARY
  Current Efficiency Score: 42/100 🔴
  Wasted Spend Detected: $19,321 (40.9% of total) 💰💰💰
  Optimized 30-day Projection: Same 94 paid conversions for $28,500 spend → CAC $303
  Or (keep spend same): 94 → 155 paid conversions (+65% volume)
  ROI on this audit: $19,321 saved / month vs $599 tool = 32.2x

──────────────────────────────────────────────────────────
💸 WASTE CATEGORY #1: Low-CTR Zombies (42% of waste = $8,115/month)
  Ads running for 7+ days with CTR <0.22% (category median 0.34%)
  → 23 ads identified. They ate 21% of total budget but produced only 6% of signups.
  → FIX: Pause IMMEDIATELY. Reallocate budget to top 5 CTR performers.
  Example Zombie #1:
    Ad Name: "HR Platform Hero Shot 007" | Budget: $3,800/mo
    CTR: 0.13% | CPC: $12.20 | Signups: 8 | CPA Signup: $475
    → Median CPA for account: $58. This ad is 8.2x more expensive per signup.

💸 WASTE CATEGORY #2: Saturated Tier S Subs (31% of waste = $5,989/month)
  Top 3 subs by spend: r/humanresources ($14K), r/HR ($9.2K), r/business ($6.5K)
  Saturation check: You've shown your #1 ad 4.2x frequency to 89% of r/humanresources active users.
  Diminishing returns curve hit: Week 1 CPA $42 → Week 4 CPA (same sub) $118.
  → FIX: Cap these subs at $8K/$5K/$4K respectively. Move $8K saved into Tier A subs:
      r/recruiting (CPM $3.9, CPA est $34), r/PeopleOperations (CPM $4.1, CPA est $36),
      r/askHR (CPM $2.8, CPA est $42) — 3 new subs, 0 competitors advertising.

💸 WASTE CATEGORY #3: Mobile Misallocation (18% of waste = $3,478/month)
  Device split: 58% mobile / 42% desktop. But HR SaaS buyers = 76% desktop (LinkedIn B2B data).
  Mobile stats: $27,380 spend → 18 paid conversions → MOBILE CAC: $1,521 😱
  Desktop stats: $19,828 spend → 76 paid conversions → DESKTOP CAC: $261 ✅
  → FIX: Day 1: Bid adjustment -60% Mobile. Day 7: If mobile CAC still >$800, turn off mobile 100%.
  → Savings: ~$3,500/month recovered. 0 conversions lost (mobile conversions = accidental clicks anyway).

💸 WASTE CATEGORY #4: No Negative Keyword List (9% of waste = $1,741/month)
  Reddit Ads has negative keyword functionality. 71% of accounts don't use it.
  You're showing your $199/month HR SaaS ad to people searching:
    - "free HR software" (2,400 impressions → 2 signups → 0 paid. $640 wasted)
    - "HR jobs near me" (1,800 impressions → 0 signups. $480 wasted)
    - "HR certification online" (1,200 impressions → 0 signups. $320 wasted)
    - "HR memes" (3,100 impressions → 1 signup → 0 paid. $301 wasted)
  → FIX: Upload negative keyword list today. Add 200 high-intent-excluding terms.

──────────────────────────────────────────────────────────
🟡 OPPORTUNITIES FOUND (not waste, but upside):
  1. Interest Targeting Underused: You only target subreddits. Interest "Human resource management" (1.8M users) is 35% cheaper CPM. Test $1,000.
  2. Conversions API Not Connected: You're using pixel only. 28% of conversions attributed wrong. Connect Reddit CAPI through Segment today.
  3. Text-Only Zero Spend: 0% of spend on text-only format. Category median = 22% spend on text = highest ROI format.
  4. Remarketing List Size 14K users but $0 spend on remarketing: Remarketing CPA is typically 1/3 of prospecting CPA. Allocate 15% budget to remarketing → 20+ extra paid conversions.

──────────────────────────────────────────────────────────
🔢 PRIORITIZED EXECUTION CHECKLIST (30-DAY ROADMAP):
  Day 0 (today):
    [ ] Pause 23 Zombie ads (CTR <0.22% 7d+) → saves $8,115
    [ ] Upload negative keyword list → saves $1,741
    [ ] Mobile bid adjustment -60% → saves ~$2,000+ first week
  Day 2:
    [ ] Cap r/humanresources at $8K, r/HR at $5K, r/business at $4K
    [ ] Launch $2K test in r/recruiting + r/PeopleOperations + r/askHR
  Day 5:
    [ ] Launch 6 text-only promoted post ads (AMA format) → $2K test budget
    [ ] Set up CAPI through Segment
  Day 10:
    [ ] Allocate 15% budget to remarketing (if CAPI conversion matches)
    [ ] Kill bottom 20% of new tests
  Day 20:
    [ ] Scale top 20% of new winners 2x
    [ ] Audit again → confirm CAC ≤ $320
```

### Step 4: 创意生成引擎（Creative AI Generator）

输入：产品描述 + 竞品TOP创意 + 品类基准 → 输出20个创意变体（Headline + Body + Visual Concept + Sub Recommendation + Expected CTR）

格式示例略，包含：Text-only AMA posts、Screenshot comparison ads、UGC-style captions、Launch announcement angles、Problem-agitate-solve、Counter-intuitive hot takes、Community-first "Redditors get X" special offer、Founder story format等8种结构化模板。

### Step 5: 周度情报简报（Weekly Competitive Intel Brief）

每周一早上推送：
- 新增竞品广告（过去7天新上线的，按投放规模排序）
- 竞品KILLED广告（推断失败者 + 原因）
- 新出现subreddit定向（竞品刚在测试的 = 机会窗口）
- 品类CPM/CPC趋势（涨了跌了？调整出价）
- 1个Actionable Recommendation（本周只需做1件事）

---

## 输出约束

- Spend估计 → 必须标明置信度（Low/Best/High三档 + confidence %）。从不给单值。
- Benchmark → 必须标明样本大小（N=147 advertisers）+ 采样时间段。
- 账户审计 → Waste分类加总必须等于Total Waste（对得上账）。每条Recommendations必须附estimated $ impact。
- White-label (Agency tier only): 移除所有RedditAds Intelligence Suite品牌标识。代理可直接交付给客户作为自己的审计产品。
- Creative生成 → 标注"Estimated CTR基于类别基准+历史同pattern表现，非保证。请A/B test。"

## 什么This Skill不做

- ❌ 不破解Reddit Ads Manager，不直接拉取竞品账户数据
- ❌ 不自动投放广告（需要人点击发布。可以给建议和草稿）
- ❌ 不保证CPA数字（基准线是中位数，你的实际表现取决于落地页、产品、报价）
- ❌ 不做TikTok/FB/Google广告间谍（纯Reddit深度，其他渠道=不同工具）
- ❌ 不做SEO/Organic Reddit增长（那是Subreddit Finder + Mention Radar组合的职责）

## 定价逻辑

| Tier | 月度价 | 竞品追踪数 | 品类基准线 | 创意生成 | 账户审计/月 | White-label |
|---|---|---|---|---|---|---|
| Starter | $299 | 2 | 1个品类 | 10个/周 | 1次/月 | ❌ |
| Pro | $599 | 10 | 3个品类 | 50个/周 | 4次/月 | ❌ |
| Agency | $1,199 | Unlimited | All 26 | Unlimited | Unlimited | ✅ |

Price anchor:
- Adbeat Reddit模块：$499/月（仅竞品spy，无基准线、无审计、无创意生成）
- SimilarWeb Paid Social: $299/月（仅总投放估计，无Reddit-specific任何东西）
- 独立Reddit Ads顾问：$200-$400/小时，做一次账户审计 = $3,000-$8,000（这个工具$599随时做）
- Performance代理佣金：客户月投放的15-20%。$50K/mo客户 = $7,500-$10,000/mo佣金。这个工具$1,199让代理一人管10个客户 → 利润翻倍。

典型ROI数学（Pro tier $599）：平均账户审计发现35-45%浪费。客户月投放$15K → 浪费~$6K/mo → 用了这个工具第一个月省$5K → 工具ROI 8.3x。后续每月节省稳定。客户投放越大，ROI越高。$50K投放客户= ~$20K/mo节省 / $599 = 33x ROI。
