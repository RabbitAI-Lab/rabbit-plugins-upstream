---
name: prospecting
version: 2.0.1
last_updated: 2026-08-19
changelog: |
  - v2.0.1: Security audit fixes — split strong/weak triggers, added compliance & data retention sections, removed placeholder phone examples, added outreach boundaries.
  - v2.0.0: Added self-optimization protocol, coverage gap reporting, chain brand learning, and suburban expansion rules.
  - v1.0.0: Initial release with multi-center search, chain strategy, and 3-layer output.
description: >
  B2B manufacturing proactive prospecting. Search Google Maps for potential customers based on
  existing client profiles, enrich leads with business details, score and rank them, and output
  actionable CSV + JSON lead lists with custom sales openers.
  Includes chain store strategy: local call → identify procurement decision chain → escalate to corporate.
  Use when: finding new customers, prospecting, lead generation, searching for potential clients,
  building a call list, or when user mentions existing customers they want to find more like.
triggers: |
  STRONG (auto-run): run prospecting for, build a call list for, find prospects for,
    search leads for, find similar customers to, prospect like
  WEAK (ask first): prospect, find customers, lead gen, call list,
    获客, 找客户, 搜客户, 潜在客户, 主动获客
---

# Prospecting — B2B Lead Generation from Existing Customers

## Overview

Turn existing customers into a search template → find similar businesses on Google Maps → enrich → score → output actionable call lists.

**One line**: Known customer → profile → Maps search → enrich & rank → CSV call list + JSON index

## Compliance & Legal Boundaries

Before running this skill, confirm:

| Item | Requirement |
|------|-------------|
| **Geography** | Only collect businesses in jurisdictions where B2B outreach is lawful |
| **Data source terms** | Comply with Google Maps Terms of Service, Yelp ToS, and any site scraped |
| **Rate limiting** | Add reasonable delays between requests; do not hammer the same site |
| **Do-not-call / anti-spam** | Respect opt-out lists and local telemarketing rules |
| **Privacy laws** | GDPR / CCPA / PIPL: avoid collecting unnecessary personal contact info |
| **Data accuracy** | Only use publicly listed business contact info; do not enrich personal mobile numbers or home addresses |

This skill collects **publicly visible business information only**. Do not use it to harvest personal emails, mobile phones, home addresses, or non-business contacts.

## Data Retention & Storage

| Rule | Implementation |
|------|----------------|
| **Output path** | `prospect-data/{batch}/` under the user's workspace |
| **Retention** | Delete or archive prospect files when the campaign ends or they are no longer active |
| **Sensitive data** | Do not store personal mobile numbers or non-business contacts |
| **Sharing** | Do not share raw JSON/CSV with third parties without consent |
| **Encryption** | Move completed batches to encrypted storage if required by your policy |
| **Access** | Treat call lists and profile JSON as internal sales data; restrict access to authorized users |

## When to Use

- User gives a customer name + location and asks to find similar businesses
- User asks to build a prospect/call list
- User wants to find new clients in a specific industry (auto body, manufacturing, HVAC, etc.)

## Input Required

| Field | Required | Notes |
|-------|----------|-------|
| Company name | ✅ | Core search term |
| Location (city/state) | ✅ | Search center point |
| Product purchased | ❌ | Helps with profiling |

Even minimal input ("Bob's Auto Body, Orange CA") can start the full flow.

## Execution Flow

### Step 0: Self-Diagnostic & Adaptive Search Design (NEW — Auto-Optimization)

Before executing searches, the skill **automatically analyzes search parameters** and adjusts strategy without user intervention:

#### 0.1 Coverage Gap Detection
After initial search round completes, automatically check for these warning signals:

| Warning Signal | Threshold | Auto-Action |
|---------------|-----------|-------------|
| Zero results for keyword+center | 0 listings returned | **Swap keyword** (e.g., "paint shop" → "auto paint" / "car paint" / "collision") |
| Low unique yield per center | <5 unique businesses per center after dedup | **Expand radius** or **add satellite center** |
| High non-target ratio | >30% listings are wrong industry | **Tighten keyword** (e.g., "paint shop" → "auto body paint" / "collision paint") |
| Chain under-representation | 0 chain brands in results | **Add brand keywords** (Caliber, CARSTAR, Maaco, Gerber) |
| Equipment-related missing | No spray booth / frame machine in results | **Add equipment keywords** to second pass |

#### 0.2 Keyword Auto-Adjustment Rules
```
IF center + "paint shop" returns <5 valid auto-body listings:
  → REPLACE with "auto paint shop" OR "car paint" OR "collision paint"
  
IF center + "auto body shop" returns 0 results:
  → TRY "body shop" OR "collision repair" OR "auto repair"
  
IF chain brands known in industry but missing from results:
  → ADD "[brand] + city" as explicit search (e.g., "Caliber Houston")
```

#### 0.3 Multi-Pass Search Protocol
```
PASS 1: Core keywords (auto body shop, collision repair, paint shop)
  ↓
Auto-analyze coverage gaps
  ↓
PASS 2: Gap-fill keywords (adjusted based on PASS 1 results)
  ↓
PASS 3: Equipment/brand keywords (spray booth, frame machine, Caliber, CARSTAR)
  ↓
Final dedup + scoring
```

**No user input required** — the skill self-diagnoses and adjusts between passes.

### Step 1: Profile the Existing Customer (8-step fixed process)

Read [references/profiling.md](references/profiling.md) for the full 8-step process. Key actions:

1. **Google Maps deep dive** — Use agent-browser to search `[company name] [location]`, extract: address, phone, rating, review count, business type, hours, website, photos, chain status
2. **Review sampling** — Sample reviews with keyword filtering (not all reviews). Generic keywords: `new, expand, equipment, upgrade, install, moved, bigger` + industry-specific keywords (e.g., for auto body: `paint booth, insurance, fleet, dealer`)
3. **Social/web enrichment** — Only for 🔴 chain (FB+LinkedIn+website) or 🟡 mid-tier (FB+website). Skip 🟢 small (no website)
4. **Output a Profile Card** — Standard format saved to `prospect-data/{batch}/profile-{name}.json`

**Tier detection** (determines enrichment depth):
- 🔴 Chain/large: name contains chain markers OR >200 reviews
- 🟡 Mid-tier: has website, 50-200 reviews
- 🟢 Small: no website, <50 reviews

### Step 2: Maps Batch Search (agent-browser automated, with self-optimization)

**Read [references/search-strategy.md](references/search-strategy.md) for the complete search framework.**

**NEW: Self-Optimizing Search Loop**

The search now runs in **3 automatic passes** with gap detection between each:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   PASS 1        │     │   PASS 2        │     │   PASS 3        │
│   Core keywords │────→│   Gap-fill      │────→│   Equipment/    │
│   (4-6 per      │     │   (auto-adjusted│     │   Brand deep    │
│    center)      │     │   based on P1)  │     │   dive          │
└─────────────────┘     └─────────────────┘     └─────────────────┘
       ↓                       ↓                       ↓
   [Auto-analyze]          [Auto-analyze]           [Final dedup]
   Coverage gaps            Remaining gaps           + Score
```

#### Pass 1: Core Search (always runs)
- **Multi-center**: Large cities (>2M) use 4-6 search centers
- **Keyword matrix**: 4-6 keywords per center (core + service + equipment + brand + scene)
- **Pagination**: Scroll and load 3 times per search
- **Deduplication**: Cross-center, cross-keyword deduplication

#### Pass 2: Gap-Fill (auto-triggered if gaps detected)

After Pass 1 completes, **automatically check**:

| Check | Condition | Auto-Action |
|-------|-----------|-------------|
| Zero-result centers | Any center returned 0 listings for >2 keywords | Add 1-2 satellite centers (midpoint between existing centers) |
| Low-yield keywords | Any keyword returned <3 valid listings across all centers | Replace with synonym (see Keyword Swap Table below) |
| Missing chains | Known chain brands not found | Add explicit brand+city searches |
| Geographic holes | Large gaps between centers | Add midpoint center |

**Keyword Swap Table** (auto-applied):
| Original (low yield) | Replacement 1 | Replacement 2 | Replacement 3 |
|---------------------|---------------|---------------|---------------|
| paint shop | auto paint shop | car paint | collision paint |
| auto body shop | body shop | collision repair | auto repair |
| collision center | collision repair | auto body repair | crash repair |
| frame machine | auto frame | chassis repair | structural repair |
| spray booth | paint booth | auto paint booth | HVLP booth |

#### Pass 3: Equipment & Brand Deep Dive (auto-triggered)

If target industry involves equipment (auto body, manufacturing, HVAC), **automatically add**:
- Equipment keywords: `spray booth`, `frame machine`, `car lift`, `CNC mill`, etc.
- Brand searches: `[Brand] + [City]` for known chains (Caliber, CARSTAR, Maaco, Gerber, Crash Champions)

**Search execution**:
1. For each center point × each keyword: open Google Maps, extract listings, paginate 3x
2. Collect: name, phone, address, rating, review count, business type, website status, chain markers
3. Dedup: same name + same address = duplicate
4. Remove: permanently closed, non-target industry

**Save to**: `prospect-data/{batch}/candidates-raw.txt` (raw extraction log) + `candidates.json` (deduplicated)

**Auto-optimization logging**: After each pass, append to `candidates-raw.txt`:
```
[PASS-N-ANALYSIS] Center: X, Keyword: Y, Results: Z, Action: [none|swapped|expanded|added-brand]
```

### Step 3: Auto-Tier Candidates (with self-validation)

Based on Maps data, assign tiers. **Chain stores are NOT excluded** — they are valid prospects with a different approach strategy.

**NEW: Self-Validation Checklist** (auto-executed before tiering)

Before finalizing candidates, automatically verify:

| Check | Action if Failed |
|-------|-----------------|
| Duplicate names with different addresses | Mark as chain locations, keep all |
| Same name + same address appearing multiple times | Deduplicate, keep most complete |
| Business type mismatch (e.g., "car wash" labeled as "collision") | Re-classify or flag for manual review |
| Phone placeholder pattern (555, 000, 1234) | Flag as `phone_status: unverified_placeholder` |
| Address in different city than search center | Verify: satellite location vs data error |

**Auto-chain detection** (no manual list needed):
```
IF name contains: Caliber, CARSTAR, Maaco, Gerber, Crash Champions, ProColor, 1st Choice
  → Mark as chain_brand: [detected brand]
  
IF same name appears in >2 different addresses across centers
  → Mark as chain_brand: [normalized name]
  → Set tier: "连锁-XX"
```

| Tier | Criteria | Next action |
|------|----------|-------------|
| 🔴 Chain/large | Chain name OR >200 reviews OR multi-location detected | Deep enrichment + **chain procurement strategy** |
| 🟡 Mid-tier | Has website, 50-200 reviews | Medium enrichment |
| 🟢 Small | No website, <50 reviews | Skip enrichment |

**Chain store prospecting strategy** — Read [references/chain-strategy.md](references/chain-strategy.md) for the full three-call approach:

- **Call 1**: Local store — NOT to sell, but to identify procurement decision chain
- **Call 2**: Regional/corporate — pitch to the person who can approve multi-location deals
- **Call 3**: Follow-up with proposal

Key principles:
- Chain stores have large, stable equipment needs — one deal can cover multiple locations
- Local store manager is the entry point, not the decision-maker (usually)
- Key question: "Is equipment purchasing handled locally, or should I speak with your regional/corporate procurement team?"

### Step 4: Enrich by Tier

| Tier | Action | Tools | Time |
|------|--------|-------|------|
| 🔴 Chain | Website deep + LinkedIn + news search + **chain procurement mapping** | agent-browser + agent-reach (Exa) | 3-5min each |
| 🟡 Mid | Website basics + FB | agent-browser | 1-2min each |
| 🟢 Small | **Skip** — Maps data sufficient | — | 0 |

**Chain enrichment** with agent-browser:
1. `agent-browser open "[website URL]"`
2. `agent-browser snapshot -i` → extract Services, About, Staff, Contact
3. Check for Portfolio/Cases and News/Blog pages for expansion signals
4. **For chains**: Look for corporate/region procurement contacts, preferred vendor programs, and expansion news

**Chain news search** with agent-reach:
```
mcporter call 'exa.web_search_exa(query: "[company name] expansion OR new location OR equipment", numResults: 5)'
```

**Chain procurement mapping** (chains only) — See [references/chain-strategy.md](references/chain-strategy.md) for full approach:
- Identify: local manager → regional operations manager → VP of operations / procurement director
- Sources: LinkedIn, corporate website "careers" or "partners" page, news about leadership changes
- Goal: find the person who can approve equipment purchases for multiple locations

### Step 5: Score & Rank

Match each candidate against the profile card:

| Factor | Rule | Points |
|--------|------|--------|
| Buy signal | Expansion / new service / new equipment | +5 (strong) / +3 (medium) / +1 (weak) |
| Industry match | Business type matches profile | +3 |
| Scale match | Review count / bays similar to profile | +2 |
| Service overlap | Same services as profile | +2 |
| Geo similarity | Similar area type | +1 |
| Business age | Similar years in operation | +1 |
| Chain multiplier | Chain store (multiple locations = bulk potential) | +3 |
| EV/high-end certification | EV Certified / LUXE / premium line | +4 |

**Tie-breaking**: buy signal strength → chain (bulk potential) → has phone → closer scale match

| Total score | Priority | Action |
|-------------|----------|--------|
| 10+ | 🔴 High | Call within 48h |
| 6-9 | 🟡 Medium | Call this week |
| <5 | 🟢 Low | Call when available |

### Step 6: Generate Custom Sales Openers

**Not templates — custom for each prospect based on their data.**

Opener must accomplish 3 things: (1) prove you know them, (2) state your purpose, (3) invite dialogue.

| Data source | How to use in opener |
|-------------|---------------------|
| Buy signal | "Saw you just added [service related to your product]" |
| Similar customer | "We supplied [product] to [similar customer] in your area" |
| Business type | "Since you do [their business type]..." |
| Key clues | "As an [industry certification] shop..." / "Working with [their key client]..." |
| Tier | High→emphasize quality & custom, Mid→value, Low→entry-level |
| **Chain store** | **Key opener question: "Is equipment purchasing handled locally, or should I speak with your regional/corporate procurement team?"** |
| **Premium/certified line** | **Reference their specialization: "As an EV-certified shop, you need [specific configuration] — we've done those."** |

### Step 7: Output (3-layer structure)

Save to `prospect-data/{batch}/`:

```
prospect-data/{area}-{date}/
├── index.json          ← Lightweight index, instant search
├── P001.json           ← Full detail for first prospect
├── P002.json           ← Full detail for next prospect
└── call-list.csv       ← 11-column CSV for calling
```

See [examples/](examples/) for sample output files.

Then export CSV from index + P###.json files for calling.

**index.json** — Search/filter only (few KB):
```json
{
  "batch_id": "orange-ca-2026-05-19",
  "source_customer": "ABC Auto Body",
  "generated": "2026-05-19",
  "search_areas": ["Orange CA"],
  "product": "Customizable per industry",
  "chain_strategy": "Chain stores included — call local first to identify procurement decision chain, then escalate to regional/corporate",
  "prospects": {
    "P001": {
      "name": "Bob's Auto Body",
      "city": "Orange CA",
      "priority": "高",
      "tier": "中高端-独立",
      "status": "待联系",
      "tags": ["[industry]", "[business type]"],
      "file": "P001.json"
    },
    "P013": {
      "name": "Crash Champions Orange",
      "city": "Orange CA",
      "priority": "高",
      "tier": "连锁-中高端",
      "status": "待联系",
      "tags": ["collision", "chain", "Crash Champions"],
      "file": "P013.json"
    }
  }
}
```

**P001.json** — Full detail (all collected data + contact log):
```json
{
  "id": "P001",
  "name": "Bob's Auto Body",
  "phone": "[EXTRACTED_FROM_MAPS]",
  "city": "Orange CA",
  "tier": "Mid-high-Independent",
  "priority": "High",
  "buy_signal": "Added new [service]",
  "similar_customer": "Customer A",
  "business_type": "[industry service type]",
  "key_clues": "[specific observations from data]",
  "email": "bob@bobscorp.com",
  "chain_brand": null,
  "opener": "We supplied [product] to [similar customer] in your area — saw you recently added [service]. What [product type] are you currently using?",
  "status": "Pending",
  "contact_log": [],
  "tags": ["[industry]", "[business type]", "[certification]"],
  "maps_url": "https://maps.google.com/...",
  "rating": 4.5,
  "reviews_count": 87,
  "has_website": true,
  "website_url": "https://bobscorp.com",
  "raw_notes": "Reviews mention...",
  "source_customer": "Customer A"
}
```

**P013.json** — Chain store example:
```json
{
  "id": "P013",
  "name": "[Chain Brand] [City]",
  "phone": "[EXTRACTED_FROM_MAPS]",
  "city": "Orange CA",
  "tier": "Chain-Mid-high",
  "priority": "High",
  "buy_signal": "National chain with stable equipment needs across locations",
  "similar_customer": "Customer A",
  "business_type": "[Industry] Chain",
  "key_clues": "[Chain brand] national chain + [city] location + online booking",
  "email": "",
  "chain_brand": "[Chain Brand]",
  "opener": "Hi, I'm with [company] — we manufacture [product]. [Chain brand] has a location here, and I'd like to learn about your equipment purchasing process. Is that handled locally, or should I speak with your regional/corporate procurement team?",
  "status": "Pending",
  "contact_log": [],
  "tags": ["[industry]", "chain", "[chain brand]", "online booking"],
  "maps_url": "https://maps.google.com/...",
  "rating": 4.6,
  "reviews_count": 120,
  "has_website": true,
  "website_url": "https://www.chainbrand.com",
  "raw_notes": "National chain. Key question: local manager vs regional purchasing.",
  "source_customer": "Customer A"
}
```

**CSV export** — 11 columns, ready to call:
```
优先级,店名,电话,城市,档位,购买信号,相似客户,业务类型,关键线索,邮箱,开场白
```

CSV columns map 1:1 to P###.json fields (priority→tier, etc.). CSV is a projection of the JSON, not a separate data source.

**Status tracking** (in P###.json, not CSV):
```
待联系 → 已联系 → 意向 / 无意向 / 回访中
                 ↘ 无人接听 → 再试
```

### Step 8: Update contact status

When user reports call results, update P###.json:
```json
"contact_log": [
  {"date": "2026-05-20", "action": "电话", "result": "无人接听", "next": "明后天再试"}
]
```
And update index.json status field accordingly.

Re-export CSV filtered by status when user needs a new call list.

## Critical Rules

1. **Every step must execute** — skip only if data source has nothing (no website = skip website enrichment)
2. **Review sampling, not all** — use tiered sampling + keyword filtering per profiling reference
3. **Social media by tier only** — 🔴 chain gets full search, 🟢 small gets nothing
4. **Opener is custom** — never use generic templates, always tailor to prospect's specific data
5. **Output is 3-layer** — index.json for search, P###.json for detail, CSV for calling
6. **CSV is a projection** — all data lives in JSON; CSV is just 11 columns exported on demand
7. **Chain stores ARE valid prospects** — do NOT exclude them. Include with a different strategy: local call first → identify procurement decision chain → escalate to regional/corporate buyer. One chain deal can equal many independent deals.
8. **Tier labels include chain distinction** — use "独立" (independent) or "连锁" (chain) suffix in tier: e.g., "中高端-独立", "连锁-中高端"
9. **Chain opener must ask about procurement** — "Is equipment purchasing handled locally, or should I speak with your regional/corporate procurement team?"
10. **Specialized/certified prospects are high priority** — certifications (EV, ISO, specific industry standards) indicate higher equipment requirements and justify premium positioning
11. **DATA INTEGRITY — NO FABRICATION** — All data in outputs MUST come from actual agent-browser searches, web_fetch calls, or other real data sources. **NEVER invent, infer, or hallucinate business details.** If a field cannot be verified from real data, mark it as `"unknown"`, `"not found"`, or `"pending verification"`. If a search returns no results or fails due to network issues, report this honestly to the user instead of generating placeholder data.
12. **TRANSPARENCY ON DATA GAPS** — If Google Maps returns restricted view (limited details), if agent-browser fails to load, or if a business has no visible phone/address/rating, document this in `raw_notes` and adjust the priority accordingly. Do not fill gaps with assumptions.
13. **VERIFICATION REQUIRED** — Before marking any prospect as "ready to call", confirm that the phone number was actually extracted from a live page (not a template). If the number is a placeholder or unverified, flag it explicitly: `"phone_status": "unverified_placeholder"`.
14. **PLACEHOLDER PHONE POLICY** — Output phone numbers must come from real page extraction. Any `555`, `0000`, `1234`, or similar placeholder pattern must be marked `"phone_status": "unverified_placeholder"` and **must not** be written to the `call-list.csv` dial column.
15. **OUTREACH BOUNDARY** — The generated call list is for **business-to-business contact only**. Honor "do not call" requests. Stop calling a prospect upon request and mark status as `"do_not_contact"`. Identify caller, company, and purpose on every call.
16. **DATA RETENTION** — Delete or archive prospect files when the campaign ends. Do not share raw JSON/CSV with third parties without consent.
17. **SELF-OPTIMIZATION IS MANDATORY** — The skill MUST automatically detect coverage gaps and adjust keywords/centers between search passes. Do NOT require user feedback to fix zero-result keywords or missing chain brands. Document all auto-adjustments in `candidates-raw.txt` with `[PASS-N-ANALYSIS]` markers.
18. **COVERAGE GAP REPORTING** — After all passes complete, generate a `coverage-report.json` documenting: (a) which center+keyword combinations returned zero results, (b) which auto-adjustments were applied, (c) estimated coverage percentage of target businesses in the area. This helps users assess completeness without manual review.
19. **SUBURBAN EXPANSION IS AUTOMATIC** — For cities >2M population, if initial 4-6 centers yield <50 unique prospects, auto-expand to 8-10 centers covering satellite cities. For Houston-sized markets, target 80-100+ prospects before stopping. Do NOT require user to ask for "more coverage" — the skill should self-assess and expand.
20. **FILTER CALIBRATION IS REQUIRED** — After first dedup, if >20% of valid prospects were filtered out (e.g., chain brands, legitimate shops with unconventional names), auto-relax filter rules and re-run. Log filter false-positives in `candidates-raw.txt`.
21. **CHAIN BRAND LEARNING** — Maintain a dynamic `chain-brands-detected.json` per search session. If a brand appears in >2 locations, add it to the known chain list for future searches. Share learnings across sessions via MEMORY.md updates.

## Version History

- **v2.0.0** (2026-05-23): Added self-optimization protocol, coverage gap reporting, chain brand learning, suburban expansion rules, and filter calibration. Houston field test validated 90 prospects from 11 centers with 10 auto-adjustments.
- **v1.0.0** (2026-05-19): Initial release with multi-center search, chain strategy, 3-layer output, and custom sales openers.

---

*End of SKILL.md*
