---
name: iran-chem-database
description: "Iran Chemical Database — an HTTrack-powered live crawling system that builds a dated, auditable, BEST-EFFORT index of confirmed and unresolved chemical offerings discovered in configured public Iranian supplier catalogues. Discovers and mirrors supplier websites with HTTrack (polite crawling, robots-aware), extracts catalogue entries from local mirrors (HTML/JSON-LD/PDF/Excel/DOCX/JSON-API), classifies with a configurable inclusion policy (research_only | lab_or_research | all_identifiable_catalogue) plus explicit structure-first organic classification, validates with RDKit/PubChem, and maintains a live PostgreSQL database with FastAPI + Streamlit interfaces. Coverage, crawl states and rejection reasons are measured and published — never claimed complete. Installation provides software, not a populated dataset. Persian NLP support, Playwright + network-recording fallback for JS/API catalogues, Celery scheduling, Docker deployment. For academic procurement research."
version: 2.4.0
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
3. **Molecule Parser & Classifier** — parses LOCAL mirror files only (HTML,
   JSON-LD, PDF, Excel, CSV, DOCX, JSON-API payloads); configurable inclusion
   policy (`research_only` | `lab_or_research` | `all_identifiable_catalogue`,
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
