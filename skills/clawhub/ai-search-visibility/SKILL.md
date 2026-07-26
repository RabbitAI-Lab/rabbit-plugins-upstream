---
name: ai-search-visibility
description: Make a site citable by AI engines — crawler allowlist, @graph @id, IndexNow, answer-first pages. Use when a site is invisible to ChatGPT. Trigger on "GEO audit", "llms.txt".
metadata: {"clawdbot":{"emoji":"🔎","requires":{"bins":["node","curl"]}}}
---

# AI Search Visibility (GEO)

Being **crawled** and being **cited** are two different pipelines. Most sites lose the second one while trying to configure the first.

## Access, data, network

| Item | Default |
|---|---|
| Network calls | Read-only GETs to public URLs **you name** — your own `robots.txt`/`sitemap.xml` (§1, §8), public competitor pages (§9), a third-party SEO index (§10 source 1). Engine probes (§10 source 4) are **run by hand or via the vendor's official API — never a scripted consumer UI**. Plus **one opt-in POST** of your own public sitemap URLs via `scripts/indexnow-ping.js`. Nothing else. No authenticated call, no page content or analytics uploaded, nothing written to the network except that one POST. |
| Credentials | None. `INDEXNOW_KEY` is read from env, never written into the repo. |
| Data persisted | Nothing. Audit output is a file you write, where you choose. |
| Third-party accounts | Search consoles, knowledge base, business listing, directories — **manual, human-operated**. This skill never logs into them. |
| Personal data | Public pages only. **Never reads, inventories, scrapes or republishes visitor, customer or prospect records.** Internal demand signals enter only as an aggregated theme list produced by a human (§10 source 3) — this skill never opens a customer-data store. Engine ToS and GDPR (or local equivalent) bind you before anything here does. |
| Authorship | Any copy this skill drafts is a **draft**. The named human author reviews and endorses before publish (§11). Never a byline on unreviewed text, never an invented person. |

## When to Use

| Trigger | Action |
|---|---|
| "we're not cited by ChatGPT / Perplexity" | Instrument first, in order: §1 taxonomy → §3 @graph → §4 sitemap → §5 IndexNow |
| "should we block AI crawlers?" | §1. Never one wholesale rule |
| "GEO audit" / "why do we rank nowhere" | Audit: §7 inventory → §8 signals → §9 benchmark → §10 scoring /100 |
| "rewrite this page" / "it isn't answer-first" | §11 template + §12 forbidden list |
| "this article is out of date" | `references/playbooks.md` §14 |
| "our two sites compete with each other" | `references/playbooks.md` §15 |

## Placeholders

| Placeholder | Example | Meaning |
|---|---|---|
| `${SITE}` | `acme-corp.com` | Product brand — short pages, urgency intent |
| `${SITE2}` | `acme-experts.com` | Expertise brand — long canonical pillars |
| `${INDEXNOW_KEY}` | env var, 32-hex | **Env only. Never hardcode, never commit, never paste into docs** |
| `#organization`, `#founder` | `https://${SITE}/#founder` | Stable @id fragments. Never a person's name in the fragment |

## 1. Crawler taxonomy — the thing everyone gets wrong

Three **distinct** classes of user-agent, from three different pipelines. A blanket "block AI bots" rule, or a WAF pattern matching `*bot*`, kills classes 2 and 3 in order to opt out of class 1 — and it is invisible to whoever shipped it.

| Class | What it does | Blocking it costs you | Named agents |
|---|---|---|---|
| **Training crawler** | Bulk-collects corpus for model training | Nothing today. Possibly long-term recall of your brand | `GPTBot`, `ClaudeBot`, `Meta-ExternalAgent`, `CCBot` |
| **Search crawler** | Builds the *answer index* the assistant retrieves from | **Citability — you vanish from answers entirely** | `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Applebot` |
| **On-demand fetcher** | Fetches a URL *because a user asked the assistant to read it* | The user pastes your link and gets "I can't access that page" | `ChatGPT-User`, `Claude-User`, `Perplexity-User` |
| **Not crawlers** | `Google-Extended` / `Applebot-Extended` are training **opt-out controls** | Disallowing them does not remove you from that vendor's search index; allowing them does not add you | — |

Agent names are public facts, but **re-verify each against the vendor's current docs before shipping** — this list moves every quarter. Full file: **`templates/robots.txt`**.

**Groups do not inherit, and a group runs until the next `User-agent:` line** (RFC 9309). An agent matching a named group ignores `User-agent: *` *entirely*, and blank lines do not end a group — so an internal `Disallow` written under the wrong heading silently belongs to the agent above it, and applies to nobody else. Repeat every internal `Disallow` in **every** group. And **put `Disallow` before `Allow: /` in each group**: RFC 9309 says the *longest* match wins, so order shouldn't matter — but plenty of live parsers take the *first* match instead, hit `Allow: /`, and serve the internal tree anyway. Disallow-first is correct under both readings, and it is free insurance against a crawler you'll never audit.

```
User-agent: OAI-SearchBot     # several agents may share one group
User-agent: Claude-SearchBot
Disallow: /internal/          # BEFORE Allow, and repeated in EVERY group
Allow: /

User-agent: Bytespider        # abusive scrapers: named block only
Disallow: /                   # covers everything; no internal lines needed

Sitemap: https://${SITE}/sitemap.xml
```

`robots.txt` is public: a `Disallow` **advertises** a path, it does not protect it. Never list a path whose existence is itself sensitive — use auth or a `noindex` header — and keep host-specific paths out, they name your vendor to every reader.

```bash
# Verify what you shipped, not what you meant to. Check the WAF too — robots.txt is not the only gate.
curl -s "https://${SITE}/robots.txt" | grep -c "^User-agent: OAI-SearchBot"
# Output: 1
# Every allowlisted group must carry the internal Disallow: count must equal the number of groups.
curl -s "https://${SITE}/robots.txt" | grep -c "^Disallow: /internal/"
# Output: 5
```

## 2. llms.txt — a brief for an engine reading you cold; the structure is the value

Copy the skeleton — six sections, in order, with the rule for each: **`templates/llms.txt`**. Two that decide whether it works: **core pages must be annotated** with what each one answers (a bare link list is worthless), and **proof must be third-party and dated** (no superlatives, every differentiator falsifiable).

**Never include** vendor stack, internal pricing logic, personal email, private booking links or unpublished client names. This is a public file, reproduced verbatim by anything that reads it: everything in it must already be published on the site.

## 3. Schema.org — one @graph, stable @id (the real technical lever)

Stacking independent JSON-LD blocks per page hands the engine three `Organization` nodes with three names and no way to know they are the same company. **One `@graph` where entities reference each other by `{"@id": ...}` gives it one entity.** The `@id` is the primary key: reuse the *same* one on every page — homepage, pricing, and the blog template — and cross-page entity resolution starts working. Full fictional graph: **`templates/graph.json`** (Organization · Person · WebSite · WebPage · BreadcrumbList · Service · FAQPage, all cross-referenced). The pattern — note the article template *references* the same two `@id`s rather than re-inlining them:

```json
{ "@type": "Organization", "@id": "https://acme-corp.com/#organization",
  "founder": { "@id": "https://acme-corp.com/#founder" } },
{ "@type": "BlogPosting", "@id": "https://acme-corp.com/blog/post/#post",
  "author":    { "@id": "https://acme-corp.com/#founder" },
  "publisher": { "@id": "https://acme-corp.com/#organization" } }
```

| Rule | Why |
|---|---|
| Article templates reference `author`/`publisher` by `@id` only — never re-inline name + logo | An inlined author drifts from the homepage's and becomes a second, weaker entity |
| `@id` fragments are role-based (`#founder`), never patronymic | Permanent keys: they must survive a person leaving and carry no PII |
| `sameAs` → knowledge-base item + one canonical profile. Not eight social links | `sameAs` disambiguates; it is not link-building |
| One `@graph` per page, not one per component | Contradictory duplicates are worse than no markup at all |
| Every `dateModified` matches a **visible** date in the rendered HTML | A date the engine can't read on the page is a claim it discounts |

## 4. Sitemap — reciprocal hreflang

Every URL declares **all** its alternates **including itself**, plus `x-default`. Non-reciprocal alternates are silently dropped: A→B without B→A groups neither.

```xml
<url>
  <loc>https://acme-corp.com/fr/pricing.html</loc>
  <lastmod>2026-02-01</lastmod>
  <xhtml:link rel="alternate" hreflang="fr" href="https://acme-corp.com/fr/pricing.html"/>
  <xhtml:link rel="alternate" hreflang="en" href="https://acme-corp.com/en/pricing.html"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://acme-corp.com/fr/pricing.html"/>
</url>
```

The `fr` self-reference is required, not redundant. Repeat the identical block on `/en/pricing.html`. `x-default` points at the primary market, identically in every block of the group.

## 5. IndexNow — most direct lever, wired so it can never break a deploy

IndexNow pushes URLs into the index feeding several assistants' search layer; everything else here is pull. Ship **`scripts/indexnow-ping.js`** — non-negotiable properties:

| Property | Implementation |
|---|---|
| Key from env | `const KEY = process.env.INDEXNOW_KEY`. The key is public *by design* — but hardcoded into script + docs + build passthrough, a rotatable key becomes three commits you have to hunt down |
| No throw path | `req.on('error')` → `resolve()`. HTTP ≥400 → log, `resolve()`. Top-level `.catch()` → warn, exit 0 |
| Timeout | `setTimeout(10000)` → destroy + `resolve()`. Never hang a build on a third party |
| Chunking | 1000 URLs per POST, well inside the protocol limit |
| Build command | `… && node scripts/indexnow-ping.js \|\| true` — the last line of defence |
| Sitemap source | `SITEMAP_PATH`, default `./site/sitemap.xml` **relative to the working directory** — not to the skill's install directory. Set it, or pass URLs as arguments |
| Entity decoding | `<loc>` is XML: `&` is escaped as `&amp;`. Decode before POSTing or you submit a URL that never existed |

```bash
export INDEXNOW_KEY=$(node -e "console.log(require('crypto').randomBytes(16).toString('hex'))")
export INDEXNOW_HOST=acme-corp.com                 # store both in the host's env, not the repo
export SITEMAP_PATH=./site/sitemap.xml             # or pass URLs as arguments instead
printf '%s' "$INDEXNOW_KEY" > "site/${INDEXNOW_KEY}.txt"   # serve at domain root
node scripts/indexnow-ping.js
# Output: [indexnow] Submitting 24 URLs to api.indexnow.org…
# Output: [indexnow] HTTP 200 (24 URLs)
```

**Never commit the key file.** The filename **is** the key, so committing it commits the key — and it survives rotation in the git history, which is the exact problem env-only handling exists to avoid. Add `site/*.txt` (or the exact key filename) to `.gitignore` and emit it from the build step that reads `$INDEXNOW_KEY`. Public *by design* is not the same as public *forever, in your history, after you rotated it*.

**The gotcha that costs a day.** You will get **HTTP 403** on every call while the key file is correctly hosted, correctly named, and byte-matches the payload. Nothing is wrong with your code: the endpoint 403s until the **domain** is validated on the engine's webmaster console — a key generated locally is not a key *declared* there. Do `playbooks.md` §16 step 4, then re-ping. Meanwhile the sitemap covers crawl on the normal schedule, so you are losing latency, not coverage. Do not "fix" the script.

## 6. External consoles → `references/playbooks.md` §16

Human-operated, every step; this skill holds no console credentials. Causal order — domain property (TXT DNS) → sitemap → secondary console by import → **declare the IndexNow key (clears the §5 403)** → knowledge-base item → business listing → directories with byte-identical NAP.

## 7. Output format — the inventory table

One row per URL, before any opinion is formed. Count words on rendered text, not source. Three verdicts, grouped by hub: **thin** (<900 words on a pillar intent) · **dated** (facts older than the last change in the underlying reality) · **orphan** (no internal inbound link). Close the audit with the verdict line, verbatim:

```
| URL           | H1 (verbatim)              | Words | Verdict                          |
| /hub/topic-a/ | "Everything about topic A" |  3500 | dated — stats 11 yrs old, 0 FAQ  |
| /hub/topic-b/ | "Topic B: what to do"      |   650 | thin — critical                  |
| /standalone/  | "Topic C"                  |  1900 | orphan — 0 inbound internal links|

GEO SCORE: 47/100 — 3 Tier S, 11 refresh, 0 FAQPage sitewide
```

## 8. Technical signals — check every one, every time

| Signal | Pass condition |
|---|---|
| JSON-LD by type | Article/BlogPosting, FAQPage, Person, Organization/LocalBusiness, BreadcrumbList — present *and* cross-referenced by `@id`. Zero FAQPage across an entire site is the most common finding, and the cheapest to fix. **Note:** FAQPage stopped producing SERP rich results for most sites in 2023 — ship it for *extraction* by generative engines (self-contained 40-60-word Q/A), not for SERP real estate. Different pipeline, still worth it |
| **Visible "Updated on"** | Rendered under the H1. Not `dateModified` alone |
| Canonical | Self-referencing on canonical pages; pointing at the canonical domain for shared subtopics |
| Open Graph | og:title/description/url/image (1200×630) + twitter:card |
| Sitemap | Reachable, real `lastmod`, reciprocal alternates, referenced from robots.txt |
| Robots | Named allowlist per §1, no wholesale AI block. Internal trees disallowed **in every named group** (groups don't inherit from `*`) and **before** each `Allow: /`. Count the Disallow lines: one per group, or it doesn't apply where you think |
| Core Web Vitals | Measured, not assumed — mobile field data |

## 9. Competitive benchmark

Score each competitor's key page on six axes — depth, FAQ schema, named author, visible update date, reviews, price shown — then read your own position on the queries that pay (commercial intent, not vanity head terms). Table shape and a worked example: **`references/playbooks.md` §17**. **Name competitors only as A/B/C in anything that can leave your machine** — a benchmark naming real firms is a document you cannot share with the client it was built for. If none ships FAQPage schema, that is a time-boxed arbitrage window, not a moat — it closes the quarter one of them notices.

## 10. Scoring /100 — and the 5 sources when you have no Search Console

No console access at kickoff is the normal case, not the exception — that is exactly what the grid is for.

| Criterion | Weight |
|---|---|
| Current organic traffic | 25 |
| Query volume potential | 20 |
| Age / obsolescence of content (penalty) | 15 |
| Alignment with what you actually sell | 15 |
| Already cited by an AI engine | 15 |
| Technical quality (length, structure, schema) | 10 |

These weights are a **starting point to adjust to your business**, not a calibrated constant. What matters is that the grid is written down *before* you score, not that these exact numbers are optimal — an explicit grid you argue with beats an implicit one you don't.

**Thresholds:** `> 60` → top-20 refresh list · `> 75` **AND** untouched > 18 months **AND** underlying facts changed since publication → **Tier S, urgent**. Scores derived from the sources below are **provisional** — re-rank once console data lands.

Cross these 5 sources to reconstruct the real top without console data:

1. **Third-party SEO index** — pages ranking on >1 000/mo keywords, pages holding backlinks, pages with the highest traffic value.
2. **Whatever analytics already exists** — sessions, conversions, >2 min dwell. A partial beacon beats guessing.
3. **Internal demand signals — themes only.** Work from an aggregated, already-anonymised list of recurring questions that a human hands you. Never from raw inboxes, DMs, CRM records or call recordings: this skill does not read a customer-data store. What people *actually* ask outranks what you assume they search — a theme list carries that signal without the records.
4. **AI engine probes — run by hand, or through the vendor's official API.** Run the target queries against each assistant, record who gets cited. **Never script the consumer UI**: it breaches most engines' terms, and a human reading five answers is faster than the scraper you'd maintain. *Competitor cited + you absent* = a scored gap, not an anecdote.
5. **Your own crawl** — sitemap `lastmod`, word count, inbound internal link count. Surfaces thin/dated/orphan mechanically.

## 11. The answer-first template — imposed order of 13 blocks, no reordering

| # | Block | Spec |
|---|---|---|
| 1 | **H1 as a question** | The question the user types, verbatim |
| 2 | **Date + author block** | "Updated on DD Month YYYY by [NAME], [credential]" |
| 3 | **Direct answer, 2-3 sentences** | Contains a **number** and names its **source**. This is the block that gets quoted |
| 4 | **TL;DR, 4-6 bullets** | Consequences, deadlines, procedure, recourse |
| 5 | **Table** | Thresholds / tiers / amounts. Real `<table>`, never an image |
| 6 | **H2s, all questions** | Each answerable in 40-60 self-contained words |
| 7 | **Numbered steps** | For anything actionable |
| 8 | **Common mistakes** | "What to avoid" — highest-engagement block on most pages |
| 9 | **FAQ, 8-12 Q/A** | `<dl><dt><dd>` + FAQPage JSON-LD |
| 10 | **Contextual CTA** | Tied to *this* page's problem. Never a generic download |
| 11 | **Hub-and-spoke links** | ≥5 internal, to sibling and child pages |
| 12 | **Author block** | Credentials + years + link to a real bio page |
| 13 | **JSON-LD** | Article + FAQPage + Person + Organization, by `@id` per §3 |

**Attribution rule.** A named author is a claim of human authorship. Any copy this skill drafts is a **draft**: the named person must read, correct and approve it before publish. Never put a byline on text that person has not endorsed, and never invent a person, a credential or a bio page — block 2 and block 12 are worthless the moment they are fiction, and an engine that catches one fabricated author discounts the whole domain.

**Typography rules:** formal register throughout · no jargon without an inline definition, re-defined on **every** page (a page is an entry point, not chapter 4) · numbers always precise ("6 to 36 months", never "several months") · every claim carries its source reference · update date under the H1 **and** at the foot · keep commercial claims sparse on a service page (3 is already a lot) · respect any advertising or claims rules binding your sector, and never promise a result you cannot evidence.

## 12. Forbidden — as prescriptive as the template

| Forbidden | Why it kills citability |
|---|---|
| **Dated statistical intro** ("according to the 2015 report…") | The engine reads the top first and infers the whole page is of that era |
| **Commercial H2** ("With [BRAND], an expert for all your…") | An H2 that isn't a question answers nothing. There is nothing to extract |
| **CTA before the factual answer** | The engine hits conversion copy where the answer should be, and cites whoever answered |
| Brand-centric opening line, or an acronym used before it is defined | Zero density in the highest-value 250 words; the passage becomes unquotable standalone — and standalone is the only way it gets quoted |

## 13. Delivery checklist (17) + KPIs

```
- [ ]  1. H1 is a question                  - [ ] 10. Every factual claim carries its source
- [ ]  2. Visible "Updated on" under H1     - [ ] 11. No statistic older than 24 months
- [ ]  3. Named author + link to a real bio - [ ] 12. >=5 internal hub-and-spoke links
- [ ]  4. Direct answer in first 250 words  - [ ] 13. "Common mistakes" section present
- [ ]  5. TL;DR bullets present             - [ ] 14. Contextual CTA, not a generic download
- [ ]  6. >=1 real HTML table               - [ ] 15. No promise of a result you can't evidence
- [ ]  7. All H2s phrased as questions      - [ ] 16. Length fits the page's job (see below)
- [ ]  8. >=8 Q/A in the closing FAQ        - [ ] 17. Named author has personally reviewed
- [ ]  9. JSON-LD Article+FAQPage+Person+Org,        and endorsed the copy before publish
          @id-linked
```

**Point 16 depends on the page's job:** 2 500-3 500 words on a pillar page (4 000 for a hub) · 1 500-2 200 on a short, urgent-intent product page. On a two-domain setup, the split is prescribed in `references/playbooks.md` §15 — applying the pillar number to a product page violates it.

**KPIs — instrument these; there are no guaranteed targets.** Structural metrics are verifiable on day one: visible update date and FAQPage schema on 100% of rewritten pages · mean pillar length. Outcome metrics — citations per engine on your top commercial queries (§10 source 4), AI-Overview citations, organic traffic on rewritten pages — have **no defensible benchmark before you have your own**: measure the baseline on the first cycle, then set targets against it. A number invented at kickoff is exactly the unsourced claim §11 and point 10 forbid.

## 14-15. Refresh & multi-domain → `references/playbooks.md`

5-phase refresh · "What changed" box · slug de-dating + 301 · article↔master-FAQ coupling · two-domain matrix, canonicalisation, anti-cannibalisation.

## Troubleshooting

| Symptom | Root cause | Fix |
|---|---|---|
| IndexNow 403, key file serves fine and matches | Domain not yet validated on the engine console. Local key ≠ declared key | `playbooks.md` §16 step 4, then re-ping. Sitemap covers crawl meanwhile. Don't touch the script |
| IndexNow **422** `One or more URLs are not related to your verified domain` | A `<loc>` host ≠ `INDEXNOW_HOST` — usually a staging URL or an unescaped `&amp;` left in the URL | One host per ping. The script decodes XML entities; check `INDEXNOW_HOST` matches the sitemap's real host |
| "I can't access that page" on a URL the user pasted | On-demand fetcher blocked by a blanket `*bot*` WAF or robots rule | §1 named allowlist — and check the WAF, robots.txt is not the only gate |
| Rich-results test green, engines still cite a competitor | Several contradictory JSON-LD blocks → no resolvable entity | Collapse to one `@graph`, `@id` cross-refs, reused across pages |
| hreflang group silently ignored | Non-reciprocal alternates, or missing self-reference | §4. Every URL declares all alternates, including itself |
| Build hangs or fails after adding the ping | An error path throws, or no timeout | All paths `resolve()`, 10 s timeout, `\|\| true` on the build command |
| `dateModified` recent, engine still treats page as stale | No **visible** date in the rendered HTML | Render "Updated on …" under the H1 |
| Page rewritten answer-first, still not quoted | The answer isn't self-contained — it leans on the paragraph above | §11 block 3: number + source, readable with no page around it |

## Scope

**This skill ONLY:** edits files you own (robots.txt, llms.txt, sitemap, JSON-LD, page copy) · reads public pages you name — your own, and competitors' during §9 · submits **your own public sitemap URLs** to a public endpoint, opt-in, key from env · produces audit tables and rewrite plans from those public pages · drafts copy for a named human to review and endorse.

**This skill NEVER:** logs into a console, CMS or third-party account for you · touches paid ranking, paid reviews, or any manipulation of a competitor's listing · reads, scrapes or stores personal data — internal demand signals enter only as an aggregated theme list a human hands you · publishes a claim without a source, or a promise of a result you cannot evidence · attributes drafted copy to a named human who has not reviewed and endorsed it, or fabricates an author, a credential or a bio · names a real competitor in a shareable artefact (A/B/C only) · writes `${INDEXNOW_KEY}` to disk outside the key file the protocol requires · advises evading a rate limit, bot detection or any anti-abuse control — if a crawler or console blocks you, stop and involve a human rather than adapting behaviour to get around it. Engine ToS and applicable data law (GDPR or local equivalent) take precedence over every line above.
