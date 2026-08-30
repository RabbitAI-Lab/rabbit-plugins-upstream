---
name: iran-chem-database
version: 2.22.0
author: orionshaowswmw
license: MIT-0
description: "Iran Chemical Database — live, dated, auditable, BEST-EFFORT index of chemical offerings in configured public Iranian supplier catalogues (websites + public Telegram channels). HTTrack/WooCommerce-REST/Telegram mirroring → local-only parsing → RDKit/PubChem/CAS-validated PostgreSQL with FastAPI + Streamlit. Fail-closed Iranian-suppliers-only country gate; coverage measured and published, never claimed complete. Installation = software + queued crawl, not a populated dataset. Ships a 1399-molecule CID-unique confirmed-organic seed baseline (v2.22, 2026-08-27: v2.19 primary + live Telegram/WooCommerce/sitemap crawl + 5-model fleet normalization, every new identity PubChem-confirmed). For academic procurement research."
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

# 🧪 Iran Chemical Database

> **🔴 Install = SOFTWARE, not data.** The initial crawl is QUEUED (hours/days). Before ANY molecule request: check `/api/v1/coverage` and state whether the crawl is complete, partial, or running. This is a best-effort index of the **configured suppliers' public catalogues** — never a national census; never infer national availability; never describe the database as "complete".

## Mandatory agent rules

1. **Terminology:** `organic_status=true` ⇒ say **"confirmed organic"**, never "all organic". Unknown-organic rows are exported separately, never silently dropped.
2. **Pagination:** `/api/v1/molecules` is paginated (default 20, `limit` ≤ 100, `total_pages`/`has_more`). Full data only via `/api/v1/export` (unpaginated). Always include the export manifest (`format=manifest` or the CSV's `# export_metadata:` line) and report its row count. `require_complete_coverage=true` ⇒ HTTP 409 until every supplier reaches a terminal crawl state.
3. **Social catalogue is Telegram-only.** Check `/api/v1/social/coverage` first; name the mirrored channels. Instagram/Facebook/X/WhatsApp are contact **leads** only — never present them as crawled. Social listings are supplier posts, **not verified stock**.
4. **🇮🇷 Iranian suppliers only — fail-closed.** Admission (country gate, default DENY) needs **≥ 2 independent signal families** (trustmark/Enamad, registry IDs شناسه ملی/کد اقتصادی/کد پستی, `.ir` domain, +98 phone, Iranian address, IRR pricing, Persian content, Iranian hosting — exact weights in `tools/audit_country.py` / `/api/v1/social/country-policy`) **and score ≥ 60, and zero foreign disqualifiers** (multinational-owned domain, foreign ccTLD, foreign HQ statement); state this scope in reports. **Supplier ≠ brand:** Iranian importers legitimately reselling Merck/Sigma/TCI are kept (foreign brand = product metadata); the multinationals themselves are rejected; never add a supplier just because it ships to Iran. Don't trust a CSV's `supplier_verified` column — re-derive it yourself and cite the endpoint: `social_crawl verify-suppliers --level offline|live|paranoid [--dataset listings.csv] [--explain]` (offline = local check-digit + mirror; live = re-fetch t.me; paranoid = rebuild verdict from live page alone). Rows failing verification go to **quarantine**, not your answer.
5. **Persian required per channel.** Channels are Iranian AND ≥ 30% Persian (Persian distinguished from Arabic via exclusive letters, measured on raw text — cite `/api/v1/social/persian-policy` / `social_crawl audit-persian`). Keep Latin-script catalogue lines inside verified Persian channels (they carry SKU/brand/purity/pack data). For retrieval prefer `social_crawl search` / `/api/v1/social/search` and report `identity_method` (`structured_pubchem` vs `alias`).
6. **Seed baseline first — it makes repeated work free.** `data/seed_export/` ships dated crawl exports (`…_catalogue_verified_2026-08-27.csv` **primary = 1399 CID-unique confirmed-organic rows**, every row PubChem-confirmed, `provenance_hash` per row, `cas_cid_conflict` flags supplier CAS/CID disagreements instead of silently editing them; the 2026-08-25 primary and previous `…_market_verified.csv` / parallel-AI / expanded / legacy files retained for audit + `iran_inorganic_excluded.csv` + `coverage_report.json`; NOT a market census, product pages ≠ stock). Before crawling or answering: `python3 -m tools.seed_load search "<name|CAS|InChIKey>"` (instant NEW-vs-known), `diff new_rows.json`, `status`; `preload-cache` makes re-parses zero-network; `export-sqlite iran_chem_seed.db` builds the DB starting point.

## Data access

```bash
# Full export (all organic statuses; also organic_status=true|unknown)
curl -L 'http://localhost/api/v1/export?format=csv&shape=molecules&organic_status=all' -o all.csv
curl -L 'http://localhost/api/v1/export?format=manifest&shape=molecules&organic_status=all'   # SHA-256 + rows + coverage

# One-command verified pipeline: gates -> CID dedupe -> unified schema -> provenance_hash = sha256(evidence_text|evidence_url|CID)
python3 -m tools.export_verified --from-seed --out baseline.csv        # --enforce-country for fail-closed gate
# Telegram social data: mirror + parse + export in one command
python3 -m src.scripts.social_crawl fetch --enrich --out listings.csv
python3 -m src.scripts.social_crawl search --query "سدیم هیدروکسید" --brand Merck --in-stock --out f.csv
# scope audits
python3 -m src.scripts.social_crawl audit-country; audit-persian
```
Gates are fail-closed; rejections land in `<out>.rejected.csv` with reasons — never silently discarded. AI normalization (`src/utils/ai_hopchain.py`): arena `router.py` first, then env-keyed providers, automatic failover + adaptive budgets; marks items unresolved when no AI is available — never invents.

## Stack (6 modules) & crawl engines

Discovery (58 fingerprint-annotated seeds: active/inactive/geo-blocked/WooCommerce status, crawl-profile hints — dead domains skipped) · **HTTrack** mirror engine (`--update` incremental, `hts-changes.json`, per-supplier profiles, Playwright fallback for JS/API) · **WooCommerce REST + sitemap engine** (public `/wp-json/wc/store/v1/products?per_page=100` + `product-sitemap.xml` — the dominant catalogue source) · Parser reads **LOCAL mirror files only** (HTML/JSON-LD/PDF/Excel/CSV/DOCX/JSON; inclusion policy `research_only|lab_or_research|all_identifiable_catalogue`, re-apply without re-download via `src.scripts.reparse_all_mirrors --inclusion-mode X`; rejections audited with stage+reason) · structure-first organic classification + RDKit/PubChem/CAS-checksum validation + deterministic InChIKey identity · PostgreSQL (SQLAlchemy) + Celery (hourly sweep, weekly discovery, 6-hourly social resync; dispatch always via `celery_app.send_task`) · FastAPI `/api/v1/*` + Streamlit dashboard · `python -m src.scripts.health` (stack AND data readiness: INITIALIZED vs OK).

**Geo-block fallback (automatic).** Zero-files + TLS/timeout signature ⇒ relay chain in order: jina → wayback (CDX + Save-Page-Now) → commoncrawl → translate → archivetoday, first success cached per host (self-maintaining; per-site preferences live in `seed_list.py`). If HTTrack is missing/blocked: python-urllib → curl → wget (optional `wget -r` recursive last resort); files land in the mirror store and feed the normal parser. Fetched pages count toward coverage.

**Telegram engine.** `t.me/s/<chan>` public previews — no login/API key, not geo-blocked; bounded-parallel backward pagination to channel start; incremental resync; local-file-only parse. Structured field extractor resolves posts **by shape** (SKU, brand, product name with locants, purity incl. Persian digits, grade, pack normalized to g/ml, checksum-validated CAS, availability) → alias dictionary → CAS anchor → PubChem (disk-cached via `ICDB_PUBCHEM_CACHE`). Prices require a unit word token nearby (no market-scale words); news/recruitment posts excluded; forwarded-from harvesting discovers new sellers.

## Install

```bash
# Docker (authoritative)
cp .env.example .env           # REQUIRED: strong DB_PASSWORD (installer refuses placeholders)
./install.sh                   # packages, migrations, seeding; QUEUES initial crawl
docker compose up -d           # api :8000, dashboard :8501, nginx :80, workers
python -m src.scripts.health
# Bare metal: httrack + venv + requirements.txt + `playwright install chromium` + PostgreSQL/Redis
#   → alembic upgrade head → seed_suppliers → trigger_initial_crawl → celery worker & beat → uvicorn :8000
```

## Verify before relying on it

`scripts/preflight.py` (env) · `scripts/self_test.py` (offline) · `tools/package_selftest.py` (release) · `pytest -q` (DB tests self-skip without PostgreSQL) · `ruff check src/ scripts/ tools/` — CI runs all on every push/PR.

## Security & legal

Outbound is crawling-only by design (`network.outbound: ["*"]` = arbitrary configured supplier URLs + optional PubChem/search APIs; nothing about you is uploaded) · secrets only via environment `.env` (gitignored; `.env.example` ships) · local-first mirrors under `/var/lib/iran_chem_db/mirrors` · polite robots-aware rate-limited crawling · API/dashboard are trusted-network services — front with nginx + auth for production. Mirror only sites you are authorized to archive; verify every supplier/molecule before reliance.

Version history (v2.5 → v2.21): `CHANGELOG.md`. Architecture/API/deployment: `docs/`, `README.md`.
