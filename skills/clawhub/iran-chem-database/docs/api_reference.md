# API Reference

Base URL: `http://localhost:8000/api/v1/`

| Method | Path | Description |
|---|---|---|
| GET | `/molecules` | Search/list molecules (**paginated** — default 20, `limit` ≤ 100; returns `total`) |
| GET | `/molecules/{identity}` | Molecule detail (by real InChIKey OR source identity) |
| GET | `/molecules/search?q=&cas=&smiles=&formula=` | Full-text / CAS / SMILES / formula search |
| GET | `/suppliers` | List suppliers |
| GET | `/suppliers/{id}` | Supplier detail |
| GET | `/suppliers/{id}/mirror-status` | HTTrack mirror health/status |
| GET | `/mirrors` | All HTTrack mirror statuses |
| GET | `/mirrors/{id}/changes` | Recent changes from hts-changes.json |
| GET | `/stats` | Global database statistics |
| GET | `/coverage` | **Measured crawl coverage** — supplier terminal statuses, molecule/offering counts, organic breakdown, `ready_for_complete_export` |
| GET | `/updates/recent` | Recently added/changed molecules |
| GET | `/export?format=csv\|json\|sdf&shape=offerings\|molecules&organic_status=true\|false\|unknown\|all&available=true\|false` | **Complete** database export with auditable metadata; never page-limited |
| GET | `/health` | Service health |
| GET | `/crawl-logs` | Recent crawl history (includes `partial_reason`) |
| GET | `/jobs` | Persisted crawl-run states (queued/running/success/partial/failed/skipped) |
| GET | `/rejections?stage=&supplier_id=&limit=` | Rejection audit trail (stage + reason per record) |
| GET | `/reconciliation` | Per-supplier funnel: offerings, unique molecules, rejections by reason, unresolved organic, crawl status |

### Pagination rules (mandatory for agents)

`GET /molecules` returns `total`, `total_pages`, `has_more`, `next_page` and an
`export_hint` — it is paginated (default 20 rows, `limit` ≤ 100) and must NEVER
be used to build a "complete" CSV. `organic_status=true|false|unknown|all` is a
supported filter. Unsupported filter values return HTTP 422.

### Export gating & manifests

- `require_complete_coverage=true` → HTTP 409 with `blocking_reasons` until
  every configured supplier has a terminal crawl state.
- `format=manifest` returns a JSON manifest for the exact CSV that would be
  produced with the same parameters: SHA-256 of the CSV, row count, coverage
  snapshot, version, scope statement, organic-status counts.
- `organic_status=true` means **confirmed organic** — records whose organic
  status could not be resolved are `unknown` and are exported separately
  (`classification_review_required` column flags them), never silently dropped.

### Export semantics (fix guide §2)

- `shape=offerings` (default) — one row per supplier offering; a molecule sold
  by three suppliers appears three times.
- `shape=molecules` — one row per unique molecule (deduplicated by source
  identity) with `n_suppliers` and `suppliers` columns.
- `organic_status` — server-side organic filter (`true`, `false`, `unknown`,
  or omitted/all).
- Every CSV starts with a `# export_metadata:` line containing the export
  timestamp, applied filters, unique molecule count, offering row count,
  supplier crawl status summary, newest/oldest crawl timestamps, and a scope
  statement. Reconcile exported rows against that line and `/coverage`
  before presenting the file as complete.
- `source_identity` is the dedup key; `inchi_key` only ever contains a real
  27-character InChIKey (empty otherwise — fallback identities are never
  labeled as InChIKeys).
- `GET /molecules` is paginated — an agent writing a CSV from a single page
  will silently truncate the catalogue. Use `/export` for full dumps, or
  paginate until `len(rows) == total`.

## Example queries

```bash
curl "http://localhost:8000/api/v1/molecules/search?q=ethanol"
curl "http://localhost:8000/api/v1/molecules/search?cas=64-17-5"
curl "http://localhost:8000/api/v1/molecules/search?formula=C2H6O"
curl "http://localhost:8000/api/v1/molecules/search?q=اتانول"
curl "http://localhost:8000/api/v1/export?format=csv"
```

Query parameters for `/molecules`:
`query`, `cas`, `formula`, `grade`, `supplierId`, `minPurity`, `available`,
`page`, `limit`.

---

## Social catalogue endpoints (v2.10)

All responses carry a `scope` field restating the platform boundary: **Telegram
public channels only**. Instagram/Facebook/X are login-walled and WhatsApp is
contact-only, so those appear as vendor contact leads, never scraped feeds.

| Endpoint | Description |
|---|---|
| `GET /api/v1/social/channels` | Verified channels + roles, and content-checked rejects with reasons |
| `GET /api/v1/social/coverage` | Per-channel mirror state: pages, id span, last run, `never_crawled` vs `mirrored` |
| `GET /api/v1/social/molecules` | **Paginated** listings (`page`, `limit`≤100, optional `grade`); announces `total_pages` / `has_more` |
| `GET /api/v1/social/rejections` | Audit trail — excluded candidates with `rejection_stage` + `rejection_reason` |
| `GET /api/v1/social/export` | Full, unpaginated catalogue + metrics; `require_complete_coverage=true` → **HTTP 409** until every channel is mirrored |
| `GET /api/v1/social/leads` | Vendor contact leads on non-automatable platforms, with `wa.me` RFQ links |

```bash
# Check coverage FIRST — never quote the catalogue without it
curl -s localhost:8000/api/v1/social/coverage

# Confirmed research-grade listings only
curl -s 'localhost:8000/api/v1/social/molecules?grade=research&limit=100'

# Full export (not page-limited)
curl -s localhost:8000/api/v1/social/export -o social-catalogue.json
```

### Rejection reasons

| Reason | Meaning |
|---|---|
| `no_sales_signal` | Not a product listing (no price/contact/brand/hashtag/verb) |
| `job_advert_not_a_product_listing` | Recruitment post (salary/shift/insurance markers) |
| `news_channel_requires_strong_marker` | News-role channel article without a strong listing marker |
| `generic_announcement_no_molecule_named` | Advertises a catalogue but names no molecule |
| `no_alias_or_cas_match` | A molecule is named but unresolved — a real dictionary gap |

The last two are deliberately separate so recall metrics stay honest: only
`no_alias_or_cas_match` indicates the alias dictionary needs extending.
