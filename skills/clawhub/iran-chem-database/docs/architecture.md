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
3. **WooCommerce REST + sitemap (v2.5)** — for `woo_rest`/`sitemap_wp`
   profiles the `WooRESTEngine` fetches the public `/wp-json/wc/store/v1/products`
   API (paginated) and `sitemap*.xml`, persisting the JSON into the mirror
   store before HTTrack runs a shallow HTML mirror. Geo-blocked mirrors (zero
   files + TLS/timeout signatures) are flagged `geo-blocked-possible`.
4. **Playwright fallback** — only for JS-rendered sites; rendered HTML is saved
   into the same mirror directory structure.
5. **Local parsing** — the parser reads ONLY local files (HTML/PDF/Excel/JSON)
   from the mirror store. Never hits the network.
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

---

## Module 7 — Social catalogue engine (v2.10)

Supplier websites are not the only public catalogue. Iranian chemical vendors
publish product, price and availability posts on **public Telegram channels**,
frequently more current than their websites — and reachable even when the
website geo-blocks foreign IPs.

### Why Telegram (and only Telegram)

`https://t.me/s/<channel>` is a server-rendered HTML preview of a public
channel. It requires **no login, no API key, no bot token**, and is not
geo-blocked from foreign datacenter IPs. Measured: ~19–20 posts/page, 90–160 KB.

Instagram, Facebook and X are login-walled; WhatsApp is contact-only and E2E
encrypted. None are automatable for free from a foreign IP, so they are modelled
as **vendor contact leads** (with `wa.me` RFQ links a human sends) and never as
a scraped feed. This boundary is deliberate and is restated in every API
response via the `scope` field.

### Data flow

```
social_seed_list (verified channels + roles)
        |
        v
telegram_engine  --network-->  <mirror>/social/telegram/<chan>/*.html
        |                       (+ .crawl_state.json for incremental resync)
        v
telegram_parser  --local only-->  posts -> listing? -> price/contact/CAS
        |
        v
social_molecule_resolver   alias dict -> CAS anchor -> PubChem (Latin only)
        |
        v
social_catalog_pipeline -> molecules + listings + rejections + metrics
        |
        v
/api/v1/social/*   and   src.scripts.social_crawl
```

Only `telegram_engine` touches the network during mirroring; parsing is strictly
local-file-only, matching the rest of the skill. PubChem enrichment is the sole
optional network step during parse and is off by default
(`social.pubchem_enrichment: false`).

### Pagination and the end condition

The cursor is `?before=<oldest_post_id>`. The crawl stops when a page yields no
new post ids, when the cursor stalls twice, or when id 1 (the true channel
beginning) is reached. **Gaps in the id space are deleted posts**, not fetch
failures — they are reported as `gaps` / `coverage_pct` rather than retried
forever. This is why coverage below 100% is normal and honest.

### Politeness

Fan-out is capped (default 6, hard maximum 8) with a configurable delay between
rounds, and all fetches go through the shared retry/backoff helper so a
transient 429/5xx fails over instead of hammering the host.

### Precision rules (learned from live debugging)

| Rule | Why |
|---|---|
| A number is a price only if a pack/volume unit is a **word token** nearby | "۱۰۰ میلیون دلار" in a news article was extracted as a price |
| Market-scale words (million/billion) disqualify a figure | same class of false positive |
| Unit matching is token-based, never substring | `gr` matched inside "group" |
| `news`-role channels require a **strong** marker (price/contact/brand/hashtag) | educational articles were parsed as listings |
| Seller-role channels may rely on sales verbs | their posts are catalogue entries by construction |
| Composites/polymers are flagged, never force-fitted to a CID | inventing a structure would be a hallucination |
| Alias keys are lint-checked for duplicates | Python keeps the last, silently dropping a richer alias set |

### Channel discovery

Posts carry a "forwarded from" attribution. Harvesting it yields candidate
channels, each of which must pass **content verification** before entering the
seed list. This mechanism found `Boof_company` and `fanchem`. Candidates that
turn out to be schools, plastics traders or stubs are written to
`REJECTED_CHANNELS` with a reason so they are never re-probed.
