# serp-keyword-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**56 endpoints across 6 platform group(s).**

## Google (40)

### `google_finance_analyst_articles`

- **HTTP:** `GET /google/finance/analyst-articles/{quote}`
- **What:** Google Finance analyst articles. Returns normalized analyst article results for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_chart`

- **HTTP:** `GET /google/finance/chart/{quote}`
- **What:** Google Finance chart data. Returns normalized chart points for a quote and window.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ; `window` (string, optional) — Window: 1d, 5d, 1m, 6m, ytd, 1y, 5y, max

### `google_finance_classification`

- **HTTP:** `GET /google/finance/classification/{quote}`
- **What:** Google Finance classification data. Returns normalized classification strings for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_company`

- **HTTP:** `GET /google/finance/company/{quote}`
- **What:** Google Finance company data. Returns normalized company information from Google Finance.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_context`

- **HTTP:** `GET /google/finance/context`
- **What:** Google Finance context search. Returns normalized Google Finance context search results.
- **Params:** `q` (string, **required**) — Search query

### `google_finance_financials`

- **HTTP:** `GET /google/finance/financials/{quote}`
- **What:** Google Finance financial statements. Returns normalized annual and quarterly financial rows when Google Finance has statement data for the quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_markets_category_news`

- **HTTP:** `GET /google/finance/markets/categories/{category}/news`
- **What:** Google Finance category news. Returns normalized news for a Google Finance category.
- **Params:** `category` (string, **required**) — Google Finance category id; `offset` (integer, optional) — Result offset

### `google_finance_markets_category_stocks`

- **HTTP:** `GET /google/finance/markets/categories/{category}/stocks`
- **What:** Google Finance category stocks. Returns normalized instruments for a Google Finance category.
- **Params:** `category` (string, **required**) — Google Finance category id; `offset` (integer, optional) — Result offset

### `google_finance_markets_earnings`

- **HTTP:** `GET /google/finance/markets/earnings`
- **What:** Google Finance earnings calendar. Returns normalized earnings calendar instruments.
- **Params:** _none_

### `google_finance_markets_featured`

- **HTTP:** `GET /google/finance/markets/featured`
- **What:** Google Finance featured stocks. Returns normalized featured instruments.
- **Params:** _none_

### `google_finance_markets_headline`

- **HTTP:** `GET /google/finance/markets/headline`
- **What:** Google Finance top headline. Returns the top Google Finance headline.
- **Params:** _none_

### `google_finance_markets_indices`

- **HTTP:** `GET /google/finance/markets/indices`
- **What:** Google Finance market indices. Returns normalized market index instruments.
- **Params:** _none_

### `google_finance_markets_movers`

- **HTTP:** `GET /google/finance/markets/movers`
- **What:** Google Finance market movers. Returns normalized market mover instruments.
- **Params:** `categories` (string, optional) — Comma-separated numeric categories; `count` (integer, optional) — Result count; `offset` (integer, optional) — Result offset

### `google_finance_markets_top`

- **HTTP:** `GET /google/finance/markets/top`
- **What:** Google Finance top stocks by metric. Returns normalized top instruments for a Google Finance metric.
- **Params:** `metric` (integer, optional) — Google Finance metric id; `page` (integer, optional) — Page number

### `google_finance_markets_trending`

- **HTTP:** `GET /google/finance/markets/trending`
- **What:** Google Finance trending stocks. Returns normalized trending instruments.
- **Params:** `limit` (integer, optional) — Result limit

### `google_finance_news`

- **HTTP:** `GET /google/finance/news/{quote}`
- **What:** Google Finance quote news. Returns normalized news articles for a quote.
- **Params:** `limit` (integer, optional) — Article limit; `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_quote`

- **HTTP:** `GET /google/finance/quote/{quote}`
- **What:** Google Finance Quote API. Fetches the latest quote data for a provided stock symbol from Google Finance https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en.
- **Params:** `quote` (string, **required**) — Stock symbol to fetch the latest quote for (e.g., AAPL:NASDAQ, BTC-USD)

### `google_finance_related`

- **HTTP:** `GET /google/finance/related/{quote}`
- **What:** Google Finance related instruments. Returns normalized related instruments for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_search`

- **HTTP:** `GET /google/finance/search`
- **What:** Google Finance Search API. Fetches normalized search results for a provided keyword from Google Finance.
- **Params:** `q` (string, **required**) — Keyword to search for (e.g., Apple)

### `google_finance_ticker`

- **HTTP:** `GET /google/finance/ticker/{ticker}`
- **What:** Google Finance Ticker API. Fetches chart ticker data from Google Finance based on a provided ticker and window period.
- **Params:** `ticker` (string, **required**) — Ticker symbol to fetch data for example:AAPL:NASDAQ, BTC-USD; `window` (string, optional) — Time window for the ticker data (default: 1d), options: 1d, 5d, 1m, 6m, 1y, 5y, max

### `google_jobs`

- **HTTP:** `POST /google/jobs`
- **What:** Search Google Jobs. Returns normalized Google Jobs results parsed from public Google web responses.
- **Params:** `option` (object, **required**) — Google Jobs search payload

### `google_map_place`

- **HTTP:** `GET /google/map/place/{place_id}`
- **What:** Google Maps place details API. Returns detailed information for a specified place_id. Rate limit is enforced at 1 request per second.
- **Params:** `place_id` (string, **required**) — Google Place ID

### `google_map_place_photos`

- **HTTP:** `GET /google/map/place/{place_id}/photos`
- **What:** Google Maps place photos API. Returns the photos Google publishes for a specified place_id — the imagery shown on the place's Google Maps page, typically dozens of images for a well-covered business. Each entry carries the image URL as served plus its pixel dimensions when reported; swap the trailing size suffix on the URL (e.g. `=w203-h100-k-no`) to request other dimensions. Contributor avatars and review-attached photos are excluded. This is the place page's image set, not a paginated archive feed. Rate limit is enforced at 1 request per second.
- **Params:** `limit` (integer, optional) — Maximum number of photos to return. Omit or 0 for all captured.; `place_id` (string, **required**) — Google Place ID

### `google_map_place_reviews`

- **HTTP:** `GET /google/map/place/{place_id}/reviews`
- **What:** Google Maps place reviews API. Returns the reviews Google shows on a specified place_id's Google Maps page — typically the 8 most relevant, each with its rating, text, reviewer, timestamp, and any photos the reviewer attached. Photo-only reviews return an empty `text`. This is the place page's first page of reviews, not the full review archive. Rate limit is enforced at 1 request per second.
- **Params:** `limit` (integer, optional) — Maximum number of reviews to return. Omit or 0 for all captured.; `place_id` (string, **required**) — Google Place ID

### `google_map_search`

- **HTTP:** `POST /google/map/search`
- **What:** Google Maps search API. Returns results from Google Maps based on search options. Rate limit is enforced at 1 request per second.
- **Params:** `mapSearchOption` (object, **required**) — Search options

### `google_news`

- **HTTP:** `GET /google/news`
- **What:** Search Google News. Returns normalized Google News vertical results (title, source, link, age) parsed from the public Google News results page. Locale defaults to country=us and lang=en. Returns 503 when Google serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `google_search`

- **HTTP:** `POST /google/search`
- **What:** Google search API. Returns normalized Google web search results. Results are fetched through proxied browser renderers that race several concurrent renders per request and return the first clean result, with stale-cache fallback when available. The endpoint returns 503 when Google serves a challenge page or unusable HTML. Rate limit is enforced at 1 request per second, and if the limit is exceeded a 429 status code is returned with rate limit headers.
- **Params:** `searchOption` (object, **required**) — Search options

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

### `google_trends_explore_interest_by_region`

- **HTTP:** `POST /google/trends/explore/interest-by-region`
- **What:** Google Trends interest by region. Returns only the interest-by-region widget from the Google Trends Explore widget flow. Supports multiple comparison terms and returns an empty interest_by_region array when Google returns no rows.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_interest_over_time`

- **HTTP:** `POST /google/trends/explore/interest-over-time`
- **What:** Google Trends interest over time. Returns only the interest-over-time timeline from the Google Trends Explore widget flow. Supports multiple comparison terms.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_related_topics`

- **HTTP:** `POST /google/trends/explore/related-topics`
- **What:** Google Trends related topics. Returns only the related topics widget from the Google Trends Explore widget flow. Returns an empty related_topics array when Google returns no topic rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_rising_queries`

- **HTTP:** `POST /google/trends/explore/rising-queries`
- **What:** Google Trends explore rising queries. Returns the Rising related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_top_queries`

- **HTTP:** `POST /google/trends/explore/top-queries`
- **What:** Google Trends explore top queries. Returns the Top related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

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
- **What:** Search Bing web results. Returns normalized Bing web search results for a query string, including organic results, optional context panel data, related queries, people-also-ask questions, news modules, video modules, and page-based pagination. Empty optional blocks are omitted from the JSON response. Locale defaults to country=us and lang=en-us. Results are fetched with a Chrome-impersonated request client and return 503 when Bing serves a challenge page, unusable HTML, or a response whose results are unrelated to the query. Queries that use the site: operator (for example site:gov.hu) are not supported: Bing serves a bot-verification challenge for them, so they are rejected with 400 before any request is made. Use the Google search endpoint (/api/v1/google/search) for domain-restricted searches.
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

## Yahoo Search (1)

### `yahoo_search`

- **HTTP:** `GET /yahoo-search/search`
- **What:** Search Yahoo web results. Returns normalized Yahoo web search results for a query string: title, destination URL, description, and hostname, plus page-based pagination. Yahoo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link. Results are fetched from Yahoo's own server-rendered search page.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query
