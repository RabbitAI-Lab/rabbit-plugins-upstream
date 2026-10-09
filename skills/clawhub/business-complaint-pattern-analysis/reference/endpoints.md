# business-complaint-pattern-analysis — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**8 endpoints across 2 platform group(s).**

## Datasets (3)

### `datasets_bbb_businesses_facets`

- **HTTP:** `GET /datasets/bbb-businesses/facets`
- **What:** Facet the BBB businesses dataset. Returns distribution counts over the BBB businesses index (dataset id enum value `bbb-businesses`), honoring the same filters as search. Facet enum: `category`, `state`, `city`, `rating`, `accredited`, `entity_type`, `run_id`.
- **Params:** `accredited` (boolean, optional) — Accreditation filter; `category` (string, optional) — Exact category filter; `city` (string, optional) — Exact city filter; `entity_type` (string, optional) — Exact entity-type filter; `facet` (string, **required**) — Facet enum: category, state, city, rating, accredited, entity_type, run_id; `q` (string, optional) — Full-text match on the business name/category, max 256 characters; `rating` (string, optional) — Exact letter-grade rating filter. Enum: A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F; `run_id` (string, optional) — Exact crawl run id filter; `state` (string, optional) — Exact 2-letter state/province filter

### `datasets_bbb_businesses_item`

- **HTTP:** `GET /datasets/bbb-businesses/items/{id}`
- **What:** Get a business from the BBB businesses dataset. Returns one business by id from dataset id enum value `bbb-businesses`. Returns 404 when the business is not in the index.
- **Params:** `id` (string, **required**) — Business id (the <bbbLocalId>-<businessId> slug from the profile URL), e.g. 0825-1000223803

### `datasets_bbb_businesses_search`

- **HTTP:** `GET /datasets/bbb-businesses/search`
- **What:** Search the BBB businesses dataset. Searches the BBB (Better Business Bureau) businesses index (dataset id enum value `bbb-businesses`) — business profiles crawled from bbb.org's own search/category-browse pages: computed A+-F letter-grade rating, paid-accreditation status, category, contact info, business details, operating hours, and products/services. Complaints, full reviews, and the full "reasons for rating"/service-area detail are NOT embedded here; each record instead carries complaints_url/reviews_url/more_info_url pointing at the live bbb-business-complaints/bbb-business-reviews/bbb-business-more-info endpoints for on-demand lookup. rating enum: `A+`, `A`, `A-`, `B+`, `B`, `B-`, `C+`, `C`, `C-`, `D+`, `D`, `D-`, `F`. sort enum: `relevance`, `rating_desc`, `rating_asc`, `accredited_first`, `name_asc`, `years_in_business_desc`.
- **Params:** `accredited` (boolean, optional) — Accreditation filter; true keeps only accredited businesses; `category` (string, optional) — Exact category filter, e.g. Plumber. Use the values returned by facets?facet=category; `city` (string, optional) — Exact city filter, parsed from the profile URL; `entity_type` (string, optional) — Exact entity-type filter, e.g. Limited Liability Company (LLC); `min_rating_rank` (integer, optional) — Numeric floor against the denormalized rating rank (A+=12 down to F=0), e.g. 10 for 'A- and above'; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text match on the business name/category, max 256 characters; `rating` (string, optional) — Exact letter-grade rating filter. Enum: A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F; `run_id` (string, optional) — Exact crawl run id filter; `sort` (string, optional) — Sort enum: relevance, rating_desc, rating_asc, accredited_first, name_asc, years_in_business_desc; `state` (string, optional) — Exact 2-letter state/province filter, parsed from the profile URL, e.g. tx

## BBB (5)

### `bbb_business`

- **HTTP:** `GET /bbb/business`
- **What:** Get a Better Business Bureau business profile. Returns a normalized bbb.org business profile: BBB rating letter grade and reasons, accreditation status and since-date, years in business, BBB file/incorporation dates, entity type, contact info, business categories, social media, and a short latest-reviews preview. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_complaints`

- **HTTP:** `GET /bbb/business/complaints`
- **What:** Get a Better Business Bureau business's complaint history. Returns a business's BBB complaint history: total complaint count, complaints closed in the last 12 months, and per-complaint detail (date, type, status, narrative text, and any business response / customer answer thread). A business with no filed complaints returns total_complaints 0 and an empty complaints list -- this is a normal result, not an error. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_more_info`

- **HTTP:** `GET /bbb/business/more-info`
- **What:** Get a Better Business Bureau business's full rating reasons and service area. Returns a business's full per-factor "Reasons for Rating" list and full service-area list, from the separate BBB business profile /more-info sub-page. The bbb-business endpoint's own rating_reasons field is read from the main profile page and typically holds only one generic boilerplate bullet regardless of actual rating; this endpoint fetches the richer, business-specific list instead. Service area is business-conditional -- some businesses render no service-area section at all, in which case service_areas is empty. Credential-free public Better Business Bureau data.
- **Params:** `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_business_reviews`

- **HTTP:** `GET /bbb/business/reviews`
- **What:** Get a Better Business Bureau business's customer reviews. Returns a business's full customer-review list (author, star rating, date, text, and any business response thread), paginated 10 per page, plus the average star rating and total review count. Credential-free public Better Business Bureau data. Unlike the other bbb-business-* endpoints, this one is fetched with browser impersonation rather than plain direct HTTP -- see the family's maintenance note for why.
- **Params:** `page` (integer, optional) — Result page (10 per page), default 1; `url` (string, **required**) — BBB business profile URL, from a bbb-search result's url or hq_profile_url

### `bbb_search`

- **HTTP:** `GET /bbb/search`
- **What:** Search Better Business Bureau businesses. Searches bbb.org for businesses by name or category near a location. Returns each business's BBB rating letter grade, accreditation status, categories, service areas, contact info, and profile URL. Credential-free public Better Business Bureau data.
- **Params:** `location` (string, **required**) — City and state (e.g. 'Austin, TX') or a ZIP code; `page` (integer, optional) — Result page, default 1; `query` (string, **required**) — Business name or category/service keyword
