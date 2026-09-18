# journalist-media-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**6 endpoints across 3 platform group(s).**

## Datasets (3)

### `datasets_journalists_facets`

- **HTTP:** `GET /datasets/journalists/facets`
- **What:** Facet the journalists dataset. Returns distribution counts over the journalists index (dataset id enum value `journalists`), honoring the same filters as search. Facet enum: `outlet`, `vertical`, `topic`, `contact_type`.
- **Params:** `contact_type` (string, optional) — Contact-availability filter. Enum: email, social, none; `facet` (string, **required**) — Facet enum: outlet, vertical, topic, contact_type; `outlet` (string, optional) — Exact outlet id filter; `q` (string, optional) — Full-text match on the journalist's name, title, and bio, max 256 characters; `topic` (string, optional) — Exact topic filter; `vertical` (string, optional) — Exact beat-vertical filter. Enum: tech, crypto, marketing, consumer_tech, consumer_policy, cybersecurity, health, gaming, climate, business, entertainment, sports, legal, science, politics, real_estate, automotive, travel, food, education, design, film_tv, fashion, music, personal_finance, tech_independent, culture_independent, local_news, construction, banking, retail, aerospace_defense, energy, agriculture, local_business

### `datasets_journalists_item`

- **HTTP:** `GET /datasets/journalists/items/{outlet}/{slug}`
- **What:** Get a journalist from the journalists dataset. Returns one journalist by outlet id and slug from dataset id enum value `journalists`. Returns 404 when the outlet is not supported or the journalist is not in the index.
- **Params:** `outlet` (string, **required**) — Outlet id, e.g. techcrunch. Use the ids returned by facets?facet=outlet; `slug` (string, **required**) — Journalist slug within the outlet, e.g. zack-whittaker

### `datasets_journalists_search`

- **HTTP:** `GET /datasets/journalists/search`
- **What:** Search the journalists dataset. Searches the journalists index (dataset id enum value `journalists`) — public journalist and reporter contact records crawled from news outlets' own staff/author pages, for PR outreach. Each record carries the outlet, title, best-effort beat topics, and any public contact info (a work email or a social handle) found on that outlet's own page. There is no cross-outlet upstream search; this dataset is built by crawling a curated roster of outlets ourselves. vertical enum: `tech`, `crypto`, `marketing`, `consumer_tech`, `consumer_policy`, `cybersecurity`, `health`, `gaming`, `climate`, `business`, `entertainment`, `sports`, `legal`, `science`, `politics`, `real_estate`, `automotive`, `travel`, `food`, `education`, `design`, `film_tv`, `fashion`, `music`, `personal_finance`, `tech_independent`, `culture_independent`, `local_news`, `construction`, `banking`, `retail`, `aerospace_defense`, `energy`, `agriculture`, `local_business`. contact_type enum: `email`, `social`, `none`. sort enum: `relevance`, `name_asc`, `outlet_asc`, `crawled_desc`.
- **Params:** `contact_type` (string, optional) — Contact-availability filter. Enum: email, social, none; `outlet` (string, optional) — Exact outlet id filter, e.g. techcrunch, coindesk. Use the ids returned by facets?facet=outlet; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text match on the journalist's name, title, and bio, max 256 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, outlet_asc, crawled_desc; `topic` (string, optional) — Exact topic filter, e.g. security, stablecoins. Use the values returned by facets?facet=topic; `vertical` (string, optional) — Exact beat-vertical filter. Enum: tech, crypto, marketing, consumer_tech, consumer_policy, cybersecurity, health, gaming, climate, business, entertainment, sports, legal, science, politics, real_estate, automotive, travel, food, education, design, film_tv, fashion, music, personal_finance, tech_independent, culture_independent, local_news, construction, banking, retail, aerospace_defense, energy, agriculture, local_business

## Bing (2)

### `bing_news`

- **HTTP:** `GET /bing/news`
- **What:** Search Bing news results. Returns normalized Bing news search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing news HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_search`

- **HTTP:** `GET /bing/search`
- **What:** Search Bing web results. Returns normalized Bing web search results for a query string, including organic results, optional context panel data, related queries, people-also-ask questions, news modules, video modules, and page-based pagination. Empty optional blocks are omitted from the JSON response. Locale defaults to country=us and lang=en-us. Results are fetched with a Chrome-impersonated request client and return 503 on a genuine transport failure or challenge page. Bing occasionally serves a well-formed page whose results share no significant term with the query; when every hedged attempt hits this, the response is still returned as 200 with data.low_confidence set to true (and the X-Low-Confidence header) instead of being withheld, so callers get Bing's real answer plus an honest signal to double-check it rather than nothing. Queries that use the site: operator (for example site:gov.hu) are not supported: Bing serves a bot-verification challenge for them, so they are rejected with 400 before any request is made. Use the Google search endpoint (/api/v1/google/search) for domain-restricted searches.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Web (1)

### `web_scrape`

- **HTTP:** `POST /web/scrape`
- **What:** Scrape a URL into markdown, HTML, links or metadata. Fetches a single public URL and returns clean content in the requested formats (markdown, html, raw_html, links, metadata). The request body IS the ScrapeOption object itself — e.g. {"url": "https://example.com"} — do not wrap it in an extra key. With render=auto the request starts as a fast HTTP fetch and escalates to a real browser when the page is blocked or rendered with JavaScript; backend only pins a specific headless-browser engine for the browser tier and is not a render mode. only_main_content (default true) strips navigation, headers, footers and other boilerplate before conversion. Only public pages are supported; respect each site's terms of use and robots directives. A handful of popular sites (Amazon, Reddit, Yelp, LinkedIn, and others) already have a dedicated, more reliable endpoint elsewhere in this API — a failed scrape against one of them names it.
- **Params:** `scrapeOption` (object, **required**) — Scrape options
- **REST body:** Send the value of the MCP argument `scrapeOption` directly as the JSON body; do not wrap it in a `scrapeOption` property.
