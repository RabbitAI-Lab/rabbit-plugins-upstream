# crypto-market-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**21 endpoints across 1 platform group(s).**

## CoinGecko (21)

### `coingecko_categories`

- **HTTP:** `GET /coingecko/categories`
- **What:** CoinGecko categories. Returns normalized CoinGecko category rows from the public categories page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_category_coins`

- **HTTP:** `GET /coingecko/category/{slug}/coins`
- **What:** CoinGecko category coins. Returns normalized coin rows from a CoinGecko public category page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `slug` (string, **required**) — CoinGecko category slug such as stablecoins; `vs_currency` (string, optional) — Quote currency

### `coingecko_chain`

- **HTTP:** `GET /coingecko/chains/{id}`
- **What:** CoinGecko chain detail. Returns normalized sections from a CoinGecko public chain detail page. Sections are omitted when not present. This endpoint supports the documented `vs_currency` enum.
- **Params:** `id` (string, **required**) — CoinGecko chain id such as ethereum; `limit` (integer, optional) — Rows per section to return, default 20, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_chains`

- **HTTP:** `GET /coingecko/chains`
- **What:** CoinGecko chains. Returns normalized chain rows from the CoinGecko public website chains table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_coin`

- **HTTP:** `GET /coingecko/coin/{id}`
- **What:** CoinGecko coin profile. Returns normalized CoinGecko profile, market stats, links, and categories for one coin id. This endpoint supports the documented `vs_currency` enum and is not intended for real-time trading.
- **Params:** `id` (string, **required**) — CoinGecko coin id such as bitcoin; `vs_currency` (string, optional) — Quote currency

### `coingecko_coin_analysis`

- **HTTP:** `GET /coingecko/coin/{id}/analysis`
- **What:** CoinGecko coin chart analysis. Returns derived price-chart metrics from CoinGecko public chart JSON. This endpoint supports the documented `vs_currency` enum and is not investment advice or real-time trading data.
- **Params:** `id` (string, **required**) — CoinGecko coin id such as bitcoin; `include_annotations` (boolean, optional) — Fetch optional CoinGecko chart annotations; `range` (string, optional) — Chart range; `vs_currency` (string, optional) — Quote currency

### `coingecko_exchange`

- **HTTP:** `GET /coingecko/exchange/{id}`
- **What:** CoinGecko exchange detail. Returns normalized profile stats and market rows from a CoinGecko public exchange page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `id` (string, **required**) — CoinGecko exchange id such as binance; `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_exchanges`

- **HTTP:** `GET /coingecko/exchanges`
- **What:** CoinGecko exchanges. Returns normalized exchange rows from CoinGecko public website exchange tables. This endpoint supports the documented `vs_currency` enum.
- **Params:** `kind` (string, optional) — Exchange table kind, default spot; `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_gainers_losers`

- **HTTP:** `GET /coingecko/gainers-losers`
- **What:** CoinGecko crypto gainers and losers. Returns normalized rows from CoinGecko's public crypto gainers and losers table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 20, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_global`

- **HTTP:** `GET /coingecko/global`
- **What:** CoinGecko global market snapshot. Returns normalized global market metrics from CoinGecko's public charts page.
- **Params:** _none_

### `coingecko_global_charts`

- **HTTP:** `GET /coingecko/global/charts`
- **What:** CoinGecko global chart series. Returns normalized global chart series from public CoinGecko website JSON endpoints.
- **Params:** `kind` (string, optional) — Chart kind, default total_market_cap; `limit` (integer, optional) — Rows per series to return, default 120, max 500; `range` (string, optional) — Chart range, default 90d

### `coingecko_learn_articles`

- **HTTP:** `GET /coingecko/learn/articles`
- **What:** CoinGecko Learn articles. Returns normalized article cards from CoinGecko Learn public pages.
- **Params:** `category` (string, optional) — Learn category, default all; `limit` (integer, optional) — Rows to return, default 20, max 50

### `coingecko_markets`

- **HTTP:** `GET /coingecko/markets`
- **What:** CoinGecko markets. Returns normalized cryptocurrency market rows from CoinGecko public pages. This endpoint supports the documented `vs_currency` enum and is not intended for real-time trading.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_new_coins`

- **HTTP:** `GET /coingecko/new-coins`
- **What:** CoinGecko new cryptocurrencies. Returns normalized rows from CoinGecko's public new cryptocurrencies table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_news`

- **HTTP:** `GET /coingecko/news`
- **What:** CoinGecko news cards. Returns normalized article cards from CoinGecko's public news page.
- **Params:** `limit` (integer, optional) — Rows to return, default 20, max 50

### `coingecko_nft_category`

- **HTTP:** `GET /coingecko/nft/category/{slug}`
- **What:** CoinGecko NFT category. Returns normalized NFT collection rows from a CoinGecko public NFT category page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `slug` (string, **required**) — CoinGecko NFT category slug such as metaverse; `vs_currency` (string, optional) — Quote currency

### `coingecko_nfts`

- **HTTP:** `GET /coingecko/nfts`
- **What:** CoinGecko NFT collections. Returns normalized NFT collection rows from the CoinGecko public website NFT table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_search`

- **HTTP:** `GET /coingecko/search`
- **What:** CoinGecko discovery search. Returns normalized CoinGecko search sections from the public website search JSON. Empty valid searches return empty arrays.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 10, max 50; `q` (string, **required**) — Search query

### `coingecko_token_unlocks`

- **HTTP:** `GET /coingecko/token-unlocks`
- **What:** CoinGecko incoming token unlocks. Returns normalized rows from CoinGecko's public incoming token unlocks page.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100

### `coingecko_treasuries`

- **HTTP:** `GET /coingecko/treasuries`
- **What:** CoinGecko crypto treasuries. Returns normalized entity rows from CoinGecko's public crypto treasuries tables. This endpoint supports the documented `vs_currency` enum.
- **Params:** `asset` (string, optional) — Treasury asset filter, default all; `holder_type` (string, optional) — Treasury holder type filter, default all; `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_trending`

- **HTTP:** `GET /coingecko/trending`
- **What:** CoinGecko trending highlights. Returns deduped trending coins and categories from the public CoinGecko highlights page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 20, max 50; `vs_currency` (string, optional) — Quote currency
