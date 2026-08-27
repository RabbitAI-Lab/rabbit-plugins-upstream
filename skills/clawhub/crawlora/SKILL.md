---
name: crawlora
description: Fetches structured public web data via the Crawlora REST API — search engines, e-commerce, social, finance, maps, app stores, media, and reviews — returning clean JSON instead of HTML. Use whenever the user needs real data from a public website (prices, listings, reviews, transcripts, SERPs, trends, financials, places) and would otherwise have to scrape or parse HTML.
---

# Crawlora — structured public web data

Crawlora is a hosted API that turns public websites into clean, normalized JSON.
One API key gives you **828 endpoints across 71 platform groups** — search engines,
marketplaces, social and video, finance and crypto, maps, app stores, media, and
reviews — so an agent can fetch real data without running a browser, proxies, or
HTML parsers.

## When to use this skill

Use Crawlora when the user asks for live data that lives on a public website, e.g.:

- "What's the price of X on Amazon / eBay / Shopify?"
- "Pull the transcript / comments of this YouTube video."
- "Get the latest Google / Bing results for …" or "what's trending on Google Trends?"
- "Reviews and ratings for this iOS / Android app."
- "Yahoo Finance quote / financials for NVDA", "top CoinGecko gainers".
- "TikTok / Instagram / Reddit posts about …", "Trustpilot reviews for …".
- Any task where the alternative would be scraping HTML or maintaining a crawler.

Prefer a more specific Crawlora skill if one is installed (e.g.
`product-price-research`, `youtube-research`, `app-review-mining`,
`serp-keyword-research`). This umbrella skill covers everything else.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- Export it so the helper and any `curl` calls can read it:

  ```sh
  export CRAWLORA_API_KEY=sk_your_key_here
  ```

- All requests go to `https://api.crawlora.net/api/v1` with the header
  `x-api-key: $CRAWLORA_API_KEY`. A missing/invalid key returns `401`.

## How it works

1. **Pick the endpoint.** Open [`reference/catalog.md`](reference/catalog.md) — it
   lists every endpoint grouped by platform, with method, path, and parameters.
   Match the user's job to a platform group, then to an endpoint.
2. **Call it** with `scripts/crawlora.sh` (see below). It handles auth and prints JSON.
3. **Parse** the JSON with `jq` and answer. Most endpoints return paginated lists;
   pass `page`/`count` params where documented.

## Calling the API

```sh
# GET with query params (key=value):
scripts/crawlora.sh /amazon/search k=laptop | jq '.'
scripts/crawlora.sh /google/suggest q="web scraping" | jq '.'
scripts/crawlora.sh /youtube/transcript/dQw4w9WgXcQ | jq '.'

# POST endpoints take a JSON body (note the -X POST):
scripts/crawlora.sh -X POST /google/search '{"searchOption":{"q":"web scraping api"}}' | jq '.'
scripts/crawlora.sh -X POST /google/trends/explore/interest-over-time '{"keywords":["bitcoin"]}' | jq '.'
```

Raw `curl` fallback (no helper):

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/bing/search?q=web%20scraping" | jq '.'
```

The catalog marks each endpoint's HTTP method. Path params like `{id}` are
substituted into the URL; `GET` params go in the query string; `POST` params go
in the JSON body.

## Endpoint reference

See [`reference/catalog.md`](reference/catalog.md) for the full list of all 828
endpoints (method, path, params, description) grouped by platform.

## Examples

- **Product price:** `scripts/crawlora.sh /amazon/search k="standing desk"` →
  read `.results[].price` to compare listings.
- **YouTube transcript:** resolve the video id from the URL, then
  `scripts/crawlora.sh /youtube/transcript/<id>` and summarize.
- **Trend check:** `scripts/crawlora.sh -X POST /google/trends/explore/interest-over-time '{"keywords":["electric bikes"]}'`.
- **Finance:** `scripts/crawlora.sh /yahoo-finance/ticker/NVDA/quote` (see the
  Yahoo Finance group in the catalog for the exact path/params).

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx` responses; failures aren't charged.
  Free tier is 2,000 credits/mo. Get a key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only.** Crawlora returns publicly available web data; no third-party
  account credentials are involved. Respect each source's terms and rate limits.
- **Security:** keep the key in `CRAWLORA_API_KEY` only — never hardcode it, never put
  it in a URL query param, never commit it.
- Some search endpoints return `503` when the upstream serves a challenge page; retry
  or fall back to another search provider (Google ↔ Bing ↔ Brave).
