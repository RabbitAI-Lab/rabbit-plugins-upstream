---
name: serp-keyword-research
description: Runs SERP and keyword research via the Crawlora API — Google, Bing, Brave, DuckDuckGo, and Yahoo search results plus Google Trends interest-over-time and related/rising queries — returning clean JSON. Use when the user wants search-engine rankings, SERP snapshots, autocomplete/keyword suggestions, or trend data instead of scraping result pages.
---

# SERP & keyword research

Capture search-engine results (Google, Bing, Brave, DuckDuckGo, Yahoo) and
keyword/trend signals (Google autosuggest, Google Trends) as normalized
JSON from the Crawlora API.

## When to use this skill

- "What ranks for <query> on Google / Bing?" / "snapshot the SERP for …".
- "Keyword ideas / autocomplete for …" (suggest endpoints).
- "Is <topic> trending?" / "interest over time / by region for <keyword>."
- "Related and rising queries for …" (Google Trends).
- SEO/SERP monitoring, keyword discovery, or trend research.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **SERP** — Google search is `POST /google/search` with a `searchOption` body;
   Bing, Brave, DuckDuckGo, and Yahoo are plain `GET` with `q`:
   `/bing/search`, `/brave/search`, `/duckduckgo/search`, `/yahoo-search/search`.
   Cross-check engines for coverage; on a `503` challenge, fall back to another engine.
2. **Verticals** — news/videos/images per engine (`/google/news`, `/bing/videos`,
   `/duckduckgo/news`, `/duckduckgo/image`, `/duckduckgo/video`, `/duckduckgo/shopping`, …).
3. **Keyword ideas** — autosuggest: `GET /google/suggest?q=...` (and `/bing/suggest`,
   `/brave/suggest`).
4. **Trends** — Google Trends `POST` endpoints:
   `/google/trends/explore/interest-over-time`, `/interest-by-region`,
   `/related-topics`, `/rising-queries`, `/top-queries` (body: `{"keywords":[...]}`),
   plus `GET /google/trends/trending` for what's hot now.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# GET search engines + suggest:
scripts/crawlora.sh /bing/search q="web scraping api" | jq '.'
scripts/crawlora.sh /brave/search q="web scraping api" | jq '.'
scripts/crawlora.sh /duckduckgo/search q="web scraping api" | jq '.'
scripts/crawlora.sh /yahoo-search/search q="web scraping api" | jq '.'
scripts/crawlora.sh /google/suggest q="web scraping" | jq '.'

# POST endpoints take a JSON body (note -X POST):
scripts/crawlora.sh -X POST /google/search '{"searchOption":{"q":"web scraping api"}}' | jq '.'
scripts/crawlora.sh -X POST /google/trends/explore/interest-over-time '{"keywords":["web scraping"]}' | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/bing/search?q=web%20scraping%20api" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Google, Bing,
Brave, DuckDuckGo, Yahoo, and Google Trends endpoint this skill uses (method,
path, params, description).

## Examples

- **SERP snapshot:** `POST /google/search` (and `/bing/search`) for a target query;
  record the ranked result titles/URLs to track positions over time.
- **Keyword expansion:** seed term → `/google/suggest` → for each suggestion,
  `POST /google/trends/explore/rising-queries` to find momentum.
- **Trend check:** `POST /google/trends/explore/interest-over-time` with
  `{"keywords":["electric bikes","e-bikes"]}` and compare the series.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public search results; respect each engine's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Search endpoints may return `503` when the engine serves a challenge page —
  retry or switch engines (Google ↔ Bing ↔ Brave). Google search is rate-limited
  to ~1 req/s (`429` on excess).
