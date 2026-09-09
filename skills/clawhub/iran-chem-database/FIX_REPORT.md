# iran-chem-database — Fix Report (v2.1.0 → v2.2.0)

Fixes applied per the attached fix guide (`iran_chem_database_fix_guide.md`), in its
recommended implementation order. All changes are covered by tests
(**87 passed**, including live PostgreSQL integration + a live FastAPI smoke test).

## 1. Export fixes (§2) — DONE
- `/api/v1/export` is the full, non-page-limited export: `shape=offerings|molecules`,
  `organic_status=true|false|unknown|all`, `available=true|false`.
- Every export carries an auditable `# export_metadata:` line: timestamp, filters,
  molecule/offering counts, supplier crawl status, newest/oldest crawl times, scope
  statement ("best-effort supplier-offering index").
- `shape=molecules` deduplicates by source identity with `n_suppliers`/`suppliers`.
- Agent instructions updated: `/molecules` is paginated — never export one page;
  reconcile against `total` and `/coverage`.

## 2. CAS-only insertion defect (§3) — DONE
- Root cause confirmed: `"fallback-" + sha256[:20]` = 29 chars into `VARCHAR(27)`.
- `Molecule.inchi_key` now nullable, holds REAL InChIKeys only.
- New unique `Molecule.source_identity`: InChIKey > normalized CAS >
  supplier+product-code > deterministic 27-char fallback. Fallbacks are never
  labeled InChIKeys in API/CSV.
- Alembic migration `0002_fix_guide` upgrades existing DBs (with backfill, verified
  against a legacy-schema DB containing old fallback rows) or creates the full
  schema on fresh DBs (verified).

## 3. Silent dropping of entries (§4) — DONE
- `parsing.inclusion_mode`: `strict_research | lab_or_research | all_catalogue`
  (default `lab_or_research`), configurable in config.yaml + env.
- New `rejected_catalogue_items` audit table — grade/validation/sync rejections
  are persisted with raw fields, stage, reason, timestamp.
- Persian grade vocabulary expanded; Persian/Arabic character variants + ZWNJ
  normalized; generic "pure" is now a confidence signal, not a guarantee.

## 4. Extraction improvements (§5) — DONE
- JSON-LD parser: additionalProperty/PropertyValue, sku/mpn/identifier, offer
  availability & currency, CAS/purity/grade from descriptions.
- New DOCX parser (stdlib only); legacy `.doc` removed from advertised filters
  and documented as unsupported.
- New generic JSON catalogue parser (list / {items,data,rows,edges} / GraphQL
  envelopes).
- New `JSCatalogueEngine`: API-hint detection, Playwright network recording,
  persisted JSON responses, bounded API pagination following.
- Real permissioned fixtures + tests for each new parser path.

## 5. Crawling & coverage (§6–7) — DONE
- New `/api/v1/coverage` endpoint (supplier terminal statuses, molecule/offering
  counts, organic breakdown, `ready_for_complete_export`).
- `mirror_all_suppliers` returns honest `{active, eligible, queued, skipped_not_due}`.
- CrawlLog gets terminal status + `partial_reason` (timeout, no HTML, zero
  products, all-grade-rejected, …).
- Supplier `crawl_profile` classification persisted (static_html /
  paginated_database / pdf_excel_catalogue / js_catalogue / login_required /
  no_public_catalogue / blocked) and respected by the profile selector.
- Discovery sweep extended: link analysis over mirrored suppliers +
  `curated_suppliers.json`; candidates still verified before crawling.
- Installer message replaced: initial crawl is queued (hours/days), monitor via
  `/coverage`, `/stats`, `/crawl-logs`.

## 6. Explicit organic classification (§8) — DONE
- New `organic_classifier.py`: structure-first (RDKit), then CAS resolution,
  then name resolution (PubChem), else `unknown` — never guessed.
- Fields stored per molecule: `organic_status`, `organic_reason`,
  `organic_confidence`; server-side export filter + coverage breakdown.

## 7. Truthful reporting (§6.1, §9) — DONE
- SKILL.md / README / docs no longer claim "every supplier" or "zero supplier
  gaps"; coverage is measured and published; scope statement on every export.

## Verification performed
- `pytest tests/` → **87 passed** (against real PostgreSQL; DB tests auto-skip
  elsewhere).
- End-to-end pipeline over sample mirror: CAS-only record inserted as
  `cas:64-17-5` with `inchi_key=None`, organic resolved `true/cas_resolution`
  via PubChem, 3 rejections audited.
- Live uvicorn smoke test: `/coverage`, paginated `/molecules`, both export
  shapes + organic filter + metadata line verified.
- Alembic migration tested on BOTH a fresh DB and a legacy-schema DB with
  old fallback rows (backfill verified).
- Version bumped to 2.2.0 (SKILL.md, skill-card.md); README verification
  hashes refreshed; CHANGELOG.md added.
