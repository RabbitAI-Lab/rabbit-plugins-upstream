# prediction-markets-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**62 endpoints across 3 platform group(s).**

## Polymarket (30)

### `polymarket_activity_trades`

- **HTTP:** `GET /polymarket/activity/trades`
- **What:** List Polymarket activity trades. Returns normalized public trade rows used by Polymarket's `/activity` page from credential-free Data API trades JSON. The `taker_only` enum accepts `true` and `false`; the `filter_type` enum accepts `CASH`; the `filter_amount` enum accepts `1`, `5`, `10`, `100`, `1000`, `10000`, and `100000`.
- **Params:** `event_id` (string, optional) — Optional Polymarket event id; `filter_amount` (string, optional) — Minimum filtered amount; `filter_type` (string, optional) — Activity amount filter type; `limit` (integer, optional) — Maximum trades, defaults to 50 and supports up to 100; `market` (string, optional) — Optional market condition id; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `taker_only` (string, optional) — Taker-only filter

### `polymarket_clob_market`

- **HTTP:** `GET /polymarket/clob/market/{condition_id}`
- **What:** Get Polymarket CLOB market. Returns one public CLOB market detail row by market condition id, including tokens, reward settings, order acceptance state, tags, and fees.
- **Params:** `condition_id` (string, **required**) — Polymarket market condition id

### `polymarket_dashboard_macro`

- **HTTP:** `GET /polymarket/dashboards/macro`
- **What:** List Polymarket macro dashboard events. Returns normalized macroeconomic event rows for Polymarket's `/dashboards/macro` page using credential-free Gamma `events/keyset` JSON with the `macro` tag.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior macro dashboard response; `limit` (integer, optional) — Maximum macro events, defaults to 20 and supports up to 100

### `polymarket_event_detail`

- **HTTP:** `GET /polymarket/event/{slug}`
- **What:** Get Polymarket event detail. Returns one normalized Polymarket event from credential-free public Gamma event JSON. This endpoint does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `slug` (string, **required**) — Polymarket event slug

### `polymarket_event_tags`

- **HTTP:** `GET /polymarket/events/{id}/tags`
- **What:** List tags for a Polymarket event. Returns normalized tag rows attached to one Polymarket event id.
- **Params:** `id` (string, **required**) — Polymarket event id

### `polymarket_events`

- **HTTP:** `GET /polymarket/events`
- **What:** List Polymarket events. Returns normalized event rows from Polymarket's credential-free public Gamma events JSON.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `closed` (string, optional) — Closed filter; `limit` (integer, optional) — Maximum events, defaults to 25 and supports up to 100; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_events_similar`

- **HTTP:** `GET /polymarket/events/similar`
- **What:** Find similar Polymarket events. Returns normalized similar events from Polymarket's credential-free public Gamma events/similar JSON.
- **Params:** `closed` (string, optional) — Closed filter; `event_slug` (string, optional) — Event slug; `event_title` (string, optional) — Event title; `id` (integer, optional) — Polymarket event id; `limit` (integer, optional) — Maximum events, defaults to 10 and supports up to 50; `market_slug` (string, optional) — Market slug; `market_title` (string, optional) — Market title

### `polymarket_homepage_feed`

- **HTTP:** `GET /polymarket/homepage/feed`
- **What:** List Polymarket homepage feed rows. Returns normalized rows for Polymarket homepage feeds discovered from the public web app and backed by credential-free Gamma JSON. The `feed` enum accepts `trending`, `breaking`, `new`, `politics`, `sports`, `crypto`, `esports`, `iran`, `finance`, `geopolitics`, `tech`, `culture`, `economy`, `weather`, `mentions`, and `elections`. Most feeds return events from Gamma `events/keyset`; `breaking` returns high-movement market rows and `mentions` returns open event search matches.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior event feed response; `feed` (string, optional) — Homepage feed; `limit` (integer, optional) — Maximum rows, defaults to 20 and supports up to 100

### `polymarket_leaderboard`

- **HTTP:** `GET /polymarket/leaderboard`
- **What:** List Polymarket leaderboard rows. Returns normalized trader leaderboard rows from Polymarket's credential-free Data API leaderboard JSON. The `window` enum accepts `1d`, `7d`, `30d`, and `all`; the `sort_by` enum accepts `profit` and `volume`.
- **Params:** `limit` (integer, optional) — Maximum rows, defaults to 20 and supports up to 100; `sort_by` (string, optional) — Leaderboard sort; `window` (string, optional) — Leaderboard time window

### `polymarket_market_detail`

- **HTTP:** `GET /polymarket/market/{id}`
- **What:** Get Polymarket market detail by id. Returns one normalized Polymarket market from credential-free public Gamma market JSON. This endpoint does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_market_liquidity`

- **HTTP:** `GET /polymarket/market/{id}/liquidity`
- **What:** Get Polymarket market liquidity. Returns a public market liquidity snapshot that joins Gamma market detail with credential-free public CLOB market-data reads when token ids are available. This endpoint is not a trading endpoint and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_market_tags`

- **HTTP:** `GET /polymarket/market/{id}/tags`
- **What:** List tags for a Polymarket market. Returns normalized tag rows attached to one Polymarket market id.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_markets`

- **HTTP:** `GET /polymarket/markets`
- **What:** List Polymarket markets. Returns normalized market rows from Polymarket's credential-free public Gamma markets JSON.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `closed` (string, optional) — Closed filter; `limit` (integer, optional) — Maximum markets, defaults to 25 and supports up to 100; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_predictions`

- **HTTP:** `GET /polymarket/predictions`
- **What:** List Polymarket predictions. Returns normalized event rows for the Polymarket `/predictions` page using credential-free Gamma `events/keyset` JSON. The `status` enum accepts `active`, `resolved`, and `all`; the `sort` enum accepts `competitive`, `volume`, `volume_24hr`, `ending_soon`, `liquidity`, `newest`, and `closed_time`; the `recurrence` enum accepts `hourly`, `daily`, `weekly`, `monthly`, and `yearly`.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior predictions response; `limit` (integer, optional) — Maximum events, defaults to 20 and supports up to 100; `recurrence` (string, optional) — Optional recurrence filter; `sort` (string, optional) — Prediction sort; `status` (string, optional) — Prediction status; `tag` (string, optional) — Optional tag slug

### `polymarket_public_data`

- **HTTP:** `GET /polymarket/fee-types`
- **What:** Polymarket fee types. Returns public fee type data from Polymarket Gamma. This is a normalized wrapper around credential-free public JSON.
- **Params:** `active` (string, optional) — Optional upstream active filter; `search` (string, optional) — Optional upstream search filter

### `polymarket_related_tags`

- **HTTP:** `GET /polymarket/tag/{id}/related-tags`
- **What:** Get related Polymarket tags by id. Returns normalized related tag rows from Polymarket's credential-free public Gamma related-tags JSON.
- **Params:** `id` (string, **required**) — Polymarket tag id; `locale` (string, optional) — Optional upstream locale; `omit_empty` (string, optional) — Omit empty related tags; `status` (string, optional) — Optional upstream status filter

### `polymarket_rewards_market`

- **HTTP:** `GET /polymarket/rewards/market/{condition_id}`
- **What:** Get Polymarket rewards market. Returns one public rewards-market row from Polymarket CLOB rewards JSON by market condition id.
- **Params:** `condition_id` (string, **required**) — Polymarket market condition id

### `polymarket_rewards_markets`

- **HTTP:** `GET /polymarket/rewards/markets`
- **What:** List Polymarket rewards markets. Returns normalized public rewards-market rows used by Polymarket's `/rewards` page. The `order_by` enum accepts `market`, `earnings`, `max_spread`, `min_size`, `rate_per_day`, `price`, `earning_percentage`, and `spread`; the `position` enum accepts `asc` and `desc`; the `tag_slug` enum accepts `all`, `politics`, `sports`, `crypto`, `pop-culture`, `middle-east`, `business`, and `science`.
- **Params:** `cursor` (string, optional) — Optional rewards cursor from a prior response; defaults to MA==; `date` (string, optional) — Reward program date in YYYY-MM-DD format; defaults to today in UTC; `limit` (integer, optional) — Maximum rows, defaults to 100 and supports up to 100; `order_by` (string, optional) — Rewards market sort; `position` (string, optional) — Sort direction; `q` (string, optional) — Optional market question search text; `tag_slug` (string, optional) — Rewards category

### `polymarket_search`

- **HTTP:** `GET /polymarket/search`
- **What:** Search Polymarket events. Searches Polymarket's credential-free public search JSON and returns normalized event results. The `status` enum accepts `open`, `closed`, and `all`; the `sort` enum accepts `relevance`, `volume24hr`, `volume`, `liquidity`, and `endDate`.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `include_profiles` (boolean, optional) — Include matching profiles; `include_tags` (boolean, optional) — Include matching tags; `limit` (integer, optional) — Maximum events, defaults to 10 and supports up to 50; `q` (string, **required**) — Search query; `sort` (string, optional) — Search sort; `status` (string, optional) — Event status filter

### `polymarket_tag`

- **HTTP:** `GET /polymarket/tag/{id}`
- **What:** Get a Polymarket tag by id. Returns one normalized Polymarket tag from credential-free public Gamma tag JSON.
- **Params:** `id` (string, **required**) — Polymarket tag id; `include_template` (boolean, optional) — Include upstream template data when supported; `locale` (string, optional) — Optional upstream locale

### `polymarket_tags`

- **HTTP:** `GET /polymarket/tags`
- **What:** List Polymarket tags. Returns normalized tag rows from Polymarket's credential-free public Gamma tags JSON.
- **Params:** `ascending` (string, optional) — Sort ascending flag; `limit` (integer, optional) — Maximum tags, defaults to 25 and supports up to 100; `locale` (string, optional) — Optional upstream locale; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_token_midpoint`

- **HTTP:** `GET /polymarket/token/{token_id}/midpoint`
- **What:** Get Polymarket token midpoint. Returns the public CLOB midpoint for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_orderbook`

- **HTTP:** `GET /polymarket/token/{token_id}/orderbook`
- **What:** Get Polymarket token order book. Returns public CLOB order-book depth for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_price`

- **HTTP:** `GET /polymarket/token/{token_id}/price`
- **What:** Get Polymarket token price. Returns the public CLOB buy or sell price for one Polymarket token id.
- **Params:** `side` (string, optional) — Order side used for the CLOB price; `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_price_history`

- **HTTP:** `GET /polymarket/token/{token_id}/price-history`
- **What:** Get Polymarket token price history. Returns public CLOB price-history points for one Polymarket token id.
- **Params:** `end_ts` (integer, optional) — Optional Unix timestamp upper bound; `fidelity` (integer, optional) — Data point resolution in minutes; 0 uses the default 60; maximum 1440; `interval` (string, optional) — History interval; `start_ts` (integer, optional) — Optional Unix timestamp lower bound; `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_spread`

- **HTTP:** `GET /polymarket/token/{token_id}/spread`
- **What:** Get Polymarket token spread. Returns the public CLOB spread for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_tokens_midpoints`

- **HTTP:** `POST /polymarket/tokens/midpoints`
- **What:** Get Polymarket token midpoints. Returns public CLOB midpoints for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_orderbooks`

- **HTTP:** `POST /polymarket/tokens/orderbooks`
- **What:** Get Polymarket token order books. Returns public CLOB order-book depth for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_prices`

- **HTTP:** `POST /polymarket/tokens/prices`
- **What:** Get Polymarket token prices. Returns public CLOB buy and sell prices for up to 25 Polymarket token ids. The `side` enum accepts `buy` and `sell`; when omitted, both sides are returned. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_spreads`

- **HTTP:** `POST /polymarket/tokens/spreads`
- **What:** Get Polymarket token spreads. Returns public CLOB spreads for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

## Kalshi (21)

### `kalshi_event`

- **HTTP:** `GET /kalshi/event/{event_ticker}`
- **What:** Kalshi event detail. Returns one normalized Kalshi event row and its normalized markets from credential-free public market-data JSON.
- **Params:** `event_ticker` (string, **required**) — Kalshi event ticker

### `kalshi_event_history`

- **HTTP:** `GET /kalshi/event/{event_ticker}/history`
- **What:** Kalshi event history. Returns normalized Kalshi candlesticks grouped by market for one event from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `event_ticker` (string, **required**) — Kalshi event ticker; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `series_ticker` (string, optional) — Kalshi series ticker. Defaults to the event ticker prefix before the last dash.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.

### `kalshi_event_metadata`

- **HTTP:** `GET /kalshi/event/{event_ticker}/metadata`
- **What:** Kalshi event metadata. Returns media, market metadata, settlement sources, and optional competition context for one Kalshi event from credential-free public market-data JSON.
- **Params:** `event_ticker` (string, **required**) — Kalshi event ticker

### `kalshi_events`

- **HTTP:** `GET /kalshi/events`
- **What:** Kalshi events. Returns normalized Kalshi event rows from credential-free public market-data JSON.
- **Params:** `category` (string, optional) — Kalshi category filter; `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `min_close_ts` (integer, optional) — Minimum event close Unix timestamp in seconds; `min_updated_ts` (integer, optional) — Minimum event update Unix timestamp in seconds; `series_ticker` (string, optional) — Kalshi series ticker filter; `status` (string, optional) — Event status filter; `with_milestones` (boolean, optional) — Include event milestones when supported upstream; `with_nested_markets` (boolean, optional) — Include nested market rows when supported upstream

### `kalshi_exchange_schedule`

- **HTTP:** `GET /kalshi/exchange/schedule`
- **What:** Kalshi exchange schedule. Returns public exchange standard hours and maintenance windows from Kalshi market-data JSON.
- **Params:** _none_

### `kalshi_exchange_status`

- **HTTP:** `GET /kalshi/exchange/status`
- **What:** Kalshi exchange status. Returns public exchange and trading active flags from Kalshi market-data JSON.
- **Params:** _none_

### `kalshi_historical_cutoff`

- **HTTP:** `GET /kalshi/historical/cutoff`
- **What:** Kalshi historical data cutoff. Returns the cutoff timestamps Kalshi uses for historical market, order, and trade data migration.
- **Params:** _none_

### `kalshi_historical_market`

- **HTTP:** `GET /kalshi/historical/market/{ticker}`
- **What:** Kalshi historical market detail. Returns one normalized settled Kalshi historical market row from credential-free public market-data JSON.
- **Params:** `ticker` (string, **required**) — Kalshi historical market ticker

### `kalshi_historical_market_history`

- **HTTP:** `GET /kalshi/historical/market/{ticker}/history`
- **What:** Kalshi historical market history. Returns normalized Kalshi candlesticks for one settled historical market from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.; `ticker` (string, **required**) — Kalshi historical market ticker

### `kalshi_historical_markets`

- **HTTP:** `GET /kalshi/historical/markets`
- **What:** Kalshi historical markets. Returns normalized settled Kalshi historical market rows from credential-free public market-data JSON. `tickers`, `event_ticker`, and `series_ticker` are mutually exclusive. The `mve_filter` enum accepts `exclude`.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `event_ticker` (string, optional) — Kalshi event ticker filter. Mutually exclusive with tickers and series_ticker.; `limit` (integer, optional) — Rows to return, default 25, max 1000; `mve_filter` (string, optional) — Multivariate event filter; `series_ticker` (string, optional) — Kalshi series ticker filter. Mutually exclusive with tickers and event_ticker.; `tickers` (string, optional) — Comma-separated Kalshi market tickers. Mutually exclusive with event_ticker and series_ticker.

### `kalshi_historical_trades`

- **HTTP:** `GET /kalshi/historical/trades`
- **What:** Kalshi historical trades. Returns normalized older Kalshi trades from credential-free historical market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `max_ts` (integer, optional) — Maximum created Unix timestamp in seconds; `min_ts` (integer, optional) — Minimum created Unix timestamp in seconds; `ticker` (string, optional) — Kalshi market ticker filter

### `kalshi_market`

- **HTTP:** `GET /kalshi/market/{ticker}`
- **What:** Kalshi market detail. Returns one normalized Kalshi market row from credential-free public market-data JSON.
- **Params:** `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_market_history`

- **HTTP:** `GET /kalshi/market/{ticker}/history`
- **What:** Kalshi market history. Returns normalized Kalshi candlesticks for one market from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `series_ticker` (string, optional) — Kalshi series ticker. Defaults to the market ticker prefix before the last dash.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.; `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_market_orderbook`

- **HTTP:** `GET /kalshi/market/{ticker}/orderbook`
- **What:** Kalshi market orderbook. Returns normalized yes/no bid levels for one Kalshi market ticker from public orderbook JSON.
- **Params:** `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_markets`

- **HTTP:** `GET /kalshi/markets`
- **What:** Kalshi markets. Returns normalized Kalshi market rows from credential-free public market-data JSON. The `status` enum accepts `unopened`, `open`, `closed`, and `settled`.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `event_ticker` (string, optional) — Kalshi event ticker filter; `limit` (integer, optional) — Rows to return, default 25, max 200; `series_ticker` (string, optional) — Kalshi series ticker filter; `status` (string, optional) — Market status filter; `ticker` (string, optional) — Kalshi market ticker filter

### `kalshi_markets_history`

- **HTTP:** `GET /kalshi/markets/history`
- **What:** Kalshi batch market history. Returns normalized Kalshi candlesticks for up to 25 market tickers from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `market_tickers` (string, **required**) — Comma-separated Kalshi market tickers. Repeated query values are also accepted.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.

### `kalshi_markets_orderbooks`

- **HTTP:** `GET /kalshi/markets/orderbooks`
- **What:** Kalshi batch market orderbooks. Returns normalized yes/no bid levels for up to 25 Kalshi market tickers from public orderbook JSON.
- **Params:** `tickers` (string, **required**) — Comma-separated Kalshi market tickers. Repeated query values are also accepted.

### `kalshi_multivariate_events`

- **HTTP:** `GET /kalshi/events/multivariate`
- **What:** Kalshi multivariate events. Returns normalized Kalshi multivariate event rows from credential-free public market-data JSON. Kalshi's regular events endpoint excludes these MVE rows.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200

### `kalshi_series`

- **HTTP:** `GET /kalshi/series`
- **What:** Kalshi series. Returns normalized Kalshi series rows from credential-free public market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200

### `kalshi_series_detail`

- **HTTP:** `GET /kalshi/series/{series_ticker}`
- **What:** Kalshi series detail. Returns one normalized Kalshi series row from credential-free public market-data JSON.
- **Params:** `series_ticker` (string, **required**) — Kalshi series ticker

### `kalshi_trades`

- **HTTP:** `GET /kalshi/trades`
- **What:** Kalshi trades. Returns normalized recent Kalshi market trades from credential-free public market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `max_ts` (integer, optional) — Maximum created Unix timestamp in seconds; `min_ts` (integer, optional) — Minimum created Unix timestamp in seconds; `ticker` (string, optional) — Kalshi market ticker filter

## Metaculus (11)

### `metaculus_category_questions`

- **HTTP:** `GET /metaculus/category/{slug}/questions`
- **What:** Metaculus category questions. Returns normalized Metaculus question rows from a credential-free public category feed page. Allowed category slugs: artificial-intelligence, computing-and-math, cryptocurrencies, economy-business, elections, environment-climate, geopolitics, health-pandemics, law, metaculus, natural-sciences, nuclear, politics, social-sciences, space, sports-entertainment, technology.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus category slug

### `metaculus_comments_feed`

- **HTTP:** `GET /metaculus/comments-feed`
- **What:** Metaculus comments feed. Returns normalized Metaculus question rows for the questions referenced by the most recent public comments, in comment recency order. Derived from credential-free public Metaculus data; upstream comment bodies are not exposed.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_project_questions`

- **HTTP:** `GET /metaculus/project/{slug}/questions`
- **What:** Metaculus project questions. Returns normalized Metaculus question rows for one public project, filtered by its slug. A slug that does not exist returns 404.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus project slug

### `metaculus_question`

- **HTTP:** `GET /metaculus/question/{id}`
- **What:** Metaculus question detail. Returns one normalized Metaculus question from credential-free public page data.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_forecast_history`

- **HTTP:** `GET /metaculus/question/{id}/forecast-history`
- **What:** Metaculus question forecast history. Returns public aggregation forecast history points for one Metaculus question from credential-free public page data. The `method` enum accepts `recency_weighted`, `unweighted`, and `single_aggregation`.
- **Params:** `id` (string, **required**) — Metaculus question or post id; `max_points` (integer, optional) — Maximum history points to return, default 500, max 2000; `method` (string, optional) — Aggregation method

### `metaculus_question_forecasts`

- **HTTP:** `GET /metaculus/question/{id}/forecasts`
- **What:** Metaculus question forecasts. Returns compact public latest forecast summaries by aggregation method for one Metaculus question.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_metadata`

- **HTTP:** `GET /metaculus/question/{id}/metadata`
- **What:** Metaculus question metadata. Returns public metadata for one Metaculus question, including option labels, option history, scaling metadata, resolution fields, and timing fields when present.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_options`

- **HTTP:** `GET /metaculus/question/{id}/options`
- **What:** Metaculus question options. Returns public multiple-choice option labels and latest option-level forecast values for one Metaculus question. The `method` enum accepts `recency_weighted`, `unweighted`, and `single_aggregation`.
- **Params:** `id` (string, **required**) — Metaculus question or post id; `method` (string, optional) — Aggregation method

### `metaculus_questions`

- **HTTP:** `GET /metaculus/questions`
- **What:** Metaculus questions. Returns normalized Metaculus question rows from credential-free public page data. The endpoint fails closed on authenticated API responses or Cloudflare challenge pages.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_top_comments`

- **HTTP:** `GET /metaculus/top-comments`
- **What:** Metaculus top comments feed. Returns normalized Metaculus question rows for the questions whose recent public comments collected the highest vote scores over roughly the last week. Derived from credential-free public Metaculus data; upstream comment bodies are not exposed.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_tournament_questions`

- **HTTP:** `GET /metaculus/tournament/{slug}/questions`
- **What:** Metaculus tournament questions. Returns normalized Metaculus question rows for one public tournament, filtered by its slug. A slug that does not exist returns 404.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus tournament slug
