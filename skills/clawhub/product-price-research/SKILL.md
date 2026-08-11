---
name: product-price-research
description: Researches products, prices, sellers, and reviews across major online marketplaces and big-box retailers (Amazon, eBay, Shopify stores, Shop.app, Target, Costco, Zalando, Walmart) using the Crawlora API, returning clean JSON. Use when the user asks to find a product, compare prices or sellers, track listings, or pull marketplace/retailer reviews — instead of scraping store pages.
---

# Product & price research

Look up and compare products, prices, sellers, and reviews across Amazon,
eBay, Shopify storefronts, Shop.app, Target, Costco, Zalando, and Walmart —
all as normalized JSON from the Crawlora API, with no HTML scraping.

## When to use this skill

- "What does X cost on Amazon / eBay / Target / Walmart?" or "compare prices
  for X across sellers/retailers."
- "Find listings for X" / "search this Shopify store" / "what's in this collection?"
- "Pull reviews / ratings for this product or seller."
- "Track this product's price / variants / availability."
- Competitive pricing, catalog, or marketplace-review research.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

Pick the marketplace, then the job:

1. **Search / discover** — `/amazon/search`, `/ebay/search`, `/shopify/products`,
   `/shop-app/search`, `/target/search`, `/costco/search`, `/walmart/search`,
   and `/zalando/search` (this one **requires `market`** — a Zalando country
   storefront code like `de`, `fr`, `com`; list them via `/zalando/markets`)
   to find candidate products by keyword.
2. **Detail** — fetch a specific product (`/amazon/product`, `/ebay/item`,
   `/shopify/products/{handle}`, `/shop-app/products/{id}`,
   `/target/product` (`tcin`), `/costco/product/{id}`, `/walmart/product/{item_id}`,
   `/zalando/product` (`sku`+`market`)) for price, variants, specs.
3. **Sellers** — for eBay/Shop.app, resolve the seller/shop (`/ebay/seller/...`,
   `/shop-app/shops/{handle}`) to compare offers.
4. **Reviews** — pull product/seller reviews where available
   (`/shop-app/products/{id}/reviews`, `/ebay/seller/.../feedback`,
   `/target/reviews`, `/costco/product/{id}/reviews`, `/walmart/product/{item_id}/reviews`).
5. **Compare** the JSON fields (price, currency, rating, seller) and answer.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Search a marketplace (GET, key=value params):
scripts/crawlora.sh /amazon/search k="standing desk" | jq '.'
scripts/crawlora.sh /ebay/search q="mechanical keyboard" | jq '.'
scripts/crawlora.sh /shop-app/search query="running shoes" | jq '.'
scripts/crawlora.sh /target/search q="standing desk" | jq '.'
scripts/crawlora.sh /walmart/search q="standing desk" | jq '.'
scripts/crawlora.sh /zalando/search q="running shoes" market=de | jq '.'

# Product detail:
scripts/crawlora.sh /amazon/product asin=B0XXXXXXX | jq '{title,price}'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/amazon/search?k=laptop" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Amazon,
eBay, Shopify, Shop.app, Target, Costco, Zalando, and Walmart endpoint this
skill uses (method, path, params, description).

## Examples

- **Cross-marketplace price compare:** search `/amazon/search` and `/ebay/search`
  for the same query, collect `price` from each, and present the spread.
- **Seller due diligence:** `/ebay/seller/{seller}` + `/ebay/seller/{seller}/feedback`
  to summarize a seller's rating and recent feedback before buying.
- **Shopify catalog audit:** `/shopify/products` (paginate) to list a store's
  catalog with prices, then flag items above/below a threshold.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public product/listing pages; respect each marketplace's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- Results are paginated — pass `page` (and `count` where supported) to walk listings.
- **Zalando always needs `market`** (no default storefront) — resolve valid
  codes via `/zalando/markets` if unsure.
