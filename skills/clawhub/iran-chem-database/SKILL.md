---
name: iran-chem-database
description: "Iran Chemical Database — an HTTrack-powered live crawling system that builds a dated, auditable, BEST-EFFORT index of confirmed and unresolved chemical offerings discovered in configured public Iranian supplier catalogues. Discovers and mirrors supplier websites with HTTrack (polite crawling, robots-aware), extracts catalogue entries from local mirrors (HTML/JSON-LD/PDF/Excel/DOCX/JSON-API), classifies with a configurable inclusion policy (research_only | lab_or_research | all_identifiable_catalogue) plus explicit structure-first organic classification, validates with RDKit/PubChem, and maintains a live PostgreSQL database with FastAPI + Streamlit interfaces. Coverage, crawl states and rejection reasons are measured and published — never claimed complete. Installation provides software, not a populated dataset. v2.6 adds a WooCommerce/WordPress REST + sitemap engine (public /wp-json/wc/store/v1/products), a fingerprint-annotated seed list (dead/parked/geo-blocked/WooCommerce per-URL), geo-block detection, and a fixed Celery dispatch path. Persian NLP support, Playwright + network-recording fallback for JS/API catalogues, Celery scheduling, Docker deployment. For academic procurement research."
version: 2.9.0
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
