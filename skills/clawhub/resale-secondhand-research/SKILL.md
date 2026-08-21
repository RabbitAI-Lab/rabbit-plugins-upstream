---
name: resale-secondhand-research
description: Researches secondhand, resale, and handmade marketplaces via the Crawlora API — Poshmark, Etsy, Vinted, StockX, Mercari, Depop, and Whatnot — returning clean JSON. Use when the user wants to find or compare listings, check a seller/shop, look up sneaker/streetwear resale prices, or research handmade/vintage goods.
---

# Resale & secondhand marketplace research

Search listings, sellers, and prices across seven C2C resale, streetwear,
and handmade marketplaces as normalized JSON from the Crawlora API — no
scraping app storefronts.

## When to use this skill

- "Find <item> for sale on <platform>" / compare listings.
- "What's this seller's/shop's closet/storefront like?"
- "What's the resale price for these sneakers?" (StockX)
- "Find handmade/vintage <item>" (Etsy).
- "What's live right now?" (Whatnot livestream shopping).

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Poshmark** — `/poshmark/search` (`query`) to find listings;
   `/poshmark/listing/{id}` for detail; `/poshmark/closet/{username}` for a
   seller's storefront; `/poshmark/brand/{name}` / `/poshmark/category/{path}`
   to browse.
2. **Etsy** — `/etsy/search` (`q`) for listings; `/etsy/listing/{id}` (+
   `/reviews`) for detail; `/etsy/shop/search` / `/etsy/shop/{id}` (+
   `/listings`, `/reviews`) for a shop's storefront.
3. **Vinted** — `/vinted/catalog` (`search_text`) for listings;
   `/vinted/item/{id}` for detail; `/vinted/member/{id}` for a seller;
   `/vinted/brand`/`/vinted/category` to filter by brand/category id
   (resolve ids via `/vinted/brands`/`/vinted/categories`).
4. **StockX** — `/stockx/search` **requires `category`** (e.g. `sneakers`,
   `apparel`, `collectibles`; `query` is the optional keyword within it) to
   find a `slug`, then `/stockx/product/{slug}` for market data;
   `/stockx/releases` for upcoming drops.
5. **Mercari** — `/mercari/search` (`query`) for listings;
   `/mercari/item/{id}` for detail; `/mercari/autocomplete` for query suggestions.
6. **Depop** — `/depop/search` (`query`, plus filters like `brand_ids`,
   `condition`, `price_min`/`price_max`) for listings; `/depop/item/{slug}`
   for detail; `/depop/shop/{username}` for a seller's storefront.
7. **Whatnot** — `/whatnot/browse` **requires `category`** to list live/
   upcoming shows; `/whatnot/live/{id}` for one livestream's detail.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Search a marketplace:
scripts/crawlora.sh /poshmark/search query="vintage levis jacket" | jq '.'
scripts/crawlora.sh /etsy/search q="handmade ceramic mug" | jq '.'
scripts/crawlora.sh /vinted/catalog search_text="north face jacket" | jq '.'

# StockX (category required):
scripts/crawlora.sh /stockx/search category=sneakers query="jordan 4" | jq '.'

# Seller/shop lookup:
scripts/crawlora.sh /depop/shop/<handle> | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/mercari/search?query=nintendo%20switch" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Poshmark,
Etsy, Vinted, StockX, Mercari, Depop, and Whatnot endpoint this skill uses.

## Examples

- **Cross-platform price compare:** search the same item on Poshmark,
  Depop, Vinted, and Mercari, then diff asking prices.
- **Sneaker resale check:** `/stockx/search category=sneakers query="..."` →
  `/stockx/product/{slug}` for current market price vs. retail.
- **Seller vetting:** `/poshmark/closet/{username}` or `/depop/shop/{username}`
  before buying, to check listing count and activity.
- **Handmade sourcing:** `/etsy/search` for a category, then
  `/etsy/shop/{id}/reviews` on top shops before ordering a custom piece.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public listing/storefront pages; no purchases or
  offers are made.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **StockX and Whatnot require a `category`** on their search/browse
  endpoints — check `reference/endpoints.md` for accepted values before calling.
- Vinted brand/category filters need numeric ids — resolve via
  `/vinted/brands`/`/vinted/categories` first if you only have a name.
