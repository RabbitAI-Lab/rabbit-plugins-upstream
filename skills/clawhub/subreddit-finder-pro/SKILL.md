---
name: subreddit-finder-pro
version: "1.0.0"
category: marketing
sub_category: community-growth
tags:
  - reddit
  - subreddit
  - community
  - growth-hacking
  - customer-acquisition
  - indie-hacker
  - saas
  - founder
  - marketing
model: claude-sonnet-4-20250514
trigger_keywords:
  - subreddit
  - reddit marketing
  - find subreddit
  - reddit promotion
  - where to post reddit
  - reddit audience
  - subreddit finder
  - reddit niche
  - founder reddit
  - startup reddit
  - indie hacker reddit
pricing: "$19.00 basic / $29.00 pro monthly"
platforms:
  agensi: "$29.00 one-time"
  capafy: "$19.00 basic / $29.00 pro monthly"
---

# Subreddit Finder Pro — 精准目标子版块挖掘 + 文化画像

**The #1 reason Reddit marketing fails: you post in the wrong subreddit.**

GummySearch (the category leader, $30K+ MRR peak with 140,000 users) shut down in November 2025 when Reddit commercial API prices made its full-scan model uneconomical. Since then, founders and SaaS marketers have been guessing.

This Skill: **paste your product URL or a 2-sentence ICP description → get a ranked list of 10+ optimal subreddits with full cultural profile + karma/age thresholds + content survival rate prediction + self-promotion rules + recommended posting calendar.**

Reddit is now the **#1 most-cited domain in ChatGPT/Perplexity/Google AI Overviews (21% of all AI citations)**, so a Reddit post now has 3 value layers: original Reddit traffic + long-tail Google SEO (ranks for 3+ years) + AI answer compound reach.

**Who uses this?** Solo SaaS founders, indie hackers, freelancers, affiliate marketers, early-stage B2B marketers with <$5K/month marketing budget.

## Trigger Scenarios

Invoke this Skill when the user:
- Pastes a product URL: "which subreddits should I post my AI meeting notes tool to?"
- Describes ICP: "Where do B2B SaaS founders making $5K-$50K MRR hang out on Reddit?"
- Asks "I got shadowbanned posting my Etsy shop — which subs allow self-promotion?"
- Wants competitor intel: "Which subreddits does Notion / Linear get mentioned in?"
- Says "I'm launching on [date] — what's my Reddit content launch plan?"

## Prerequisites

- **Mandatory**: Product URL OR 2-sentence ICP (Ideal Customer Profile) description OR competitor product name
- Optional: user provides their own Reddit OAuth token (enriches data with subreddit rule APIs but the Skill works without — uses public RSS + cached subreddit metadata)
- No API key required for base functionality
- Works entirely on public Reddit data + pushshift historical datasets (cached, respects Reddit API rate limits 100% — no full subreddit scraping to avoid GummySearch's death trap)

## Workflow

### Step 1: Parse Product / ICP Input

If product URL provided:
- Crawl the landing page's <title>, <h1>, meta description, hero headline, 3 key feature bullets, pricing tier language, target audience cues
- Extract: category keywords (up to 15), audience persona words, pain point language

If ICP description provided:
- Extract structured: Industry, Role, Company size (employee count), Geography, Tech stack, Pain points, Budget level

Generate the Primary Search Vector: 15 weighted keywords + 5 audience persona tags.

### Step 2: Subreddit Discovery Engine

Run 4 parallel discovery modes:

**Mode A: Keyword Match** — Search Reddit's native subreddit search + cached 250K+ subreddit metadata for keyword overlap. Score: % of primary keywords that appear in sub name, description, sidebar rules, or top 100 post titles past 30 days.

**Mode B: Competitor / Category Co-occurence** — If competitor product known (e.g. Linear / Notion), find subs where competitor name appears >5 times in past 90 days. Co-occurrence = users who discuss competitor may discuss you.

**Mode C: Operator Sub Mapping** — For B2B products, map roles to operator subreddits:
```
Product Managers → r/ProductManagement (125K), r/ProductOps, r/ProductMarketing
Founders → r/Entrepreneur (2M), r/SaaS (200K), r/IndieHackers, r/startups (1.2M)
Dev Tools → r/webdev (2M), r/programming (6M), r/node, r/Python (6M)
VPs of Sales → r/sales (400K), r/SaaS (200K posts mention sales ops)
Marketers → r/marketing (2.3M), r/content_marketing, r/SEO (400K)
Consultants → r/consulting (350K), r/freelance (1M)
Agency Owners → r/agency, r/DigitalMarketing (900K)
```

**Mode D: Self-Promo Tolerance Filter** — Separate subs by self-promotion rule class:
```
Class A 🟢: Explicit self-promotion allowed, weekly threads
  (r/SideProject, r/IMadeThis, r/startups weekly promo, r/Entrepreneur Showoff Saturdays)
Class B 🟡: Implicit — value post first, MAY mention your thing in comments if relevant
  (r/SaaS, r/webdev, r/programming, r/marketing — but NOT in top-level post)
Class C 🔴: STRICT NO SELF-PROMO even in comments, autoban on link
  (r/AskReddit, r/todayilearned, r/science, r/pics, r/videos — massive subs but useless for you)
Class D ⚪: Shill-friendly / affiliate-tolerant subs (r/AffiliateMarketing, r/Emailmarketing, etc. — lower quality audience but easier)
```

Merge results: deduplicate, require minimum subscriber count threshold (<10K = ignore, unless engagement rate >20% which indicates hyper-niche goldmine).

### Step 3: Per-Subreddit Deep Dive (10 subs, ranked)

For each of the top 10 candidate subreddits, produce:

| Field | Data |
|---|---|
| **Rank** | 1–10 (weighted composite score) |
| **Subreddit Name** | r/Example |
| **Subscriber Count** | 147K (30d growth: +2,100 / +1.4%) |
| **24h Active Users** | 3,800 → Engaged Audience Estimate (EAE): ~11,400 (3x 24h active, Reddit formula) |
| **Operator Class** | Founders / SaaS / DevTools / PM / Marketer / Sales etc. |
| **Self-Promo Tolerance** | 🟢 Class A / 🟡 Class B / 🔴 Class C — with verbatim rule quote from sidebar |
| **Minimum Karma Threshold** | 100 karma + 30 days account age (detected by: 90% of posts in past 30d by accounts with >100 karma) |
| **Survival Rate Score (0-100)** | 78/100 = "If you post a VALUE POST (non-promo, teaching/sharing), 78% chance it's not removed in 4 hours. If you post a link to your product, 22% survival rate." |
| **Best Posting Window (localized)** | Mon 9am–12pm ET (highest mean upvote velocity based on past 30d top 100 post timestamps) |
| **Avg. Upvotes / Top Post** | 48 upvotes (post must get ~30 in first 4 hours to hit rising algo) |
| **Content Forms That Win** | Bullet list: "SaaS case studies with revenue numbers ($X MRR screenshots)", "Tech architecture diagrams", "AMA with founder who built [niche thing]", "Showoff Saturday posts before 10am ET", "Takedown / analysis of popular product" |
| **Content Forms That FAIL** | Bullet list: "Direct link to landing page with no context", "Generic 'check out my new startup'", "ChatGPT-created 'ultimate guide' spam", "Posts with affiliate links in top 3 comments", "Posts by accounts with 'Startup Founder' in username + no comment history" |
| **Cultural Signal: Top 3 Phrases That Get Upvotes** | E.g. "I built this in my garage", "made $X MRR", "solo founder", "here's what I learned", "shut down my last project" — extract from top 50 post titles NLP analysis |
| **Cultural Signal: 3 Phrases That Get Downvoted** | E.g. "revolutionary", "game-changing", "10x", "best on the market", "disrupt", "AI-powered" (overused / hype language) |
| **Active Competitor Mentions** | 34 mentions of "Linear" in past 90 days, 12 of which were comparison posts, 8 of which had critique-worthy top comments → good entry point |
| **Recommended Action** | 🟢 HIGH PRIORITY: Post a $X MRR case study next Monday 10am ET, then mention your product in a comment reply to a comparison thread / OR 🟡 MEDIUM: Spend 2 weeks commenting in value posts first, then post / OR ⏳ WAIT: Build karma elsewhere first |

**Composite Score Formula (0-100)**:
```
Score = Audience fit × 40% + Self-promo tolerance × 25% + Engagement rate × 20% + Survival rate × 15%

Example: r/SaaS
Audience fit: 95/100 (literally your ICP name in sub title)
Self-promo: 55/100 (Class B, no top-level promo but comments OK)
Engagement: 82/100 (200K subs, 6K 24h active = healthy 3%)
Survival: 91/100 (very few autobans if you follow rules)
→ COMPOSITE: 86.2/100 (your #1 choice)
```

### Step 4: Launch Plan Calendar

Append a **14-day Reddit content launch plan** based on the user's product type and top 3 subs:

```
## 📅 Your 14-Day Reddit Launch Plan

*Assumption: You have a Reddit account with ≥100 karma. If <100 karma → use Karma Coach Skill first, delay launch by 30 days.*

### Phase 1: Comment-only Warmup (Days 1-7)
| Day | Subreddit | Action |
|---|---|---|
| Day 1 | r/SaaS (med) | Comment depth on 2 top posts about churn. Use own founder experience. NO mention of product. |
| Day 2 | r/Entrepreneur | Comment depth on a "mistakes I made" post. Share 1 specific failure story. |
| Day 3 | r/IndieHackers | Comment on 2 revenue update posts. Congratulate OP, ask 1 specific follow-up question. |
| Day 4 | r/SaaS | Comment on a Stripe/Payments integration pain thread. Share actual technical lesson. |
| Day 5 | r/SideProject | Comment depth on 2 Showoff Saturday posts. Give constructive, specific feedback. |
| Day 6 | r/ProductManagement | Comment on a product-market-fit thread. Share your ICP discovery story. |
| Day 7 | (Any) | You should now have ~14-21 quality comments. Check karma: should be +20 to +80. If not → delay launch another week and keep commenting. |

### Phase 2: First Value Post (Day 8 or 9)
**Subreddit**: r/SideProject → 🟢 Class A — explicitly allows Showoff Saturday
**When**: Saturday 9am ET (Showoff Saturday thread goes live at 8am ET, post by 10am for maximum early visibility)
**Post format**: "I built [product name] because [specific, relatable pain story]. It's [1 sentence what it does]. Here's what it looks like: [screenshot 1 main UI, screenshot 2 key feature]. I'm a solo founder working on this for 3 months. AMA."
**Length**: 150-250 words. NO landing page link in the POST BODY. Put it ONLY in a top-level comment REPLYING TO YOUR OWN POST. Add context: "Landing page here if you want to try: [link]. The Reddit community gets a [discount / free trial code / early access] — use code REDDIT20."
**Follow-up**: Reply to EVERY comment within first 4 hours. This 4-hour window determines algorithm weight.

### Phase 3: Deep Value Post (Day 12-14)
**Subreddit**: r/SaaS → 🟡 Class B — no promo in top-level post
**Post format**: Long-form case study. Title: "How I built [X] as a solo founder: 6 months, 142 paying customers, $4,230 MRR, and what I'd do differently". Body: 400-800 words with specific numbers. NO links. NO "check out my tool". At the END of the post, a single sentence like: "If you're curious what I built it's [product name] — I won't link drop but you can find it in my profile bio or comment history."
**Why this works**: Long-form with specific numbers gets upvoted. The "find it in my bio" trick avoids autobans while still driving traffic.

---
🚨 **RULES TO NOT GET SHADOWBANNED**:
1. Never post the same content across >2 subreddits in a 7-day window
2. Never use URL shorteners (Bitly / TinyURL = instant shadowban)
3. Never DM more than 3 people per day per account
4. If you get shadowbanned: Stop posting for 7 days, then test with a harmless comment in r/test.
5. The account with which you promote should be 90% value comments, 10% self-promotion MAX.
```

### Step 5: Optional Competitor Reddit Radar

If user provides 1-3 competitor names: append a section showing which subreddits mention each competitor, with sentiment breakdown (from top 50 recent comments per mention):

```
## 🔍 Competitor Reddit Radar — Last 90 Days

| Competitor | Mentions | Top 3 Subreddits | Sentiment % (Positive/Neutral/Negative) |
|---|---|---|---|
| Competitor A | 68 | r/SaaS (21), r/ProductManagement (15), r/webdev (9) | 47% / 31% / 22% |
| Competitor B | 34 | r/IndieHackers (12), r/SideProject (8), r/Entrepreneur (5) | 62% / 28% / 10% |
| → Insight | Competitor B is LIKED but under-discussed. Post where they are absent. The 22% negative sentiment on A is an opening — find those comment threads, write a reply: "Have you tried [your product]? We built it specifically to fix [the exact negative complaint]." NO DIRECT LINK. Add profile bio trick. |
```

## Output Constraints

- **MUST include the 5-rule shadowban warning block in launch plans**. Never omit.
- All subreddit metadata fields must have actual numbers, not "N/A". If unknown, use cached averages and annotate "⚠️ Historical estimate".
- Karma threshold detection: Must explicitly state if account age requirement exists.
- Cultural Signal phrases (upvote / downvote) MUST come from NLP analysis of actual top 50 post titles, not generic advice.
- Self-promotion tolerance: Quote the sidebar rule VERBATIM (or closest paraphrase) — don't guess.
- Never promise specific traffic numbers ("this will get you 500 visitors"). Promise survival rates and relative engagement probabilities instead.

## What This Skill Does NOT Do

- ❌ Does NOT post to Reddit for you (requires user OAuth + HITL approval = Reddit Post Guardian Skill for that)
- ❌ Does NOT do full real-time subreddit scraping (avoids GummySearch's death by API costs; uses cached/historical + public RSS)
- ❌ Does NOT auto-DM Reddit users (TOS gray zone)
- ❌ Does NOT build karma for you (use Karma Coach Skill)
- ❌ Does NOT track conversions back to sales (use Reddit Mention Radar + Stripe attribution Skill)

## Pricing Logic

| Tier | Monthly | What's Included |
|---|---|---|
| Basic | $19/mo | 10 subreddit searches/month, 1 full ranked report per search, launch plan generator (1 product), competitor radar (max 1 competitor) |
| Pro | $29/mo | UNLIMITED subreddit searches, competitor radar (up to 5 competitors per search), multi-product launch plans, export results to CSV/Notion, save subreddit lists as "audiences" |
| LTD | $249 one-time | Pro tier, lifetime access. No recurring billing. (GummySearch sold $50K of LTD in 2 months → this pricing proven converts.) |

Price anchors against:
- GummySearch (pre-death): $19-$48/mo + $10 day pass + $50K LTD sales
- SubredditSignals: $19.99-$29+/mo
- Prowlo (GummySearch replacement): $19 flat / month
- SubHunt: Free tier + paid (not public pricing)
- Brand24 enterprise social listening: $99-$399+/mo

$19 Basic / $29 Pro lands exactly at the GummySearch-validated sweet spot. LTD option capitalizes on indie hacker's strong preference for buy-once (GummySearch did $50K LTD in 2 months with this exact model).
