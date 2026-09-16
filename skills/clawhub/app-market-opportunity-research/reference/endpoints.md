# app-market-opportunity-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**19 endpoints across 4 platform group(s).**

## Datasets (3)

### `datasets_apps_charts_search`

- **HTTP:** `GET /datasets/apps-charts/search`
- **What:** Search the app-charts dataset. Searches daily top-chart snapshots scraped from the iOS App Store and Google Play, stored in a search index (one document per chart × snapshot × rank). With no `date` the latest snapshot is returned (today's chart); pair `app_id` with `sort=date_desc` for an app's rank over time. Store enum: `ios`, `android`. Chart type enum: `top_free`, `top_paid`, `top_grossing`, `new`. Platform enum (Apple device platforms, ios charts only): `phone`, `pad`, `mac`. Sort enum: `rank`, `rank_desc`, `date_desc`.
- **Params:** `app_id` (string, optional) — Exact app filter — iOS numeric track id or Android package; pair with sort=date_desc for rank history; `category` (string, optional) — Store category/genre filter, max 128 characters; empty for the overall charts; `chart_type` (string, optional) — Chart enum: top_free, top_paid, top_grossing, new; `collection` (string, optional) — Raw store collection id filter (e.g. topgrossingapplications, GROSSING), max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `date` (string, optional) — Snapshot date filter yyyy-MM-dd; defaults to the latest snapshot; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `platform` (string, optional) — Apple device-platform filter, iOS charts only; see platform enum above; `q` (string, optional) — Full-text query over chart-entry title and developer, max 256 characters; `sort` (string, optional) — Sort enum: rank, rank_desc, date_desc; `store` (string, optional) — Store enum: ios, android

### `datasets_apps_reviews_search`

- **HTTP:** `GET /datasets/apps-reviews/search`
- **What:** Search the app-reviews dataset. Searches user reviews scraped from the iOS App Store and Google Play, stored in a search index (one document per review). Store enum: `ios`, `android`. Sort enum: `recent`, `score_desc`, `score_asc`, `helpful_desc`.
- **Params:** `app_id` (string, optional) — Exact app filter — iOS numeric track id or Android package, max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `min_score` (integer, optional) — Minimum star rating, 1 through 5; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over review text, title and author, max 256 characters; `sort` (string, optional) — Sort enum: recent, score_desc, score_asc, helpful_desc; `store` (string, optional) — Store enum: ios, android

### `datasets_apps_search`

- **HTTP:** `GET /datasets/apps/search`
- **What:** Search the apps-intelligence dataset. Searches resolved iOS App Store and Google Play apps stored in a search index. Store enum: `ios`, `android`, `both`. Platform enum (Apple device platforms, ios records only): `phone`, `pad`, `mac`, `tv`, `watch`, `vision`. Sort enum: `relevance`, `rating_desc`, `reviews_desc`, `installs_desc`, `updated_at_desc`, `popularity_desc`.
- **Params:** `category` (string, optional) — Exact app-store category filter, max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `developer` (string, optional) — Exact developer/publisher name filter, max 128 characters; `free` (boolean, optional) — Filter by price; true keeps only free apps, false only paid; `min_rating` (number, optional) — Minimum store rating, 0 through 5; `min_reviews` (integer, optional) — Minimum ratings/review count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `platforms` (array, optional) — Repeatable Apple device-platform filter (OR); see platform enum above; `q` (string, optional) — Full-text query over title, developer and category, max 256 characters; `sort` (string, optional) — Sort enum: relevance, rating_desc, reviews_desc, installs_desc, updated_at_desc, popularity_desc; `store` (string, optional) — Store enum: ios, android, both

## AppStore (6)

### `appstore_app`

- **HTTP:** `GET /appstore/app`
- **What:** Retrieve full App Store app details. Returns normalized app metadata from the App Store lookup API. Provide either `id` (numeric track ID) or `app_id` (bundle ID). `id`/`app_id` can identify an iPhone, iPad, or Mac App Store listing.
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag; `platforms` (boolean, optional) — Include the full device-platform compatibility list (adds one extra upstream fetch); `ratings` (boolean, optional) — Include ratings histogram

### `appstore_list`

- **HTTP:** `GET /appstore/list`
- **What:** Retrieve App Store collection rankings. Returns ranked App Store apps from an iTunes RSS collection, optionally expanded to full lookup details. `collection` enum: `topfreeapplications`, `toppaidapplications`, `topgrossingapplications`, `topfreeipadapplications`, `toppaidipadapplications`, `topgrossingipadapplications`, `topmacapps`, `topfreemacapps`, `topgrossingmacapps`, `toppaidmacapps`, `newapplications`, `newfreeapplications`, `newpaidapplications`. Of the Mac collections, only `topfreemacapps` currently returns ranked apps — `topmacapps`, `topgrossingmacapps`, and `toppaidmacapps` are accepted but Apple's feed for them is currently empty. There is no separate Games `collection` — combine any collection with `category=6014` (or a Games subgenre ID, e.g. `7012` for Puzzle) to get its Games-only equivalent, e.g. Top Free Games. See the endpoint markdown for the full category ID table.
- **Params:** `category` (integer, optional) — Numeric App Store category ID, see description for the full enum; e.g. 6014 = Games, 7012 = Games/Puzzle; `collection` (string, optional) — Chart collection slug, see description for the full enum; `country` (string, optional) — Two-letter storefront country code; `full_detail` (boolean, optional) — Expand each app via lookup API; `lang` (string, optional) — Result language tag; `num` (integer, optional) — Number of apps to return

### `appstore_reviews`

- **HTTP:** `GET /appstore/reviews`
- **What:** Retrieve App Store reviews. Returns one page of customer reviews for an app. Provide either `id` (numeric track ID) or `app_id` (bundle ID).
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag; `page` (integer, optional) — Review page number (1-10); `sort` (string, optional) — Sort order

### `appstore_search`

- **HTTP:** `GET /appstore/search`
- **What:** Search the App Store. Returns App Store search results for a term. Set `ids_only=true` to return only app IDs. `platform` enum: `phone`, `pad`, `mac`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `ids_only` (boolean, optional) — Return only app IDs; `lang` (string, optional) — Result language tag; `num` (integer, optional) — Number of apps per page; `page` (integer, optional) — Search page number (1-based); `platform` (string, optional) — App Store catalog to search: phone, pad, mac; `term` (string, **required**) — Search term

### `appstore_similar`

- **HTTP:** `GET /appstore/similar`
- **What:** Retrieve "You Might Also Like" apps. Returns the related apps shown on the App Store product page. Provide either `id` (numeric track ID) or `app_id` (bundle ID).
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

### `appstore_version_history`

- **HTTP:** `GET /appstore/version-history/{id}`
- **What:** Retrieve App Store version history. Returns the version history entries shown in the App Store "What's New" section.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

## GooglePlay (6)

### `googleplay_app`

- **HTTP:** `GET /googleplay/app`
- **What:** Retrieve full Google Play app details. Returns normalized app metadata from a Google Play details page, including installs, ratings, pricing, version info, developer metadata, media assets, release state, selected user comments, and "More by this developer" and "Similar apps" recommendation rails. For a per-device (phone/tablet/Chromebook) ratings-and-reviews breakdown, see `/googleplay/ratings`. Defaults: `country=us`, `lang=en`.
- **Params:** `app_id` (string, **required**) — Google Play package name; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code

### `googleplay_categories`

- **HTTP:** `GET /googleplay/categories`
- **What:** Retrieve Google Play app categories. Returns category ids found in the Google Play apps navigation.
- **Params:** `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code

### `googleplay_list`

- **HTTP:** `GET /googleplay/list`
- **What:** Retrieve apps from a Google Play top collection. Returns apps from a Google Play collection and category.
- **Params:** `age` (string, optional) — Family age range; `category` (string, optional) — Category id; `collection` (string, optional) — Collection: TOP_FREE, TOP_PAID, GROSSING, NEW_FREE, NEW_PAID; `country` (string, optional) — Two-letter country code; `device` (string, optional) — Google Play device tab: phone, tablet, tv, chromebook, watch, xr, car; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_reviews`

- **HTTP:** `GET /googleplay/reviews`
- **What:** Retrieve Google Play reviews. Returns one or more pages of app reviews. Set `paginate=true` to fetch only the requested page.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `next_pagination_token` (string, optional) — Token from a previous response; `num` (integer, optional) — Number of reviews; `paginate` (boolean, optional) — Only fetch the requested page; `sort` (string, optional) — Sort: helpfulness, newest, rating

### `googleplay_search`

- **HTTP:** `GET /googleplay/search`
- **What:** Search Google Play. Returns Google Play search results for a term.
- **Params:** `country` (string, optional) — Two-letter country code; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps; `price` (string, optional) — Price filter: all, free, paid; `term` (string, **required**) — Search term

### `googleplay_similar`

- **HTTP:** `GET /googleplay/similar`
- **What:** Retrieve similar Google Play apps. Returns apps from the "Similar apps" cluster on an app details page.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

## Google (4)

### `google_trends_categories`

- **HTTP:** `GET /google/trends/categories`
- **What:** Google Trends categories. Returns supported top-level Google Trends category ids and labels for Trending Now category filters.
- **Params:** _none_

### `google_trends_enums`

- **HTTP:** `GET /google/trends/enums`
- **What:** Google Trends enum metadata. Returns supported Google Trends enum values for explore/trending filters, including locations, date ranges, search types, categories, statuses, and sort modes.
- **Params:** _none_

### `google_trends_explore_interest_over_time`

- **HTTP:** `POST /google/trends/explore/interest-over-time`
- **What:** Google Trends interest over time. Returns only the interest-over-time timeline from the Google Trends Explore widget flow. Supports multiple comparison terms.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_locations`

- **HTTP:** `GET /google/trends/locations`
- **What:** Google Trends locations. Returns supported Google Trends location codes. Explore endpoints also accept WORLDWIDE.
- **Params:** _none_
