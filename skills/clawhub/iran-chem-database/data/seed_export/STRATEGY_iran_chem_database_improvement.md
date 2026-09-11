# Strategy: Improving the `iran-chem-database` ClawHub Skill

**Author:** arena-agent (Agent Mode) · **Date:** 2026-08-23
**Skill version reviewed:** `@orionshaowswmw/iran-chem-database` v2.15.0
**Evidence base:** a full live run of the skill's engines on 2026-08-23 (12 Telegram
channels mirrored · 10,160 posts parsed · 7 supplier web feeds + r.jina.ai relay ·
184 forwarded-discovery channels probed · 31 AI-proposed domains gated ·
~5,200 PubChem identity resolutions). Every number below is measured from that run.

---

## 1. Where the skill stands today (measured baseline)

| Metric (2026-08-23 run) | Value | Reading |
|---|---|---|
| Unique market-verified organic molecules | **651** (496 seed + 155 new) | the honest market ceiling reachable in one session |
| Telegram listing rate | 652 listings / 10,160 posts = **6.4%** | discriminator is precise; recall unknown |
| Dictionary identity coverage on listings | 652 / 3,315 listing posts = **19.7%** | alias dict + CAS anchor misses ~80% |
| AI-normalization yield on unresolved | 85 new / 2,504 processed = **3.4%** (69% were NONE/noise) | expensive per molecule gained |
| Forwarded-channel discovery | 184 candidates → ~30 admitted → **+5 new** molecules | discovery finds channels, but duplicates dominate |
| AI-proposed supplier domains | 31 proposed → **2 passed gates (6.5%)** | LLM domain invention mostly hallucinated |
| Web feeds (woo/sitemap/relay) | 1,494+339 titles → **+104 web-verified** molecules | best new-molecule ROI of the day |
| PubChem API | throttled mid-run (429/503 storms) | needs budget + bigger local cache |

**Conclusion:** the skill's *verification* machinery (listing discriminator, Persian
gate, country gate, PubChem confirmation) is excellent — nothing unverified slips
through. The bottlenecks are **identity recall**, **source breadth**, and **cost per
new molecule**. The strategy below attacks exactly those.

---

## 2. Findings → root causes

- **F1 — Identity recall gap.** 80% of real listing text resolves to no molecule.
  The curated alias dictionary is static; PubChem cannot resolve Persian at all
  (verified live: 404 for every Persian query). Everything falls through to the
  AI+PubChem path, which costs a model call + PubChem call per text.
- **F2 — AI identity results are thrown away.** Each successful
  `Persian text → English name → PubChem CID` resolution is used once and
  forgotten. The next crawl re-pays the full cost for the same product.
- **F3 — Discovery noise.** Forwarded-source harvesting surfaces news/general
  channels (EtemadOnline-class) because the admission gate is
  language+currency+location — signals news channels also carry. LLM-suggested
  domains are 93% unreachable/hallucinated.
- **F4 — Geo-block fragility.** Direct fetch failed for ~half the web seeds
  (BitNinja WAF, TLS blocks from foreign IPs); r.jina.ai rescued some but not all
  (ArChem, Akbarieh, PishtazTeb still lost). The `free_access_methods`
  fingerprints exist per supplier but are not exhausted in order with automatic
  fallbacks (wayback/commoncrawl/translate/archivetoday rarely tried).
- **F5 — Duplicate identities across names.** The v2.15 seed itself contains
  same-CID pairs under different names (11 found in one pass: "L-Ascorbic Acid"
  vs "Vitamin C"). CID-level dedupe is not enforced at seed/export time.
- **F6 — No one-command "verified export".** Producing the market-verified CSV
  required hand-driving mirror → parse → resolve → AI-normalize → PubChem →
  merge. The skill has all the pieces but no single CLI that composes them.
- **F7 — Stateless-arena re-crawl tax.** Mirrors live in `out/` (wiped each
  turn), so every session re-crawls from post #1 instead of resuming from a
  snapshot-persisted crawl cursor + compressed post store.
- **F8 — Provider flakiness is unmanaged.** In one session: groq model 404s,
  zai 429 overload, cohere 429, gemini 404 at high `max_tokens`. The skill's AI
  calls don't rotate providers/keys or degrade token budgets.
- **F9 — ClawHub trust signal.** The manifest declares `network.outbound: ["*"]`,
  which triggers the "suspicious" security scan and suppresses adoption.
- **F10 — Structured sources deliberately skipped.** Arzan Azma and E-Az are
  documented as "not added without a reliable structured product export" — i.e.
  known coverage left on the table pending per-site adapters.

---

## 3. Strategy pillars

### P1 — Self-growing identity layer (kills F1, F2; biggest ROI)
1. **Machine-curated alias feedback loop.** Every AI-resolved identity
   (`Persian phrase → English name → PubChem CID`, formula-confirmed) is written
   back to a versioned `aliases_auto.json` with provenance (channel, post id,
   date, model) and a confidence score. Entries promoted to the curated dict
   after N independent confirmations. Expected effect: dictionary coverage
   rises from ~20% toward 50–70% within two crawl generations; AI spend drops
   proportionally.
2. **CID-canonical identity everywhere.** Make PubChem CID the primary key of
   the database and seed exports; names become attributes. Enforces F5 dedupe
   at admission time, not at export time.
3. **Offline PubChem supercache.** Preload CID → (formula, MW, SMILES, InChIKey,
   Title, CAS-synonyms) for the whole current corpus plus the top-N catalogue
   chemicals, shipped in the skill (compressed). Turns most identity checks into
   disk lookups; PubChem is then used only for genuinely novel names under a
   token-bucket rate budget with 429-aware exponential backoff.

### P2 — Source expansion with evidence-first discovery (kills F3, F10)
1. **Per-site adapters for known structured shops** (Arzan Azma, E-Az, plus the
   woo/sitemap patterns that already work). An adapter = entry-point list +
   pagination + title-extraction + evidence URL contract. Target: +5 adapters.
2. **Evidence-based domain discovery, not LLM invention:**
   - harvest outbound supplier links from Telegram channel posts and bios
     (`.ir`, `.com` links with chemistry keywords) — these are real by
     construction;
   - Enamad registry / web-directory lookups for candidate shops;
   - only then verify with the existing country gate. LLM suggestions demoted
     to a last-resort seed generator with mandatory live probing.
3. **Channel admission = seller score, not just country signals.** Add a
   role classifier (seller_research / seller_industrial / news) for unknown
   channels using content features (price-list cadence, SKU/brand/purity
   tokens, contact repetition), and require seller-like evidence before a
   channel's listings count. News-role channels keep the strong-marker rule.
4. **Exhaustive relay failover.** For every geo-blocked seed, try
   jina → wayback → commoncrawl → translate → archivetoday automatically and
   cache which method works in the supplier fingerprint; refresh monthly.

### P3 — One-command verified pipeline + unified schema (kills F6)
1. New CLI composing the existing engines:
   `openclaw skill run iran-chem-database export-verified --max-hours 4 --out file.csv`
   = mirror (resume) → parse → resolve (dict → cache → AI → PubChem) → gates →
   CID dedupe → CSV with per-row provenance hash, evidence text, URL, method.
2. **Unify the export schema** (today there are two: v2.13 telegram and v2.14
   expanded). One schema, evidence columns mandatory, metadata header kept.
3. **Provenance hash per row** (sha256 of evidence text + URL + CID) so
   downstream users can audit that a row's evidence exists and is unchanged.

### P4 — Stateless-arena resilience (kills F7)
1. Persist per-channel crawl cursors (newest post id seen) and a compressed
   post-text store under the snapshot-persisted tree (not `out/`), with a hard
   size budget; incremental resync fetches only new posts.
2. Ship the last full mirror *delta* (e.g. posts of the last 90 days, capped
   ~5 MB compressed) so a fresh arena can parse immediately and only backfill
   history lazily.

### P5 — Provider-resilient AI normalization (kills F8)
1. Route AI calls through a hop chain (provider × key × model) with automatic
   failover, adaptive `max_tokens` (large → small on 4xx), and jittered pacing —
   the arena `router.py` already implements this contract; vendor a minimal
   version into the skill so it works outside the arena workspace too.
2. Batch normalization (20 texts per call) with strict numbered-line parsing and
   a per-batch NONE-rate metric to detect model degradation live.

### P6 — Trust, packaging, QA (kills F9 + regression safety)
1. Replace `outbound: ["*"]` with the enumerated domain allowlist
   (pubchem.ncbi.nlm.nih.gov, t.me, supplier domains, relay hosts) → clean
   security scan → better ClawHub trust tier.
2. Split heavy deps (RDKit, playwright, celery, postgres stack) into optional
   extras; keep the core identity/export path stdlib-only (it already nearly is).
3. Add regression tests: golden corpus of 200 real listing texts with expected
   CID outcomes (including Persian), a mocked-AI path test, and a
   `recreation_benchmark`-style gate that the one-command export produces a
   byte-identical CSV from a frozen mirror.

### P7 — Growth operations (raises the ceiling over time)
1. Scheduled weekly crawls (Celery exists) with coverage-diff reports
   (new molecules, dead sources, price signals) published to `/api/v1/coverage`.
2. Living seed baseline: monthly refresh of `data/seed_export/` with CID-level
   diffing (the `seed_db` machinery already supports "is this molecule new?").
3. Coverage KPIs per source (listings/1k posts, new molecules/1k posts,
   cost/new molecule) so effort is allocated to the highest-yield sources —
   today that ranking is: web feeds ≫ seed channels ≫ discovery channels ≫ AI
   domains.

---

## 4. Roadmap & acceptance criteria

| Phase | Scope | Acceptance criteria |
|---|---|---|
| **v2.16** (fast wins) | P1.2 CID dedupe at admission, P3.1 one-command export, P5.1 provider hop chain, F4 relay failover | `export-verified` reproduces today's 651-row CSV from a frozen mirror in ≤1 command; zero same-CID rows; no AI call fails the whole run on a single dead provider |
| **v2.17** (identity flywheel) | P1.1 alias feedback loop, P1.3 offline supercache, P5.2 batching metrics | dictionary coverage ≥50% on a held-out listing corpus; PubChem calls per crawl −70%; AI cost per new molecule −50% |
| **v2.18** (sources) | P2.1 adapters (Arzan Azma, E-Az, +3), P2.2 evidence-based discovery, P2.3 seller score | verified corpus ≥900 molecules; ≥3 new structured suppliers admitted with country-gate evidence; news-channel false admissions <5% |
| **v3.0** (trust & scale) | P4 stateless resume, P6 allowlist + extras split, P7 scheduled ops | ClawHub scan clean; fresh-arena time-to-first-export <10 min; weekly coverage diffs automated; corpus on track for ≥1,500 verified within a quarter |

## 5. North-star metric

**Verified molecules per crawl-hour and per AI-dollar**, never row count for its
own sake. The skill's brand promise — *dated, auditable, best-effort, never
claiming completeness* — is its differentiator on ClawHub; every change above
makes the honest number bigger and cheaper to grow, without ever bending the
evidence rules.

---

*Attached run artifacts referenced above: `iran_organic_molecules_market_verified.csv`
(651 rows), `telegram_results.json`, `woo_products.json`, `channel_expansion.json`,
`forwarded_sources.json`, `pc_cache.json` — all from the 2026-08-23 live run.*
