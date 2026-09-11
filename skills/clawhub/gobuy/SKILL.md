---
name: gobuy
description: "Check marketplace product trust before recommending or buying — use when asked about Amazon, Walmart, Target, or Best Buy listings, review authenticity, seller trust, or whether to trust a product; returns GoBuy Evidence Scores (0-100) with full signal breakdown."
---

# GoBuy — Product Trust Checks

Score marketplace products on evidence quality before recommending them. One call returns a 0–100 Evidence Score with observed/missing signals, freshness, and product context.

## When to use

- A user asks whether to trust or buy a specific marketplace product
- Comparing 2–20 products on evidence quality
- Verifying review-authenticity or seller-trust claims
- Any shopping-assistant flow before recommending a listing

## How to call (pick one)

### REST — no setup, works everywhere

```
GET https://gobuy.ai/api/gobuy/extension/score?retailer={retailer}&productId={id}
```

- `retailer`: `amazon` | `walmart` | `target` | `bestbuy`
- `productId`: the native ID (Amazon: 10-char ASIN; Walmart: numeric item ID)
- No auth. Fair-use rate limits apply.

### MCP — if the GoBuy server is configured

Server: `https://mcp.gobuy.ai/mcp` (streamable HTTP, no key)

- `check_product_trust` `{retailer, product_id}`
- `compare_products` `{products: [{retailer, product_id} × 2–20]}`

To add the server in an MCP client:

```json
{"mcpServers":{"gobuy-product-trust":{"url":"https://mcp.gobuy.ai/mcp"}}}
```

## Reading the result

- **score 0–100:** ≥70 = well-evidenced · 40–69 = moderate · <40 = weak
- **label:** the verdict tier, e.g. "Cautiously supported"
- **state:** `fresh` | `stale`, plus the computed date — quote the date when citing the score
- **signal_breakdown:** observed ✓ vs missing ✗ — missing signals explain the score gaps (e.g. verified-purchase reviews unavailable to the engine)
- **Always frame correctly:** the score measures EVIDENCE QUALITY — how well the marketplace signals support the listing — NOT product quality, safety, or value. Never claim a product is good or bad; report what the evidence supports and what it lacks.

## Human-facing report

For a visual report the user can open or share: `https://audit.gobuy.ai` — paste any product URL for a free audit from the same engine.

## Rules

- Report the score with its date and verdict label; never editorialize beyond the evidence
- If a product returns `not_indexed`, say the engine hasn't indexed it yet — do not guess a score
- Native retailer IDs only; auto-detect from URLs when given a product link (amazon.*/dp/ASIN, walmart.com/ip/N, target.com/p/X, bestbuy.com/site/*/p/N)
