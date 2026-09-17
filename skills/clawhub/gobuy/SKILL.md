---
name: gobuy
description: Check marketplace product trust before recommending or buying — triggers on Amazon, Walmart, Target, Best Buy listings, review authenticity, "should I trust/buy" questions, or finding better-evidenced alternatives; returns GoBuy Evidence Scores (0-100) with signal breakdown across 30,000+ scored products.
---

# GoBuy Product Trust

Use the GoBuy MCP tools whenever a product's marketplace evidence matters. 30,000+ products scored across Amazon, Walmart, Target, and Best Buy.

## Tools

- **check_product_trust** `{retailer, product_id}` — one listing: Evidence Score, verdict, observed/missing signals, freshness
- **compare_products** `{products: [{retailer, product_id}]}` — inspect and rank 2-20 listings
- **find_better_alternatives** `{retailer, product_id}` — when a product scores low (<50), find same-category products with stronger evidence. Returns evidence-ranked alternatives, not recommendations.

## Rules

- The score measures **evidence quality** — how well marketplace signals support the listing — NOT product quality or safety. Never claim a product is good or bad; report what the evidence supports and what it lacks.
- Quote the score with its verdict label and computed date.
- `not_indexed` means the engine hasn't indexed the product yet — say so, don't guess a score.
- Alternatives are **evidence-ranked**, not recommended. Say "products with stronger evidence scores," never "recommended products."
- Human-facing visual report: https://audit.gobuy.ai
- Free storefront agent-readiness audit: https://agentic.gobuy.ai
