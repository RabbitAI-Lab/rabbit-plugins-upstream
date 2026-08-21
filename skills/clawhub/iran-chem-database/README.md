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
| Supplier Discovery | `src/discovery/` | seed list (35 suppliers + 15 directories) + search engines, HTTrack directory crawling, link analysis, citations, registries |
| HTTrack Mirror Engine | `src/crawler/` | `httrack` wrapper, `--update`, `hts-changes.json`, profiles, Playwright fallback, mirror manager |
| Parser & Classifier | `src/parser/` | LOCAL HTML/PDF/Excel parsing, research-grade classifier, RDKit/PubChem validator, CAS resolver |
| Database Engine | `src/database/` | SQLAlchemy models, live sync, change tracker, queries |
| UI & API | `src/api/`, `src/dashboard/` | FastAPI REST + Streamlit dashboard (mirror monitor) |
| Tasks | `src/tasks/` | Celery crawl/discovery/sync tasks |
| Tests | `tests/` | unit + integration + fixtures |
| Docs | `docs/` | architecture, HTTrack integration, API, deployment, adding suppliers |

## Quick start

```bash
# Docker (httrack installed in the container)
cp .env.example .env
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

- **SKILL.md SHA-256:** `044faa5456a9a826302b2bc7e83fde4e67cf26ec77c2cecc2ae0cf1093272b61`
- **src/crawler/httrack_engine.py SHA-256:** `b463f13cf7c889ebcdb94e270b06184b69d8b77fd0f0d411319866e8d0002079`
- **src/parser/grade_classifier.py SHA-256:** `05ced7c7ed6c4fb59dd569582db3fc0897c9c969fd098fd5c9e43d5be9922edc`
- **requirements.txt SHA-256:** `c180b9ff8c4f2ac1f57ae6c910fc474de87af76c93febb0d590b53e6d2985634`

Verify locally:

```bash
sha256sum SKILL.md src/crawler/httrack_engine.py src/parser/grade_classifier.py requirements.txt
# compare the output to the SHA-256 values above.
```

---

## License

MIT-0 (see `LICENSE`). HTTrack itself is GNU GPL v3 and is a system dependency,
not part of this repository.
