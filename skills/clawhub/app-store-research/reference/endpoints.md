# app-store-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**35 endpoints across 3 platform group(s).**

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

## ChromeWebStore (12)

### `chromewebstore_categories`

- **HTTP:** `GET /chromewebstore/categories`
- **What:** List Chrome Web Store categories and collections. Returns the reference taxonomy for the list endpoints: extension category groups and their subcategory slugs, the top-chart identifiers, and known curated collection slugs.
- **Params:** _none_

### `chromewebstore_category`

- **HTTP:** `GET /chromewebstore/category`
- **What:** List items in a Chrome Web Store category. Returns the item cards listed under an extensions category slug (e.g. `productivity/tools`, `lifestyle/shopping`, `make_chrome_yours/privacy`). Use /chromewebstore/categories for the reference taxonomy. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `category` (string, **required**) — Category slug under extensions; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_charts`

- **HTTP:** `GET /chromewebstore/charts`
- **What:** List a Chrome Web Store top chart. Returns the item cards in a store top chart. `chart` accepts `trending`, `popular`, or `notable`. Defaults: `chart=popular`, `num=50`, `country=us`, `lang=en`.
- **Params:** `chart` (string, optional) — Top chart to list; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_collection`

- **HTTP:** `GET /chromewebstore/collection`
- **What:** List items in a curated Chrome Web Store collection. Returns the item cards in a curated store collection slug (e.g. `editors_picks_extensions`, `dark_mode`, `ai_productivity`). Use /chromewebstore/categories for known collection slugs. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `collection` (string, **required**) — Curated collection slug; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_developer`

- **HTTP:** `GET /chromewebstore/developer`
- **What:** Retrieve a Chrome Web Store publisher and their items. Returns a Chrome Web Store publisher (developer) by publisher id, including the disclosed trader details — legal name, email, phone, address, website, and D-U-N-S number — plus the publisher's listed items ("More from ..."). Trader fields are only present for publishers that identify as EU traders. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store publisher id (u + 32 hex chars); `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_item`

- **HTTP:** `GET /chromewebstore/item`
- **What:** Retrieve Chrome Web Store item details. Returns normalized detail for a Chrome Web Store extension or theme, including name, rating, rating count, user count, version, last-updated date, size, supported languages, developer, category, screenshots, and privacy links. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_permissions`

- **HTTP:** `GET /chromewebstore/permissions`
- **What:** Retrieve a Chrome Web Store item's declared permissions. Returns the permissions a Chrome Web Store extension declares in its manifest: `permissions`, `optional_permissions`, `host_permissions`, `optional_host_permissions`, plus `manifest_version` and `min_browser_version`. Useful for security and supply-chain review. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_privacy`

- **HTTP:** `GET /chromewebstore/privacy`
- **What:** Retrieve a Chrome Web Store item's privacy disclosures. Returns an extension's privacy disclosures as the store renders them: the developer's data-use statement, whether it collects data, the standard data-handling declarations, and the privacy-policy link. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_reviews`

- **HTTP:** `GET /chromewebstore/reviews`
- **What:** Retrieve Chrome Web Store item reviews. Returns the reviews the store renders on an item's reviews page, each with author, star rating, text, posted/edited dates and reviewed version. Defaults: `num=20`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of reviews; `sort` (string, optional) — Review sort order

### `chromewebstore_search`

- **HTTP:** `GET /chromewebstore/search`
- **What:** Search Chrome Web Store items. Returns Chrome Web Store search result cards for a keyword, each with id, name, rating, user count, publisher and detail URL. Defaults: `num=30`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of results; `term` (string, **required**) — Search keyword

### `chromewebstore_similar`

- **HTTP:** `GET /chromewebstore/similar`
- **What:** Retrieve related Chrome Web Store items. Returns the related-items shelf the store renders on an item's detail page. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_suggest`

- **HTTP:** `GET /chromewebstore/suggest`
- **What:** Suggest Chrome Web Store search terms. Returns item-name suggestions for a search prefix, drawn from the top store-search results. Defaults: `num=8`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of suggestions; `term` (string, **required**) — Search prefix to autocomplete
