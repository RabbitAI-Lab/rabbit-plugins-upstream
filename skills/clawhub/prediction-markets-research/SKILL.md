---
name: prediction-markets-research
description: Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API, returning clean JSON. Use when the user asks what the market thinks will happen, wants current odds/prices for an event, wants a market's price history or order book, or wants a forecasting community's aggregate prediction on a question.
---

# Prediction markets research

Pull live and historical odds, order books, and forecast questions from
Polymarket, Kalshi, and Metaculus as normalized JSON — no scraping
market-maker sites or parsing raw order-book blobs.

## When to use this skill

- "What does the market think will happen with <event>?" / "current odds for …"
- "Show me the order book / spread / price history for this market."
- "What are the top trending prediction markets right now?"
- "What's the community forecast (Metaculus) for <question>?"
- Election, macro, sports, or crypto-outcome forecasting research.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Polymarket** — `/polymarket/search` or `/polymarket/events` to find an
   event; `/polymarket/event/{slug}` for detail (nested markets);
   `/polymarket/market/{id}` for one market; then token-level pricing via
   `/polymarket/token/{token_id}/price|midpoint|orderbook|spread|price-history`
   (or the batched `POST /polymarket/tokens/prices` etc. for up to 25 at once).
   `/polymarket/leaderboard` and `/polymarket/dashboards/macro` cover traders
   and macro events.
2. **Kalshi** — `/kalshi/events` / `/kalshi/markets` to browse; `/kalshi/event/{event_ticker}`
   or `/kalshi/market/{ticker}` for detail; `/kalshi/market/{ticker}/history`
   for candlesticks, `/kalshi/market/{ticker}/orderbook` for depth,
   `/kalshi/trades` for recent fills. `/kalshi/historical/*` covers settled
   (closed) markets.
3. **Metaculus** — `/metaculus/questions` to browse; `/metaculus/question/{id}`
   for detail; `/metaculus/question/{id}/forecasts` for the current
   community aggregate, `/forecast-history` for how it moved over time.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Polymarket:
scripts/crawlora.sh /polymarket/search q="fed rate cut" | jq '.'
scripts/crawlora.sh /polymarket/event/will-the-fed-cut-rates | jq '.'

# Kalshi:
scripts/crawlora.sh /kalshi/markets | jq '.markets[:5]'
scripts/crawlora.sh /kalshi/market/INXD-24DEC31-T5000/history | jq '.'

# Metaculus:
scripts/crawlora.sh /metaculus/questions | jq '.results[:5]'
scripts/crawlora.sh /metaculus/question/12345/forecasts | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/polymarket/markets" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Polymarket,
Kalshi, and Metaculus endpoint this skill uses.

## Examples

- **Cross-platform odds check:** `/polymarket/search` and `/kalshi/markets`
  for the same real-world event, compare implied probabilities.
- **Market momentum:** `/kalshi/market/{ticker}/history` or
  `/polymarket/token/{token_id}/price-history` plotted over time to see how
  sentiment shifted.
- **Forecast vs. market:** `/metaculus/question/{id}/forecasts` (community
  aggregate) alongside the matching Polymarket/Kalshi market price.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public, credential-free data only** — no trading, no order placement;
  read-only market data. This is not financial advice.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Batch endpoints (`/polymarket/tokens/*`) accept up to 25 ids per call —
  chunk larger lists.
