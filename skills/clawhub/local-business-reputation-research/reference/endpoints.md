# local-business-reputation-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**28 endpoints across 4 platform group(s).**

## Yelp (8)

### `yelp_business`

- **HTTP:** `GET /yelp/business/{id}`
- **What:** Get Yelp business detail. Looks up a single Yelp business by alias or encoded id via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_menu`

- **HTTP:** `GET /yelp/business/{id}/menu`
- **What:** Get Yelp business menu. Fetches menu items for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_photos`

- **HTTP:** `GET /yelp/business/{id}/photos`
- **What:** Get Yelp business photos. Fetches the photo gallery for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max photos to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_review_highlights`

- **HTTP:** `GET /yelp/business/{id}/reviews/highlights`
- **What:** Get Yelp business review highlights. Fetches thematic review snippets (extracted talking points with a supporting quote) for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_reviews`

- **HTTP:** `GET /yelp/business/{id}/reviews`
- **What:** Get Yelp business reviews. Fetches reviews for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max reviews to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_reviews_search`

- **HTTP:** `GET /yelp/business/{id}/reviews/search`
- **What:** Search Yelp business reviews by keyword. Searches a Yelp business's reviews for a keyword via Yelp's real Android app backend, returning a highlighted excerpt per match. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `term` (string, **required**) — Keyword to search reviews for

### `yelp_geocode`

- **HTTP:** `GET /yelp/geocode`
- **What:** Geocode a free-form address. Resolves a free-form address into structured location data (coordinates, city, state, zip, county) via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller. Not business-scoped.
- **Params:** `address` (string, **required**) — Free-form address to geocode

### `yelp_search`

- **HTTP:** `GET /yelp/search`
- **What:** Search Yelp businesses. Searches Yelp's real Android app business-search backend for a term and location. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `limit` (integer, optional) — Max results to return, 1-50; `location` (string, **required**) — Neighborhood, city, state, or zip code; `offset` (integer, optional) — Pagination offset; `term` (string, **required**) — Search term

## BBB (9)

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

### `bbb_category`

- **HTTP:** `GET /bbb/category`
- **What:** Browse a Better Business Bureau category. Browses bbb.org businesses by category and location directly, without a free-text search query. Returns the same normalized business-result shape as bbb-search. Credential-free public Better Business Bureau data.
- **Params:** `page` (integer, optional) — Result page, default 1; `url` (string, **required**) — BBB category browse URL, from a bbb-search result's related_categories

### `bbb_scamtracker_detail`

- **HTTP:** `GET /bbb/scamtracker/{id}`
- **What:** Get a Better Business Bureau Scam Tracker report. Returns one normalized BBB Scam Tracker consumer scam report: description, dollars lost, targeted person's location, scammer location/email/phone/URL (when known), scam type, business name used, and date reported. Credential-free public Better Business Bureau data.
- **Params:** `id` (string, **required**) — BBB Scam Tracker report id, from a bbb-scamtracker-search result's id or url

### `bbb_scamtracker_search`

- **HTTP:** `GET /bbb/scamtracker/search`
- **What:** Search Better Business Bureau Scam Tracker reports. Searches bbb.org Scam Tracker's consumer-reported-scam database by free-text query, scam category, targeted-victim state/province, reported-scammer state/province, report-date range, and/or dollar-loss range, paginated 10 results/page. Omit every filter to browse the most-recent-first feed. Credential-free public Better Business Bureau data. This is a separate BBB dataset from the bbb-search/bbb-business/bbb-business-complaints business-rating family -- consumer-reported scam incidents, not business ratings.
- **Params:** `date_from` (string, optional) — Optional report-date range start (YYYY-MM-DD), inclusive. Must be set together with date_to; `date_to` (string, optional) — Optional report-date range end (YYYY-MM-DD), inclusive. Must be set together with date_from; `max_dollars_lost` (integer, optional) — Optional maximum reported dollar loss. Must be set together with min_dollars_lost; `min_dollars_lost` (integer, optional) — Optional minimum reported dollar loss. Must be set together with max_dollars_lost; `page` (integer, optional) — Result page (10 per page), default 1; `query` (string, optional) — Free-text search (phone number, website, email, business name, scam ID, description). Omit to browse the most-recent feed; `scam_type` (string, optional) — Scam category filter; `scammer_state` (string, optional) — Optional 2-letter reported-scammer state/province code (US state or Canadian province) -- where the scammer is reported to be, not the victim; `state` (string, optional) — Optional 2-letter targeted-victim state/province code (US state or Canadian province)

### `bbb_scamtracker_state_stats`

- **HTTP:** `GET /bbb/scamtracker/state-stats`
- **What:** Get Better Business Bureau Scam Tracker state/province aggregate stats. Returns aggregate scam-report stats per US state and Canadian province for a given time window: report counts, dollar losses, per-capita rates, year-over-year change, and top scam-type breakdown. This calls the same JSON API the BBB Scam Tracker heatmap dashboard's own frontend uses -- not an HTML scrape. Credential-free public Better Business Bureau data.
- **Params:** `period` (string, optional) — Aggregation window, default 90

### `bbb_search`

- **HTTP:** `GET /bbb/search`
- **What:** Search Better Business Bureau businesses. Searches bbb.org for businesses by name or category near a location. Returns each business's BBB rating letter grade, accreditation status, categories, service areas, contact info, and profile URL. Credential-free public Better Business Bureau data.
- **Params:** `location` (string, **required**) — City and state (e.g. 'Austin, TX') or a ZIP code; `page` (integer, optional) — Result page, default 1; `query` (string, **required**) — Business name or category/service keyword

## Trustpilot (7)

### `trustpilot_business`

- **HTTP:** `GET /trustpilot/business/{slug}`
- **What:** Get Trustpilot business profile. Returns a summary Trustpilot business profile parsed from the public business page.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_related`

- **HTTP:** `GET /trustpilot/business/{slug}/related`
- **What:** Get Trustpilot related businesses. Returns related company cards from Trustpilot's public business page rails.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_reviews`

- **HTTP:** `GET /trustpilot/business/{slug}/reviews`
- **What:** Get Trustpilot business reviews. Returns paginated Trustpilot business reviews parsed from the public review page.
- **Params:** `date_from` (string, optional) — Date range start in YYYY-MM-DD; currently rejected by upstream; `date_to` (string, optional) — Date range end in YYYY-MM-DD; currently rejected by upstream; `language` (string, optional) — Review language code used by Trustpilot; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, optional) — Text search within reviews; `replied` (boolean, optional) — Filter to reviews with business replies; `slug` (string, **required**) — Trustpilot business slug; `stars` (integer, optional) — Filter by star rating from 1 to 5; `verified` (boolean, optional) — Filter to verified reviews

### `trustpilot_business_search`

- **HTTP:** `GET /trustpilot/business-units/search`
- **What:** Search Trustpilot business units. Returns normalized business-unit search results from Trustpilot's JSON business-unit search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `page` (integer, optional) — 1-based page number; defaults to 1; `page_size` (integer, optional) — Results per page; defaults to 20, maximum 100; `q` (string, **required**) — Search query

### `trustpilot_categories`

- **HTTP:** `GET /trustpilot/categories`
- **What:** Get Trustpilot categories. Returns the Trustpilot public category index grouped by top-level category.
- **Params:** _none_

### `trustpilot_category`

- **HTTP:** `GET /trustpilot/category/{slug}`
- **What:** Get Trustpilot category detail. Returns category metadata, company cards, and side rails from Trustpilot's public category page.
- **Params:** `page` (integer, optional) — 1-based page number; defaults to 1; `slug` (string, **required**) — Trustpilot category slug

### `trustpilot_category_search`

- **HTTP:** `GET /trustpilot/categories/search`
- **What:** Search Trustpilot categories. Returns normalized category search results from Trustpilot's JSON category search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `locale` (string, optional) — Locale in ll-CC format; defaults to en-US; `q` (string, **required**) — Search query; `size` (integer, optional) — Maximum number of categories; defaults to 20

## OpenTable (4)

### `opentable_restaurant`

- **HTTP:** `GET /opentable/restaurant`
- **What:** Get an OpenTable restaurant's profile and live availability. Returns a restaurant's profile (location, cuisines, hours, price band, review summary) plus real-time bookable timeslots for the given date/time and party size. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `party_size` (integer, optional) — Party size, default 2; `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_menus`

- **HTTP:** `GET /opentable/restaurant/menus`
- **What:** Get an OpenTable restaurant's menus. Returns a restaurant's menus (sections, items, prices). Credential-free.
- **Params:** `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_reviews`

- **HTTP:** `GET /opentable/restaurant/reviews`
- **What:** Get a page of an OpenTable restaurant's diner reviews. Returns a page of diner reviews (author, text, per-category ratings) for a restaurant. Credential-free.
- **Params:** `page` (integer, optional) — Page number, default 1; `restaurant_id` (string, **required**) — OpenTable restaurant id; `size` (integer, optional) — Reviews per page, default 20

### `opentable_search`

- **HTTP:** `GET /opentable/search`
- **What:** Search OpenTable restaurants near a location. Searches restaurants by free-text term (cuisine, name, neighborhood) near a latitude/longitude, for a given date/time and party size, including inline live availability per result. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `latitude` (number, **required**) — Search center latitude; `longitude` (number, **required**) — Search center longitude; `party_size` (integer, optional) — Party size, default 2; `size` (integer, optional) — Max results, default 10; `term` (string, **required**) — Free-text search term
