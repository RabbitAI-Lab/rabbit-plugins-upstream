# apple-jobs-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**2 endpoints across 1 platform group(s).**

## Apple Jobs (2)

### `apple_jobs_job`

- **HTTP:** `GET /apple-jobs/job`
- **What:** Apple Jobs single posting. Returns one Apple Careers posting by its job id (the `id` field returned by search, e.g. `200674676-0836` for a specific requisition or `PIPE-200314122` for an evergreen/pipeline retail role). Parsed from jobs.apple.com's server-rendered job detail page.
- **Params:** `id` (string, **required**) — Apple job id

### `apple_jobs_search`

- **HTTP:** `GET /apple-jobs/search`
- **What:** Apple Jobs search. Searches Apple's public careers site (jobs.apple.com) via its server-rendered search page's embedded job data. Page size is fixed by Apple at 20 results. Search results carry identity/location/team metadata only — call the job endpoint for the full description and qualifications.
- **Params:** `location` (string, optional) — Location filter in Apple's own slug format, e.g. united-states-USA or singapore-SGP; `page` (integer, optional) — Page number, 1-based; `q` (string, **required**) — Search query
