---
name: iran-chem-database
description: "Iran Chemical Database — an HTTrack-powered live crawling system that autonomously discovers every Iranian chemical supplier, mirrors their websites with HTTrack, extracts research-grade molecule catalogs from the local mirrors, validates them with RDKit/PubChem, and maintains a live PostgreSQL database with FastAPI + Streamlit interfaces. Research-grade only (strict English/Persian grade classification), Persian NLP support, Playwright fallback for JS sites, Celery scheduling, Docker deployment. For academic procurement research."
version: 2.1.0
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

**A production-ready Linux application that discovers, mirrors, and indexes every
Iranian chemical supplier's website — extracting research-grade molecule catalogs
into a live, continuously-updated relational database.**

This skill packages the complete application specified by the project master prompt:
HTTrack as the primary fetching engine, autonomous supplier discovery, local-file
parsing, strict research-grade classification, RDKit/PubChem validation, live
database sync, FastAPI REST API, Streamlit dashboard, Celery scheduling, and full
Docker deployment. It ships **complete, runnable source code** — no stubs.

## Architecture (5 modules)

1. **Supplier Discovery Engine** — seed list (35 known suppliers + 15 B2B
   directories) + autonomous discovery (search engines EN/FA, HTTrack directory
   crawling, link analysis, academic citations, business registries).
2. **HTTrack Mirror Engine** — Python wrapper around the `httrack` CLI; initial
   mirror, `--update` incremental sync, `hts-changes.json` change detection,
   pre-built profiles (standard/PDF/large/sensitive/login/.ir), Playwright
   fallback for JS-rendered sites.
3. **Molecule Parser & Classifier** — parses LOCAL mirror files only
   (BeautifulSoup HTML, pdfplumber/PyMuPDF PDF, openpyxl/pandas Excel);
   strict research-grade filter (English + Persian keywords, excludes
   industrial/technical/food grades); RDKit + PubChem + CAS-checksum validation;
   InChIKey deduplication.
4. **Database Engine** — PostgreSQL (SQLAlchemy) with suppliers / molecules /
   supplier_offerings / httrack_mirrors / crawl_log / offering_history;
   live sync inserts new, updates changed, discontinues removed products.
5. **UI & API** — FastAPI REST API (`/api/v1/*`), Streamlit dashboard with an
   HTTrack Mirror Monitor panel, CSV/JSON/SDF export.

## Quick start

```bash
# Docker (httrack is installed inside the container via the Dockerfile)
cp .env.example .env        # set DB_PASSWORD
./install.sh                # installs httrack+docker, builds, seeds, starts

# Or bare metal
sudo apt install httrack
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt && playwright install chromium
alembic upgrade head
python -m src.scripts.seed_suppliers
uvicorn src.api.app:app --port 8000
```

Dashboard at `http://localhost:8501`, API at `http://localhost:8000/api/v1/`.

## Requirements checklist (met — see docs/architecture.md)

HTTrack primary engine · `--update` live sync · `hts-changes.json` selective
parsing · Playwright fallback only · parser reads LOCAL files only · zero
supplier gaps · research-grade only · live database · Persian NLP · RDKit/PubChem
validation · InChIKey dedup · audit trail · httrack in Docker · persistent mirror
volume · polite crawling · scalable · documented · tested.

## 🔒 Security posture

- **Outbound is crawling-only.** The `network.outbound: ["*"]` declaration is
  *by design*: the whole purpose is mirroring arbitrary supplier websites. In
  practice the app only makes requests to (a) supplier/B2B URLs you configure,
  and (b) optional public APIs (PubChem for validation, search APIs if you
  provide a key). Nothing is uploaded about you or your machine.
- **No secrets in the skill.** `DB_PASSWORD` / `SEARCH_API_KEY` come from the
  environment (`.env`, gitignored) only.
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

See `README.md` (this file doubles as the project README with security/privacy
and verification hashes), `docs/`, `tests/`, and the full `src/` tree.
