# Playbooks — consoles, refresh & multi-domain

Companion to SKILL.md. Read §14 here when an article is stale, §15 when one entity owns two domains, §16 when setting up the external consoles.

---

## §17. Competitive benchmark — the shape

Illustrative — **every figure below is fictional**. Fill it from public pages you actually read. Name competitors **only** as A/B/C in anything that can leave your machine (SKILL.md §9).

| Competitor | Depth of key page | FAQ schema | Named author | Visible update date | Reviews | Price shown |
|---|---|---|---|---|---|---|
| Competitor A | Long-form pillar | No | Yes, credentialed | Yes | — | Yes |
| Competitor B | Mid-length | No | Yes | Yes | High volume, high rating | On request |
| Competitor C | Mid-length | No | No | Yes | — | Partial |
| **You** | Uneven | **No** | Yes | **No** | — | **No** |

Then read your position on the queries that actually pay — commercial intent, not vanity head terms:

| Query | Top 5 observed | You? |
|---|---|---|
| "[category] + [problem] + [city]" | Competitor B #1, Competitor A #2 | Outside top 5 |
| "how to [action] a [thing]" | A, C, … | **Absent** |
| "best [category] for [use case]" | B, …, **you** | Present, low |

---

## §16. External consoles — order of operations

**Human-operated, every step.** This skill never logs into a console for you: it has no credentials and asks for none. The order is causal — doing step 5 before step 1 wastes the entity signal, and step 4 is what clears the IndexNow 403 in SKILL.md §5.

| # | Step | Detail |
|---|---|---|
| 1 | Verify **domain property**, primary console | TXT DNS record, not the HTML-file method — domain property captures subdomains + http/https |
| 2 | Submit the sitemap there | `https://${SITE}/sitemap.xml` |
| 3 | Create the **secondary console** property by **importing** from the primary | Minutes, instead of a second verification round |
| 4 | Declare the IndexNow key in the secondary console | Settings → IndexNow → use my own key. **This is what clears the 403 in SKILL.md §5** |
| 5 | Create an item on the **open knowledge base** | Instance-of, founder, inception, HQ, official website, official name, languages. LLMs use it to resolve entities → link it from `sameAs`. Allow days to propagate |
| 6 | Business listing | Primary category = the most specific one that exists. Service area if no public address |
| 7 | Directories | **NAP (Name-Address-Phone) byte-identical everywhere** — same accents, spacing, legal form. A drifting NAP splits one entity into three |

---

## §14. Refresh playbook — 5 phases

| Phase | Time | Actions |
|---|---|---|
| **1. Pre-audit** | 20 min/article | List every number, deadline and source cited. Flag obsolete references, dead outbound links, and statistics predating the last real-world change. Re-check tables and infographics — a correct paragraph beside a stale table still reads stale |
| **2. Editorial rewrite** | 1-2 h | "Updated on" under H1 · **"What changed"** box · intro rewritten answer-first (SKILL.md §11, blocks 3-4) · H2s restructured into questions · table added or rebuilt · 3-5 Q/A mini-FAQ · 3-5 hub-and-spoke links · author signature |
| **3. Inject JSON-LD** | 5 min | Real `datePublished` + `dateModified`; `author` and `publisher` **by `@id` only** (SKILL.md §3) |
| **4. QA** | 15 min | Structured-data test · link check · subject-matter review by the named author **before** publish, never after. The author's name is on the page; the review is not optional |
| **5. Post-publication** | 10 min | Request re-indexing · update sitemap `lastmod` · IndexNow ping · archive the previous version for traceability |

### The "What changed" box

Mandatory on any article touched by a real-world change. Put it directly under the update line — it is the block an engine quotes when asked "what changed in [year]".

```
🔄 Updated [Month Year]
- [Threshold] raised from [old] to [new] (source: [official source, dated])
- [New obligation] now applies to [scope] (source: [official source, dated])
- [Removed rule] no longer applies since [date]
```

### De-dating slugs

A slug carrying a year (`/topic-guide-2024/`) is a self-inflicted expiry stamp: it tells every engine the page is about a year, not a subject, and it ages badly whether or not the content does.

1. Create the year-less slug: `/topic-guide-2024/` → `/topic-guide/`
2. **301** the old slug to the new one — never leave both live
3. Add the "Updated on" line and the "What changed" box to the new page
4. Update `sitemap.xml` with the new slug and a real `lastmod`
5. Re-ping IndexNow for the new URL

Publishing both versions splits the signal and competes with yourself. There is no case where keeping the dated slug live is the right call.

### Article ↔ master FAQ, without duplicate content

One master FAQ page holds the full Q/A set **and is the only page carrying the complete FAQPage schema**.

| Rule | Detail |
|---|---|
| Subset, not fork | Each article embeds a **3-5 Q/A subset drawn verbatim** from the master — never a divergent rewrite |
| Schema scope | The article marks up **only its subset**. The master marks up the full set |
| Mapping is written once | `topic A article → Q1.1, Q1.3, Q1.6` · `topic B article → Q2.1, Q2.3, Q2.5`. Decide it in a file, not per-article improvisation |
| Single source of truth | Change a wording? Change it in the master, then propagate. Never the reverse |

Two different answers to the same question on your own domain is the fastest way to be dropped as an unreliable source. The consistency is the point — a subset repeated verbatim reads as one authority; a subset paraphrased reads as two contradicting pages.

### Cadence

8-10 articles refreshed per month is a sustainable rate for one writer plus one reviewer. Anything claiming much more is skipping phase 4. Mandatory quarterly re-review of any Q/A or figure that cites a rule which can change.

---

## §15. One entity, two domains

A generic pattern, applicable whenever one entity owns both a product brand (`${SITE}` = `acme-corp.com`) and an expertise brand (`${SITE2}` = `acme-experts.com`) — a common split in any sector where a product is sold alongside advisory work. The two properties have different audiences, different intents, and must never answer the same query. Adapt every row below to your own structure; none of it is prescriptive for a particular industry.

| Dimension | `${SITE}` (product) | `${SITE2}` (expertise) |
|---|---|---|
| Audience | Someone with an urgent problem, acting now | Someone evaluating expertise for a complex case |
| Format | Short (1 500-2 200 w) | Long (2 500-3 500 w) |
| Author shown | "The [BRAND] team" | The named expert, personally |
| Tone | Reassuring, direct, action-first | Precise, sourced, rigorous |
| Conversion | Product signup / first step | Contact the named expert |

### Distribution matrix

| Content type | `${SITE}` (product) | `${SITE2}` (expertise) |
|---|---|---|
| "What do I do right now" page (<2 000 w) | **Yes** — first step + CTA | No |
| Deep pillar page (>2 500 w) | No | **Yes — canonical** |
| In-depth methodology / analysis | No | **Yes — exclusive** |
| News & customer alerts | **Yes** | No |
| Commentary on a change in the field | No | **Yes** |
| Case study / documented outcome | No | **Yes — exclusive** |
| Product FAQ (app, pricing, process) | **Yes — exclusive** | No |
| Domain FAQ (the subject itself) | Short subset, canonical → `${SITE2}` | **Yes — full** |
| Product pricing grid | **Yes** | No |
| Expert / consulting rates | No | **Yes** |
| Geographic pages (city, region) | No | **Yes — exclusive** |
| Named-expert / team page | Summary | **Yes — canonical** |

### Canonicalisation

- Any page living on both domains carries a `canonical` to the version designated **canonical** above.
- Same-language `hreflang` declared identically on both.
- Never republish one subject as two similar versions — that is not "covering it twice", it is competing with yourself twice.

### Anti-cannibalisation rules

1. **One subject = one canonical domain.** No exceptions, and no "but it converts on both".
2. Shared subtopic → short version on the product domain + `canonical` to the expertise domain + contextual cross-links both ways.
3. Cross-links are **mandatory and contextual**: product page → "complex case? talk to [expert]" pointing at the *matching* pillar, not the homepage. Expertise page → "simple case? do it yourself in 2 min" pointing at the *matching* product page.
4. Distinct author signatures: "The [BRAND] team" product-side, the named expert expertise-side. Never the same byline on both.
5. Proof figures never cross: product metrics stay product-side, engagement outcomes stay expertise-side. **A number that appears on both belongs to neither** — it reads as marketing rather than evidence.
6. No geographic pages and no segment pages on the product domain — local and segment intent stay where the named entity is.
