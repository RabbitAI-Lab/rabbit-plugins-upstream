# serp-keyword-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**36 endpoints across 5 platform group(s).**

## Google (15)

### `google_news`

- **HTTP:** `GET /google/news`
- **What:** Search Google News. Returns current Google News search results using anonymous HTTP requests with fresh proxy profiles, without browser rendering. Pages slice the finite result snapshot; they do not traverse the Google Search index. Results include title, source, publisher article URL, age, and thumbnail when available. Valid no-results searches and exhausted pages return an empty array. Locale defaults to country=us and lang=en. Returns 503 for blocked or malformed upstream responses.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `page` (integer, optional) — 1-based page within the current finite result snapshot; defaults to 1; `q` (string, **required**) — Search query

### `google_news_search`

- **HTTP:** `POST /google/news`
- **What:** Search Google News with JSON. Restored JSON compatibility endpoint. Returns current Google News articles using anonymous HTTP requests with fresh proxy profiles, without browser rendering. Pages slice the finite current result snapshot. Uses the legacy result array and field names; no-results searches and exhausted pages return an empty result array.
- **Params:** `searchOption` (object, **required**) — Search options; keyword, language and country are required. limit defaults to 10 and is clamped to 10..100; page defaults to 1.
- **REST body:** Send the value of the MCP argument `searchOption` directly as the JSON body; do not wrap it in a `searchOption` property.

### `google_suggest`

- **HTTP:** `GET /google/suggest`
- **What:** Suggest Google search queries. Returns Google autosuggest query completions from the public unauthenticated suggest JSON endpoint.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Google result country; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `q` (string, **required**) — Search query prefix

### `google_trends_categories`

- **HTTP:** `GET /google/trends/categories`
- **What:** Google Trends categories. Returns supported top-level Google Trends category ids and labels for Trending Now category filters.
- **Params:** _none_

### `google_trends_enums`

- **HTTP:** `GET /google/trends/enums`
- **What:** Google Trends enum metadata. Returns supported Google Trends enum values for explore/trending filters, including locations, date ranges, search types, categories, statuses, and sort modes.
- **Params:** _none_

### `google_trends_explore`

- **HTTP:** `POST /google/trends/explore`
- **What:** Google Trends explore data. Returns normalized Google Trends keyword analytics from internal Trends widget requests: interest over time, interest by region, related queries, and related topics when available.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_explore_interest_by_region`

- **HTTP:** `POST /google/trends/explore/interest-by-region`
- **What:** Google Trends interest by region. Returns only the interest-by-region widget from the Google Trends Explore widget flow. Supports multiple comparison terms and returns an empty interest_by_region array when Google returns no rows.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_explore_interest_over_time`

- **HTTP:** `POST /google/trends/explore/interest-over-time`
- **What:** Google Trends interest over time. Returns only the interest-over-time timeline from the Google Trends Explore widget flow. Supports multiple comparison terms.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_explore_related_topics`

- **HTTP:** `POST /google/trends/explore/related-topics`
- **What:** Google Trends related topics. Returns only the related topics widget from the Google Trends Explore widget flow. Returns an empty related_topics array when Google returns no topic rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_explore_rising_queries`

- **HTTP:** `POST /google/trends/explore/rising-queries`
- **What:** Google Trends explore rising queries. Returns the Rising related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_explore_top_queries`

- **HTTP:** `POST /google/trends/explore/top-queries`
- **What:** Google Trends explore top queries. Returns the Top related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_trends_locations`

- **HTTP:** `GET /google/trends/locations`
- **What:** Google Trends locations. Returns supported Google Trends location codes. Explore endpoints also accept WORLDWIDE.
- **Params:** _none_

### `google_trends_trending`

- **HTTP:** `GET /google/trends/trending`
- **What:** Google Trends trending now data. Returns normalized Google Trends Trending Now rows from the internal TrendsUi batch RPC replay.
- **Params:** `category` (integer, optional) — Trending category id; `geo` (string, optional) — Country/territory location code; `hl` (string, optional) — Google Trends UI locale; `limit` (integer, optional) — Maximum rows to return; `sort_by` (string, optional) — Sort mode; `status` (string, optional) — Trend status filter; `time_range` (string, optional) — Alias for window; `tz` (integer, optional) — Timezone offset minutes; `window` (string, optional) — Trend window

### `google_trends_trending_detail`

- **HTTP:** `POST /google/trends/trending/detail`
- **What:** Google Trends trending term detail. Returns the Explore detail widgets for a single trending term, including interest over time, regional interest, top/rising related queries, and related topics when Google returns them.
- **Params:** `request` (object, **required**) — Trending detail request
- **REST body:** Send the value of the MCP argument `request` directly as the JSON body; do not wrap it in a `request` property.

### `google_videos`

- **HTTP:** `GET /google/videos`
- **What:** Search Google video results. Returns normalized Google video vertical results (title, platform, link, duration, age) parsed from the public Google video results page. Locale defaults to country=us and lang=en. Returns 503 when Google serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Bing (5)

### `bing_images`

- **HTTP:** `GET /bing/images`
- **What:** Search Bing image results. Returns normalized Bing image search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing image HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_news`

- **HTTP:** `GET /bing/news`
- **What:** Search Bing news results. Returns normalized Bing news search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing news HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_search`

- **HTTP:** `GET /bing/search`
- **What:** Search Bing web results. Returns normalized Bing web search results for a query string, including organic results, optional context panel data, related queries, people-also-ask questions, news modules, video modules, and page-based pagination. Empty optional blocks are omitted from the JSON response. Locale defaults to country=us and lang=en-us. Results are fetched with a Chrome-impersonated request client and return 503 on a genuine transport failure or challenge page. Bing occasionally serves a well-formed page whose results share no significant term with the query; when every hedged attempt hits this, the response is still returned as 200 with data.low_confidence set to true (and the X-Low-Confidence header) instead of being withheld, so callers get Bing's real answer plus an honest signal to double-check it rather than nothing. Queries that use the site: operator (for example site:gov.hu) are not supported: Bing serves a bot-verification challenge for them, so they are rejected with 400 before any request is made. Use the DuckDuckGo (/api/v1/duckduckgo/search), Brave (/api/v1/brave/search), or Yahoo (/api/v1/yahoo-search/search) search endpoints for domain-restricted searches instead.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_suggest`

- **HTTP:** `GET /bing/suggest`
- **What:** Suggest Bing search queries. Returns Bing autosuggest query completions for a query prefix. Locale defaults to country=us and lang=en-us. Suggestions are fetched from public Bing suggest endpoints and trimmed to the requested count.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `q` (string, **required**) — Search query prefix

### `bing_videos`

- **HTTP:** `GET /bing/videos`
- **What:** Search Bing video results. Returns normalized Bing video search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing video HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Brave (5)

### `brave_images`

- **HTTP:** `GET /brave/images`
- **What:** Search Brave image results. Returns normalized Brave image search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search image HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query

### `brave_news`

- **HTTP:** `GET /brave/news`
- **What:** Search Brave news results. Returns normalized Brave news search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search news HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

### `brave_search`

- **HTTP:** `GET /brave/search`
- **What:** Search Brave. Returns normalized web search results from Brave Search for a query string, along with offset-based pagination, related queries, discussions, videos, and the right-side knowledge card when Brave includes one. Use time_range for preset ranges or date_from/date_to for a custom YYYY-MM-DD range. Locale defaults to country=us and lang=en-us.
- **Params:** `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

### `brave_suggest`

- **HTTP:** `GET /brave/suggest`
- **What:** Suggest Brave search queries. Returns Brave autosuggest query completions for a query prefix. Locale defaults to country=us and lang=en-us. Suggestions are fetched from public Brave Search suggest JSON and trimmed to the requested count.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Brave result country; defaults to us; `lang` (string, optional) — Brave UI language; defaults to en-us; `q` (string, **required**) — Search query prefix

### `brave_videos`

- **HTTP:** `GET /brave/videos`
- **What:** Search Brave video results. Returns normalized Brave video search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search video HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

## DuckDuckGo Search (5)

### `duckduckgo_image`

- **HTTP:** `GET /duckduckgo/image`
- **What:** Search DuckDuckGo image results. Returns normalized DuckDuckGo image results for a query string: title, source page URL, image URL, thumbnail, dimensions, and hostname, plus page-based pagination. Results are fetched from DuckDuckGo's own image JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

### `duckduckgo_news`

- **HTTP:** `GET /duckduckgo/news`
- **What:** Search DuckDuckGo news results. Returns normalized DuckDuckGo news results for a query string: title, destination URL, source, excerpt, thumbnail, and relative/published time, plus page-based pagination. Results are fetched from DuckDuckGo's own news JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

### `duckduckgo_search`

- **HTTP:** `GET /duckduckgo/search`
- **What:** Search DuckDuckGo web results. Returns normalized DuckDuckGo web search results for a query string: title, destination URL, description, and hostname, plus page-based pagination. DuckDuckGo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link. Results are fetched from DuckDuckGo's own server-rendered search page.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default); `safe_search` (string, optional) — Safe search level, defaults to DuckDuckGo's own moderate setting when omitted; `time_range` (string, optional) — Restrict results to a recency window

### `duckduckgo_shopping`

- **HTTP:** `GET /duckduckgo/shopping`
- **What:** Search DuckDuckGo shopping results. Returns normalized DuckDuckGo shopping results for a query string: title, brand, merchant, description, price, rating, and review count, plus total page count. DuckDuckGo's shopping vertical is ad-funded, syndicated product listings, not organic content; every product link is wrapped in an ad-click-tracking redirect with no clean destination to unwrap, so no destination URL is returned. DuckDuckGo's own pagination token for this vertical is an opaque per-response blob rather than a plain page offset, so only the first page is supported.
- **Params:** `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo market code, e.g. us-en, uk-en

### `duckduckgo_video`

- **HTTP:** `GET /duckduckgo/video`
- **What:** Search DuckDuckGo video results. Returns normalized DuckDuckGo video results for a query string: title, destination URL, description, duration, thumbnail, publisher/uploader, published time, and view count, plus page-based pagination. Results are fetched from DuckDuckGo's own video JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

## Yahoo Search (6)

### `yahoo_search`

- **HTTP:** `GET /yahoo-search/search`
- **What:** Search Yahoo web results. Returns normalized Yahoo web search results for a query string: title, destination URL, description, and hostname, plus page-based pagination. Yahoo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link. Results are fetched from Yahoo's own server-rendered search page.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `time_range` (string, optional) — Restrict results by recency. Omit for unfiltered ('Anytime').

### `yahoo_search_images`

- **HTTP:** `GET /yahoo-search/images`
- **What:** Search Yahoo image results. Returns Yahoo's image-search results for a query: title, direct image URL, the page hosting the image, source domain, thumbnail, and original image dimensions when available. Results are fetched from Yahoo's own server-rendered image-search page.
- **Params:** `q` (string, **required**) — Search query

### `yahoo_search_local`

- **HTTP:** `GET /yahoo-search/local`
- **What:** Search Yahoo local business results. Returns Yahoo's local-business-search results for a query: name, category, price range, address, phone, open status, rating, and review count. Location is resolved from the query text itself, the same way a user would type into Yahoo's own local search box (e.g. "pizza near seattle wa"), not a separate coordinate parameter. Results are fetched from Yahoo's own server-rendered local-search page.
- **Params:** `q` (string, **required**) — Search query, including any location intent

### `yahoo_search_news`

- **HTTP:** `GET /yahoo-search/news`
- **What:** Search Yahoo news results. Returns Yahoo's news-search results for a query: title, destination URL, description, source, and relative publish age. Results are fetched from Yahoo's own server-rendered news-search page (news.search.yahoo.com) -- a distinct product from the yahoo-news family, which covers the www.yahoo.com/news portal itself. Yahoo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link.
- **Params:** `q` (string, **required**) — Search query

### `yahoo_search_suggest`

- **HTTP:** `GET /yahoo-search/suggest`
- **What:** Yahoo web search autocomplete suggestions. Returns Yahoo's own search-box autocomplete suggestions for a partial query: a flat list of suggested search terms, each optionally carrying knowledge-panel entity metadata (type, image, subtitle, description) when Yahoo resolves the term to a known company, place, product, or similar entity rather than a plain phrase.
- **Params:** `count` (integer, optional) — Number of suggestions to return, default 10, clamped to 1..20; `q` (string, **required**) — Partial search query to autocomplete

### `yahoo_search_videos`

- **HTTP:** `GET /yahoo-search/videos`
- **What:** Search Yahoo video results. Returns Yahoo's video-search results for a query: title, destination page URL, source domain, description, thumbnail, and duration. Results are fetched from Yahoo's own server-rendered video-search page.
- **Params:** `q` (string, **required**) — Search query
