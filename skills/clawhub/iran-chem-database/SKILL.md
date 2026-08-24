---
name: iran-chem-database
description: "Iran Chemical Database — an HTTrack-powered live crawling system that builds a dated, auditable, BEST-EFFORT index of confirmed and unresolved chemical offerings discovered in configured public Iranian supplier catalogues. Discovers and mirrors supplier websites with HTTrack (polite crawling, robots-aware), extracts catalogue entries from local mirrors (HTML/JSON-LD/PDF/Excel/DOCX/JSON-API), classifies with a configurable inclusion policy (research_only | lab_or_research | all_identifiable_catalogue) plus explicit structure-first organic classification, validates with RDKit/PubChem, and maintains a live PostgreSQL database with FastAPI + Streamlit interfaces. Coverage, crawl states and rejection reasons are measured and published — never claimed complete. Installation provides software, not a populated dataset. v2.6 adds a WooCommerce/WordPress REST + sitemap engine (public /wp-json/wc/store/v1/products), a fingerprint-annotated seed list (dead/parked/geo-blocked/WooCommerce per-URL), geo-block detection, and a fixed Celery dispatch path. v2.10 adds a SOCIAL CATALOGUE engine: content-verified public Telegram channels (t.me/s/<chan> — no login/API key, not geo-blocked) are mirrored with bounded-parallel backward pagination to the true channel beginning and incremental resync, then parsed locally into molecules via a curated Persian/Latin alias dictionary + CAS-anchored fallback + PubChem enrichment, with a role-aware listing discriminator, unit-anchored price extraction, domain-aware grade classification, forwarded-from channel discovery, and /api/v1/social/* endpoints. v2.11 enforces a HARD Iranian-suppliers-ONLY scope rule: an evidence-based country gate (Enamad trust-seal, شناسه ملی/کد اقتصادی/کد پستی registry IDs, .ir ccTLD, +98 telephony, IRR pricing, Iranian hosting) requires at least two INDEPENDENT signal families and zero foreign disqualifiers (multinational-owned domain, foreign ccTLD, foreign HQ statement) before any supplier is admitted, defaulting to DENY; it distinguishes supplier nationality from product brand so Iranian importers reselling Merck/Sigma/TCI are kept while the multinationals themselves are rejected, and records auditable per-vendor provenance exposed via /api/v1/social/country-policy and tools/audit_country.py. v2.12 hardens Telegram extraction: a structured field extractor reads supplier catalogue lines (SKU, brand, IUPAC name, purity, grade, pack size normalised to g/ml, availability) so posts are resolved by SHAPE instead of only by a curated alias dictionary, lifting the live corpus from 84 to 240 molecules; a Persian/Farsi language gate requires every channel to be Iranian AND to publish Persian (Arabic-script and English-only channels are refused, with Persian-vs-Arabic disambiguation); a cached PubChem resolver makes re-parses free; and one-command retrieval (`social_crawl fetch|search --query --brand --in-stock --with-price --out file.csv|json|xlsx`, plus /api/v1/social/search) makes the data trivial to pull. Persian NLP support, Playwright + network-recording fallback for JS/API catalogues, Celery scheduling, Docker deployment. v2.16 adds the 651-row market-verified seed (every row backed by a real crawled listing; unified evidence schema), the one-command tools/export_verified.py pipeline (gates -> CID dedupe at admission -> unified schema -> provenance hash per row, zero same-CID rows), the provider-resilient AI normalization hop chain (src/utils/ai_hopchain.py, arena router.py first, env-key providers with failover/adaptive budgets after), exhaustive ordered relay failover with a per-host working-method cache (fetch_with_failover), .env.example restoration, and 14 new regression tests; v2.15 expanded the baseline to 692 deduped molecules; v2.14 added the seed-baseline machinery (data/seed_export/, tools/seed_load.py, src/utils/seed_db.py). v2.17 grows the market-verified seed from 651 to 873 molecules (+224) from a deep historical Telegram sweep (14,907 -> 29,841 posts across 12 channels), backfills canonical_smiles on 615 existing rows after PubChem retired the CanonicalSMILES property (use SMILES/ConnectivitySMILES/IsomericSMILES), and fixes a false-organic gate: carbon is now matched as element C via regex C(?![a-z]) instead of a bare substring test that admitted CuO4S, CaCl2, ClH and Cu as organic (29 rows relabelled inorganic, 3 rows re-verified against PubChem where the CID disagreed with the row's own InChIKey, 2 duplicate structures merged). For academic procurement research."
version: 2.17.2
categories: [research, development]
topics: [chemistry, ht, crawling, database, chemical-suppliers]
metadata:
  openclaw:
    emoji: "🧪"
    requires:
      bins: ["httrack", "python3"]
      apis: ["PostgreSQL (local), Redis (local), optional SerpAPI/Google-CSE search key, optional PubChem (public)"]
    network:
      outbound: ["*"]
---

# 🧪 Iran Chemical Database — HTTrack-Powered Live Crawling System

> **🔴 IMPORTANT: Installation provides SOFTWARE, not a populated dataset.**
> A successful installation means services and jobs are initialized; the
> initial crawl is QUEUED and may take hours or days. Never describe the
> database as "complete" right after installation — check `/api/v1/coverage`.

This skill is a **dated, auditable, best-effort index of confirmed and
unresolved chemical offerings discovered in configured public Iranian supplier
catalogues.** What the system has and has NOT covered is measured and
published via `/api/v1/coverage`; no web crawler can guarantee "all organic
molecules available in Iran", and this skill never claims to.

## 🔴 MANDATORY AGENT INSTRUCTIONS

Before answering ANY request for molecules from this database:

1. Check `/api/v1/coverage` first.
2. State whether the configured supplier crawl is complete, partial, or still running.
3. Never infer national availability from this database — it indexes the
   configured suppliers' public catalogues only.
4. **Never make a "complete" CSV from `/api/v1/molecules`: it is paginated**
   (default 20 rows, `limit` ≤ 100, returns `total_pages`/`has_more`).
   For a full export use `/api/v1/export` (not page-limited).
5. Call `organic_status=true` **"confirmed organic"**, never "all organic";
   unresolved records are `unknown` and are exported separately, never
   silently discarded.
6. Include the export metadata/manifest (`format=manifest` or the CSV's
   `# export_metadata:` line) and report its row count when presenting files.
7. **The social catalogue (v2.10) is Telegram-only.** Check
   `/api/v1/social/coverage` before quoting it, say which channels are mirrored,
   and never present Instagram/Facebook/X/WhatsApp data as crawled — those are
   contact *leads* only. Social listings are supplier posts, not verified stock.
8. **🇮🇷 IRANIAN SUPPLIERS ONLY (v2.11) — never relax this.** Every supplier in
   this database is a verified Iranian entity; data from suppliers of any other
   country is out of scope and is rejected at ingestion. When reporting, state
   that the scope is Iranian suppliers only, and cite
   `/api/v1/social/country-policy` (or `tools/audit_country.py`) for the
   per-vendor evidence rather than asserting it. **Distinguish supplier from
   brand:** Iranian importers legitimately resell Merck / Sigma-Aldrich / TCI
   product, so a foreign BRAND in a listing is product metadata and does NOT
   make the supplier foreign — never "correct" this by dropping those vendors,
   and never present a foreign brand as a foreign supplier. Conversely, never
   add a supplier just because it ships to Iran.
9. **Persian is required, per channel (v2.12).** Every channel is Iranian AND
   Persian-publishing; cite `/api/v1/social/persian-policy` or
   `social_crawl audit-persian` for the measured ratios. Do NOT drop a
   Latin-script catalogue post from a verified Persian channel — those carry
   the SKU/brand/purity/pack data. For retrieval prefer
   `social_crawl search --query ... --out file.csv` or
   `/api/v1/social/search`; report `identity_method` so
   `structured_pubchem` results are distinguishable from `alias` hits.

10. **Do not take our word for the country — verify it yourself (v2.13).**
   This package ships an *agent-runnable* verification mechanism. Before you
   present these listings as Iranian-sourced, re-derive that conclusion:

   ```bash
   # verify every seeded supplier (exit code 1 if any fails)
   python3 -m src.scripts.social_crawl verify-suppliers --level offline
   python3 -m src.scripts.social_crawl verify-suppliers --explain   # show working
   # verify the suppliers behind an export you were handed
   python3 -m src.scripts.social_crawl verify-suppliers --dataset listings.csv
   ```
   API: `GET /api/v1/social/verify-suppliers?level=offline&explain=true`.

   Levels: `offline` (check-digit arithmetic + local mirror, no network),
   `live` (also re-fetches `t.me/s/<channel>` now), `paranoid` (**discards**
   our stored claims and rebuilds the verdict from the live page alone).

   A verdict needs **≥2 independent evidence families** and **score ≥60**;
   evidence families are registry (شناسه ملی / کد پستی), phone, domain,
   location, currency and language. Everything else fails **closed** —
   an unknown channel is DENIED by default. Never treat the
   `supplier_verified` column of a CSV as proof in itself: it is a
   convenience, and a forged one is ignored because verification re-derives
   the verdict from the claims. Rows whose supplier does not verify belong in
   quarantine, not in your answer.

11. **🌱 Use the seed baseline as your starting point (v2.14, expanded
    v2.15).** This package ships real crawl exports in `data/seed_export/`:
    a 480-row EXPANDED confirmed-organic baseline (9 source sets: TamadKala,
    Fardad Shimi, DigiShimi, Isatis Shimi, BehChin Chemi Pharmed, Pishgaman
    Shimi, ShimiMan, Rooz Darou + the retained 207-row Telegram catalogue)
    plus the v2.14 baseline (334 rows incl. 124 unknown-organic) and 74
    inorganic exclusions — **692 molecules deduped** after cross-file
    supplier/URL merge. Before crawling or answering, check the baseline
    first: it makes repeated work free and tells you instantly which
    molecules are NEW.

## 🌱 Seed Baseline (v2.14 + v2.15 expansion) — starting point for the database

`data/seed_export/` contains real, dated crawl exports:

| File | What it is |
|---|---|
| `iran_organic_molecules_market_verified.csv` | **v2.16 primary baseline** — 651 rows, ALL `confirmed_organic`, MARKET-VERIFIED ONLY: every row backed by a real crawled Iranian supplier listing (479 verified_catalogue + 68 verified_telegram_listing + 104 verified_web_catalogue; 2026-08-23). Unified evidence schema: molecule_name, common_name, cas_number, pubchem_cid, inchi_key, molecular_formula, molecular_weight, canonical_smiles, organic_status, category, grade, supplier_name, supplier_platform, availability_status, **evidence_url**, **evidence_text**, identity_method, source_type, record_date. CID-unique (0 duplicates), 0 carbon-less formulas, all CAS checksum-valid; 155 previously empty categories were classified by cloud models (router.py hop chain) during v2.16 packaging. Row 1 is the `# export_metadata:` manifest. |
| `iran_organic_molecules_expanded.csv` | v2.15 baseline — 480 rows, ALL `confirmed_organic` (2026-08-23 12:30 UTC). 9 source sets (TamadKala 3484 product URLs, Fardad Shimi 569, DigiShimi 268, Isatis Shimi 188, BehChin Chemi Pharmed, Pishgaman Shimi, ShimiMan, Rooz Darou 114, + retained 207-row Telegram catalogue). Richer schema incl. category, research_grade_candidate, supplier_country_evidence, catalogue_presence, evidence_record_count. |
| `iran_organic_molecules.csv` | v2.14 legacy baseline — 334 rows: 210 confirmed-organic + 124 unknown-organic (flagged, never discarded), crawled 2026-08-23 03:30 UTC from 12 verified Telegram channels + supplier web catalogs. |
| `iran_inorganic_excluded.csv` | 74 inorganic rows (separated, not deleted) |
| `coverage_report.json` | per-channel / per-supplier coverage, rejections, AI-assist stats, country verification (v2.14 run) |

The loader **merges duplicates across files** (same InChIKey/CAS/CID →
one row; supplier, source-URL and NAME-VARIANT evidence is unioned, so a
molecule sold by TamadKala *and* a Telegram channel carries both, and
"L-Ascorbic Acid" / "Vitamin C" survive as variants of one identity —
strategy P1.2: names are attributes of the CID-canonical identity),
normalizes the three schema dialects onto one column set, and reports
**835 deduped molecules** (649 confirmed-organic, 124 unknown-organic,
62 inorganic; 495 rows carry >1 name variant). `export_sqlite` adds a
UNIQUE `identity_key` (stereoisomer-aware merge identity) with CID as the
primary scientific index.

## 🔁 One-command verified export (v2.16)

`tools/export_verified.py` composes the pipeline in a single command
(strategy P3.1): **gates → CID dedupe at admission → unified schema →
provenance hash per row → CSV + manifest**:

```bash
# reproduce the 651-row market-verified baseline from the frozen file
python3 -m tools.export_verified \
  --files data/seed_export/iran_organic_molecules_market_verified.csv \
  --out /tmp/verified.csv        # -> 651 rows, zero same-CID rows

# export the full merged baseline (confirmed only; unknowns via --include-unknown)
python3 -m tools.export_verified --from-seed --out /tmp/baseline.csv

# enforce the telegram country gate (fail-closed) instead of audit-only
python3 -m tools.export_verified --from-seed --enforce-country --out out.csv
```

Gates (fail-closed; rejections are written to `<out>.rejected.csv` with
reasons — never silently discarded): organic status, carbon-containing
formula, CAS checksum (invalid → CAS cleared, row kept if CID/InChIKey
remains), identity present. Every output row carries `provenance_hash` =
sha256(evidence_text|evidence_url|CID) so downstream users can audit that a
row's evidence exists and is unchanged (P3.3). The output NEVER contains
two rows with the same PubChem CID (P1.2).

AI normalization (strategy P5.1) is available through
`src/utils/ai_hopchain.py`: a provider hop chain (arena `router.py` first,
then env-keyed gemini/mistral/openrouter/llm7) with automatic failover,
adaptive token budgets (4xx → halve; 429/5xx → backoff + next hop),
jittered pacing, strict numbered-JSON parsing and a live per-batch
NONE-rate degradation metric. `normalize_batch(texts, value_field=...)`
works for identity normalization and classification alike; with no AI
available it marks items unresolved and never invents.

### Exhaustive relay failover (v2.16, strategy F4)

`FreeAccessEngine.fetch_with_failover(url, output_dir, host_key=…,
cache_path=…)` tries the geo-block relays IN ORDER (jina → wayback →
commoncrawl → translate → archivetoday) and stops at the first method that
saves a page. The working method per host is cached in a JSON file and
tried first on later runs, so the per-supplier `free_access_methods`
fingerprints become self-maintaining instead of being re-probed from
scratch every crawl.

**This is a starting point, not a claim of completeness** — exactly as dated
and best-effort as any `/api/v1/coverage` report. The expanded export's own
manifest states it: *not a complete national market census, not a
current-stock guarantee*; product-page presence is not proof of stock.

### Fast workflow (zero-network re-parse + instant "is it new?")

```bash
# 1. Prime the resolver's PubChem cache from the baseline (one time).
#    After this, re-parsing any seeded molecule costs ZERO network calls.
python3 -m tools.seed_load preload-cache

# 2. Is this molecule already known? (name / CAS / InChIKey)
python3 -m tools.seed_load search "melamine"     # -> 1 row (CID 7955)
python3 -m tools.seed_load search "67-64-1"      # -> acetone
python3 -m tools.seed_load search "sodium borohydride"  # -> "NOT in seed baseline: NEW"

# 3. Which freshly-parsed rows are NEW vs the baseline?
python3 -m tools.seed_load diff new_rows.json

# 4. Build the live database's starting point (SQLite seed file).
python3 -m tools.seed_load export-sqlite iran_chem_seed.db
#    -> tables: molecules, molecule_suppliers, export_manifest
#    Import this into PostgreSQL as the initial dataset.

# 5. See what the baseline covers.
python3 -m tools.seed_load status
```

Library use (from Python):

```python
from src.utils import seed_db
idx = seed_db.build_index()
idx.lookup("triethanolamine")          # list of seed rows
seed_db.diff_against(idx, new_rows)    # only the molecules you have NOT seen
seed_db.preload_pubchem_cache()        # 0-network re-parses
seed_db.export_sqlite("seed.db")       # database starting point
```

**Proven offline:** with all network sockets blocked, `pubchem_lookup()` still
resolves seeded molecules (melamine → CID 7955, C3H6N6; triethanolamine →
CID 7618) entirely from the preloaded cache.

### Provenance
Three dated exports, all 2026-08-23:
- **v2.16 market-verified (21:08 UTC)** — the 651-row primary baseline
  above: 12 Telegram channels (10,160 posts) + 7 supplier web feeds
  (WooCommerce REST, sitemaps, r.jina.ai relay for geo-blocks) merged on
  PubChem CID, every identity PubChem-confirmed (CID + carbon formula).
  155 empty categories backfilled via the router.py hop chain during
  v2.16 packaging. The strategy document that shaped this release ships
  as `data/seed_export/STRATEGY_iran_chem_database_improvement.md`.
- **v2.14 baseline (03:30 UTC)** — this skill's own pipeline (v2.13.0):
  12 content-verified Persian Telegram channels (12,367 posts) plus public
  supplier web catalogs (Chemical Iran, Karina Polymer, and Jina-relayed
  geo-blocked sites). Identities resolved by the skill's alias dictionary,
  CAS anchors, PubChem enrichment, and — for 194 rows — cloud-model
  identification via the workspace's `router.py`, each cross-checked against
  PubChem CID/CAS. See `coverage_report.json` for per-source coverage and
  the v2.13 country-verification verdict per channel.
- **v2.15 expansion (12:30 UTC)** — 9 additional source sets (TamadKala
  product sitemaps, Fardad Shimi shop listings, DigiShimi/Isatis Shimi
  WooCommerce stores, BehChin Chemi Pharmed public API lists, Pishgaman
  Shimi category pages, ShimiMan sitemap, Rooz Darou pharmaceutical
  catalogue). 1,616 new source records → 948 after the chemistry filter
  (668 excluded: non-confirmed-organic, mixtures, polymers, equipment,
  unresolved). Persian/English product titles were normalized with
  `router.py` and every admitted record was independently structure/formula
  checked via PubChem. Foreign brands listed by Iranian retailers are
  product metadata, not evidence of a foreign supplier.

Example full exports:

```bash
# All identified catalogue molecules, preserving organic uncertainty
curl -L 'http://localhost/api/v1/export?format=csv&shape=molecules&organic_status=all' \
  -o iran-catalogue-molecules-all-statuses.csv

# Only confirmed-organic molecules
curl -L 'http://localhost/api/v1/export?format=csv&shape=molecules&organic_status=true' \
  -o iran-confirmed-organic-molecules.csv

# Unresolved organic status — queue for remediation/review
curl -L 'http://localhost/api/v1/export?format=csv&shape=molecules&organic_status=unknown' \
  -o iran-organic-status-unknown.csv

# Machine-readable export manifest (SHA-256 + row count + coverage snapshot)
curl -L 'http://localhost/api/v1/export?format=manifest&shape=molecules&organic_status=all'
```

`require_complete_coverage=true` makes the export return HTTP 409 until every
configured supplier has a terminal crawl state.

## What it is

A production-ready Linux application that discovers, mirrors, and indexes
Iranian chemical supplier websites, extracting catalogue entries into a live
relational database. Coverage, crawl states (queued → running → success /
partial / failed), rejection reasons and organic-classification uncertainty
are all measured and published.

## Architecture (6 modules)

1. **Supplier Discovery Engine** — seed list (35 curated suppliers, the first
   crawl cohort) + autonomous discovery (search engines EN/FA, link analysis
   of mirrored sites, academic citations, business registries, manual
   curation). Directory discovery is a separate, opt-in, strictly time-bounded
   task so it can never delay seed crawling. Every candidate is verified
   before crawling.
2. **HTTrack Mirror Engine** — Python wrapper around the `httrack` CLI; initial
   mirror, `--update` incremental sync, `hts-changes.json` change detection,
   per-supplier crawl profiles (static/paginated/PDF-Excel/JS/login/blocked),
   Playwright fallback and JS/API catalogue capture with network recording.
2b. **WooCommerce REST + sitemap engine (v2.5)** — the majority of
   catalog-carrying Iranian supplier sites are WordPress/WooCommerce
   storefronts. `src/crawler/woo_rest_engine.py` fetches their PUBLIC,
   unauthenticated product API (`/wp-json/wc/store/v1/products?per_page=100`)
   plus `sitemap.xml`/`product-sitemap.xml`, and persists the JSON into the
   local mirror store — the existing local-file-only parser consumes it with
   no network access. Cheap, structured, and far faster than a full mirror.
3. **Molecule Parser & Classifier** — parses LOCAL mirror files only (HTML,
   JSON-LD, PDF, Excel, CSV, DOCX, JSON-API payloads, Woo REST JSON); configurable
   inclusion policy (`research_only` | `lab_or_research` | `all_identifiable_catalogue`,
   default `all_identifiable_catalogue`); explicit structure-first organic
   classification; RDKit + PubChem + CAS-checksum validation; deterministic
   source identity (real InChIKeys only); every rejection preserved in an
   audit table with stage + reason.
4. **Database Engine** — PostgreSQL (SQLAlchemy): suppliers / molecules /
   supplier_offerings / httrack_mirrors / crawl_log / crawl_run_state /
   offering_history / rejected_catalogue_items; live sync inserts new, updates
   changed, discontinues removed products.
5. **UI & API** — FastAPI REST API (`/api/v1/*` incl. `coverage`, `jobs`,
   `rejections`, `reconciliation`, full `export` + JSON manifest), Streamlit
   dashboard (search, coverage & jobs, rejection audit, reconciliation,
   export readiness).
6. **Health & observability** — `python -m src.scripts.health` verifies the
   stack AND data readiness (INITIALIZED vs OK), distinguishing a fresh
   install from a populated database.

## Quick start (Docker — the authoritative path)

```bash
cp .env.example .env           # REQUIRED: set a strong DB_PASSWORD (installer refuses placeholders)
./install.sh                   # system packages, migrations, seeding, QUEUES the initial crawl
docker compose up -d           # api :8000, dashboard :8501, nginx :80, crawler+scheduler workers
python -m src.scripts.health   # stack + data readiness
```

## Quick start (bare metal — complete)

```bash
sudo apt install httrack
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt && playwright install chromium
cp .env.example .env           # set DB_PASSWORD; SEARCH_API_KEY optional (seed-only discovery works without it)
docker compose up -d postgres redis   # or run PostgreSQL+Redis any way you like (config.yaml)
alembic -c alembic/alembic.ini upgrade head
python -m src.scripts.seed_suppliers
python -m src.scripts.trigger_initial_crawl        # QUEUES seed crawling (returns in seconds)
celery -A src.tasks.celery_app worker --loglevel=info &   # worker (required for the queued crawl)
celery -A src.tasks.celery_app beat --loglevel=info &     # scheduler (hourly sweep + weekly discovery)
uvicorn src.api.app:app --port 8000
```

Dashboard at `http://localhost:8501`, API at `http://localhost:8000/api/v1/`
(Docker: nginx fronts it on port 80).

## Inclusion policy & reparse

```bash
# config.yaml: parsing.inclusion_mode = research_only | lab_or_research | all_identifiable_catalogue
# Re-apply a policy to every existing mirror without re-downloading:
python -m src.scripts.reparse_all_mirrors --inclusion-mode all_identifiable_catalogue
# (reports candidates/accepted/per-reason rejections/sync errors; nonzero exit
#  above parsing.reparse_failure_threshold)
```

Excluded entries are never silently dropped — they live in
`rejected_catalogue_items` with `rejection_stage` + `rejection_reason`
(queryable via `/api/v1/rejections`, dashboard tab "Rejections").

## Requirements checklist (see docs/architecture.md)

HTTrack primary engine · `--update` live sync · `hts-changes.json` selective
parsing · Playwright fallback + JSON-API capture · parser reads LOCAL files
only · measured coverage (no "zero supplier gaps" claim) · configurable
inclusion policy + reparse · explicit organic classification
(structure-first, lookup errors recorded, unknown exported separately) ·
persisted queued/running/terminal crawl states · paginated endpoints announce
pagination (`total_pages`/`has_more`) · full export + JSON manifest ·
rejection audit table · reconciliation reports · live database · Persian NLP ·
RDKit/PubChem validation · deterministic source identity (real InChIKeys
only) · httrack in Docker · persistent mirror volume · polite crawling ·
documented · tested.

## 🆕 v2.8 — multi-tool HTTP fetch fallback (curl / wget / python)

HTTrack is the primary mirror engine, but it can be missing, its default
User-Agent blocked, or a catalog may need only a few pages. The new
`src/crawler/http_fetch_engine.py` provides graceful fallbacks:

- **python-urllib** (always available, no binary) → **curl** (browser UA,
  `-L` redirects) → **wget** (browser UA, `--tries=2`) — first success wins;
- optional **`wget -r -k -p`** recursive mirror as a last-resort site downloader;
- tools are detected at runtime (`shutil.which`); a missing tool is skipped;
- fetched pages land in `<mirror>/fetch-fallback/<tool>/` with the right
  extension (.html/.json/.pdf/...) and flow into the existing local-file parser;
- `crawl_tasks.py` now degrades gracefully when HTTrack is missing or errors,
  and runs the HTTP fallback when a mirror comes back empty (but not
  geo-blocked — those go to the free-access engine). Coverage counts the files.

Config: `http_fetch:` section (enabled, timeout, delay, `wget_recursive` +
depth). Zero new dependencies.

## 🆕 v2.7.1 — Wayback "Save Page Now" (invented via adversarial debate)

Two debate rounds among the reasoning team produced a new, live-verified method:
**SPN2** — `https://web.archive.org/save/<url>` forces the Internet Archive
crawler to fetch a blocked page FRESH from its own (allowed) IPs, then reads the
capture back. Verified live on rockchemie.com (428 KB, 2026-08-22). The method
is appended to every supplier's free-access list automatically and fails
gracefully when IA is busy.

## 🆕 v2.7 — Common Crawl + screenshot fetchers

Exhaustive round-3 sweep added two more free fetchers:

- **Common Crawl** — `https://index.commoncrawl.org` (index) +
  `https://data.commoncrawl.org` (WARC store, S3 — not geo-blocked). Returns
  RECENT full-HTML captures via tiny HTTP Range requests. Verified live:
  rockchemie.com 27 captures (Jul 2026), pgsoc.ir 1, irandaru.com 3,
  shimico.com 407. This gives the "Wayback-only" sites (pgsoc, novichem) a
  second, fresher source. Saved under `<mirror>/free-access/commoncrawl/`.
- **thum.io screenshot** — `https://image.thum.io/get/width/1200/<url>` renders
  the page server-side to a PNG (verified: 492 KB render of rockchemie.com).
  Image-only visual evidence; opt-in (`screenshot`), not in the default list.

`DEFAULT_FREE_ACCESS_METHODS` is now `jina, wayback, commoncrawl, translate,
archivetoday`.

## 🆕 v2.6 — free-access fallback for geo-blocked Iranian sites

Field-verified 2026-08-21 on the 12 geo-blocked seed sites (rockchemie.com,
abnoos.com, artinkimya.com, pakshoo.com, pgsoc.ir, tebgostar.com, novichem.ir,
basparsazan.com, mahdistejarat.com, irandaru.com, shimico.com, parsisotope.com):
**every one of them is reachable through at least one FREE third-party fetcher**
whose own IPs are not on the Iranian hosts' blocklist.

- **Jina Reader** — `https://r.jina.ai/<url>` returns the page as markdown text
  (worked on 9/12 sites). Saved as `.md` under `<mirror>/free-access/jina/`.
- **Wayback Machine** — the CDX API enumerates archived snapshots;
  `https://web.archive.org/web/<ts>id_/<url>` serves the raw HTML (10/12 sites).
  Saved as `.html` under `<mirror>/free-access/wayback/`.
- **Google Translate proxy** — `translate.google.com/translate?u=<url>` fetches
  server-side (9/12 sites). Saved as `.html` under `<mirror>/free-access/translate/`.
- **archive.today** (v2.6.1) — `archive.ph/newest/<url>` serves an existing
  snapshot; reachable from residential/operator networks (blocks many datacenter
  IPs, fails gracefully). Saved under `<mirror>/free-access/archivetoday/`.

`src/crawler/free_access_engine.py` implements all four (stdlib only, no keys);
`src/parser/markdown_parser.py` extracts CAS-bearing molecule candidates from
the Jina text. When a mirror looks geo-blocked (zero files + TLS/timeout
signature), `crawl_tasks.py` runs the free-access engine automatically and the
saved files feed the normal local-file parse pass — so `/coverage` reflects
real fetched content instead of a false "no-html-mirrored".

**Per-site preferences (v2.6.1):** every geo-blocked seed entry carries a
field-verified `free_access_methods` list — e.g. novichem.ir and pgsoc.ir are
**Wayback-only** (their WAFs reset even Jina/Translate), basparsazan.com uses
`["jina","translate"]`, artinkimya.com uses all three. `free_access_preference()`
in `seed_list.py` picks the right methods per site; unknown domains fall back
to `free_access.methods` in `config.yaml`.

## 🆕 v2.5 — what changed (field-hardened)

- **WooCommerce REST + sitemap engine** (`src/crawler/woo_rest_engine.py`):
  the dominant catalog engine among the seeded Iranian suppliers is
  WordPress/WooCommerce. The public Store API (`/wp-json/wc/store/v1/products`)
  needs no key and returns structured products; `sitemap.xml` / `product-sitemap.xml`
  enumerate product URLs cheaply. Fetched JSON lands in the local mirror store
  and is parsed by the existing local-file-only pipeline.
- **Fingerprint-annotated seed list** (`src/discovery/seed_list.py`): every one
  of the 35 suppliers now carries its 2026-08 live-probe status — `active` vs
  `inactive` (12 dead domains, 2 parked, 1 inorganic-only, 1 radiopharma), a
  crawl-profile hint (`woo_rest` / `sitemap_wp` / `playwright_js` / …), notes
  (geo-blocked, WAF) and concrete REST/sitemap entry points. Dead domains are
  seeded `inactive` and skipped by `mirror_all_suppliers` — zero crawl budget
  wasted.
- **Geo-block detection** (`_looks_geo_blocked`): a mirror that yields zero
  files with an SSL/TLS/handshake/timeout signature — the failure mode of ~13
  live `.ir` hosts that reject foreign datacenter IPs — is flagged
  `geo-blocked-possible (retry via Iranian proxy)` instead of being retried
  blindly.
- **Celery dispatch fix** (`trigger_initial_crawl.py`): the previous release
  called `.delay()` on a bare `@shared_task` without the Redis-bound
  `celery_app` as current app, so Celery fell back to the AMQP broker and the
  seed dispatch failed with "Connection refused" while the worker was healthy.
  All dispatch now goes through `celery_app.send_task(...)`.

## 🆕 v2.10 — social catalogue engine (public Telegram channels)

Iranian suppliers publish **live catalogue and price data on public Telegram
channels** — often fresher than their websites, and reachable when the website
is geo-blocked. The preview endpoint `t.me/s/<channel>` is server-rendered,
needs **no login, API key or bot token**, and is not geo-blocked from foreign
datacenter IPs. That makes it the one social source genuinely automatable for
free.

```bash
python -m src.scripts.social_crawl verify    # content-verify channels (live probe)
python -m src.scripts.social_crawl mirror    # mirror to the local store
python -m src.scripts.social_crawl parse     # build the catalogue (LOCAL FILES ONLY)
python -m src.scripts.social_crawl parse --enrich   # + PubChem enrichment
python -m src.scripts.social_crawl leads     # vendor contact leads + wa.me RFQ links
```

**What it does**

- **`src/crawler/telegram_engine.py`** — mirrors a channel by walking
  `?before=<oldest_id>` backwards to the true beginning (id 1). Bounded
  parallel fan-out (capped at 8, default 6) with a request delay keeps it
  polite; per-channel state makes a re-run **incremental** (only pages newer
  than the cache). Raw pages land in `<mirror>/social/telegram/<chan>/`, so the
  **local-file-only parser contract is preserved**.
- **`src/discovery/social_seed_list.py`** — 11 **content-verified** channels
  with roles (`seller_research`, `seller_industrial`, `news`, `lead_source`),
  plus 15 content-checked **rejects** (empty "Channel created" stubs,
  educational channels) recorded with reasons so no budget is re-spent on them.
- **`src/parser/telegram_parser.py`** — role-aware listing discriminator,
  unit-anchored price extraction, contact/CAS capture, and **forwarded-from
  harvesting**, the discovery mechanism that surfaced new real sellers
  (`Boof_company`, `fanchem`).
- **`src/parser/social_molecule_resolver.py`** — resolver chain
  **alias dict → CAS-anchored fallback → PubChem**. PubChem is used only for
  *Latin* names/CAS (it returns 404 for Persian, verified live), while the
  curated dictionary handles Persian naming. Composites and polymers are
  flagged, never force-fitted to a CID.
- **`src/api/routes/social.py`** — `/api/v1/social/channels`, `/coverage`,
  `/molecules` (paginated, announces `total_pages`/`has_more`), `/rejections`,
  `/export` (unpaginated; `require_complete_coverage=true` → HTTP 409), `/leads`.
- **Celery** — `mirror_all_social_channels` runs every 6 h; dispatch goes
  through `celery_app.send_task` (never bare `.delay()`).

**Two precision bugs, fixed and regression-tested**

1. *Market-value false positive.* "۱۰۰ میلیون دلار" in a coatings-news article
   was extracted as a product price. A figure now counts as a price only when a
   pack/volume unit appears as a **word token** near it and no market-scale word
   (million/billion) qualifies it. Token matching also killed a subtle leak
   where the unit `gr` matched inside the English word "group".
2. *Educational articles parsed as listings.* On `news`-role channels a bare
   Persian sales verb is no longer enough — a **strong** marker (price, contact,
   brand or product hashtag) is required. Seller channels still accept verbs.

3. *Recruitment adverts parsed as listings.* Lab marketplaces are dominated by
   job posts carrying salary figures, phone numbers and hashtags — every
   "strong marker" a product listing has. These are now excluded on all roles
   (2,349 phantom candidates removed from the live run).

Plus a lint that fails on **duplicate alias keys** (Python keeps the last, which
had silently discarded a richer alias set).

**Honest scope.** Telegram only. Instagram, Facebook and X are login-walled and
WhatsApp is contact-only/E2E — none are automatable for free from a foreign IP.
Those platforms are exposed as **vendor contact leads** (with `wa.me` RFQ links
a human sends), never as a scraped feed. Rejections are never silently dropped:
`generic_announcement_no_molecule_named` (advertises a catalogue, names no
molecule) is distinguished from `no_alias_or_cas_match` (a real dictionary gap),
so recall metrics stay honest.

## 🆕 v2.11 — Iranian-suppliers-ONLY country gate

**The scope rule is now enforced, not assumed.** Before v2.11 nothing in the
code actually restricted suppliers to Iran: `SupplierValidator` only *added*
points for Iranian-looking signals (so a foreign vendor whose page mentioned
"Tehran" scored 30/100 and was never rejected), and the social/Telegram path
had no country check at all.

`src/discovery/country_gate.py` is now the single enforcement point for both
ingestion paths.

**How a supplier is admitted** — evidence-based, cross-referenced, default deny:

| Signal family | Examples | Weight |
|---|---|---|
| trustmark | Enamad (نماد اعتماد الکترونیکی) — state-verified identity **and** address | 50 |
| registry | شناسه ملی, کد اقتصادی, کد پستی, شماره ثبت | 35–45 |
| domain | `.ir` / `ایران.` ccTLD | 40 |
| phone | `+98` / `0098`, `09xx` mobile, `021`-style landline | 25–35 |
| address | Iranian city **and** country named | 15–30 |
| currency | ریال / تومان pricing | 20 |
| language | Persian content (weak — Persian is not only Iran) | 10 |
| hosting | Iranian IP range (supporting evidence only) | 10 |

Admission requires **≥ 2 INDEPENDENT signal families** (grouping stops one fact
counting twice — a `.ir` domain on Iranian hosting is still one fact) **and** a
total ≥ 60, **and** zero disqualifiers. Only the strongest signal in each family
counts, so repeating weak evidence cannot inflate a score. No evidence ⇒ **DENY**
(an unreachable site can no longer earn points).

**Disqualifiers veto everything**, however strong the positive evidence:
multinational-owned domain (`merckmillipore.com`, `sigmaaldrich.com`,
`chemicalbook.com`, …), foreign ccTLD, or a foreign HQ statement about the
vendor itself ("headquartered in Darmstadt").

### Supplier nationality ≠ product brand

The subtle failure mode a naive filter would cause: Iranian lab-reagent vendors
are overwhelmingly **importers** of Merck/Sigma/TCI product, so their pages are
full of foreign brands and "ساخت آلمان" / "Made in Germany". Treating that as
foreign-origin evidence would delete the most valuable Iranian suppliers in the
dataset. The gate therefore scores the **supplier entity** only: brand and
country-of-manufacture lines are stripped before foreign detection, while a HQ
statement about the vendor is still caught.

Worked example — the Telegram channel `merckmillipore` is **not** Merck KGaA:
its bio reads «واردات مرك به صورت عمده و سفارشى» (bulk Merck importer) with the
Iranian mobile 09121161187. It is a Tehran importer that brand-squats the name,
so the **channel is kept** (Iranian supplier) while the **website
merckmillipore.com is rejected** (German multinational). Both behaviours are
locked by regression tests.

**Auditability** — every verdict carries its evidence (family, signal, matched
value, confidence, source, timestamp):

```bash
python3 tools/audit_country.py            # PASS/FAIL over all supplier sources
python3 -m src.scripts.social_crawl audit-country
curl -s localhost/api/v1/social/country-policy | jq .
```

## 🆕 v2.12 — hardened extraction, Persian gate, one-command retrieval

### The extraction problem this fixes

v2.11 resolved a post only if the curated alias dictionary matched a name in
it. Everything else became `no_alias_or_cas_match` — **3,256 posts** in the
live corpus. Sampling them showed the loss was not noise but the most valuable
post shape on the network, the **structured catalogue line**:

```
006123 Exir Melamine, 99% 500g
🔜 موجود و آماده تحویل  ✅ شیمیران صنعت فقط اصلی
```

SKU, brand, IUPAC name, purity and pack size — discarded because "Melamine"
was not in the dictionary. Growing the dictionary is a treadmill; parsing the
*shape* is not.

`src/parser/listing_extractor.py` now extracts, from every post:

| Field | Example |
|---|---|
| `sku` | `006123` |
| `brand` | Merck, Sigma-Aldrich, Exir, Daejung (Persian «مرک» too) |
| `product_name` | `1,4-Butanediol` (locants preserved) |
| `purity_percent` | 99.5 (Persian digits «۹۸ درصد» handled) |
| `grade_token` | USP, GR, HPLC, ACS |
| `pack_size` | `۵ کیلوگرم` → 5000 g; `2.5L` → 2500 ml |
| `cas_numbers` | checksum-validated (rejects dates/phones) |
| `availability` | in_stock / to_order / unavailable |

Extracted names are resolved against the alias dictionary, then PubChem
(`structured_pubchem`). A structured post is also admitted by the listing
discriminator **without** a sales verb or price.

**Result on the live corpus: molecules 84 → 240, listings 685 → 852, vendors
10 → 12** — and every `structured_pubchem` listing carries a real PubChem CID
and molecular formula (0 missing).

### 🇮🇷 Persian/Farsi channel gate

Every channel must now be **Iranian (country gate) AND publish Persian**.
`src/parser/persian_gate.py` measures the share of Persian posts across the
whole mirror (≥30% required) and distinguishes **Persian from Arabic** using
Persian-exclusive letters (گ چ پ ژ ک ی) plus Persian/Arabic function words —
measured on the RAW text, because normalisation folds ي→ی and would erase the
discriminator. English-only and Arabic-script channels are refused.

Enforcement is at **channel** level by design: a Latin-only catalogue line
inside a verified Persian channel is kept, because that is exactly the
high-value structured data above. All 12 seeded channels are verified Persian
(56%–100%).

### Retrieval — one command

```bash
# mirror + parse + export in one go
python3 -m src.scripts.social_crawl fetch --enrich --out listings.csv

# search by name, CAS, brand, SKU — or in Persian
python3 -m src.scripts.social_crawl search --query "سدیم هیدروکسید"
python3 -m src.scripts.social_crawl search --query 67-56-1 --out methanol.csv
python3 -m src.scripts.social_crawl search --query acid --brand Merck --in-stock

# prove the scope
python3 -m src.scripts.social_crawl audit-persian
python3 -m src.scripts.social_crawl audit-country
```

`--out` writes `.csv`, `.json` or `.xlsx` by extension. Persian queries work
because each listing keeps a `text_snippet` of the vendor's own wording.
API equivalents: `/api/v1/social/search`, `/api/v1/social/persian-policy`.

PubChem results are cached on disk (`ICDB_PUBCHEM_CACHE`), so a re-parse of a
mirrored corpus is fast and reproducible.

## ✅ Verify before relying on it (v2.9)

```bash
python3 scripts/preflight.py      # environment readiness (httrack/curl/wget)
python3 scripts/self_test.py      # offline self-test (compile + files + imports + pytest subset)
python3 tools/package_selftest.py # release readiness (run before publishing)
python3 -m pytest -q              # full suite (DB tests self-skip without PostgreSQL)
python3 -m ruff check src/ scripts/ tools/   # bug-focused lint (E/F/W/B)
```

CI (`.github/workflows/ci.yml`) runs all of the above on every push and PR.

## 🔒 Security posture

- **Outbound is crawling-only.** The `network.outbound: ["*"]` declaration is
  *by design*: the whole purpose is mirroring arbitrary supplier websites. In
  practice the app only makes requests to (a) supplier/B2B URLs you configure,
  and (b) optional public APIs (PubChem for validation, search APIs if you
  provide a key). Nothing is uploaded about you or your machine.
- **No secrets in the skill.** `DB_PASSWORD` / `SEARCH_API_KEY` come from the
  environment (`.env`, gitignored); `.env.example` ships WITH the release.
- **Local-first.** The parser reads only local mirror files; mirrors live under
  `/var/lib/iran_chem_db/mirrors`.
- **Polite crawling.** robots.txt honored, rate-limited, identifiable
  User-Agent, per-supplier overrides.
- **Production hardening** (see `docs/deployment_guide.md`): put the API behind
  nginx with authentication, allowlist egress to supplier domains if you use a
  firewall, and treat the API/dashboard as trusted-network services by default.

## Legal & ethical use

Only mirror websites you are authorized to archive. Respect robots.txt and site
terms of service. The database is a research/procurement reference — verify
every supplier and molecule before relying on it.

## Files

See `README.md` (security/privacy + verification hashes), `CHANGELOG.md`,
`docs/` (architecture, API reference, deployment), `tests/`, and the full
`src/` tree.
