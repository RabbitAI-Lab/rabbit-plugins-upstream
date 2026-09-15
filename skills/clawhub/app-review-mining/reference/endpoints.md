# app-review-mining — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**23 endpoints across 2 platform group(s).**

## AppStore (12)

### `appstore_app`

- **HTTP:** `GET /appstore/app`
- **What:** Retrieve full App Store app details. Returns normalized app metadata from the App Store lookup API. Provide either `id` (numeric track ID) or `app_id` (bundle ID). `id`/`app_id` can identify an iPhone, iPad, or Mac App Store listing.
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag; `platforms` (boolean, optional) — Include the full device-platform compatibility list (adds one extra upstream fetch); `ratings` (boolean, optional) — Include ratings histogram

### `appstore_developer`

- **HTTP:** `GET /appstore/developer/{dev_id}`
- **What:** Retrieve apps by developer ID. Returns App Store apps associated with a specific developer artist ID.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `dev_id` (string, **required**) — Developer artist ID; `lang` (string, optional) — Result language tag

### `appstore_editorial`

- **HTTP:** `GET /appstore/editorial`
- **What:** Retrieve an App Store device or Arcade editorial landing page. Returns the curated editorial shelves from one of Apple's per-device App Store landing pages (the same content shown by apps.apple.com's device switcher). `device` enum: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`. `section` enum: `main` (the device's Today/Discover/Apps & Games landing page), `arcade` (the device's Apple Arcade landing page). Watch has no Arcade page — `device=watch` with `section=arcade` returns `400`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `device` (string, **required**) — Apple device catalog; `lang` (string, optional) — Result language tag; `section` (string, optional) — Editorial section within the device

### `appstore_editorial_category`

- **HTTP:** `GET /appstore/editorial/category`
- **What:** Retrieve an App Store category-scoped editorial page. Returns the curated editorial shelves for one device category page (e.g. "Entertainment Apps for Vision"). `category_id` is a numeric, device-specific editorial page ID — not a static enum — discovered from an `appstore_editorial` response for the SAME `device`, in its "Browse by Category" shelf items' `destination_id` field. `device` enum: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`.
- **Params:** `category_id` (string, **required**) — Numeric App Store editorial page ID, discovered from appstore_editorial (same device); `country` (string, optional) — Two-letter storefront country code; `device` (string, **required**) — Apple device catalog; `lang` (string, optional) — Result language tag

### `appstore_list`

- **HTTP:** `GET /appstore/list`
- **What:** Retrieve App Store collection rankings. Returns ranked App Store apps from an iTunes RSS collection, optionally expanded to full lookup details. `collection` enum: `topfreeapplications`, `toppaidapplications`, `topgrossingapplications`, `topfreeipadapplications`, `toppaidipadapplications`, `topgrossingipadapplications`, `topmacapps`, `topfreemacapps`, `topgrossingmacapps`, `toppaidmacapps`, `newapplications`, `newfreeapplications`, `newpaidapplications`. Of the Mac collections, only `topfreemacapps` currently returns ranked apps — `topmacapps`, `topgrossingmacapps`, and `toppaidmacapps` are accepted but Apple's feed for them is currently empty. There is no separate Games `collection` — combine any collection with `category=6014` (or a Games subgenre ID, e.g. `7012` for Puzzle) to get its Games-only equivalent, e.g. Top Free Games. See the endpoint markdown for the full category ID table.
- **Params:** `category` (integer, optional) — Numeric App Store category ID, see description for the full enum; e.g. 6014 = Games, 7012 = Games/Puzzle; `collection` (string, optional) — Chart collection slug, see description for the full enum; `country` (string, optional) — Two-letter storefront country code; `full_detail` (boolean, optional) — Expand each app via lookup API; `lang` (string, optional) — Result language tag; `num` (integer, optional) — Number of apps to return

### `appstore_privacy`

- **HTTP:** `GET /appstore/privacy/{id}`
- **What:** Retrieve App Store privacy disclosures. Returns the app privacy cards shown on the App Store page, including data categories and purposes.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

### `appstore_ratings`

- **HTTP:** `GET /appstore/ratings`
- **What:** Retrieve App Store ratings histogram. Returns total ratings count and the 1-5 star histogram shown on the App Store product page.
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

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

### `appstore_suggest`

- **HTTP:** `GET /appstore/suggest/{term}`
- **What:** Retrieve App Store search suggestions. Returns suggested search terms for the given partial keyword.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `term` (string, **required**) — Partial search term

### `appstore_version_history`

- **HTTP:** `GET /appstore/version-history/{id}`
- **What:** Retrieve App Store version history. Returns the version history entries shown in the App Store "What's New" section.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

## GooglePlay (11)

### `googleplay_app`

- **HTTP:** `GET /googleplay/app`
- **What:** Retrieve full Google Play app details. Returns normalized app metadata from a Google Play details page, including installs, ratings, pricing, version info, developer metadata, media assets, release state, selected user comments, and "More by this developer" and "Similar apps" recommendation rails. For a per-device (phone/tablet/Chromebook) ratings-and-reviews breakdown, see `/googleplay/ratings`. Defaults: `country=us`, `lang=en`.
- **Params:** `app_id` (string, **required**) — Google Play package name; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code

### `googleplay_categories`

- **HTTP:** `GET /googleplay/categories`
- **What:** Retrieve Google Play app categories. Returns category ids found in the Google Play apps navigation.
- **Params:** `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code

### `googleplay_datasafety`

- **HTTP:** `GET /googleplay/datasafety`
- **What:** Retrieve Google Play data safety details. Returns the data safety information displayed on Google Play.
- **Params:** `app_id` (string, **required**) — Google Play app id; `lang` (string, optional) — Two-letter language code

### `googleplay_developer`

- **HTTP:** `GET /googleplay/developer/{dev_id}`
- **What:** Retrieve apps by Google Play developer. Returns apps published by a developer id or developer name.
- **Params:** `country` (string, optional) — Two-letter country code; `dev_id` (string, **required**) — Developer id or name; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_list`

- **HTTP:** `GET /googleplay/list`
- **What:** Retrieve apps from a Google Play top collection. Returns apps from a Google Play collection and category.
- **Params:** `age` (string, optional) — Family age range; `category` (string, optional) — Category id; `collection` (string, optional) — Collection: TOP_FREE, TOP_PAID, GROSSING, NEW_FREE, NEW_PAID; `country` (string, optional) — Two-letter country code; `device` (string, optional) — Google Play device tab: phone, tablet, tv, chromebook, watch, xr, car; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_permissions`

- **HTTP:** `GET /googleplay/permissions`
- **What:** Retrieve Google Play app permissions. Returns Google Play permission groups or a short permission name list.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `short` (boolean, optional) — Return only permission names

### `googleplay_ratings`

- **HTTP:** `GET /googleplay/ratings`
- **What:** Get Google Play ratings by device. Returns the ratings-and-reviews breakdown Google Play shows under the details page's device tabs, one entry each for phone, tablet, and Chromebook. Defaults: `country=us`, `lang=en`.
- **Params:** `app_id` (string, **required**) — Google Play package name; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code

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

### `googleplay_suggest`

- **HTTP:** `GET /googleplay/suggest/{term}`
- **What:** Retrieve Google Play query suggestions. Returns up to 10 suggestions for a search term.
- **Params:** `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `term` (string, **required**) — Search term prefix
