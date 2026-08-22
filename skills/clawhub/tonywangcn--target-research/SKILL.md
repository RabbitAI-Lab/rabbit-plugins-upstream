---
name: target-research
description: Researches Target's catalog — categories, products, filters, prices, questions, and reviews — using the Crawlora API, returning clean JSON. Use when the user asks to find a product on Target, browse a Target category, compare Target prices/availability by store, or pull Target product Q&A and reviews — instead of scraping target.com.
---

# Target research

Browse and search Target's catalog and pull product detail, pricing,
availability, questions, and reviews — all as normalized JSON from the
Crawlora API, with no HTML scraping.

## When to use this skill

- "What does X cost on Target?" or "find X on Target."
- "Browse this Target category" / "what's in Target's [department]?"
- "Filter Target results by [brand/size/price]."
- "Pull the Q&A / reviews for this Target product."
- "Check price or availability for this Target item at a specific store."

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Browse or search** — `/target/categories` lists the category menu and
   ids; `/target/category-products` (`category_id`) or `/target/search`
   (`q`) return paginated products plus the filter groups/options available
   for that result set.
2. **Filter** — `/target/filter-options` returns the dynamic filter groups
   for a query (`q`) or category (`category_id`) on its own, if you need
   them before browsing; pass selected option ids back through
   `filter_ids` (comma-separated) on category-products or search to narrow
   results.
3. **Detail** — `/target/product` (`tcin`) fetches full product content,
   images, price, rating, category, and store-level availability.
4. **Q&A and reviews** — `/target/questions` and `/target/reviews` (both
   keyed by `tcin`) pull paginated product questions/answers and written
   reviews.
5. **Compare** the JSON fields (price, rating, availability) across items
   or stores and answer.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Search Target (GET, key=value params):
scripts/crawlora.sh /target/search q="standing desk" sort=price-low | jq '.'

# Browse a category, filtered and priced for a store:
scripts/crawlora.sh /target/category-products category_id=5xtg6 store_id=1234 filter_ids=5xtvw | jq '.'

# Product detail:
scripts/crawlora.sh /target/product tcin=54191097 | jq '{title,price}'

# Reviews:
scripts/crawlora.sh /target/reviews tcin=54191097 per_page=20 | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/target/search?q=standing+desk" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Target
endpoint this skill uses (method, path, params, description).

## Examples

- **Category sweep with pricing:** `/target/categories` to find a
  department's `category_id`, then `/target/category-products` paginated
  with `store_id` set, to list local prices and availability.
- **Product due diligence:** `/target/product` for price/rating, then
  `/target/questions` and `/target/reviews` (both by `tcin`) to summarize
  what shoppers ask and say before recommending it.
- **Filtered search:** `/target/search` for a query, inspect the returned
  filter groups, then re-call with `filter_ids` set to narrow by
  brand/size/price band.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public Target product/category pages; respect Target's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Results are paginated — pass `page` (and `per_page`/`count` where supported) to walk listings.
- **Product identity is `tcin`** (numeric Target item id), not a SKU or ASIN —
  `/target/product`, `/target/questions`, and `/target/reviews` all key off it.
- **Pagination isn't uniform:** `category-products`/`search` use one-based
  `page` (max 50), while `questions`/`reviews` use zero-based `page` (also
  max 50 on reviews).
- `store_id` is optional but drives store-specific pricing and
  availability — omit it for a generic/national result.
