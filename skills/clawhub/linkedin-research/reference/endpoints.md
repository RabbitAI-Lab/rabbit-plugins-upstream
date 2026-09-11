# linkedin-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**3 endpoints across 1 platform group(s).**

## LinkedIn (3)

### `linkedin_company`

- **HTTP:** `GET /linkedin/company/{id}`
- **What:** Get LinkedIn Company info by ID. Returns detailed company information by LinkedIn ID.
- **Params:** `id` (string, **required**) — LinkedIn Company ID

### `linkedin_product`

- **HTTP:** `GET /linkedin/product/{id}`
- **What:** Get LinkedIn Product info by ID. Returns detailed product information from LinkedIn by product ID.
- **Params:** `id` (string, **required**) — LinkedIn Product ID

### `linkedin_showcase`

- **HTTP:** `GET /linkedin/showcase/{id}`
- **What:** Get Linkedin Showcase Page Info. Returns detailed information about a LinkedIn showcase page by ID.
- **Params:** `id` (string, **required**) — LinkedIn Showcase Page ID
