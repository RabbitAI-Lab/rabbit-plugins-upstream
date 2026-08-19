---
name: amazon-research
description: Researches products, prices, availability, and search suggestions on Amazon (amazon.com) using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Amazon, look up an ASIN's price/details, or pull Amazon autocomplete/keyword suggestions — instead of scraping Amazon pages.
---

# Amazon product research

Look up and search Amazon products — pricing, availability, overview data,
inline reviews, and search suggestions — all as normalized JSON from the
Crawlora API, with no HTML scraping.

## When to use this skill

- "What does X cost on Amazon?" / "find this product on Amazon."
- "Search Amazon for X" and return candidate listings.
- "Look up this ASIN" / "get price and availability for B0XXXXXXX."
- "What does Amazon autocomplete suggest for this keyword?"
- Competitive pricing or catalog research scoped to Amazon.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Search** — `/amazon/search` with a keyword (`k`) to find candidate
   products; paginate with `page`, sort with `s`.
2. **Detail** — `/amazon/product/{asin}` to fetch a specific product's
   pricing, availability, overview data, inline review samples, and
   descriptive content; optionally scope by `currency`/`language`.
3. **Suggest** — `/amazon/suggest/{keyword}` for Amazon's own typeahead
   keyword suggestions, useful for discovering related search terms before
   running a full search.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Search Amazon (GET, key=value params):
scripts/crawlora.sh /amazon/search k="standing desk" | jq '.'

# Product detail (ASIN is a path param):
scripts/crawlora.sh /amazon/product/B0XXXXXXX | jq '{title,price}'

# Search suggestions (keyword is a path param):
scripts/crawlora.sh /amazon/suggest/standing | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/amazon/search?k=laptop" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Amazon
endpoint this skill uses (method, path, params, description).

## Examples

- **Price check by ASIN:** `/amazon/product/{asin}` and read `price` /
  `availability` from the response.
- **Keyword-to-listing pipeline:** `/amazon/suggest/{keyword}` to expand a
  rough query into Amazon's own suggested terms, then `/amazon/search` on
  the best ones to collect candidate listings.
- **Catalog sweep:** paginate `/amazon/search` with `page` for a keyword,
  collecting `asin` + `price` from each result to build a price snapshot.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public Amazon product/listing pages; respect Amazon's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Results are paginated — pass `page` on `/amazon/search` to walk listings.
- `asin` and `keyword` are **path** params (substituted into the URL), not
  query params — pass them as the last path segment, e.g.
  `/amazon/product/B0XXXXXXX`, not `asin=B0XXXXXXX`.
- All endpoints target `amazon.com` only.
