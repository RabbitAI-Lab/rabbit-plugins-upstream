---
name: seo-keyword-research-pro
version: "1.0.0"
category: marketing
tags:
  - seo
  - keyword-research
  - content-strategy
  - semrush
  - ahrefs
  - google-keywords
  - search-volume
  - content-gap
  - serp-analysis
model: claude-sonnet-4-20250514
trigger_keywords:
  - keyword research
  - SEO strategy
  - search volume
  - keyword difficulty
  - content gap
  - SERP analysis
  - long-tail keywords
  - keyword cluster
  - search intent
  - topic cluster
pricing: "$7.99 one-time"
---

# SEO Keyword Research Pro

> **End-to-end keyword research workflow: seed keyword expansion, search intent classification, difficulty scoring, SERP gap analysis, and topic cluster creation.** Outputs a prioritized content calendar with ROI estimates.

## Why This Skill Exists

Keyword research tools (Ahrefs, Semrush) cost $100-400/month. Most creators and indie hackers can't justify that cost. This skill encodes the same methodology into a structured workflow using free data sources (Google Suggest, People Also Ask, SERP analysis) and produces actionable content plans.

## When to Activate

Activate when the user:
- Asks for keyword research, SEO strategy, or content ideas
- Mentions search volume, keyword difficulty, or search intent
- Wants to find content gaps or topic clusters
- Says "what should I write about" or "what keywords to target"
- Plans a content calendar or blog strategy

## Workflow

### Step 1: Seed Keyword Expansion

Given a seed keyword/topic, generate expanded keyword lists:

**Category 1: Head Terms** (1-2 words, high volume, high difficulty)
- Example: "project management", "task tracker"

**Category 2: Body Keywords** (3-4 words, medium volume, medium difficulty)
- Example: "project management for startups", "task tracker for teams"

**Category 3: Long-Tail Keywords** (5+ words, lower volume, low difficulty)
- Example: "best project management tool for remote startups", "free task tracker for small teams"

**Category 4: Question Keywords** (from Google PAA, Reddit, Quora)
- Example: "how to choose project management software", "what is the best free task tracker"

**Expansion Sources:**
- Google Suggest (autocomplete variations)
- Google "People Also Ask" questions
- Google "Related Searches"
- Reddit/Quora thread titles
- Competitor blog post titles
- Forum discussions (Stack Overflow, Hacker News, Product Hunt)

### Step 2: Search Intent Classification

Classify each keyword into one of four intent types:

| Intent | User Goal | Content Format | Example |
|--------|-----------|---------------|---------|
| **Informational** | Learn something | Blog post, guide, tutorial | "what is agile project management" |
| **Navigational** | Find specific site/brand | Landing page | "asana login", "jira pricing" |
| **Commercial** | Compare options before buying | Comparison, review, listicle | "best project management tools 2026" |
| **Transactional** | Ready to buy/sign up | Product page, pricing, demo | "buy asana premium", "jira free trial" |

### Step 3: Keyword Difficulty Estimation

Score each keyword 1-100 based on:

| Factor | Weight | How to Estimate (Without Paid Tools) |
|--------|--------|--------------------------------------|
| Domain Authority of top 10 SERP results | 40% | Check if sites like Wikipedia, Forbes, or major brands rank — if yes, difficulty is high |
| Content depth of top results | 20% | Do top results have 2000+ words? Difficulty is higher |
| Backlinks to top results | 20% | More referring domains = harder to outrank |
| SERP feature saturation | 10% | Featured snippets, PAA, image packs reduce organic opportunity |
| Search volume | 10% | Higher volume = more competition |

**Scoring bands:**
- 1-30: 🟢 Easy — new sites can rank in 3-6 months
- 31-50: 🟡 Moderate — needs 20+ quality backlinks, 6-12 months
- 51-70: 🟠 Hard — needs established domain, 12+ months
- 71-100: 🔴 Very Hard — avoid unless you have strong domain authority

### Step 4: SERP Gap Analysis

For top 3 target keywords, analyze the current SERP:
- What content formats rank (listicle, how-to, comparison, video)
- Average word count of top 10 results
- Common subheadings/topics covered by all top results
- **Gaps**: topics your competitors are NOT covering that you should
- **SERP features**: featured snippets, PAA, image packs, video carousels
- Content freshness: when were top results last updated?

### Step 5: Topic Cluster Creation

Organize keywords into topic clusters:

```
Pillar Page: "Project Management Guide"
├── Cluster: "Agile Methodology"
│   ├── "what is agile project management" (Informational, KD: 25)
│   ├── "agile vs waterfall" (Commercial, KD: 35)
│   └── "agile sprint planning guide" (Informational, KD: 20)
├── Cluster: "Project Management Tools"
│   ├── "best project management tools 2026" (Commercial, KD: 45)
│   ├── "free project management software" (Commercial, KD: 40)
│   └── "asana vs jira vs monday" (Commercial, KD: 30)
├── Cluster: "Team Collaboration"
│   ├── "how to manage remote teams" (Informational, KD: 28)
│   └── "team communication best practices" (Informational, KD: 22)
```

### Step 6: Prioritized Content Calendar

Output a 90-day content calendar:

```markdown
## 90-Day Content Calendar

### Month 1: Foundation (Low KD, High Intent)
| Week | Keyword | Intent | KD | Est. Volume | Content Type | Word Count | Priority |
|------|---------|--------|-----|------------|-------------|------------|----------|
| 1 | "what is agile project management" | Info | 25 | 2,900 | Guide | 2,500 | 🔴 High |
| 1 | "agile vs waterfall" | Commercial | 35 | 1,900 | Comparison | 2,000 | 🔴 High |
| 2 | "free task tracker for small teams" | Commercial | 28 | 880 | Listicle | 1,500 | 🟡 Med |
| 3 | "how to manage remote teams" | Info | 28 | 1,300 | Guide | 2,000 | 🟡 Med |
| 4 | "agile sprint planning guide" | Info | 20 | 720 | Tutorial | 1,800 | 🟡 Med |

### Month 2: Authority Building (Medium KD)
[... similar table ...]

### Month 3: Competitive (Higher KD, High ROI)
[... similar table ...]

## ROI Estimation

| Keyword | Est. Monthly Traffic (3 months) | Est. Monthly Traffic (12 months) | Conversion Rate | Est. Revenue/Month |
|---------|-------------------------------|--------------------------------|----------------|-------------------|
| "best project management tools" | 150 | 800 | 2% | $480 |
| "free task tracker" | 80 | 400 | 1.5% | $180 |
```

## Output Constraints

- All keyword suggestions must include estimated difficulty score (1-100)
- All keywords must have search intent classified
- Content calendar must be ordered by priority (Low KD + High Intent first)
- Topic clusters must show pillar→cluster hierarchy
- ROI estimates must be conservative (use 1-3% conversion rate)
- Mark all estimates with "est." — never present as exact data without a paid API

## What This Skill Does NOT Do

- Does not access paid keyword tool APIs (Ahrefs, Semrush, Moz)
- Does not provide exact search volumes (estimates only)
- Does not track rankings over time
- Does not build backlinks
- Does not write the content (plans the strategy only)
