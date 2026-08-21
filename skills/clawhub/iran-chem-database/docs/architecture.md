# Architecture — Iran Chemical Database

HTTrack-powered live crawling architecture for discovering, mirroring, and
indexing Iranian chemical suppliers' catalogues as a measured best-effort index.

## Module layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        MASTER CONTROLLER                                │
│              (Orchestrator / Scheduler / Monitor)                       │
├───────────┬──────────────┬────────────┬────────────┬───────────────────┤
│ MODULE 1  │   MODULE 2   │  MODULE 3  │  MODULE 4  │     MODULE 5      │
│ Supplier  │   HTTrack    │  Molecule  │  Database  │   UI / API        │
│ Discovery │   Mirror     │  Parser &  │  Engine    │   Interface       │
│ Engine    │   Engine     │  Classifier│ (Live Sync)│   (Dashboard)     │
│           │ + Playwright │            │            │                   │
│           │   Fallback   │            │            │                   │
└───────────┴──────────────┴────────────┴────────────┴───────────────────┘
```

## Data flow

1. **Discovery** — SupplierDiscoveryEngine finds Iranian chemical suppliers
   (seed list + search engines + B2B directory crawling via HTTrack + link
   analysis + academic citations + business registries).
2. **HTTrack mirror** — `httrack <url> -O <path> ...` mirrors each supplier
   site to `/var/lib/iran_chem_db/mirrors/<project>/`. Updates use
   `httrack --update` and emit `hts-changes.json`.
3. **Playwright fallback** — only for JS-rendered sites; rendered HTML is saved
   into the same mirror directory structure.
4. **Local parsing** — the parser reads ONLY local files (HTML/PDF/Excel) from
   the mirror store. Never hits the network.
5. **Classify** — strict research-grade filter (English + Persian keywords,
   exclude industrial/technical/food grades).
6. **Validate** — RDKit SMILES canonicalization, CAS checksum, PubChem
   cross-reference, InChIKey deduplication.
7. **Live sync** — new/changed/removed products are reconciled against
   PostgreSQL; `hts-changes.json` drives selective re-parsing.
8. **Serve** — FastAPI REST API + Streamlit dashboard + CSV/JSON/SDF export.

## Tech stack

httrack (system package) · Python 3.11+ · BeautifulSoup4/lxml/parsel ·
pdfplumber/PyMuPDF · openpyxl/pandas · PostgreSQL 15+ (pg_trgm) · Redis ·
Celery · RDKit · Open Babel · PubChemPy · hazm/parsivar/langdetect (Persian) ·
FastAPI · Streamlit/Dash · Docker Compose.

## Requirements checklist (spec §8)

- [x] HTTrack is the PRIMARY fetching engine (wrapped in `src/crawler/httrack_engine.py`)
- [x] `httrack --update` for live sync
- [x] `hts-changes.json` drives selective parsing (`change_detector.py`)
- [x] Playwright is a fallback only; output into the same mirror structure
- [x] Parser reads LOCAL files only
- [x] Zero supplier gaps — autonomous discovery (search, directories, link analysis, registries)
- [x] Research grade ONLY — `grade_classifier.py` with EN/FA keyword lists + excludes
- [x] LIVE database — `live_sync.py` marks changed/removed records
- [x] Persian support — `persian_utils.py`, RTL handling, bilingual search
- [x] Chemical validation — `chemical_validator.py` (RDKit + PubChem + CAS checksum)
- [x] Deduplication via InChIKey
- [x] Audit trail — `crawl_log` + `offering_history` tables
- [x] HTTrack installed in Docker (`apt install httrack` in Dockerfile)
- [x] Persistent mirror storage (Docker bind-mount volume)
- [x] Polite crawling — robots.txt, rate limits, identifiable User-Agent
- [x] Scalable — indexes, Celery workers, selective re-parsing
- [x] Fully documented — docs/, inline comments, README
- [x] Tested — tests/ (unit + integration + fixtures)

## Legal note

Only mirror websites you are authorized to archive. Respect robots.txt and
site terms of service. Data collected is for research/procurement reference.
