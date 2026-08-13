---
name: reddit-mention-radar
version: "1.0.0"
category: marketing
sub_category: geo-seo
tags:
  - reddit
  - brand-monitoring
  - mentions
  - seo
  - geo
  - ai-citations
  - perplexity
  - chatgpt-citations
  - competitor-intel
  - reputation
model: claude-sonnet-4-20250514
trigger_keywords:
  - reddit mentions
  - brand monitoring reddit
  - reddit seo
  - reddit geo
  - ai citations
  - perplexity mentions
  - chatgpt sources reddit
  - competitor reddit
  - reddit reputation
  - google reddit ranking
pricing: "$19.00 basic / $49.00 pro monthly"
platforms:
  agensi: "$29.00 one-time"
  capafy: "$19.00 basic / $49.00 pro monthly"
---

# Reddit Mention Radar — 品牌+竞品监控 + Google排名识别 + GEO引用概率评分

**Reddit changed the Internet in 2025-2026.** Three massive shifts every founder needs to wake up to:

1. **Reddit is now the #1 most-cited domain in AI answers** (Profound Labs: analyzed 10M ChatGPT / Perplexity / Google AI Overviews citations → Reddit = 21% of all citations, more than Wikipedia, StackOverflow, and YouTube COMBINED.)
2. **Google-Reddit $60M/year data licensing deal (Feb 2024)** → Reddit now ranks in ~97% of product-review search queries. A Reddit comment can outrank your own landing page on your own brand search.
3. **Reddit-OpenAI ~$70M/year training data deal (2025)** → Reddit comments directly train GPT-5 / Claude 4.

This means a single Reddit post now has 3 value streams stacked:
```
Stream 1: Original Reddit traffic (users seeing your comment)
Stream 2: Google SEO for 3+ YEARS (Reddit posts are long-lived, sticky)
Stream 3: AI Citation compounding → ChatGPT/Perplexity quote Reddit to answer user questions → 10x the reach of Google alone
```

F5Bot is $17/mo but it's a pure keyword alert email with no SEO/GEO intelligence. Airefs ($24-$199/mo) does AI citation tracking but is enterprise-focused. CommunityMentions is $1,000/mo.

This Skill: **Monitor 5+ keywords (brand, product, competitors, pain points) → See all Reddit mentions, check which ones already rank in Google, score each one's probability of being cited by ChatGPT/Perplexity, get Slack/email/Telegram alerts, track positive/negative sentiment + reply intercept windows.**

**Who uses this?** SaaS founders, indie hackers, brand reputation managers, SEO agencies, AI-optimization (GEO) specialists, B2B marketers whose ICP lives on Reddit.

## Trigger Scenarios

Invoke this Skill when the user:
- Sets up radar: "Monitor [Brand Name], [Competitor A], [Competitor B], [pain phrase] on Reddit"
- Wants GEO check: "Which of my Reddit mentions are already in Google top 10? Which will be cited by Perplexity?"
- Weekly digest: "Give me brand mentions weekly report with sentiment + GEO scores"
- Competitor intel: "What are people saying bad about [competitor] this week? I want to reply with our product as solution."
- Crisis alert: "Alert me immediately if my brand gets >5 negative mentions in 24h"

## Prerequisites

- **Mandatory**: 1-5 keywords (Basic) / 5-50 keywords (Pro)
  - Keyword types allowed: Brand names, product names, competitor names, founder names, exact pain-point phrases, category phrases
- GEO Lookup: Uses public Google search API (SerpAPI free tier 100 searches/mo user provides their own key — OR Skill caches last-known Google positions for known Reddit URLs and does incremental update)
- Citation prediction: Uses citation-probability ML model (heuristic-based, no external API — 7-factor formula below)
- Alert channels: Email, Slack incoming webhook, Telegram bot token (user provides). Can run as frequently as every 15 minutes for crisis keywords, but default daily digest (respects API costs).

## Workflow

### Step 1: Keyword Setup & Classification

```
📡 KEYWORD CONFIGURATION
───────────────────────────────────────
Tier A — BRAND / FOUNDER NAMES (Instant alert, 15-min cadence)
  [YourBrand]
  [YourProduct]
  [Founder Name] + Reddit username if public
  Trigger ANY mention: POSITIVE / NEGATIVE / NEUTRAL

Tier B — COMPETITOR NAMES (Daily digest)
  Competitor A
  Competitor B
  🔴 Sub-filter: "Competitor A" + negative sentiment words = 4h priority alert
  (Intercept window: 36 hours — competitor user is upset → reply with YOUR solution)

Tier C — PAIN-POINT PHRASES / CATEGORY (Daily digest)
  "hate [category tool]"
  "too expensive [category]"
  "alternative to [category]"
  "frustrated with [pain point]"
  "switching from [legacy tool]"

Tier D — CRISIS WORDS (Instant alert, combined with Brand Tier A)
  [YourBrand] + "scam" / "stole" / "sued" / "data leak" / "hacked" / "shut down"
  → Negative Tier D + Tier A overlap = SOUND THE ALARM: push within 15 minutes to phone (SMS via Telegram/Slack priority)
```

### Step 2: Mentions Ingestion + 7-Factor GEO Scoring

For EACH mention pulled, run all 7 GEO (Generative Engine Optimization) factors:

```
🧮 GEO CITATION PROBABILITY (0-100) — Will ChatGPT/Perplexity quote this Reddit comment?
─────────────────────────────────────────────────────────────────────────
Factor 1: Google SERP Position (does the Reddit URL rank top 10 for relevant search?)
  → Weight 30%. Google #1 = 30 pts. #2-3 = 25. #4-10 = 15. #11-20 = 5. Not in top20 = 0.
  → (This is STRONGEST predictor. AI engines pull from Google's index first.)

Factor 2: Reddit Comment Score & Upvotes
  → Weight 20%. Score >200 upvotes = 20 pts. 50-199 = 15. 10-49 = 10. 1-9 = 3. 0 or negative = 0.
  → (Upvotes = social proof AI models weight heavily)

Factor 3: Comment Length & Structured Information Density
  → Weight 15%. 200-500 words, 3+ specific points (numbers, comparison, step-by-step) = 15 pts.
  → <50 words (one-liner) = 0 pts. 50-200 words medium = 5 pts. >500 words unstructured = 8 pts.

Factor 4: Sentiment Neutrality & Balance
  → Weight 10%. Balanced review (both pros + cons, not unhinged rant or gushing shill) = 10 pts.
  → One-sided extreme sentiment = 2 pts. AI models CITE neutral sources MORE. (Profound data)

Factor 5: Domain Authority of Subreddit + Account Age/Karma
  → Weight 10%. r/[industry] with >100K subs + comment from >1y/1k karma account = 10 pts.
  → New accounts / low-karma subs = 0-2 pts.

Factor 6: Recency (is this answer FRESH?)
  → Weight 10%. Posted <90 days = 10 pts. 90-365 days = 5 pts. 1-2 years = 2 pts. >2 years = 0.
  → (AI freshness penalty for 2+ year old information — especially if technology changed)

Factor 7: "Quote-Worthy" Phrase Score
  → Weight 5%. Contains concise, quotable standalone sentence (e.g. "I tested 12 tools and [X] was the only one that didn't crash during 8-hour exports") = 5 pts.
  → Generic "it's good" = 0 pts.

─────────────────────────────────────────────────────────────────────────
Interpretation of TOTAL GEO Score (0-100):
75-100  → 🏆 CITATION MAGNET: This comment WILL / IS being quoted in AI answers.
         → ROI priority: MAXIMUM. If it's POSITIVE about your brand → amplify. If NEGATIVE → fix within 48h.
50-74   → 🟡 LIKELY TO BE CITED within 6 months if upvotes grow.
25-49   → 🔴 Unlikely to be cited organically. If it's a negative comment, safe to ignore for AI. If positive, you can seed links from other sources to boost its Google rank → score up.
0-24    → ⚪ Noise. No AI value, but still track for sentiment/trends.
```

### Step 3: Daily Mention Radar Format

Structure:

```
📡 REDDIT MENTION RADAR — DAILY DIGEST — Aug 12, 2026
──────────────────────────────────────────────────────────
📊 TODAY'S SUMMARY:
Total Mentions: 62
  Brand (Tier A): 14 (7 positive, 4 neutral, 3 negative)
  Competitors (Tier B): 28 (12 A, 16 B)
  Pain Points (Tier C): 18
  Crisis Triggers (Tier D): 0 ✅

GEO SCORE DISTRIBUTION (of all 62 mentions):
🏆 Citation Magnet 75+: 3 mentions
🟡 Likely 50-74: 11 mentions
🔴 Unlikely 25-49: 22 mentions
⚪ Noise 0-24: 26 mentions

──────────────────────────────────────────────────────────
🏆 #1 TOP GEO MENTION — Citation Magnet 92/100
──────────────────────────────────────────────────────────
Keyword Match: [YourBrand] (Tier A Brand)
Subreddit: r/SaaS (200K subs, 🔴 TARGET ICP MATCH)
Comment Author: u/pragmatic_dev (4.2y karma 8.4K ✅ Real)
Posted: 2 days ago (Aug 10) | Comment Score: 247 upvotes, 38 replies 🔥🔥
Link to comment: [Reddit permalink]

💬 Comment Text (partial):
  "I went through 12 project management tools in the last 3 months trying to replace Linear (they raised prices 40% and our startup couldn't afford it anymore).
  I tried Asana, Monday, ClickUp, Wrike, Height, Basecamp, Notion Projects, and a bunch of indie ones.
  [YourBrand] was the only one that didn't crash during 8-hour exports of our 2-year ticket backlog. The rest of them timed out or corrupted 20%+ of ticket attachments.
  Support got back to me in 2 hours on a Sunday when I had an import issue.
  It's not perfect — the mobile app still needs dark mode, and the burndown chart is basic. But for $5/user/month vs Linear's $14 now? It's not even close.
  I've been recommending it to every bootstrapped founder group I'm in."

📊 GEO SCORE BREAKDOWN: 92/100 🏆
→ Google SERP: #2 for "[Brand] vs Linear comparison" (30/30)
→ Reddit Score: 247 upvotes (20/20)
→ Density: 360 words, specific numbers (12 tools, 8h exports, 40% price rise, $5 vs $14, 2h Sunday support) (15/15)
→ Sentiment: Balanced! Both pro (8h export stability, price, support) AND con (no mobile dark mode, basic burndown) = extremely quotable (10/10)
→ Authority: r/SaaS 200K + 4.2y/8.4K account (10/10)
→ Recency: 2 days (10/10)
→ Quote-worthy: ✅ "I tried 12 tools and [X] was the only one that didn't crash during 8-hour exports" (5/5)

Google Rank Check: ✅ This specific comment URL ranks #2 on Google for "[Brand] Linear comparison" search. Estimated 800-1,200 visits/month from Google alone = $1,500+/month in equivalent AdWords value (if you had to buy those clicks).
AI Citation Check: ✅ Perplexity.ai search "[Brand] vs Linear 2026" → does it QUOTE this comment? [YES / NO / PARTIAL — check result]
→ If YES: Estimated additional 2,000-5,000 AI reach per month = Priceless (AI answers don't have CPC yet).

🎯 RECOMMENDED ACTION:
1. ✅ URGENT: Save this comment link, screenshot it, put it on your landing page TESTIMONIALS section (with permission — DM user and ask: "Love your balanced review, would you mind if I quoted you on our site with a link back to your comment? Most users say yes when you ask nicely + link back.")
2. ✅ Reply within thread (if not too old): "Hey, [YourBrand] founder here. Thanks for the honest review — the dark mode mobile push is scheduled for v2.18 on Sept 5. Ping me if you want to beta test it and I'll comp you a month for the feedback." (Founder reply → community trust boost + more upvotes → higher Google rank → higher GEO score)
3. ✅ Reply to EVERY sub-comment under this parent (38 replies — 4 hours of work but compounds SERIOUS community goodwill). Your replies get upvoted too, your username becomes known.
4. Long-term: Drop this Reddit link as a backlink from your newsletter + 1 relevant blog post → pushes it from Google #2 → #1 = +50% more traffic.

──────────────────────────────────────────────────────────
🔴 TOP 3 NEGATIVE BRAND MENTIONS
──────────────────────────────────────────────────────────
(Format: Similar but includes "Negative Sentiment Level" + "Response Time Window" + "Reply Crisis Draft")

NEGATIVE #1: GEO Score 78/100 🔴 DANGEROUS (highly citeable NEGATIVE review)
Comment: "Tried [YourBrand] for 2 weeks — import corrupted my 3-year ticket history and support took 3 days to reply (even though they advertise 2h response). Back to Linear, never again."
→ Subreddit: r/business (890K subs) / 84 upvotes / ranks #8 Google for "[Brand] import problems"
→ Response Window: 36 HOURS. Every hour past 36h = 10% less likely user edits/deletes.
→ Suggested Founder Reply Draft (72 hours max to get pinned):
  > Hey sorry to hear about the import issue — [Brand] founder here. The 3-day response delay that weekend was because we had a Postgres incident that took down half the ticket system (we posted about it on status.[Brand].com but that only notifies existing users, not people going through the import flow which was wrong of me).
  > If you PM me the email you used with us I'll personally pull your corrupted export, fix it, and get you a working CSV within 24h. I'll also comp you 3 months free if you want to give us another shot (no pressure either way).
  > And the support SLA issue — you're right, we don't hit the 2h target during infrastructure incidents. I'll fix that this week by routing critical support tickets to my personal phone after-hours.
  > No excuse — this was a bad experience and we own it.

→ Follow-up: 72h later, if user responds positively, DM asking if they'd consider editing their original post to add "Founder reached out within the hour, fixed the file, 3 months free — fair response." (About 40% of people WILL edit when you take real ownership + action — this changes the Google-ranked review from NEGATIVE to balanced = massive GEO risk mitigated.)

(Then 2 more negative mentions with similar format.)
```

### Step 4: Weekly GEO Trend Report + Competitor Intercept Window

Weekly, output:
```
📊 WEEKLY GEO TREND REPORT (Aug 5-11, 2026)
───────────────────────────────────────────
Your Brand: Reddit Mentions +42% WoW (62 vs 43 last week)
  → Positive: % (from 47% → 52%)
  → GEO Citation Magnet (>75) count: 3 this week vs 1 last week (GOOD, your community engagement is working)
  → Est. Google traffic from all ranked Reddit comments: 4,200 visits (~$7,800 AdWords equivalent value = FREE)
  → Est. AI answer citations (Profound API estimate): ~18,000 AI answer exposures (PRICELESS)

Competitor Landscape:
  Competitor A: 12 negative mentions this week (vs 2 last week)
  → 5 of 12 are "import corruption" exactly the same complaint Competitor A has ignored for 3 months.
  → 🔴 YOUR INTERCEPT WINDOW: Go reply to all 5 with our product's import feature success story + data (case study link). ~15-30% conversion on competitor intercepts when the competitor has dropped the ball publicly.
  Competitor B: 4 negative mentions about price raise (similar to what Competitor A did 2 months ago). Reply with your "bootstrapped, no VC → no price raise ever" positioning.

Reddit SEO Health:
  Top 10 Google-ranked Reddit URLs mentioning your brand: up from 4 → 6 this month.
  Average rank: #6.8 (up from #8.2 last month = trend is GOOD)
  Low-hanging fruit: 3 Reddit threads at #11-15 that need 5-10 more upvotes to hit top10 → go reply to them with additional context (upvote + comments push rankings up within days).

Action Plan for Next Week (7 items):
1. 🔴 Fix negative mention #1 above (72h response window)
2. 🟢 Intercept 5 Competitor A "import corruption" threads
3. 🟢 DM user of top Citation Magnet 92/100 for testimonial permission
4. 🟢 Reply to + comment on 3 rank #11-15 threads to push them top10
5. 🟡 Add "Reddit Reviews" carousel slide to homepage (already have 3 ranked threads)
6. ⚪ Monitor Tier D crisis words during product update release
7. ⚪ Run 1x monthly competitor GEO audit (what are their high-scoring negative threads we can intercept)
```

### Step 5: Crisis Alert Thresholds (Instant Push)

Email/Slack/Telegram push triggers:
- Brand + 1 Crisis keyword (scam / hacked / data leak) = IMMEDIATE PUSH within 15 minutes
- Brand + negative sentiment volume: >5 negative mentions in rolling 24h window = ALERT
- Competitor + mass exodus pattern: >10 mentions of "switching from Competitor A" in 24h = ALERT (intercept window open)

## Output Constraints

- **Mandatory GEO score breakdown**: EVERY mention >50 score must show the 7-factor breakdown (how many points each factor contributed). Never output just a number.
- **Mandatory Google Rank Check**: Explicitly state which of the top 3 mentions are in Google top 10, with search query that ranks them. If no SerpAPI key provided, annotate "⚠️ Google rank data not available. Provide SerpAPI free key for accurate tracking."
- **Mandatory crisis response templates**: Negative mentions >70 GEO score MUST include a specific founder reply draft (not generic "sorry you had issues"). Draft must include: Founder identity disclosure → specific ownership of problem → concrete action → time-bound → no-excuse closing line.
- **Never overpromise ROI**: State ranges ("~4,200 visits, ~$7,800 AdWords EQUIVALENT value" — not "this made you $7,800 this week")
- **Never fabricate comment text**: If comment is long + truncated, show 200 chars around keyword match + permalink for user to verify full text. Never invent upvote numbers.

## What This Skill Does NOT Do

- ❌ Does NOT reply to comments for user (generates reply drafts only — HITL principle)
- ❌ Does NOT scrape full subreddits (keyword pull only — avoids GummySearch API death)
- ❌ Does NOT track Twitter/LinkedIn/HackerNews comments (strictly Reddit — multi-platform is Syften/Brand24 territory, overkill for this Skill focus)
- ❌ Does NOT remove Reddit comments or DM other users to delete negative mentions (ethics: users have right to their criticism — you fix the product, you don't silence critics. The reply-intercept method IS the legitimate way to manage reputation.)
- ❌ Does NOT provide sentiment analysis of private Reddit DMs (only public comments/posts)

## Pricing Logic

| Tier | Monthly | Features |
|---|---|---|
| Basic | $19/mo | 5 keyword phrases, 1 user/brand, daily digest, GEO 7-factor scoring, sentiment classification, crisis alert (email only), 30-day history |
| Pro | $49/mo | 50 keyword phrases, 3 competitor brands + brand monitoring, hourly scan cadence, Telegram/Slack alerts, Google SerpAPI rank tracking, weekly trend reports, CSV export, AI citation prediction confidence (heuristic), 12-month history tracking, saved response templates |
| Team | $149/mo | 5 team seats, unlimited keywords, white-label PDF client reports, Slack multi-channel routing, webhook API, unlimited history, agency dashboard |

Price anchors against:
- F5Bot Power: $17/mo (NO GEO, 90% noise, NO Google rank, NO reply drafts)
- Airefs (AI citation tracking): $24 Basic / $99 Pro / $199 Enterprise (just citations, no Reddit-specific)
- CommunityMentions: $1,000+/month (enterprise, out of indie reach)
- Brand24: $99-$399+/month (10+ platforms, overkill for Reddit-focused indie founder)
- Syften: From $19/mo (Boolean only, NO AI scoring)

$19/$49 price point: Under $20 = indie founder coffee/month comparison. Pro tier includes the UNIQUE combination: Reddit mentions + GEO citation score + Google rank + competitor intercept window. No other tool has all 4 in this price band. The "AdWords equivalent value" metric ($7,800/mo for a successful thread) is a staggering 160x ROI on the $49/mo Pro tier — this converts.
