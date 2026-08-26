## v2.21.1 (2026-08-26) — 3 country-gated research-grade providers

Published as 2.21.1: version 2.21.0 was reserved server-side by an interrupted
upload and never became a resolvable public version. Content is the v2.21.0
provider update.

## v2.21.0 (2026-08-26) — reserved / not public

Version number reserved by an interrupted upload. Public release is 2.21.1.

---

## v2.21.0 content (identical to 2.21.1)

### Added
- **3 Iranian research-grade sellers** admitted to `SUPPLIER_SEEDS`
  (55 → 58) after a live probe + fail-closed `country_gate.evaluate()`
  (≥2 independent families, score ≥ 60, zero disqualifiers). Notes quote
  only page-visible facts. Listing ≠ stock.
  1. **Shimi Merck (شیمی مرک)** — `shimimerck.ir` (sitemap_wp). WP
     storefront; Merck/Sigma lab-chemical importer. 021-66368169 /
     WhatsApp 09377601793. sitemap.xml reachable from foreign IP
     (post-sitemap lastmod 2026-08-24); Woo REST HTTP 404.
     Country-gate score 100 (cctld + phone + address + persian).
  2. **Rad Kimyagaran (راد کیمیاگران)** — `radkimia.ir` (static_html).
     Custom ASPX; lab-chemical + equipment importer since 1381; Merck
     reagent pages; Iranian hosting 185.192.112.69.
     Country-gate score 75 (cctld + Rasht + persian + iran_ip).
  3. **Neutron Pharmachemical (شیمی دارویی نوترون)** —
     `neutronpharmachemical.com` (static_html). Iranian manufacturer
     (Neutronco). Azadi Ave., Tehran; +98 937 054 9881. Catalog on
     neutronco.com: USP/BP/JP/ACS reagents, HPLC/GC solvents, CoA/SDS.
     Country-gate score 65 (phone + Tehran/Iran).
- **4 contact leads** added to `CONTACT_LEADS` (27 → 31) for Shimi Merck
  and Neutron phones/WhatsApp as published on their pages.

### Not admitted (fail-closed)
- **Rad Zist Shimi** (`radzistchem.com`) — own-host DNS fail; Wayback
  2019 homepage had no ≥2 country-gate families.
- **Rad Shimi Alborz** (`radchemi.com`) — own-host DNS fail; a third-party
  directory page (bamahse.com) is not used as the vendor's Enamad.

### Unchanged
Crawler/parser/country-gate behavior. 1041-row CID-unique
confirmed-organic primary seed is unchanged. Standing honesty rules:
dated best-effort catalogue index; listing ≠ stock; not a national census.

---

## v2.20.0 (2026-08-25) — 5 research-grade website providers added

### Added
- **5 Iranian research-grade chemical sellers** admitted to
  `src/discovery/seed_list.py` (`SUPPLIER_SEEDS` 50 → 55). Each was
  live-probed 2026-08-25 (DNS + TCP 443/80 open; direct TLS handshake
  timeout from a foreign IP = geo-blocked) and **country-gate admitted**
  (`evaluate()` ≥2 independent families, score ≥ 60, zero disqualifiers).
  Homepage/contact text via jina; notes quote only page-visible facts.
  Listing presence is not stock. Not a national census.
  1. **Hamrahan Safineh Danesh (HSD LifeScience)** — `hsdlifescience.com`
     (sitemap_wp). WP/Woo storefront; lab chemicals/kits/media +
     Merck/Sigma/Thermo/USP/BP importer. Enamad id=504011; Tehran
     Shariati / Seyed Khandan; 021-88444222 / 09121194596.
     product-sitemap.xml present; Woo REST HTTP 500 via jina.
     Country-gate score 90 (enamad + address + persian).
     `free_access_methods`: jina, wayback, commoncrawl, translate.
  2. **Imen Gostar Shimi** — `imengostarshimi.com` (static_html). Custom
     catalogue (lab chemicals/solvents/media + USP/EP/BP/NIBSC +
     Merck/Sigma brands; COA; PDF catalog). شماره ثبت ۵۱۰۳۵۸; Tehran
     Chamran / Tohid / Bagherkhan 101; 021-66412612 / 021-66412608.
     Country-gate score 105 (registry + phone + address + persian).
  3. **Nirvana Exir Gostar Pars** — `nirvanashimi.com` (woo_rest).
     Merck/Sigma lab chemicals + USP/EP/BP standards. Tehran Enghelab /
     Forsat Shirazi 94; 021-65020336 / 09122308697. Woo REST live JSON
     via jina (~47 KB, IRR). Country-gate score 105
     (phone + address + IRR + persian + iran_ip 89.42.211.109).
  4. **Arzan Azma** — `arzanazma.com` (woo_rest). Woo shop: Merck /
     Mojallali / Neutron chemicals + glassware + nano; IRR تومان.
     Enamad id=114637; Tehran Navab / Dampezeshki برج شهاب ۳;
     021-66381559/60 + 09364702056; کد پستی ۱۳۴۶۹۵۵۵۳۸. Woo REST live
     JSON via jina (currency IRT). Country-gate score 175
     (enamad + postal + phone + address + IRR + persian).
  5. **Nova Shimi** — `novashimi.ir` (static_html). Custom .ir shop;
     Merck lab reagents (acids/solvents/HPLC/organic-synthesis/media) +
     glassware + API. 021-92003669; info@novashimi.ir.
     Country-gate score 105 (cctld + phone + address + persian +
     iran_ip 94.182.154.71).
- **10 contact leads** added to `CONTACT_LEADS` (17 → 27) for the same
  five firms (Telegram/Instagram/WhatsApp/phone as published on their
  pages). `@HSDLifeScience` is a bio-only Telegram page (no public
  posts) so it is a lead, not a `SOCIAL_CHANNELS` catalogue.

### Verification record
- Probe artefacts: `/home/user/iran_chem_work/seller_probe_2026-08-25/`
  (jina homepages + contact/about, sitemaps, Woo JSON, country_gate.json).
- Router.py `--providers all` (9/9 providers, 29 stored keys) used only
  to normalise the already-fetched page text; invented extras from model
  output were discarded. No new molecule rows.

### Unchanged
Crawler/parser/country-gate behavior. 1041-row CID-unique
confirmed-organic primary seed is unchanged. Standing honesty rules:
dated best-effort catalogue index; listing ≠ stock; not a national census.

---

## v2.19.1 (2026-08-25) — 1041 CID-unique confirmed-organic seed

Published as 2.19.1: version 2.19.0 was reserved server-side by an interrupted
upload and never became the public `latest` tag (inspect still showed 2.18.3).
Content is the v2.19.0 seed update.

### Added
- **`data/seed_export/iran_organic_molecules_catalogue_verified_2026-08-25.csv`
  is the new PRIMARY seed: 1041 CID-unique confirmed-organic molecules.**
  This file is the 2026-08-25 workspace export merged onto the previous
  skill seed (market-verified + expanded + parallel-AI + legacy). Every
  previous seed molecule is retained (CID merge; evidence/suppliers unioned).
  **+84 new unique CIDs** vs the 957-row workspace export that already
  included the prior seed.
- Live harvest that produced the new CIDs: public Telegram (incl. ATRmedShop),
  WooCommerce catalogues (Mojallali/DRM, DigiShimi, Isatis, IR Chem, Temad,
  Exir, Chemical Iran, …), TamadKala product sitemaps (jina relay for
  geo-blocked hosts). Title normalization via `router.py --batch` across
  stored API keys; **every identity PubChem-confirmed**. No invented rows.
- `coverage_report.json` section `v2_19_catalogue_verified`.

### Changed
- `src/utils/seed_db.py` `CURRENT_BASELINE_CSV` now points at the 1041-row
  file; older CSVs still load afterwards for audit / inorganic / unknown.
- `tools/seed_load.py status` reports v2.19 as CURRENT/PRIMARY.
- SKILL.md / README / skill-card version and seed counts updated.

### Unchanged
Crawler/parser/country-gate behavior. Standing honesty rules: dated
best-effort catalogue index; listing ≠ stock; not a national census.

---

## v2.19.0 (2026-08-25) — reserved / not public

Version number reserved by an interrupted upload. Public release is 2.19.1.

---

## v2.18.3 (2026-08-25)

Token-optimization release: SKILL.md input tokens cut 79% (11,083 -> ~2,290,
o200k_base) with zero behavioral change. (v2.18.1/v2.18.2 were interrupted uploads that
never completed publication; this is the identical content published cleanly) — verified by independent multi-model
semantic-diff audits (verdict: PRESERVED). All 11 mandatory agent rules,
commands, flags, endpoints, install paths, and the fail-closed country gate
semantics are preserved verbatim in meaning.

### Changed
- Version-history sections v2.5-v2.12 consolidated into three compact
  operational sections (crawl engines, geo-block fallback chain, Telegram
  engine); the full history remains in this CHANGELOG.md.
- Removed the duplicated "Example full exports" block and the Requirements
  checklist paragraph (duplicated the Architecture section).
- Frontmatter description: 1,139 -> 117 tokens (a changelog essay is now a
  two-sentence summary); stale `version: 2.9.0` field corrected.
- Dropped source-code internals from SKILL.md (function signatures, internal
  identifiers, DB table lists, per-site arrays, worked bug examples, full CSV
  schemas, per-export timestamps) — all discoverable in the code, docs/, and
  this CHANGELOG.

## v2.18.0 — Parallel-AI supplier discovery wave (27 verified suppliers added)

### Added
- **27 AI-verified Iranian suppliers** admitted through the country gate
  (>=2 independent signal families, fail-closed, proliferation entities
  hard-excluded). Verification ran as a multi-model campaign on the
  `router.py` provider pool (gemini / mistral / cohere / zai / llm7 working
  in parallel via a work-stealing queue; 2-model quorum wherever provider
  capacity allowed; per-provider verdicts + signal families + confidence
  recorded in the export).
  * **15 website seeds** added to `src/discovery/seed_list.py`
    (`SUPPLIER_SEEDS` 35 -> 50), each live-fingerprinted on 2026-08-24:
    Chemical2.ir (live WooCommerce wp-json + sitemap), Genius Shimi
    (static, reachable); 13 GEO-BLOCKED hosts with field-verified
    `free_access_methods` (jina-checked for 10; xchem.ir / eaz.ir / 30o2.com
    fail jina -> wayback/commoncrawl/translate).
  * **1 research channel**: `ATRmedShop` added to `social_seed_list.py`
    (SOCIAL_CHANNELS 12 -> 13) — ATR Med (Arka Teb Roham), research
    chemicals + kits since 2017, Tehran landlines, Persian feed,
    www.atrmed.com; audited country provenance recorded.
  * **4 phone contact leads** added to `CONTACT_LEADS` (13 -> 17) for
    directory-verified lab suppliers without websites (Bluemoonlight,
    Kimyagaran Saadat, Navid Kala Daran, Jonoub Laboratory Supplies).
- **873-row market-verified parallel-AI molecule baseline promoted to
  PRIMARY seed**: `data/seed_export/iran_organic_molecules_parallel_ai_2026-08-24.csv`
  (+ `iran_inorganic_excluded_parallel_ai_2026-08-24.csv`, 96 rows) —
  built from a ~79k-post mirror of all 12 channels + multi-model identity
  work, every identity PubChem-verified, CID-deduped. `seed_db.load_seed_rows()`
  loads it first (highest priority); `tools/seed_load.py status` reports it
  as CURRENT.

### Verification record
- Source export: `iranian_chemical_suppliers_2026-08-24.csv` (54 candidates:
  27 accepted — 7 by 2-model quorum, 20 single-model + country-gate —,
  26 held for review, 1 rejected, 0 unverified).
- Hard exclusions: Parchin Chemical Industries, Isfahan Chemical Industries
  (WMD-related), 3 non-Iranian suppliers.
- Mirror lead harvest (401 forwarded-from handles) content-checked: long
  tail is educational, no additional sales channels admitted.

### Notes
- Review-list candidates (industrial-bulk focus or thin directory evidence)
  are deliberately NOT seeded — fail-closed per the country gate; re-run the
  screening with a 2-model quorum before admission.
- sigmairan.ir may operate under the same group as merckchemical.ir
  (Safir Azma Kian); CID-dedup at ingestion prevents double counting.

## v2.17.2 — +224 market-verified molecules, SMILES backfill, false-organic gate fix

### Added
- **`data/seed_export/iran_organic_molecules_market_verified.csv`: 651 -> 873
  rows (+224 new molecules).** Every new row is backed by a real crawled
  Iranian supplier listing. Sourced from a deep historical Telegram sweep
  that lifted the mirror from 14,907 to 29,841 posts across 12 channels
  (IranChemicals 3.3k->11.8k, LabTel 3.2k->12.3k) by raising
  `max_pages_per_channel` 200->700 and bypassing incremental crawl state.
  22,375 unique posts were AI-screened via the `router.py` hop chain for
  identity normalization ONLY; every identity was then independently
  confirmed against PubChem (CID + InChIKey + carbon-containing formula).
  No AI-invented molecules.
- `data/seed_export/coverage_report.json`: new `v2_17_market_verified`
  section with row/category/source composition and the data corrections
  below. Legacy v2.14 sections are retained unchanged.

### Fixed
- **False-organic gate.** `tools/export_verified.py::gate_row` tested
  `"C" not in formula`, so the C of **Ca/Cl/Cu/Co/Cr/Ce** satisfied the
  carbon check and inorganic salts passed as organic (`CuO4S`, `CaCl2`,
  `ClH`, `ClNa`, `CaO`, `Cu`, ...). Carbon is now matched as the *element*
  via `re.search(r"C(?![a-z])", formula)`. **29 seed rows** mislabelled
  `confirmed_organic` are relabelled `inorganic` (seed is now 844
  confirmed-organic + 29 inorganic, explicitly flagged rather than silently
  shipped as organic). Verified export: 0 carbonless rows admitted.
- **`canonical_smiles` was empty in all 651 shipped rows** — PubChem PUG REST
  retired the `CanonicalSMILES` property and silently omits it from
  responses. Re-fetched with `SMILES`/`IsomericSMILES`: **615 rows
  backfilled**, seed now 840/873 with structure.
- **3 rows whose `pubchem_cid` contradicted their own `inchi_key`**, which
  also produced 3 duplicate InChIKeys: CID 33032 was L-Glutamic acid on a
  row keyed as L-Aspartic acid; CID 444305 (L-Tartaric acid) on the Tris
  base row; CID 5462310 (elemental Carbon) on the methane row. All
  re-verified against PubChem and re-pointed to the compound each row's
  InChIKey describes.
- **2 duplicate structures merged** (evidence URLs/text unioned, no crawled
  proof discarded). Seed is now 873 rows / 873 unique InChIKeys / 873
  unique CIDs.
- New rows carry ISO-date-normalised `record_date` (`YYYY-MM-DD`), and all
  873 categories fall inside the closed 8-value vocabulary.

- **Restored `.env.example`, which was missing from the installed package.**
  `install.sh` hard-aborts with "Missing .env.example in this release; cannot
  safely continue", so the shipped skill could not complete its own install;
  `tests/test_packaging.py` and `test_env_example_shipped` also failed. The
  file documents every environment variable the code actually reads
  (`DB_PASSWORD`, `SEARCH_API_KEY`, `IRANCHEM__REDIS__URL`, the hop-chain
  provider keys, `ICDB_ROUTER`, `ICDB_PUBCHEM_CACHE`) and flags that enabling
  the hop chain sends crawled listing text to third-party APIs.
- `tools/seed_load.py` no longer hardcodes "v2.14.0"/"v2.16"/"408 molecules";
  the status line derives the version and post count from the seed manifest.

### Notes
- Verified export grows 688 -> 883 rows, 649 -> 844 distinct CIDs.
- Seed totals: 873 rows, 424 with CAS, 791 with an evidence URL.

---

- Published as 2.17.1: the 2.17.0 publish attempt reserved the version server-side but the artifact never became resolvable, so the identical content ships under 2.17.1.

- Packaging fix: the ClawHub registry strips leading-dot files, so `.env.example` never
  reached installers and `install.sh` aborted with "Missing .env.example". The release now
  also ships `env.example` (identical content) and `install.sh` accepts either name.
  Verified against a dotfile-stripped copy of the published artifact.

## v2.16.1 — status display fix

### Fixed
- `tools/seed_load.py status` now lists the v2.16 MARKET-VERIFIED baseline
  (651 rows, composition, crawl summary) as PRIMARY, above the v2.15
  expanded and v2.14 legacy entries (previously the v2.15 expanded
  manifest headed the list even though it is no longer the primary).

No data or pipeline changes; full suite still 304 passed / 20 skipped /
0 failed.

---

## v2.16.0 — market-verified baseline + one-command verified pipeline

### Added
- `data/seed_export/iran_organic_molecules_market_verified.csv` — the new
  PRIMARY seed baseline: 651 rows, ALL confirmed-organic, MARKET-VERIFIED
  ONLY (every row backed by a real crawled Iranian supplier listing: 479
  verified_catalogue + 68 verified_telegram_listing + 104
  verified_web_catalogue; 12 Telegram channels / 10,160 posts + 7 supplier
  web feeds incl. r.jina.ai relay). Unified evidence schema
  (evidence_url, evidence_text, source_type, record_date, category, grade);
  CID-unique, 0 carbon-less formulas, all CAS checksum-valid. 155 previously
  empty categories were classified by cloud models (router.py arena hop
  chain) during packaging — all 651 rows now carry a category. The
  improvement strategy that shaped this release ships as
  `data/seed_export/STRATEGY_iran_chem_database_improvement.md`.
- `tools/export_verified.py` — one-command verified export (P3.1/P3.2/P3.3):
  gates (organic status, carbon formula, CAS checksum, identity present;
  optional --enforce-country fail-closed) → CID dedupe at admission (P1.2,
  output NEVER contains two rows with the same CID) → unified schema →
  sha256 provenance hash per row (evidence_text|evidence_url|CID, computed
  over the exported row so it recomputes from the CSV) → CSV + manifest +
  `<out>.rejected.csv` (rejections with reasons, never silently discarded).
  Acceptance met: reproduces the 651-row market-verified CSV from the
  frozen file in one command.
- `src/utils/ai_hopchain.py` — provider-resilient AI normalization (P5.1):
  hop chain (arena router.py first, then env-keyed gemini/mistral/
  openrouter/llm7), automatic failover, adaptive max_tokens (4xx → halve,
  dead hop remembered per process), 429/5xx backoff, jittered pacing,
  strict numbered-JSON parsing, per-batch NONE-rate degradation metric,
  value_field parameter (identity AND classification tasks). With no AI
  available it marks items unresolved — it never invents.
- `FreeAccessEngine.fetch_with_failover()` (F4) — exhaustive ORDERED relay
  failover (jina → wayback → commoncrawl → translate → archivetoday, stop
  on first success) with a per-host JSON cache of the working method that
  is tried first on later runs (self-maintaining fingerprints).
- `.env.example` — RESTORED (was missing since before v2.15; the installer
  and two packaging tests depended on it). Documents DB_PASSWORD
  placeholder + recovery command, optional SEARCH_API_KEY,
  ICDB_PUBCHEM_CACHE, and IRANCHEM__SECTION__KEY overrides.
- `tests/test_v216_improvements.py` — 14 regression tests (P6.3): seed
  baseline integrity, CID dedupe at admission (incl. the "L-Ascorbic Acid"
  vs "Vitamin C" case), provenance hash reproducibility, 651-row
  reproduction, rejection sidecar, CAS checksum, hop-chain graceful
  degradation (no AI → never invents), numbered-JSON parsing, value_field,
  failover ordering + method cache, all-failed path.
- `seed_db` upgrades: market-verified file loaded as primary source;
  name-variant tracking on merge (F5: variants preserved, not dropped);
  `export_sqlite` adds UNIQUE `identity_key` (stereoisomer-aware merge
  identity) + name_variants + evidence columns; loader now reports 835
  deduped molecules (649 confirmed / 124 unknown / 62 inorganic, 495 rows
  with >1 name variant).

### Fixed
- `.env.example` missing → 2 packaging tests + installer path now pass.
- `normalize_batch` NoHopError path did not count unresolved items in
  none_rate (degradation metric under-reported).
- `hop_chain_call` sliced string-returning hops character-wise (contract
  now accepts both [text] and text).

### Full test suite
304 passed, 20 skipped, 0 failed (290 → 304 with the 14 new tests; the
three previously-failing organic-classifier tests pass once rdkit from
requirements.txt is installed; test deps sqlalchemy/fastapi/psycopg2/
pdfplumber/PyMuPDF are the skill's declared requirements).

### Unchanged
Crawler/parser/verification behavior is untouched — this release is
additive: seed data + composition layer + resilience. Standing honesty
rules apply: dated, auditable, best-effort; listing presence is not proof
of stock; foreign brands in Iranian listings are product metadata.

---

## v2.15.0 — expanded seed baseline: 692 deduped molecules, 9 source sets

### Added
- `data/seed_export/iran_organic_molecules_expanded.csv` — a 480-row,
  ALL-confirmed-organic baseline (exported 2026-08-23 12:30 UTC) adding 9
  source sets: TamadKala (3,484 product URLs from product sitemaps),
  Fardad Shimi (569 paginated shop listings), DigiShimi (268 WooCommerce
  products), Isatis Shimi (188), BehChin Chemi Pharmed (public
  human/veterinary API, excipient/cosmetic/food-additive lists), Pishgaman
  Shimi (IR Chem), ShimiMan (sitemap titles), Rooz Darou (114 pharmaceutical
  product pages), plus the retained 207-row live-verified Telegram
  catalogue. 1,616 new source records were admitted down to 948 after the
  chemistry filter (668 excluded: non-confirmed-organic, mixtures,
  polymers, equipment, unresolved). Persian/English titles were normalized
  with the workspace router; every admitted record was structure/formula
  checked against PubChem.
- Richer per-row schema: `category` (organic_reagent / pharmaceutical_or_api
  / cosmetic_raw_material / colorant_or_indicator / fragrance_or_aroma /
  vitamin / supplement_active / secondary_metabolite_or_natural_product),
  `research_grade_candidate` + `research_grade_signal`, `supplier_platform`,
  `supplier_country_evidence`, `catalogue_presence`, `availability_status`,
  `source_product_titles`, `evidence_record_count`.
- `common_name` filled for all 480 expanded rows (PubChem Title), so every
  molecule in the baseline is searchable by its everyday name.

### Changed
- `src/utils/seed_db.py` is now schema-tolerant: it loads BOTH the expanded
  and legacy organic exports plus the inorganic exclusions, maps the two
  column dialects onto one canonical set, and **merges duplicate molecules**
  across files (InChIKey/CAS/CID keyed; supplier and source-URL evidence
  unioned, max evidence count kept). Seed baseline grows from 408 to
  **692 deduped molecules** (494 confirmed-organic, 124 unknown-organic,
  74 inorganic; 1,153 name variants, 474 CAS, 571 InChIKeys, 570 CIDs).
- `export_sqlite` gains the expanded provenance columns (category,
  research_grade_candidate/signal, supplier_platform,
  supplier_country_evidence, catalogue_presence, availability_status,
  source_product_titles, evidence_record_count) — the SQLite starting point
  for the live database now carries the full evidence trail.
- `tools/seed_load.py status` reports the expanded export's manifest and all
  9 source sets alongside the legacy baseline.

### Unchanged
All crawler/parser/verification behavior (v2.13–v2.14) is untouched; this is
additive seed data + loader work. Standing honesty rules apply: the baseline
is a dated, best-effort index — product-page presence is not proof of stock,
and foreign brands in Iranian retail listings are product metadata, not
supplier-country evidence.

---

## v2.14.1 — seed baseline: 408-molecule starting point + zero-network re-parse

### Added
- `data/seed_export/` — a real crawl export (408 unique molecules, crawled
  2026-08-23 via this skill's own v2.13 pipeline from 12 verified Telegram
  channels, 12,367 posts + public supplier web catalogs):
  `iran_organic_molecules.csv` (334 rows: 210 confirmed-organic + 124
  unknown-organic, flagged per the standing mandate),
  `iran_inorganic_excluded.csv` (74 rows), `coverage_report.json`.
- `common_name` column — PubChem `Title` (preferred name) per PubChem CID, so
  molecules are searchable by their everyday name (e.g. "Triethanolamine",
  "L-(+)-Cysteine") alongside IUPAC/CAS/InChIKey.
- `src/utils/seed_db.py` — stdlib-only seed-baseline library:
  `load_seed_rows()`, `SeedIndex` (O(1) lookup by name/common name/CAS/
  InChIKey/CID), `lookup()`, `diff_against()` (which freshly-parsed rows are
  NEW), `preload_pubchem_cache()` (primes the resolver's on-disk PubChem
  cache so seeded molecules cost ZERO network calls), `export_sqlite()`
  (a real SQLite file — `molecules` + `molecule_suppliers` +
  `export_manifest` — as the starting point for the live PostgreSQL
  database).
- `tools/seed_load.py` — CLI: `status | search | diff | export-sqlite |
  preload-cache`.

### Why
Crawls are expensive and sandboxes are stateless. The baseline makes repeat
work free: re-parsing a known corpus needs no network, "is this molecule new
?" is instant, and the live database has a verified initial dataset instead
of starting from an empty schema.

### Verified
- Offline proof: with all sockets blocked, `pubchem_lookup("melamine")` →
  CID 7955 / C3H6N6 and `pubchem_lookup("triethanolamine")` → CID 7618, served
  entirely from the preloaded cache.
- `export-sqlite` produces a queryable seed DB (408 rows, indexed on
  cas/inchi_key/cid/molecule/common_name, 510 supplier links, manifest table).

### Unchanged
All v2.13 behavior (crawler, parsers, verification, API) is untouched; the
seed data is additive. The standing honesty rules still apply: the baseline
is a dated, best-effort index — never a claim of national completeness.

---

## v2.13.0 — agent-runnable verification of Iranian sellers

### Added
- `src/verification/` — a mechanism that lets a CONSUMING AGENT prove for
  itself that the data comes from Iranian sellers, instead of trusting this
  package's banner. `verify_channel()`, `verify_dataset()`,
  `verify_listing_row()`, `AgentVerdict.explain()`.
- `src/verification/claims.py` — ten independently re-checkable claim types
  with real arithmetic: شناسه ملی (11-digit company ID) check digit, کد پستی,
  ITU dialling-code resolution, Iranian mobile/area-code tables, ccTLD, IRR
  pricing, Persian text, Iranian city, Iran reference, multinational deny-list.
- Three verification levels: `offline` (no network), `live` (re-fetches
  t.me/s/<channel>), `paranoid` (ignores stored claims; the live page must
  stand on its own).
- CLI `social_crawl verify-suppliers [--level] [--dataset] [--explain] [--json]`,
  exiting non-zero when anything fails to verify, so it works as a pipeline gate.
- API `GET /api/v1/social/verify-suppliers` returning per-claim working.
- Row-level attestation columns (`supplier_country`, `supplier_verified`,
  `supplier_verify_score/families/evidence/level`, `supplier_verified_at`) via
  `attach_attestations()`, making an exported row self-verifying.
- `tests/test_verification_v213.py` — 33 tests covering the arithmetic,
  fail-closed defaults, forged-attestation resistance and the round trip.

### Fixed
- شناسه ملی check digit was read from the wrong index, rejecting officially
  valid IDs; corrected against the published algorithm and worked example.
- Live language detection judged the first 4 KB of the raw page, which is
  English Telegram boilerplate — a wholly Persian channel could read as `en`.
  It now scores the post bodies.
- Iranian landline numbers (0XX + 8 digits) were missed by the live phone
  regex, and Persian-digit numbers were not folded before matching.
- City matching used bare substrings, so «ری» matched inside «دیگری» and
  manufactured location evidence; matches are now bounded by Persian word edges.
- `load_rows()` missed a banner comment written as a quoted CSV field, which
  silently produced rows with no `channel` — every row then failed attribution.

### Verification status at release
- 10/12 seeded suppliers verify offline; `labshop` and `chemgroup` publish no
  phone, postal code or company ID and are QUARANTINED rather than asserted.
- 804 of 852 listings carry a passing attestation; 48 are quarantined.

## v2.12.0 — hardened Telegram extraction, Persian gate, one-command retrieval

### Added
- `src/parser/listing_extractor.py` — structured field extraction from supplier
  posts: SKU, brand (Latin + Persian spellings), Latin product name with
  locants preserved, purity (Persian digits supported), grade token, pack size
  normalised to g/ml, checksum-validated CAS, and availability.
- Structured resolution route in `social_molecule_resolver.resolve()`:
  extracted names are matched against the alias dictionary then PubChem
  (`structured_alias` / `structured_pubchem`), instead of relying solely on a
  curated dictionary. Unverified extractions are kept as `name_candidate`.
- `src/parser/persian_gate.py` — Persian/Farsi language gate with Persian-vs-
  Arabic disambiguation, text normalisation (ي→ی, ك→ک, ZWNJ) and Persian/
  Arabic-Indic digit conversion.
- On-disk PubChem cache (`ICDB_PUBCHEM_CACHE`) incl. negative caching.
- CLI: `fetch`, `search`, `audit-persian`; flags `--out` (csv/json/xlsx),
  `--query`, `--brand`, `--in-stock`, `--with-price`. `parse --out` too.
- API: `GET /api/v1/social/search`, `GET /api/v1/social/persian-policy`.
- Per-channel Persian provenance (`language`, `persian_ratio`,
  `persian_verified_on`) on all 12 seeded channels.
- `tests/test_extraction_v212.py` — 39 tests.

### Changed
- Listing discriminator admits `structured_catalogue_line` posts without a
  sales verb or price.
- Listings now carry `sku`, `brand`, `purity_percent`, `grade_token`,
  `pack_size`, `availability`, `post_language`, `text_snippet`.
- `is_iranian_channel()` requires Iranian country **and** `language == "fa"`.
- Catalogue output gained `persian_language_policy` and field-coverage metrics.

### Fixed
- CAS checksum validation was unreachable (regex lookarounds broke `fullmatch`),
  so valid CAS numbers were dropped.
- Product names lost leading locants (`1,4-Butanediol` → `Butanediol`) and
  gained trailing purity digits (`Melamine, 99`).
- Persian/Arabic conflation: normalisation ran before the language check and
  erased the discriminating letters.
- Small-sample channels are judged on available evidence rather than refused.

### Results (live corpus, 12 channels, ~12,900 posts)
- molecules **84 → 240**, listings **685 → 852**, vendors **10 → 12**
- 270 listings with brand, 249 with SKU, 176 with pack size, 80 with purity
- every `structured_pubchem` listing has a PubChem CID + formula (0 missing)
- 12/12 channels verified Iranian and Persian (56%–100% Persian posts)

## v2.11.0 — Iranian-suppliers-ONLY country gate

**Enforces the database's hard scope rule: every supplier is Iranian.**

### Added
- `src/discovery/country_gate.py` — evidence-based country determination for
  both ingestion paths. Requires >=2 INDEPENDENT Iranian signal families and a
  weighted score >=60, with zero foreign disqualifiers; **defaults to DENY**.
  Signals: Enamad trust seal, شناسه ملی / کد اقتصادی / کد پستی / شماره ثبت,
  `.ir` ccTLD, `+98`/`09xx`/landline telephony, Iranian city+country, IRR
  pricing, Persian content, Iranian IP ranges (supporting only, expanded from
  16 to ~380 CIDRs). Only the strongest signal per family counts.
- Disqualifiers that veto admission: multinational-owned domains (48 entries),
  foreign ccTLDs (54), and foreign HQ statements about the vendor itself.
- `FOREIGN_CHANNELS` deny-list (16 handles) for the social path.
- Audited country provenance on all 12 seeded Telegram channels
  (`country`, `country_confidence`, `country_signals`, `country_evidence`,
  `country_verified_on`), established by live probe on 2026-08-23.
- `GET /api/v1/social/country-policy`, `social_crawl audit-country`, and
  `tools/audit_country.py` (exit 1 on any policy violation).
- `supplier_country_policy` block in `config.yaml`.
- `tests/test_country_gate.py` — 43 tests, including regressions for foreign
  rejection and for the Iranian-importer false-positive guard.

### Changed
- `SupplierValidator` now delegates country determination to the gate;
  `score()` returns **0** for any rejected supplier, so existing callers that
  threshold on `min_verification_score` inherit the Iran-only guarantee.
  Added `verify()` (returns evidence) and `is_iranian()`.
- `active_channels()` and `build_catalog()` both apply the gate, so even an
  explicit `--channel` argument cannot inject a foreign supplier.
- All four `Supplier` insertion points now require `country == "IR"`.
- Forwarded-from lead discovery never proposes a known foreign supplier.
- Social catalogue output gained a `supplier_country_policy` block listing
  per-vendor evidence and any excluded foreign channels.

### Fixed
- An unreachable homepage no longer earns +10 toward verification (no evidence
  can no longer look like weak evidence).
- A lone mention of "Tehran"/"Iran" on a foreign vendor's page no longer
  contributes 30 points toward admission.

### Notes
- **Supplier != brand.** Iranian importers reselling Merck/Sigma/TCI are
  retained; brand and "Made in Germany" lines are excluded from foreign
  detection. The `merckmillipore` *channel* is a Tehran importer that
  brand-squats the name and is KEPT; the `merckmillipore.com` *website* is
  Merck KGaA and is REJECTED.
- No change to molecule/listing extraction: all 44 v2.10 social tests still pass.

## v2.10.0 — social catalogue engine (public Telegram channels)

Iranian suppliers publish live catalogue/price data on public Telegram channels,
often fresher than their websites and reachable when the site is geo-blocked.

### Added
- `src/crawler/telegram_engine.py` — mirrors `t.me/s/<channel>` (no login/API
  key, not geo-blocked): backward `?before=<id>` pagination to the true channel
  beginning, bounded parallel fan-out (default 6, hard cap 8), request delay,
  atomic per-channel state for incremental resync, content-verification that
  distinguishes real channels from "Channel created" stubs by CONTENT not size.
- `src/discovery/social_seed_list.py` — 11 content-verified channels with roles
  (seller_research / seller_industrial / news / lead_source), 15 content-checked
  rejects with reasons, vendor contact leads and a `wa.me` RFQ link builder.
- `src/parser/telegram_parser.py` — DOM parser, role-aware listing
  discriminator, unit-anchored price extraction, contact/CAS capture,
  forwarded-from harvesting (how `Boof_company` and `fanchem` were discovered).
- `src/parser/social_molecule_resolver.py` — alias dict → CAS-anchored fallback
  → PubChem resolver chain (PubChem for Latin names/CAS only; it 404s on
  Persian), composite/polymer flagging, domain-aware grade classifier, and an
  alias duplicate-key lint.
- `src/parser/social_catalog_pipeline.py` — mirror → parse → resolve → metrics,
  with every rejection carrying a stage + reason.
- `src/api/routes/social.py` — `/api/v1/social/{channels,coverage,molecules,
  rejections,export,leads}`; molecules paginated with `total_pages`/`has_more`,
  export unpaginated with a `require_complete_coverage` 409 gate.
- `src/tasks/social_tasks.py` + beat entry — 6-hourly incremental sweep,
  dispatched via `celery_app.send_task` (never bare `.delay()`).
- `src/scripts/social_crawl.py` — `verify | mirror | parse | leads | channels`.
- `tests/test_social_catalog.py` — 36 offline tests including regressions for
  both precision bugs below.
- `config.yaml` — new `social:` section.

### Fixed
- **Price market-value false positive**: "۱۰۰ میلیون دلار" in a news article was
  extracted as a product price. A figure is now a price only when a pack/volume
  unit is a WORD TOKEN near it and no market-scale qualifier applies. Token
  matching also fixed `gr` matching inside the word "group".
- **Educational articles parsed as listings**: `news`-role channels now require
  a strong listing marker (price/contact/brand/hashtag); a bare Persian sales
  verb is no longer sufficient. Seller channels keep verb acceptance.
- **Duplicate alias keys** removed (Python keeps the last, silently discarding
  a richer alias set); `lint_aliases()` now guards this in CI.
- CAS-only hits no longer surface a `None` name — they get a `CAS <n>` display
  name (and a real IUPAC name + InChIKey when PubChem enrichment is enabled),
  fixing an unsortable-`None` crash when listing molecules.
- Rejection reasons split `generic_announcement_no_molecule_named` from
  `no_alias_or_cas_match` so recall metrics stay honest.
- **Recruitment adverts parsed as product listings**: lab marketplaces
  (`lead_source`, e.g. LabTel) are dominated by job posts carrying salary
  figures, phone numbers and hashtags — i.e. every "strong marker" a product
  listing has. `is_job_advert()` now excludes them on every channel role,
  filtering 2,349 phantom candidates and cutting real dictionary gaps from
  4,049 to 1,849.

### Changed
- Alias dictionary expanded 137 → 204 entries by mining unresolved live seller
  posts: metal stearates (zinc/calcium/magnesium/aluminium/sodium + stearic
  acid — fanchem's product line), choline chloride, ammonium sulfate, calcium
  formate, zinc acetate/nitrate/oxide/chloride, terephthalic and vanillic
  acids, oxalyl chloride, 2-methylimidazole and more. **Every CAS
  PubChem-verified.** Live catalogue: 54 → 77 molecules, 445 → 478 listings.

### Scope (unchanged honesty guarantees)
Telegram only. Instagram/Facebook/X are login-walled and WhatsApp is
contact-only — captured as vendor leads, never scraped. Coverage is measured
and published; nothing is claimed complete.

## v2.9.0 — reliability & verification best practices

A hardening pass to ensure every functionality works as expected.

### Added
- `scripts/self_test.py` — one-command offline self-test: compiles every .py,
  checks required files + SKILL.md frontmatter + config.yaml, imports core
  modules, and runs the offline pytest subset. Exit 0 only when all pass.
- `scripts/preflight.py` — environment readiness report (httrack/curl/wget
  binaries, python version, optional packages, config load) with install hints.
- `tools/package_selftest.py` — release-readiness check to run before publishing.
- `.github/workflows/ci.yml` — CI on push/PR: preflight → self-test → full
  pytest (DB tests self-skip) → package selftest.
- `src/utils/http_util.py` — shared `get_bytes()` with retry + exponential
  backoff on transient HTTP 408/425/429/5xx and socket errors; TLS verified by
  default.

### Changed
- `httrack_engine.py` — `require_httrack` flag + graceful `mirror_supplier()`
  returning an empty stats dict when httrack is missing (the fallback chain —
  playwright, curl/wget/python, free-access — now takes over instead of
  crashing). `build_command` uses the resolved binary path.
- `directory_crawler.py` — discovery engine no longer hard-crashes without
  httrack (uses `require_httrack=False`).
- `free_access_engine.py` / `woo_rest_engine.py` / `http_fetch_engine.py` —
  all network GETs now go through the shared retry/backoff helper.
- `pyproject.toml` — ruff bug-focused rules (E/F/W/B) with FastAPI-aware
  ignores; pytest `integration` / `network` markers.
- Removed 4 dead code spots (unused imports/variable) flagged by ruff.

### Verification
- Full pytest suite passes (DB tests self-skip without PostgreSQL).
- `ruff check` clean; `preflight` + `self_test` + `package_selftest` all green.

---
## v2.8.0 — multi-tool HTTP fetch fallback (curl / wget / python)

### Added
- `src/crawler/http_fetch_engine.py` — single-page fetch chain
  (python-urllib → curl → wget, browser UA, redirect-following, timeout +
  size guards) plus optional `wget -r -k -p` recursive mirror. Tools detected
  at runtime; missing ones skipped. Output saved under
  `<mirror>/fetch-fallback/<tool>/` and parsed by the existing pipeline.
- `config.yaml` → `http_fetch:` section.

### Changed
- `crawl_tasks.py`: the HTTrack mirror call is now wrapped so a missing httrack
  binary (or any mirror error) degrades gracefully instead of failing the
  supplier; when the mirror is empty and the site is NOT geo-blocked, the
  HTTP-fetch fallback runs (homepage + catalog entry points). Its saved files
  are counted in `/coverage` instead of a false "no-html-mirrored".

---
## v2.7.1 — Wayback "Save Page Now" (SPN2) — invented via adversarial debate

A 2-round adversarial debate among the reasoning team (cmdr, qwen, devstral,
gemini — each proposed 6 novel methods, then cross-critiqued the other 21)
produced one genuinely new, live-verified method:

### Added
- `fetch_via_spn2()` — forces a FRESH capture of a blocked page via
  `https://web.archive.org/save/<url>`, then reads the new capture back from
  `web.archive.org/web/<ts>id_/<url>`. The IA crawler fetches from its own
  (allowed) IPs, so geo-blocked hosts are captured on demand. Verified live:
  rockchemie.com captured 2026-08-22 (428 KB full HTML). Fails gracefully when
  IA's save endpoint is busy (HTTP 5xx) and is appended to every site's method
  list automatically.
- `DEFAULT_FREE_ACCESS_METHODS` now: jina, wayback, commoncrawl, spn2,
  translate, archivetoday. `free_access_preference()` always appends spn2.

### Debate verdicts (documented for the record)
- Google PageSpeed Insights — real & keyless, but Google hard-rate-limits
  datacenter IPs (429 in testing) — NOT shipped.
- Facebook Graph scrape / Twitter Card Validator / LinkedIn Post Inspector —
  real but metadata-only (or login-walled) — NOT shipped.
- Yandex Turbo, Google AMP cache, W3C validator from DC IPs, "Cloudflare Edge
  Fetch", "Tehran Uni Archive", "performance-tester", "data-saver transcoder",
  "webcache.search-engine" — dead, keyed, or hallucinated by the models —
  rejected after live testing.

---
## v2.7.0 — Common Crawl + screenshot fetchers (exhaustive round-3 sweep)

Exhaustive sweep (4 reasoning models + live tests of 20+ candidates on the
geo-blocked sites) added two genuinely new working methods:

### Added
- `fetch_via_commoncrawl()` — queries the Common Crawl index
  (index.commoncrawl.org) for recent captures and downloads each WARC record
  with a tiny HTTP Range request from data.commoncrawl.org (S3, not
  geo-blocked), extracting the full HTML body (chunked/gzip handled). Verified
  live: rockchemie.com 27 captures (2026-07), pgsoc.ir 1 (2026-07),
  irandaru.com 3, shimico.com 407. Gives the "Wayback-only" sites a second
  source with much fresher captures.
- `fetch_via_screenshot()` — thum.io renders the page server-side to a PNG
  (verified: 492 KB render of rockchemie.com). Image-only visual evidence —
  intentionally NOT in the default method list.
- `DEFAULT_FREE_ACCESS_METHODS` now `jina, wayback, commoncrawl, translate,
  archivetoday`; `free_access.methods` / `max_commoncrawl_pages` in config.yaml.

### Verified dead/blocked this round (not implemented)
allorigins(522) · codetabs(522) · corsproxy.io(403) · thingproxy(DNS) ·
fetch.hix.ai(dead) · md.dhr.wtf(dead) · memento(dead) · textise(403) ·
urltotext(own page) · rss2json(500) · rendertron(404) · google-docs-viewer +
officeapps (wrappers) · mshots (placeholder).

---
## v2.6.2 — archive.today method + per-site free-access preferences (2026-08-21)

Round-2 investigation (4 reasoning models + live tests on all 12 geo-blocked
sites) showed the three v2.6 fetchers are the only broadly-working free
front-ends, plus one additional one:

### Added
- `free_access_engine.py`: `fetch_via_archive_today()` — a 4th fetcher using
  the archive.today family (archive.ph / archive.today / archive.is). Serves
  existing snapshots via `/newest/<url>`; reachable from residential/operator
  networks (blocks many datacenter IPs, fails gracefully). Added to
  `DEFAULT_FREE_ACCESS_METHODS` and the orchestrator.
- `seed_list.py`: every geo-blocked seed entry now carries a field-verified
  `free_access_methods` preference, e.g. novichem.ir/pgsoc.ir = ["wayback"]
  (Jina/Translate both fail on them), basparsazan.com = ["jina","translate"],
  artinkimya.com = all three. New `free_access_preference(url)` returns the
  per-site list, defaulting to `DEFAULT_FREE_ACCESS_METHODS`.
- `crawl_tasks.py`: the free-access fallback now uses `free_access_preference()`
  per site (config list is the fallback for unknown domains).
- `config.yaml` → `free_access.methods` now includes "archivetoday".

---
## v2.6.0 — free-access fallback for geo-blocked Iranian sites (2026-08-21)

Field-verified on the 12 geo-blocked seed sites (rockchemie, abnoos,
artinkimya, pakshoo, pgsoc, tebgostar, novichem, basparsazan, mahdistejarat,
irandaru, shimico, parsisotope): every one is reachable through at least one
FREE third-party fetcher whose IPs the Iranian hosts do not block.

### Added
- `src/crawler/free_access_engine.py` — three fetchers:
  - Jina Reader (`https://r.jina.ai/<url>`, markdown) — works on 9/12 sites;
  - Wayback Machine (CDX API enumerates snapshots, `web/…/id_/` serves raw HTML)
    — works on 10/12;
  - Google Translate proxy (`translate?u=`) — works on 9/12.
  Fetched files are stored under `<mirror>/free-access/{jina,wayback,translate}/`
  and parsed by the existing local-file-only pipeline. Stdlib only, no keys.
- `src/parser/markdown_parser.py` — scans Jina markdown for CAS-number patterns
  and emits molecule candidates (name + CAS + purity) for text-only fetches.
- `.md` / `.txt` added to `PARSEABLE_EXTENSIONS` and `SUPPORTED_EXTS`.
- `config.yaml` → `free_access:` section (enabled, methods order, timeout,
  delay, max_wayback_pages).

### Changed
- `crawl_tasks.py`: when a mirror looks geo-blocked (or the supplier notes say
  GEO-BLOCKED), the free-access engine runs automatically; its saved files are
  counted in `/coverage` (no more false "no-html-mirrored" partial reason) and
  the method breakdown is recorded in `partial_reason`.

---
## v2.5 — field-hardened release (2026-08-21)

Derived from a live crawl run + full fingerprinting of the 35-supplier seed list.

### Added
- `src/crawler/woo_rest_engine.py` — WooCommerce/WordPress REST + sitemap engine:
  public, unauthenticated `/wp-json/wc/store/v1/products` pagination (WP core
  REST fallback) plus `sitemap.xml`/`product-sitemap.xml` enumeration; JSON is
  persisted into the local mirror store and consumed by the existing
  local-file-only parser (`.json` added to PARSEABLE_EXTENSIONS).
- Fingerprint-annotated seed list: every supplier carries status
  (active/inactive), crawl-profile hint (`woo_rest`, `sitemap_wp`,
  `playwright_js`, …), notes and REST/sitemap entry points. 12 dead domains,
  2 parked, 1 inorganic-only and 1 radiopharma-only are seeded `inactive` and
  skipped by the crawl sweep.
- `woo_rest` / `sitemap_wp` HTTrack profiles + `classify_profile` mapping.
- Geo-block detection: zero-file mirrors with TLS/handshake/timeout signatures
  are flagged `geo-blocked-possible (retry via Iranian proxy)`.

### Fixed
- `trigger_initial_crawl.py`: dispatch now uses `celery_app.send_task(...)`
  instead of `.delay()` on a bare `@shared_task` — the old path fell back to
  the default Celery app (AMQP broker) and failed with "Connection refused"
  while the Redis-bound worker was healthy.

---
## Description: <br>
Iran Chemical Database — an HTTrack-powered live crawling system that autonomously discovers Iranian chemical suppliers, mirrors their websites with HTTrack (with Playwright fallback for JavaScript sites) and a WooCommerce/WordPress REST + sitemap engine, extracts research-grade molecule catalogs from the local mirrors, validates molecules with RDKit/PubChem, and maintains a live PostgreSQL database served by FastAPI (REST) and Streamlit (dashboard), with Celery scheduling and Docker deployment. Ships complete, runnable source code: discovery engine, HTTrack wrapper, local-file parsers (HTML/PDF/Excel), strict research-grade classifier (English + Persian), live sync, API, dashboard, tests, and docs. For academic procurement research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, lab managers, and procurement staff use this skill to build and maintain a live, searchable database of research-grade chemical molecules offered by Iranian suppliers — automatically discovered and kept up to date via HTTrack website mirrors — for sourcing, price comparison, and catalog analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The system crawls third-party websites, which may violate their terms of service or robots.txt if misconfigured. <br>
Mitigation: Polite crawling defaults (robots.txt respected, rate limits, identifiable User-Agent), per-supplier overrides, and explicit legal guidance to mirror only authorized sites. <br>
Risk: Extracted chemical data (grades, purities, prices, GHS) can be inaccurate. <br>
Mitigation: Every record is validated (CAS checksum, RDKit structure, PubChem cross-reference) and flagged with extraction confidence; users must verify before relying on it. <br>
Risk: Requires system services (PostgreSQL, Redis) and, for crawling, the httrack binary and outbound network access. <br>
Mitigation: Full Docker Compose deployment with persistent volumes and a clearly documented environment contract. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Architecture](docs/architecture.md) <br>
- [HTTrack integration guide](docs/httrack_integration.md) <br>
- [API reference](docs/api_reference.md) <br>
- [Deployment guide](docs/deployment_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, python, sql, yaml, dockerfile, markdown] <br>
**Output Format:** [A complete, runnable Python application (source tree, Docker Compose, migrations, tests, fixtures, docs) implementing the HTTrack-powered crawling database] <br>
**Output Parameters:** [2D] <br>
**Other Properties Related to Output:** [The system writes mirrored websites to a local directory and populates a PostgreSQL database; it makes outbound HTTP requests only to the supplier sites it is configured to mirror.] <br>

## Skill Version(s): <br>
2.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, mirror only websites they are authorized to archive, respect robots.txt and site terms of service, verify all extracted chemical data before relying on it, and comply with applicable data/procurement regulations. <br>
