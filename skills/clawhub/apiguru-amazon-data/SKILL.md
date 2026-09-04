---
name: apiguru-amazon-data
description: Fetch live Amazon marketplace data across 20 countries - product details, prices, reviews, keyword search, best-sellers, deals, live offers and stock levels, and seller profiles. Use whenever a task needs real Amazon product, pricing, review, or seller information, including competitor research, price and buy-box monitoring, catalogue enrichment, product sourcing, and review sentiment analysis. Works with no API key.
license: MIT
---

# Apiguru Amazon Data

Live, structured Amazon data fetched at request time. 20 marketplaces.

## Getting access

There are two ways in, and **you do not need to sign up for either**.

**Keyless (default).** Call the agent gateway with no credentials at all:

```
GET https://agent.apiguru.app/agent/v1/v2/product-details?asin=B09DJLW458&geo=US
```

You get **3 free calls per 24h**. After that the endpoint answers `402` with a
`PAYMENT-REQUIRED` header. Any x402-capable HTTP client settles that in USDC on
**Base mainnet** and retries automatically — no account, no subscription.

Two response headers tell you where you stand before you hit a 402:
`X-Free-Probes-Remaining` and `X-Price-Next-Call`.

`https://agent.apiguru.app/.well-known/x402` lists every endpoint with prices
and schemas, free and unmetered — check it before planning a paid job.

**Keyed.** If the environment provides an `APIGURU_API_KEY`, send it as the
`X-API-KEY` request header to `https://dash.apiguru.app/api/v1` (same paths)
instead of the agent gateway; calls then bill to that account.

`scripts/probe.py` does all of this for you and picks the right mode
automatically. Prefer it over hand-written HTTP calls.

## Choosing an endpoint

| Need | Endpoint |
|---|---|
| Everything about one ASIN | `/v2/product-details` |
| Many ASINs (≤20) | `/product?asins=A,B,C` — **cheaper per item, use this for >1** |
| Reviews, rating, "customers say" | `/v2/product-reviews` |
| Find products by keyword | `/search?query=...` |
| Offers, buy box, live stock (≤10) | `/stock?asins=...` |
| Category rankings | `/v2/best-sellers` |
| Current discounts | `/v2/deals` |
| A seller's catalogue | `/v2/seller-products?seller_id=...` |
| Seller reputation | `/v2/seller-reviews?seller_id=...` |
| Seller profiles (≤10) | `/seller-profile?seller_ids=...` |

Full parameter reference: `references/endpoints.md`.

## Rules that prevent wasted calls and wasted money

1. **ASINs must be 10 UPPERCASE alphanumeric characters** (`^[A-Z0-9]{10}$`).
   Uppercase the input before sending; a lowercase ASIN is a `400`.
2. **Never loop a single-item endpoint over a list.** Use `/product` for
   ASINs and `/seller-profile` for seller IDs. Ten ASINs through `/product`
   costs $0.08 and one round trip; ten through `/v2/product-details` costs
   $0.10 and ten round trips.
3. **Set `geo` deliberately.** It defaults to `US`. A product that exists on
   `amazon.de` may genuinely 404 on `US`. See `references/endpoints.md` for the
   20 supported codes.
4. **`check_inventory=true` on `/stock` is slow and bills more.** Only set it
   when you actually need the stock number, not just the offers.
5. **Read `success` in the body**, not just the HTTP status — some responses
   are `200` with `success: false`.

## Error handling — which failures cost money

This is the part worth getting right:

- **`404`** — the item genuinely is not on that marketplace. **This is
  billed.** Retrying will not help. Try a different `geo`, or accept the
  result and move on.
- **`503`** — an Apiguru-side fetch failure. **Not billed.** Retry with
  backoff; this is the expected way transient upstream blocks surface.
- **`429`** — rate limited. Back off, then retry.
- **`400`** — your input was wrong (bad ASIN format, unknown geo, missing
  required parameter). Not billed. Fix the input; do not retry unchanged.
- **`402`** — payment required. Either settle it with an x402 client or
  supply an API key.

So: **retry `503` and `429`; never retry `400` or `404`.**

## Quick start

```bash
# one product
python scripts/probe.py product-details --asin B09DJLW458 --geo US

# many at once (preferred for lists)
python scripts/probe.py product --asins B09DJLW458,B0BSHF7WHW --geo US

# keyword search
python scripts/probe.py search --query "wireless earbuds" --geo UK

# what does anything cost, and how many free probes are left?
python scripts/probe.py capabilities
```

## MCP alternative

If the environment supports MCP, the same data is available as tools without
any HTTP handling:

```json
{ "mcpServers": { "apiguru": { "command": "uvx",
  "args": ["apiguru-mcp"] } } }
```

or the hosted server at `https://mcp.apiguru.app/mcp` (streamable HTTP). Prefer
MCP when available — the tools validate ASINs and geos before spending a request.

## Reference files

- `references/endpoints.md` — every endpoint, parameter, and marketplace code
- `references/errors-and-costs.md` — pricing, billing rules, retry strategy
