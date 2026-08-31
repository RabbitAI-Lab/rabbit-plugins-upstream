# 🧪 Iran Chemical Database — HTTrack-Powered Live Crawling System

> **🔴 Installation provides SOFTWARE, not a populated dataset.** Services and
> jobs are initialized; the initial crawl is queued and may take hours or days.

**A production-ready Linux application that automatically discovers, mirrors
(via HTTrack), and indexes Iranian chemical supplier websites — as a dated,
auditable, best-effort supplier-offering index with measured, published
coverage,
extracts their research-grade chemical molecule catalogs, and maintains a live,
continuously-updated relational database.**

HTTrack is the primary fetching engine: the app wraps the `httrack` CLI to mirror
supplier sites, updates them incrementally with `httrack --update`, and uses
`hts-changes.json` for change-driven re-parsing. A Playwright layer renders
JavaScript-heavy pages into the same mirror store. The parser reads **only local
mirror files**, classifies molecules as research-grade (strict English + Persian
rules), validates them with RDKit/PubChem/CAS-checksum, and syncs a PostgreSQL
database (FastAPI REST API + Streamlit dashboard + Celery scheduling).

## Architecture

| Module | Location | Role |
|---|---|---|
| Supplier Discovery | `src/discovery/` | seed list (58 suppliers + 15 directories) + search engines, HTTrack directory crawling, link analysis, citations, registries |
| HTTrack Mirror Engine | `src/crawler/` | `httrack` wrapper, `--update`, `hts-changes.json`, profiles, Playwright fallback, mirror manager |
| WooCommerce REST + sitemap | `src/crawler/woo_rest_engine.py` | public `/wp-json/wc/store/v1/products` + `sitemap*.xml` → local JSON (v2.5) |
| Free-access fallback | `src/crawler/free_access_engine.py` | Jina Reader + Wayback + Google Translate fetches for geo-blocked `.ir` hosts (v2.6) |
| HTTP fetch fallback | `src/crawler/http_fetch_engine.py` | python-urllib / curl / wget single-page + `wget -r` mirror when HTTrack fails (v2.8) |
| Social catalogue (Telegram) | `src/crawler/telegram_engine.py`, `src/parser/telegram_parser.py` | mirrors PUBLIC `t.me/s/<chan>` (no login/API key, not geo-blocked) with backward pagination + incremental resync; role-aware listing discriminator, unit-anchored prices, forwarded-from channel discovery (v2.10) |
| Social molecule resolver | `src/parser/social_molecule_resolver.py` | alias dict → CAS anchor → PubChem (Latin only; PubChem 404s on Persian); composites/polymers flagged not force-fitted (v2.10) |
| Seed baseline (v2.14–v2.22) | `data/seed_export/`, `src/utils/seed_db.py`, `tools/seed_load.py` | **1399 CID-unique confirmed-organic PRIMARY** (`iran_organic_molecules_catalogue_verified_2026-08-27.csv`, v2.22) plus retained historical files (1041-row v2.19 primary, 873-row market-verified, parallel-AI, expanded, legacy) + inorganic exclusions + O(1) name/CAS/InChIKey/CID index, name-variant tracking, "is it new?" diff, zero-network PubChem-cache preload, SQLite starting point with UNIQUE identity_key |
| Verified export + AI resilience (v2.16) | `tools/export_verified.py`, `src/utils/ai_hopchain.py`, `src/crawler/free_access_engine.py::fetch_with_failover` | one-command gates → CID dedupe at admission → unified schema → per-row provenance hash (zero same-CID output, rejections to sidecar); provider hop chain (arena router.py first) with failover + adaptive budgets; ordered relay failover with per-host working-method cache |
| Parser & Classifier | `src/parser/` | LOCAL HTML/PDF/Excel/JSON/Markdown parsing, research-grade classifier, RDKit/PubChem validator, CAS resolver |
| Database Engine | `src/database/` | SQLAlchemy models, live sync, change tracker, queries |
| UI & API | `src/api/`, `src/dashboard/` | FastAPI REST + Streamlit dashboard (mirror monitor) |
| Tasks | `src/tasks/` | Celery crawl/discovery/sync tasks |
| Tests | `tests/` | unit + integration + fixtures |
| Docs | `docs/` | architecture, HTTrack integration, API, deployment, adding suppliers |

## Quick start

```bash
# Docker (httrack installed in the container)
cp env.example .env   # or .env.example if you cloned the source tree
./install.sh

# Bare metal
sudo apt install httrack
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt && playwright install chromium
alembic upgrade head
python -m src.scripts.seed_suppliers
uvicorn src.api.app:app --host 0.0.0.0 --port 8000
```

- Dashboard: http://localhost:8501
- API: http://localhost:8000/api/v1/
- HTTrack mirrors: `/var/lib/iran_chem_db/mirrors/`

### 🌱 Seed baseline (no services needed)

The package ships a 1399-molecule CID-unique confirmed-organic crawl export in `data/seed_export/` (plus historical seed files, incl. the 1041-row 2026-08-25 primary).
Use it to start the live database and to skip re-resolving molecules you have
already seen — no Docker/PostgreSQL/Redis required for any of this:

```bash
python3 -m tools.seed_load status                 # what the baseline covers
python3 -m tools.seed_load preload-cache          # 0-network re-parses
python3 -m tools.seed_load search "melamine"      # name / CAS / InChIKey
python3 -m tools.seed_load diff new_rows.json     # which are NEW
python3 -m tools.seed_load export-sqlite seed.db  # PostgreSQL starting point
```

### 🔁 One-command verified export (v2.16+)

```bash
# reproduce the 873-row market-verified baseline (zero same-CID rows,
# per-row provenance hash, rejections -> <out>.rejected.csv)
python3 -m tools.export_verified \
  --files data/seed_export/iran_organic_molecules_market_verified.csv \
  --out verified.csv

# full merged baseline
python3 -m tools.export_verified --from-seed --out baseline.csv
```

## 🔐 Permissions & Requirements

- Runtime: Python 3.11+, the `httrack` system binary (`sudo apt install httrack`),
  PostgreSQL 15+, Redis (for Celery), and — for the JS fallback — Playwright
  Chromium (`playwright install chromium`).
- Network: **outbound HTTP/HTTPS only to the supplier/B2B sites it is configured
  to mirror**, plus optional public APIs (PubChem for validation, SerpAPI/Google
  CSE for discovery if you provide a key). No inbound services except the local
  FastAPI/Streamlit/nginx ports.
- Filesystem: writes the mirror store under `/var/lib/iran_chem_db/mirrors`
  (configurable) and logs under `/var/log/iran_chem_db`.
- Secrets: `DB_PASSWORD` and optional `SEARCH_API_KEY` are read from the
  environment / `.env` only — never hardcoded.

## 🔒 Security & Privacy

- What it reads/collects: the public web pages and catalog files of the supplier
  sites you configure it to mirror, stored locally for offline parsing.
- Does data leave the machine? It **downloads from** the target sites to your
  local mirror store; it does not upload or transmit anything about you. The only
  outbound traffic is the mirroring itself (and optional PubChem/search lookups).
- **Third-party AI providers:** when the normalization hop chain
  (`src/utils/ai_hopchain.py`) is enabled, *crawled listing text* (Persian/English
  product titles) is sent to the configured AI providers to be normalised into a
  molecule name/category. Listing text leaves the machine in that path. It is
  used for identity normalization ONLY — never to invent rows — and every result
  is independently confirmed against PubChem. Disable the hop chain if your
  sources are sensitive.
- No secrets are read, stored, logged, or transmitted by the skill; `.env` is
  gitignored and read from the environment only.
- Known risks: crawling third-party sites can violate their terms of service or
  robots.txt if misconfigured; extracted chemical data (grade/purity/price/GHS)
  can be inaccurate or stale; mirrored pages may contain scripts/cookies.
- Mitigations: polite-crawling defaults (robots.txt `--robots=2`, rate limits,
  identifiable User-Agent), per-supplier overrides, strict research-grade
  filtering, RDKit/PubChem validation with confidence flags, and clear guidance
  to verify every supplier/molecule before relying on it. Coverage is
  reported via `/api/v1/coverage`; the system does NOT promise "every
  supplier" or complete market coverage.
- Review before install: read `SKILL.md`, `docs/architecture.md`, and
  `src/crawler/httrack_engine.py`.

## ✅ Verification Hash

Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digests below:

- **SKILL.md SHA-256:** `ab622b91700256750d0466f1caedd62d657213044f1d0ee6379d011d5573ffec`
- **CHANGELOG.md SHA-256:** `a2a6be09a28742b5df322dd88adb6ee5dd15a5010b5fd9c015eb80fa4217c439`
- **src/crawler/httrack_engine.py SHA-256:** `4e5a79413c07ae8b19c69e6fae2c2216d4540ff023fcb25293e0ff8056c298b4`
- **src/parser/grade_classifier.py SHA-256:** `05ced7c7ed6c4fb59dd569582db3fc0897c9c969fd098fd5c9e43d5be9922edc`
- **requirements.txt SHA-256:** `c180b9ff8c4f2ac1f57ae6c910fc474de87af76c93febb0d590b53e6d2985634`
- **src/utils/seed_db.py SHA-256:** `0bdcb0df6e214e728dd7ccea7057c78d63038d6f32410101e0b06e783d680eeb`
- **tools/seed_load.py SHA-256:** `8389b261499c387c2035dd32ce104996875527821846179b91c72cffc0116a75`
- **tools/export_verified.py SHA-256:** `91eacdc42d4530dc3f0f6c147de74a0dc4069ecb84143aea5dcfb3fc5ab2080c`
- **src/utils/ai_hopchain.py SHA-256:** `24f5933b5583e945c50024d0e49f129710b8dac33966f287a91092b0bf1e097e`
> Note: the ClawHub registry strips leading-dot files from published artifacts, so the
> release ships `env.example` (identical content). `install.sh` accepts either name.

- **env.example SHA-256:** `06ad1684bcb3862af39095b507dd0804e560667bd927d3abb2a4f7199642e5dc`
- **data/seed_export/iran_organic_molecules_catalogue_verified_2026-08-27.csv SHA-256:** `f7db86689208a5c775e952e6fb46c27e1304eaa45aa943d81480a68a66da0493`
- **data/seed_export/iran_organic_molecules_catalogue_verified_2026-08-25.csv SHA-256:** `3c704d3ad9647ecde6236d1315a29ea2b6c815f73c02960650bc4b97b2ae8be6`
- **data/seed_export/iran_organic_molecules_market_verified.csv SHA-256:** `263f835aa53c06ece88ffc79d49ba9083d0c2957c16cc288730b37384f3bcfa1`
- **data/seed_export/iran_organic_molecules_expanded.csv SHA-256:** `42fc077f7bc6255afc7f0576993a677c0327fcde32cb2e6d906d2ed9fdb38804`
- **data/seed_export/iran_organic_molecules.csv SHA-256:** `b0b1e165327c2ac5832a61c396881822d1daa2bf21aab9de2bb70bdef976844c`
- **data/seed_export/iran_inorganic_excluded.csv SHA-256:** `fe87e12a70b3cda9c2b7b1b159ec2247f4af6cc031feca14c1a5b7777078fdc7`
- **data/seed_export/coverage_report.json SHA-256:** `19e428b375264de65e8408ce9d731236940a51bfc7a0d2bab973f4fd2cf7a642`

Verify locally:

```bash
sha256sum SKILL.md CHANGELOG.md src/crawler/httrack_engine.py src/parser/grade_classifier.py \
  requirements.txt src/utils/seed_db.py tools/seed_load.py tools/export_verified.py \
  src/utils/ai_hopchain.py env.example \
  data/seed_export/iran_organic_molecules_catalogue_verified_2026-08-27.csv \
  data/seed_export/iran_organic_molecules_catalogue_verified_2026-08-25.csv \
  data/seed_export/iran_organic_molecules_market_verified.csv \
  data/seed_export/iran_organic_molecules_expanded.csv \
  data/seed_export/iran_organic_molecules.csv \
  data/seed_export/iran_inorganic_excluded.csv data/seed_export/coverage_report.json
# compare the output to the SHA-256 values above.
```
---

## License

MIT-0 (see `LICENSE`). HTTrack itself is GNU GPL v3 and is a system dependency,
not part of this repository.
