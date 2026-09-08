# iran-chem-database — Remediation Report (v2.2.0 → v2.3.0)

All changes follow `iran-chem-database-remediation-plan.md`, in its recommended
implementation sequence (P0 first). **101 tests pass** against live PostgreSQL,
plus a live end-to-end smoke test of every new surface.

## P0 — install path, async crawl, exports, coverage

### §1 Fresh-install path repaired
- `.env.example` ships in the release archive (packaging regression test
  `tests/test_packaging.py` extracts the release tar and asserts it, plus all
  source/migration files).
- `install.sh` refuses to continue on a missing `.env.example` or placeholder
  `DB_PASSWORD`, prints the recovery `sed -i` command, and no longer requires
  `SEARCH_API_KEY` for basic operation.
- PostgreSQL readiness is awaited (`pg_isready` loop) instead of `sleep 5`.

### §2 Initial discovery is asynchronous
- `trigger_initial_crawl.py` now only ENQUEUES Celery jobs (`.delay()`),
  returns in seconds; the installer message says "Installation provides
  SOFTWARE, not a populated dataset".
- Directory discovery split into its own opt-in task with strict budgets
  (`discovery.directory_timeout_seconds`, `max_directories_per_run`,
  `max_new_candidates_per_run`, `initial_directory_discovery: false`);
  `httrack_engine.mirror_using_url_list` accepts a timeout instead of a
  hard-coded 3600 s.
- Seed crawling uses the 35 curated supplier seeds as the first cohort.

### §3 Pagination guardrails + export gating
- `/api/v1/molecules` returns `total_pages`, `has_more`, `next_page`,
  `export_hint`, supports `organic_status=true|false|unknown|all` (422 on
  unsupported values), default `limit` raised to 100.
- `/api/v1/export` gets `require_complete_coverage=true` → **HTTP 409** with
  `blocking_reasons` until every configured supplier has a terminal crawl
  state. `format=manifest` returns a machine-readable JSON manifest.
- SKILL.md carries the mandatory agent-instruction block (check coverage,
  never export one page, "confirmed organic" language, report metadata).

### §4 Coverage correctness + manifests
- New `crawl_run_state` table: every run persists `queued → running →
  success|partial|failed|skipped` with timestamps/reasons; new `/api/v1/jobs`
  endpoint lists them.
- `/api/v1/coverage` uses the LATEST run per supplier (a later `success`
  correctly supersedes `partial` — tested), reports real queued/running
  counts, records (accepted/rejected/organic split), and
  `export_readiness` with blocking reasons.
- Every export carries a JSON metadata line; `format=manifest` emits the
  full manifest incl. **SHA-256 of the exact CSV bytes** (checksum-match
  test included).

## P1 — records, classification, crawling, observability, docs

### §5 Nothing identifiable is lost; policy is explicit
- Inclusion modes renamed: `research_only` | `lab_or_research` |
  `all_identifiable_catalogue` (default; old names accepted as aliases).
- In `all_identifiable_catalogue`, even industrial-grade entries are RETAINED
  with grade preserved (`excluded-grade-retained`, low confidence) — tested.
- `python -m src.scripts.reparse_all_mirrors --inclusion-mode MODE`
  re-applies any policy to existing mirrors, reports candidates/accepted/
  per-reason rejections/sync errors, exits nonzero above
  `parsing.reparse_failure_threshold`.
- Policy is visible in `/coverage`, exports and the dashboard.

### §6 Organic classification communicates uncertainty
- `organic_status=true` is labeled **confirmed organic** in code, docs and
  exports; `unknown` rows are exported separately and flagged with
  `classification_review_required`.
- PubChem resolution is cached with retry/backoff/rate pause; lookup failures
  are recorded distinctly in `organic_lookup_error` — never treated as
  indistinguishable unknowns.

### §7 Crawler reliability
- Supplier onboarding fields: `expected_catalogue_type`,
  `expected_pagination`, `requires_login`, `robots_status`,
  `last_http_status`, `last_successful_product_count`, `partial_reason`.
- Partial-crawl detection now also covers pagination gaps
  (`pagination-incomplete:x/N`), API-hints-present-but-zero-json-captured,
  pages-mirrored-but-zero-products and unexpected product-count drops.

### §8 Docs/runtime consistency
- SKILL.md: "Installation provides SOFTWARE, not a populated dataset" +
  mandatory agent instructions; one authoritative Docker path + one complete
  bare-metal path (incl. Celery worker/beat steps).
- New `python -m src.scripts.health` command verifying httrack/PostgreSQL/
  Redis/coverage and distinguishing INITIALIZED from OK (bare-metal redis
  host fallback included).

### §9 Observability
- New `/api/v1/rejections` (stage/supplier filtered) and
  `/api/v1/reconciliation` (per-supplier funnel: offerings, unique molecules,
  rejections by reason, unresolved organic, crawl status, partial reason).
- Dashboard gains Coverage & Jobs, Rejections and Reconciliation panels;
  stats include rejection and organic distributions.

### §10 Tests — 101 passing
- Packaging: `.env.example` + required files in the release archive,
  installer placeholder logic, trigger script only enqueues.
- Integration (PostgreSQL): >100-molecule pagination metadata, export
  completeness + manifest SHA-256 match, 409 gating, latest-run partial→
  success transition, reparse restores previously rejected records, rejected
  items retain provenance, unknown-organic exported separately, organic
  filters on /molecules.

## Verification performed
- `pytest tests/` → **101 passed** (PostgreSQL-backed; auto-skip elsewhere).
- Live uvicorn smoke test (150 molecules, 2 suppliers, 1 partial):
  pagination metadata, organic filters (60/45/45), 422 on bad filter, 409
  gate with correct blocking reason, coverage latest-run logic, manifest
  (row_count + SHA-256 + version), /jobs, /rejections, /reconciliation,
  health command (INITIALIZED vs OK).
- Alembic chain: `0002_fix_guide` → `0003_remediation` (additive), verified
  on a fresh DB.
- Release tarball re-verified: 145 files incl. `.env.example` and all new
  modules.
- Version bumped to 2.3.0 (SKILL.md / skill-card / CHANGELOG / manifest);
  README verification hashes refreshed.
