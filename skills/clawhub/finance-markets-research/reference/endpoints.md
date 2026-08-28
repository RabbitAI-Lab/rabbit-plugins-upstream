# finance-markets-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**77 endpoints across 5 platform group(s).**

## Yahoo Finance (39)

### `yahoo_finance_calendar_results`

- **HTTP:** `GET /yahoo-finance/calendars/{type}`
- **What:** Yahoo Finance calendar results. Returns global Yahoo Finance calendar rows for earnings, IPOs, economic events, or splits.
- **Params:** `end` (string, optional) — End date as YYYY-MM-DD, RFC3339, or Unix seconds; `filter_most_active` (boolean, optional) — Earnings-only most-active filter, default true; `limit` (integer, optional) — Result count, max 100; `market_cap` (number, optional) — Earnings-only market cap minimum; `offset` (integer, optional) — Result offset; `start` (string, optional) — Start date as YYYY-MM-DD, RFC3339, or Unix seconds; `type` (string, **required**) — Calendar type: earnings, ipo, economic-events, or splits

### `yahoo_finance_calendars`

- **HTTP:** `GET /yahoo-finance/calendars`
- **What:** Yahoo Finance calendar types. Lists global Yahoo Finance calendar types supported by this integration.
- **Params:** _none_

### `yahoo_finance_download`

- **HTTP:** `POST /yahoo-finance/download`
- **What:** Yahoo Finance batch historical prices. Returns historical price data for up to 25 symbols.
- **Params:** `request` (object, **required**) — Batch download request

### `yahoo_finance_industries`

- **HTTP:** `GET /yahoo-finance/industries`
- **What:** Yahoo Finance industries. Lists Yahoo Finance industry keys that can be queried with the industry endpoint.
- **Params:** _none_

### `yahoo_finance_industry`

- **HTTP:** `GET /yahoo-finance/industries/{key}`
- **What:** Yahoo Finance industry detail. Returns overview, sector linkage, top companies, growth companies, and research reports for an industry key.
- **Params:** `key` (string, **required**) — Industry key such as semiconductors

### `yahoo_finance_lookup`

- **HTTP:** `GET /yahoo-finance/lookup`
- **What:** Yahoo Finance lookup. Returns Yahoo Finance instrument matches for a query, optionally filtered by instrument type.
- **Params:** `count` (integer, optional) — Result count; `query` (string, **required**) — Ticker symbol or company name; `start` (integer, optional) — Result offset; `type` (string, optional) — Instrument type filter

### `yahoo_finance_market_status`

- **HTTP:** `GET /yahoo-finance/market/{market}/status`
- **What:** Yahoo Finance market status. Returns Yahoo Finance open/close status for a market such as US.
- **Params:** `market` (string, **required**) — Market such as US

### `yahoo_finance_market_summary`

- **HTTP:** `GET /yahoo-finance/market/{market}/summary`
- **What:** Yahoo Finance market summary. Returns Yahoo Finance market summary rows for a market such as US.
- **Params:** `market` (string, **required**) — Market such as US

### `yahoo_finance_screener`

- **HTTP:** `GET /yahoo-finance/screener/{id}`
- **What:** Yahoo Finance predefined screener results. Runs a predefined Yahoo Finance screener such as day_gainers or most_actives.
- **Params:** `count` (integer, optional) — Result count; `id` (string, **required**) — Predefined screener id; `offset` (integer, optional) — Result offset; `sort_asc` (boolean, optional) — Sort ascending; `sort_field` (string, optional) — Sort field for offset/customized runs

### `yahoo_finance_screener_custom`

- **HTTP:** `POST /yahoo-finance/screener`
- **What:** Yahoo Finance custom screener. Runs a constrained Yahoo Finance custom screener query using Yahoo's public screener JSON shape.
- **Params:** `request` (object, **required**) — Custom screener request

### `yahoo_finance_screeners`

- **HTTP:** `GET /yahoo-finance/screeners`
- **What:** Yahoo Finance predefined screeners. Lists the predefined screeners supported by the Yahoo Finance integration.
- **Params:** _none_

### `yahoo_finance_search`

- **HTTP:** `GET /yahoo-finance/search`
- **What:** Yahoo Finance search. Returns normalized Yahoo Finance quotes, news, lists, and optional research reports for a query.
- **Params:** `enable_fuzzy_query` (boolean, optional) — Enable fuzzy matching; `include_research` (boolean, optional) — Include research reports when Yahoo returns them; `lists_count` (integer, optional) — List result count; `news_count` (integer, optional) — News result count; `q` (string, **required**) — Ticker symbol or company name; `quotes_count` (integer, optional) — Quote result count

### `yahoo_finance_sector`

- **HTTP:** `GET /yahoo-finance/sectors/{key}`
- **What:** Yahoo Finance sector detail. Returns overview, top companies, ETFs, mutual funds, industries, and research reports for a sector key.
- **Params:** `key` (string, **required**) — Sector key such as technology

### `yahoo_finance_sectors`

- **HTTP:** `GET /yahoo-finance/sectors`
- **What:** Yahoo Finance sectors. Lists Yahoo Finance sector keys that can be queried with the sector endpoint.
- **Params:** _none_

### `yahoo_finance_ticker_actions`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/actions`
- **What:** Yahoo Finance corporate actions. Returns dividends, splits, and capital gains for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_analysts`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/analysts`
- **What:** Yahoo Finance analyst data. Returns recommendations, upgrades/downgrades, price targets, and estimate modules where Yahoo provides them.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_calendar`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/calendar`
- **What:** Yahoo Finance calendar. Returns Yahoo Finance calendar events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_capital_gains`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/capital-gains`
- **What:** Yahoo Finance capital gains. Returns capital gain events for ETF or mutual fund symbols when Yahoo provides them.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as SPY

### `yahoo_finance_ticker_dividends`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/dividends`
- **What:** Yahoo Finance dividends. Returns dividend events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_earnings`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/earnings`
- **What:** Yahoo Finance earnings. Returns Yahoo Finance earnings modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_earnings_dates`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/earnings-dates`
- **What:** Yahoo Finance earnings dates. Returns standalone earnings-date rows from Yahoo Finance calendar HTML when Yahoo serves the table.
- **Params:** `limit` (integer, optional) — Result count, max 100; `offset` (integer, optional) — Result offset; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_financials`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/financials`
- **What:** Yahoo Finance financial statements. Returns annual, quarterly, or supported trailing income, balance sheet, or cash flow statement data.
- **Params:** `period` (string, optional) — annual, quarterly, or trailing; `statement` (string, optional) — Statement type. Allowed values: income (alias income-statement), balance-sheet (alias balance), cash-flow (alias cashflow); `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_funds`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/funds`
- **What:** Yahoo Finance fund data. Returns fund profile, top holdings, equity/bond holdings, and sector weighting modules for ETF and mutual fund symbols.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as SPY

### `yahoo_finance_ticker_history`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/history`
- **What:** Yahoo Finance historical prices. Returns normalized OHLCV points for a symbol. Use either period or start/end.
- **Params:** `auto_adjust` (boolean, optional) — Adjust OHLC prices with adjusted close; `back_adjust` (boolean, optional) — Back-adjust OHLC prices while keeping close; `end` (string, optional) — Unix seconds, RFC3339, or YYYY-MM-DD; `include_actions` (boolean, optional) — Include dividends, splits, and capital gains; `include_prepost` (boolean, optional) — Include pre/post market data; `interval` (string, optional) — Interval such as 1d, 1h, 5m; `keepna` (boolean, optional) — Keep fully empty chart rows; `period` (string, optional) — Range such as 1d, 1mo, 1y, max; `rounding` (boolean, optional) — Round prices to two decimals; `start` (string, optional) — Unix seconds, RFC3339, or YYYY-MM-DD; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_history_metadata`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/history-metadata`
- **What:** Yahoo Finance history metadata. Returns Yahoo Finance chart metadata for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_holders`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/holders`
- **What:** Yahoo Finance holders. Returns major, institutional, fund, and insider holder modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_info`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/info`
- **What:** Yahoo Finance ticker info. Returns normalized profile, quote type, price, statistics, and summary modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_isin`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/isin`
- **What:** Yahoo Finance ticker ISIN. Returns the experimental yfinance-compatible ISIN lookup result for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_news`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/news`
- **What:** Yahoo Finance ticker news. Returns Yahoo Finance news search results for a symbol.
- **Params:** `count` (integer, optional) — News result count; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL; `tab` (string, optional) — News tab: news, all, or press_releases

### `yahoo_finance_ticker_options`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/options`
- **What:** Yahoo Finance options chain. Returns option expiration dates and the current option chain for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_options_expiration`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/options/{expiration}`
- **What:** Yahoo Finance options chain by expiration. Returns calls and puts for a specific Unix expiration timestamp.
- **Params:** `expiration` (string, **required**) — Unix expiration timestamp; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_quote`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/quote`
- **What:** Yahoo Finance ticker quote. Returns normalized fast quote fields for one Yahoo Finance symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_sec_filings`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/sec-filings`
- **What:** Yahoo Finance SEC filings. Returns Yahoo Finance SEC filing summaries for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_shares`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/shares`
- **What:** Yahoo Finance share counts. Returns current share-count fields from Yahoo key statistics.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_shares_full`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/shares-full`
- **What:** Yahoo Finance historical share counts. Returns historical shares-out rows from Yahoo fundamentals timeseries.
- **Params:** `end` (string, optional) — End date as YYYY-MM-DD, RFC3339, or Unix seconds; `start` (string, optional) — Start date as YYYY-MM-DD, RFC3339, or Unix seconds; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_splits`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/splits`
- **What:** Yahoo Finance splits. Returns split events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_sustainability`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/sustainability`
- **What:** Yahoo Finance sustainability. Returns ESG and sustainability modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_valuation`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/valuation`
- **What:** Yahoo Finance valuation measures. Returns the valuation table from the Yahoo Finance key statistics page when Yahoo serves the table.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_trending`

- **HTTP:** `GET /yahoo-finance/trending/{region}`
- **What:** Yahoo Finance trending symbols. Returns trending Yahoo Finance symbols for a region.
- **Params:** `count` (integer, optional) — Symbol count; `region` (string, **required**) — Region such as US

## SEC EDGAR (10)

### `sec_company_intelligence`

- **HTTP:** `GET /sec/company/intelligence`
- **What:** Company 360 overview from SEC data. Aggregates a company's profile, a latest-annual financial snapshot, the latest 10-K/10-Q/8-K, and recent material events into one call. Provide cik or ticker. Optionally fuse live cross-source data with enrich (a comma list of market, news, hiring): market and news are keyed on the ticker; hiring needs ats plus that ATS's careers slug (or tenant/datacenter/site for Workday). Enrichment is best-effort — requested-but-unavailable sources are listed under degraded and never fail the SEC-native response. Credential-free public data.
- **Params:** `ats` (string, optional) — ATS provider for hiring enrichment; `careers_slug` (string, optional) — Careers board slug for hiring (greenhouse/lever/ashby/smartrecruiters); `cik` (string, optional) — SEC CIK (numeric or zero-padded); `datacenter` (string, optional) — Workday datacenter shard (hiring, when ats=workday); `enrich` (string, optional) — Comma list of cross-source enrichments; `site` (string, optional) — Workday career site (hiring, when ats=workday); `tenant` (string, optional) — Workday tenant (hiring, when ats=workday); `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_company_search`

- **HTTP:** `GET /sec/company/search`
- **What:** Resolve a ticker or company name to EDGAR companies. Resolves a ticker symbol or company-name query to SEC EDGAR companies (CIK, ticker, name) using the official company_tickers map. Credential-free public SEC data.
- **Params:** `limit` (integer, optional) — Max matches, default 10, max 100; `q` (string, **required**) — Ticker symbol or company name

### `sec_company_submissions`

- **HTTP:** `GET /sec/company/submissions`
- **What:** List a company's EDGAR filings. Returns a company's recent SEC filings (form, dates, primary document URL) filtered by form type and date range, plus company profile fields as reported by EDGAR: entity_type, former_names, exchanges, category, fiscal_year_end, state_of_incorporation. Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `form` (string, optional) — Filter by form type, e.g. 10-K, 10-Q, 8-K; `from` (string, optional) — Earliest filing date (YYYY-MM-DD); `limit` (integer, optional) — Max filings, default 50, max 500; `ticker` (string, optional) — Ticker symbol (alternative to cik); `to` (string, optional) — Latest filing date (YYYY-MM-DD)

### `sec_filing`

- **HTTP:** `GET /sec/filing`
- **What:** Get a single filing by accession number. Returns a single SEC filing's metadata and primary document URL. Provide accession plus cik or ticker. Credential-free public SEC data.
- **Params:** `accession` (string, **required**) — Accession number; `cik` (string, optional) — SEC CIK (numeric or zero-padded); `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_filing_sections`

- **HTTP:** `GET /sec/filing/sections`
- **What:** Extract 10-K/10-Q/8-K item sections. Extracts item sections (e.g. 1A Risk Factors, 7 MD&A) from a 10-K/10-Q/8-K primary document as clean text. Provide accession plus cik or ticker. Credential-free public SEC data.
- **Params:** `accession` (string, **required**) — Accession number; `cik` (string, optional) — SEC CIK (numeric or zero-padded); `items` (string, optional) — Comma-separated item numbers to return, e.g. 1A,7; `max_chars` (integer, optional) — Max characters per section, default 20000, max 200000; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_financials`

- **HTTP:** `GET /sec/financials`
- **What:** Normalized income statement, balance sheet, or cash flow. Returns a company's normalized financial statements across recent periods, resolving EDGAR's inconsistent XBRL tags to a stable schema. Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `limit` (integer, optional) — Number of periods, default 5, max 20; `period` (string, optional) — Period basis, default annual; `statement` (string, optional) — Statement, default income; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_frames`

- **HTTP:** `GET /sec/frames`
- **What:** Cross-company values for one XBRL concept and period. Returns every filer's reported value for one XBRL concept in one reporting period (an EDGAR "frame"). Credential-free public SEC data.
- **Params:** `concept` (string, **required**) — XBRL concept tag, e.g. Assets, Revenues; `limit` (integer, optional) — Max companies, default 200, max 2000; `period` (string, **required**) — Reporting frame, e.g. CY2024, CY2024Q1, CY2024Q4I; `taxonomy` (string, optional) — XBRL taxonomy, default us-gaap; `unit` (string, optional) — Unit of measure, default USD

### `sec_full_text_search`

- **HTTP:** `GET /sec/full-text-search`
- **What:** Full-text search across EDGAR filings. Searches the full text of SEC EDGAR filings (efts), filtered by form and date, with pagination. Credential-free public SEC data; free where incumbents gate full-text search behind paid tiers.
- **Params:** `forms` (string, optional) — Filter by form types, comma-separated; `from` (string, optional) — Earliest filing date (YYYY-MM-DD); `page` (integer, optional) — 1-based page number, default 1; `q` (string, **required**) — Search query (supports quoted phrases); `to` (string, optional) — Latest filing date (YYYY-MM-DD)

### `sec_insider`

- **HTTP:** `GET /sec/insider`
- **What:** Insider transactions (Forms 3/4/5). Returns a company's recent insider transactions parsed from Form 3/4/5 ownership filings (owner, role, security, shares, price). Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `limit` (integer, optional) — Max transactions, default 10, max 30; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_institutional_holdings`

- **HTTP:** `GET /sec/institutional-holdings`
- **What:** Institutional holdings (13F-HR). Returns the latest 13F-HR holdings for an institutional manager (by CIK): issuer, value, shares, sorted by value. Credential-free public SEC data.
- **Params:** `cik` (string, **required**) — Institutional manager CIK; `limit` (integer, optional) — Max holdings, default 50, max 1000

## Congress (2)

### `congress_report`

- **HTTP:** `GET /congress/report`
- **What:** Fetch and parse a congressional disclosure report. Fetch a single disclosure report by its filing_url (as returned by.
- **Params:** `url` (string, **required**) — Filing URL, as returned by congress-stock-disclosures' filing_url field. Must be an efdsearch.senate.gov /search/view/annual/..., /search/view/ptr/..., or /search/view/extension-notice/regular/... URL.

### `congress_stock_disclosures`

- **HTTP:** `GET /congress/stock-disclosures`
- **What:** Search congressional stock-disclosure filings. Search public congressional stock disclosure filings (House or Senate).
- **Params:** `candidate_state` (string, optional) — Candidate state filter (Senate only, 2-letter code).; `chamber` (string, optional) — Chamber filter. Allowed values: house, senate.; `district` (string, optional) — House district filter (House only).; `election_year` (string, optional) — House candidate-search election year filter (requires filer_type=candidate).; `filer_type` (string, optional) — Filer-type filter, meaning differs by chamber. House: member (default) or candidate. Senate: comma-separated senator, candidate, former_senator, or the standalone all value. Defaults to senator when omitted.; `first_name` (string, optional) — Senate filer first-name prefix (Senate only; cannot be combined with member).; `from` (string, optional) — Minimum filing date. House accepts YYYY. Senate accepts YYYY or MM/DD/YYYY and defaults to 2012 when omitted.; `last_name` (string, optional) — Senate filer last-name prefix (Senate only; cannot be combined with member).; `limit` (integer, optional) — Max results (1-500).; `member` (string, optional) — Member name. Required for House. For Senate, this backward-compatible shorthand maps one word to last_name and maps the first word plus the complete remaining surname to first_name/last_name; it cannot be combined with either exact name field.; `page` (integer, optional) — 1-based result page (1-1000).; `report_type` (string, optional) — Comma-separated Senate report-type filter (Senate only). Allowed values: annual, periodic_transaction, due_date_extension, blind_trust, other. Defaults to all types when omitted.; `senator_state` (string, optional) — Senator state filter (Senate only, 2-letter code).; `sort` (string, optional) — Sort key. Allowed values: name_asc, name_desc, office_asc, office_desc, filing_year_asc, filing_year_desc.; `state` (string, optional) — State or territory filter (2-letter code). For Senate this backward-compatible shorthand applies to both Senator and Candidate states and cannot be combined with senator_state or candidate_state.; `ticker` (string, optional) — Deprecated unsupported parameter; any non-empty value returns a validation error and the parameter is planned for removal.; `to` (string, optional) — Maximum filing date. House accepts YYYY. Senate accepts YYYY or MM/DD/YYYY.

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

## PitchBook (5)

### `pitchbook_advisor`

- **HTTP:** `GET /pitchbook/advisor`
- **What:** PitchBook advisor profile. Returns the free/teaser content of a PitchBook advisor (service provider, e.g. investment bank, lender, or financing advisory firm) profile page: overview, description, contact/HQ, and a preview of serviced companies/deals, co-lenders, and subsidiaries. PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook advisor id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/advisor/<id> URL

### `pitchbook_company`

- **HTTP:** `GET /pitchbook/company`
- **What:** PitchBook company profile. Returns the free/teaser content of a PitchBook company profile page (overview, description, contact/HQ, industry, funding-round history without dollar amounts, a preview of investors, acquisitions, and subsidiaries). PitchBook gates most numeric figures (deal amounts, cap tables, full investor/LP lists) behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook company id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/company/<id> URL

### `pitchbook_fund`

- **HTTP:** `GET /pitchbook/fund`
- **What:** PitchBook fund profile. Returns the free/teaser content of a PitchBook fund profile page (strategy, status, manager, size, vintage, and a preview of limited partners and benchmark peer funds). PitchBook gates most numeric figures (returns/IRR, full LP lists) behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook fund id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/fund/<id> URL

### `pitchbook_investor`

- **HTTP:** `GET /pitchbook/investor`
- **What:** PitchBook investor profile. Returns the free/teaser content of a PitchBook investor (fund manager/firm) profile page (overview, description, contact/HQ, and a preview of investments, exits, and co-investors). PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook investor id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/investor/<id> URL

### `pitchbook_limited_partner`

- **HTTP:** `GET /pitchbook/limited-partner`
- **What:** PitchBook limited partner profile. Returns the free/teaser content of a PitchBook limited partner (institutional investor, e.g. pension fund, endowment, or insurance company) profile page: overview, description, contact, and a preview of fund commitments. PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Some limited partner profiles have no FAQ section (thinner profiles) -- this is normal, not a sign of a blocked or broken response. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook limited partner id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/limited-partner/<id> URL
