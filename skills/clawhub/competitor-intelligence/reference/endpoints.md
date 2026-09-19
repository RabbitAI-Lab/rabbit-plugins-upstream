# competitor-intelligence — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**17 endpoints across 7 platform group(s).**

## Bing (1)

### `bing_search`

- **HTTP:** `GET /bing/search`
- **What:** Search Bing web results. Returns normalized Bing web search results for a query string, including organic results, optional context panel data, related queries, people-also-ask questions, news modules, video modules, and page-based pagination. Empty optional blocks are omitted from the JSON response. Locale defaults to country=us and lang=en-us. Results are fetched with a Chrome-impersonated request client and return 503 on a genuine transport failure or challenge page. Bing occasionally serves a well-formed page whose results share no significant term with the query; when every hedged attempt hits this, the response is still returned as 200 with data.low_confidence set to true (and the X-Low-Confidence header) instead of being withheld, so callers get Bing's real answer plus an honest signal to double-check it rather than nothing. Queries that use the site: operator (for example site:gov.hu) are not supported: Bing serves a bot-verification challenge for them, so they are rejected with 400 before any request is made. Use the Google search endpoint (/api/v1/google/search) for domain-restricted searches.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Web (2)

### `extract`

- **HTTP:** `POST /extract`
- **What:** Extract schema-conforming JSON from a URL. Scrapes a public URL into clean Markdown, then returns data that strictly conforms to the supplied bounded JSON Schema.
- **Params:** `extractOption` (object, **required**) — Extraction options
- **REST body:** Send the value of the MCP argument `extractOption` directly as the JSON body; do not wrap it in a `extractOption` property.

### `web_scrape`

- **HTTP:** `POST /web/scrape`
- **What:** Scrape a URL into markdown, HTML, links or metadata. Fetches a single public URL and returns clean content in the requested formats (markdown, html, raw_html, links, metadata). The request body IS the ScrapeOption object itself — e.g. {"url": "https://example.com"} — do not wrap it in an extra key. With render=auto the request starts as a fast HTTP fetch and escalates to a real browser when the page is blocked or rendered with JavaScript; backend only pins a specific headless-browser engine for the browser tier and is not a render mode. only_main_content (default true) strips navigation, headers, footers and other boilerplate before conversion. Only public pages are supported; respect each site's terms of use and robots directives. A handful of popular sites (Amazon, Reddit, Yelp, LinkedIn, and others) already have a dedicated, more reliable endpoint elsewhere in this API — a failed scrape against one of them names it.
- **Params:** `scrapeOption` (object, **required**) — Scrape options
- **REST body:** Send the value of the MCP argument `scrapeOption` directly as the JSON body; do not wrap it in a `scrapeOption` property.

## SimilarWeb (2)

### `similarweb_search`

- **HTTP:** `GET /similarweb/search`
- **What:** Search SimilarWeb Info. Returns SimilarWeb data for a given query (typically a domain).
- **Params:** `q` (string, **required**) — Domain or keyword to search

### `similarweb_web`

- **HTTP:** `GET /similarweb/web/{domain}`
- **What:** Get SimilarWeb Web Info. Returns traffic and engagement data from SimilarWeb for a specific domain.
- **Params:** `domain` (string, **required**) — Domain to fetch SimilarWeb data for

## ProductHunt (4)

### `producthunt_alternatives`

- **HTTP:** `GET /producthunt/product/{id}/alternatives`
- **What:** Retrieve Product Hunt product alternatives. Returns paginated alternatives, tags, and related discussions for a Product Hunt product.
- **Params:** `cursor` (string, optional) — Pagination cursor; `first` (integer, optional) — Page size; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Sort order; `tags` (string, optional) — Comma-separated tag slugs

### `producthunt_launches`

- **HTTP:** `GET /producthunt/product/{id}/launches`
- **What:** Retrieve Product Hunt product launches. Returns paginated launch posts for a Product Hunt product using Product Hunt's ProductPageLaunches GraphQL operation.
- **Params:** `cursor` (string, optional) — Pagination cursor; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Product Hunt launch order

### `producthunt_product`

- **HTTP:** `GET /producthunt/product/{id}`
- **What:** Retrieve Product Hunt product details. Returns the core Product Hunt product details.
- **Params:** `id` (string, **required**) — Product Hunt slug or numeric ID

### `producthunt_search`

- **HTTP:** `GET /producthunt/search`
- **What:** Search for products, users, or launches on Product Hunt. Performs a full-text Product Hunt search and returns matching products, users, or launches.
- **Params:** `featured` (boolean, optional) — Launch search only: featured launches only; `page` (integer, optional) — Page number (1-based); `query` (string, **required**) — Search keywords; `topics` (string, optional) — Launch search only: comma-separated topic slugs; `type` (string, optional) — Result type: **product** (default), **user**, or **launch**

## Trustpilot (3)

### `trustpilot_business`

- **HTTP:** `GET /trustpilot/business/{slug}`
- **What:** Get Trustpilot business profile. Returns a summary Trustpilot business profile parsed from the public business page.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_reviews`

- **HTTP:** `GET /trustpilot/business/{slug}/reviews`
- **What:** Get Trustpilot business reviews. Returns paginated Trustpilot business reviews parsed from the public review page.
- **Params:** `date_from` (string, optional) — Date range start in YYYY-MM-DD; currently rejected by upstream; `date_to` (string, optional) — Date range end in YYYY-MM-DD; currently rejected by upstream; `language` (string, optional) — Review language code used by Trustpilot; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, optional) — Text search within reviews; `replied` (boolean, optional) — Filter to reviews with business replies; `slug` (string, **required**) — Trustpilot business slug; `stars` (integer, optional) — Filter by star rating from 1 to 5; `verified` (boolean, optional) — Filter to verified reviews

### `trustpilot_business_search`

- **HTTP:** `GET /trustpilot/business-units/search`
- **What:** Search Trustpilot business units. Returns normalized business-unit search results from Trustpilot's JSON business-unit search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `page` (integer, optional) — 1-based page number; defaults to 1; `page_size` (integer, optional) — Results per page; defaults to 20, maximum 100; `q` (string, **required**) — Search query

## Capterra (3)

### `capterra_product`

- **HTTP:** `GET /capterra/product`
- **What:** Get a Capterra product. Returns a normalized Capterra product profile: name, description, category, and aggregate rating. Credential-free public Capterra data, rendered from the product page through proxied browser renderers.
- **Params:** `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_reviews`

- **HTTP:** `GET /capterra/product/reviews`
- **What:** Get Capterra product reviews. Returns a page of normalized Capterra reviews (author, headline, rating) plus the product's aggregate rating. Credential-free public Capterra data, rendered from the reviews page through proxied browser renderers.
- **Params:** `page` (integer, optional) — Page number (default 1); `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_search`

- **HTTP:** `GET /capterra/search`
- **What:** Search Capterra products. Returns Capterra search-result products (id, name, url, description, rating). Credential-free public Capterra data, rendered from the search page through proxied browser renderers. Note: Capterra renders a fallback product list even for queries with no genuine match, rather than a distinct empty-results page, so callers should treat low-relevance results as an upstream characteristic, not a bug.
- **Params:** `q` (string, **required**) — Search query

## Datasets (2)

### `datasets_jobs_companies`

- **HTTP:** `GET /datasets/jobs/companies`
- **What:** Find which companies are hiring. Searches the discovered company board registry — which companies are hiring, on which ATS (or, for the 5 single-company big-tech providers, which platform), with how many open roles. Set sponsors_visa=true to keep companies with certified employer filings in recent public U.S. Department of Labor LCA disclosure data. This is company-level historical evidence, not a guarantee for a specific role or candidate. provider enum: `greenhouse`, `lever`, `ashby`, `workday`, `smartrecruiters`, `workable`, `recruitee`, `rippling`, `personio`, `teamtailor`, `oracle`, `ukg`, `icims`, `eightfold`, `gem`, `pinpoint`, `amazon-jobs`, `apple-jobs`, `google-jobs`, `meta-jobs`, `tesla-jobs`. status enum: `active`, `empty`, `gone`, `blocked`, `pending`, `invalid`. sort enum: `open_desc`, `company_asc`, `crawled_desc`.
- **Params:** `min_open_roles` (integer, optional) — Minimum open roles; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; `provider` (string, optional) — Provider filter; `q` (string, optional) — Match on company name / domain; `sort` (string, optional) — Sort enum: open_desc, company_asc, crawled_desc; `sponsors_visa` (boolean, optional) — Keep companies with recent certified DOL LCA filings (default false); `status` (string, optional) — Board status. Enum: active, empty, gone, blocked, pending, invalid

### `datasets_jobs_search`

- **HTTP:** `GET /datasets/jobs/search`
- **What:** Search the jobs dataset (all companies' live postings). Full-text + faceted search over every job posting crawled from every discovered company ATS board (Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Recruitee, Rippling, Personio, Teamtailor, Oracle, UKG, iCIMS, Eightfold, Gem, Pinpoint) plus 5 single-company big-tech careers platforms (Amazon, Apple, Google, Meta, Tesla). Open roles only by default (set include_closed=true for historical/filled roles). Salary is parsed from a structured field when the provider has one, or from an explicit pay figure stated in the description otherwise, so coverage varies by posting rather than by provider; min_salary/max_salary filter on it and require salary_currency, since comparing raw compensation numbers across currencies is meaningless. Location is also exposed as structured city/state/country fields alongside the free-text location string, so city/state/country filter on an exact match of those parsed components rather than substring-matching the display string. job_family is an exact level-2 ISCO family label assigned from ESCO occupation evidence; ambiguous postings remain unclassified and do not match that filter. employment_type is never populated for google-jobs/meta-jobs, and posted_at (so sort=posted_desc) is never populated for meta-jobs/tesla-jobs -- their upstream APIs expose no such field. provider enum: `greenhouse`, `lever`, `ashby`, `workday`, `smartrecruiters`, `workable`, `recruitee`, `rippling`, `personio`, `teamtailor`, `oracle`, `ukg`, `icims`, `eightfold`, `gem`, `pinpoint`, `amazon-jobs`, `apple-jobs`, `google-jobs`, `meta-jobs`, `tesla-jobs`. workplace_type enum: `onsite`, `hybrid`, `remote`. sort enum: `relevance`, `posted_desc`, `company_asc`.
- **Params:** `city` (string, optional) — Exact city filter (parsed location component); `company` (string, optional) — Company name match; `country` (string, optional) — Exact country filter (parsed location component); ISO country code or name, matched case-insensitively; `department` (string, optional) — Exact department filter; `employment_type` (string, optional) — Exact employment-type filter; `include_closed` (boolean, optional) — Include closed/filled roles (default false = open only); `job_family` (string, optional) — Exact ESCO/ISCO job-family label filter; `location` (string, optional) — Location match; `max_salary` (number, optional) — Maximum salary (matches postings whose range starts at or below this); requires salary_currency; `min_salary` (number, optional) — Minimum salary (matches postings whose range reaches at least this); requires salary_currency; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; page*page_size must be <= 10000; `provider` (string, optional) — Provider filter; `q` (string, optional) — Full-text over title, company, description; `remote` (boolean, optional) — Filter by remote (true or false); `salary_currency` (string, optional) — 3-letter ISO currency code (e.g. USD) the min_salary/max_salary bounds are in; required when either bound is set; `sort` (string, optional) — Sort enum: relevance, posted_desc, company_asc; `state` (string, optional) — Exact state/region filter (parsed location component); `workplace_type` (string, optional) — Workplace type filter
