# amazon-jobs-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**2 endpoints across 1 platform group(s).**

## Amazon Jobs (2)

### `amazon_jobs_job`

- **HTTP:** `GET /amazon-jobs/job`
- **What:** Amazon Jobs single posting. Returns one Amazon.jobs posting by its numeric job id (the `id` field returned by search). Parsed from amazon.jobs's stable server-rendered job detail page — there is no separate JSON detail endpoint upstream.
- **Params:** `id` (string, **required**) — Numeric Amazon job id

### `amazon_jobs_search`

- **HTTP:** `GET /amazon-jobs/search`
- **What:** Amazon Jobs search. Searches Amazon's public careers site (amazon.jobs) via its credential-free search JSON. Each result includes the full description and qualifications inline. `sort` accepts `relevant` (default, upstream relevance ranking) or `recent` (newest posted first). Either `q` or `category` (or both) must be given -- `category` filters by Amazon's own job-category taxonomy and works with no text query at all.
- **Params:** `category` (string, optional) — Amazon's own job-category taxonomy slug. Either q or category is required; `country` (string, optional) — ISO 3166-1 alpha-3 country code filter; `limit` (integer, optional) — Results per page, max 100 (default 20); `page` (integer, optional) — Page number, 1-based; `q` (string, optional) — Search query. Either q or category is required; `sort` (string, optional) — Sort order
