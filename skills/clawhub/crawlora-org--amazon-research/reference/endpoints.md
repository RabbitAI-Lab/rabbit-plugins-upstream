# amazon-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**5 endpoints across 1 platform group(s).**

## Amazon (5)

### `amazon_charts`

- **HTTP:** `GET /amazon/charts`
- **What:** Amazon product charts. Returns one page of a ranked Amazon chart (Best Sellers, New Releases, or Most Wished For) for a department or department subcategory on `amazon.com`. Discover valid department/node values with amazon-charts-categories.
- **Params:** `chart` (string, **required**) — Chart type; `department` (string, **required**) — Amazon department slug; `node` (string, optional) — Numeric browse node id; `page` (integer, optional) — 1-based page number

### `amazon_charts_categories`

- **HTTP:** `GET /amazon/charts/categories`
- **What:** Amazon chart categories. Returns the department and subcategory values amazon-charts accepts for a given chart. Omit department to list a chart's top-level departments; pass a department (and optionally a node) to get that category's own name plus its immediate child categories.
- **Params:** `chart` (string, **required**) — Chart type; `department` (string, optional) — Amazon department slug; `node` (string, optional) — Numeric browse node id (requires department)

### `amazon_product`

- **HTTP:** `GET /amazon/product/{asin}`
- **What:** Retrieve Amazon product details. Returns product details for an Amazon ASIN on `amazon.com`, including pricing, availability, overview data, inline review samples, and descriptive content.
- **Params:** `asin` (string, **required**) — Amazon ASIN; `currency` (string, optional) — Amazon currency; `language` (string, optional) — Amazon language

### `amazon_search`

- **HTTP:** `GET /amazon/search`
- **What:** Search Amazon products. Searches `amazon.com` by keyword, with optional sort order and page. Each result card has the ASIN, title, link, image, price and list price, rating and review count, the bought-in-last-month figure, and flags for sponsored placement and free delivery.
- **Params:** `k` (string, **required**) — Search keyword; `page` (integer, optional) — 1-based page number; `s` (string, optional) — Sort order

### `amazon_suggest`

- **HTTP:** `GET /amazon/suggest/{keyword}`
- **What:** Retrieve Amazon search suggestions. Returns Amazon's search-box autocomplete suggestions for a keyword prefix on `amazon.com`, as a plain list of suggested search phrases such as `apple watch bands`.
- **Params:** `keyword` (string, **required**) — Suggestion prefix
