# tiktok-trend-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**11 endpoints across 1 platform group(s).**

## TikTok (11)

### `tiktok_category`

- **HTTP:** `GET /tiktok/category`
- **What:** List TikTok explore categories. Returns the category list exposed by the TikTok Explore page.
- **Params:** _none_

### `tiktok_challenge`

- **HTTP:** `GET /tiktok/hashtag/{name}`
- **What:** Retrieve TikTok hashtag details. Returns the metadata payload for a TikTok hashtag page.
- **Params:** `name` (string, **required**) — Hashtag name (e.g., 'christmas')

### `tiktok_challenge_list`

- **HTTP:** `GET /tiktok/hashtags`
- **What:** Retrieve TikTok hashtag posts. Returns the videos listed for a TikTok hashtag id with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `id` (string, **required**) — Hashtag id returned by the hashtag detail endpoint

### `tiktok_creative_center_hashtags`

- **HTTP:** `GET /tiktok/creative-center/hashtags`
- **What:** Retrieve TikTok Creative Center trending hashtags. Returns TikTok Creative Center's ranked trending hashtags for a country and period. TikTok gates this endpoint's full result set behind a logged-in TikTok One account: an anonymous request always receives at most 3 hashtags regardless of country or period.
- **Params:** `country_code` (string, **required**) — ISO-2 country code; `period` (integer, optional) — Lookback window in days

### `tiktok_creative_center_videos`

- **HTTP:** `GET /tiktok/creative-center/videos`
- **What:** Retrieve TikTok Creative Center trending videos. Returns TikTok Creative Center's ranked trending videos for a country, period, and sort order. TikTok reports the true result-set size (see total_count/page_count in the response) but gates access to it behind a logged-in TikTok One account: an anonymous request always receives page 1 (4 videos) regardless of sort order or period. Country coverage is uneven: US, JP, ID, VN, and TH reliably return populated results; other countries have been observed to return an empty videos array (a genuine no-data response, not an error).
- **Params:** `content_label_id` (string, optional) — Content tag id to filter by; `country_code` (string, **required**) — ISO-2 country code; `organic_only` (boolean, optional) — Restrict to organic (non-paid) videos only; `period` (integer, optional) — Lookback window in days; `sort_by` (string, optional) — Sort order

### `tiktok_explore`

- **HTTP:** `GET /tiktok/explore/{id}`
- **What:** Retrieve the TikTok explore feed for a category. Returns explore videos for a TikTok category id from the category endpoint.
- **Params:** `id` (integer, **required**) — Category type id returned by the category endpoint

### `tiktok_popular_trend_country_industry_meta`

- **HTTP:** `GET /tiktok/popular-trend/country-industry-meta`
- **What:** Retrieve TikTok popular-trend country and industry metadata. Returns the country and industry metadata used by the TikTok Creative Center popular-trend endpoints.
- **Params:** _none_

### `tiktok_post`

- **HTTP:** `GET /tiktok/post/{id}`
- **What:** Retrieve TikTok video details. Returns the TikTok video detail payload for a video id.
- **Params:** `id` (string, **required**) — TikTok video id

### `tiktok_search`

- **HTTP:** `GET /tiktok/search`
- **What:** Search TikTok videos. Searches TikTok videos by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_search_hashtag`

- **HTTP:** `GET /tiktok/search/hashtag`
- **What:** Search TikTok hashtags. Searches TikTok hashtags/challenges by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_trending`

- **HTTP:** `GET /tiktok/trending`
- **What:** Retrieve TikTok trending posts. Returns the current TikTok trending feed.
- **Params:** _none_
