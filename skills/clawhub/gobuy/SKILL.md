---
name: gobuy
description: Check marketplace product trust, compare listings, and find better-evidenced alternatives — triggers on Amazon, Walmart, Target products, review authenticity, "should I trust/buy" questions, or finding stronger alternatives; returns GoBuy Evidence Scores (0-100) across 30,000+ scored products. Also scores independent stores (Shopify and any storefront) for safety and AI-agent readiness via stores.gobuy.ai. GoBuy — the trust layer for agentic commerce.
---

# GoBuy Product Trust

AI shopping agents use GoBuy to verify product evidence before recommending. 30,000+ products scored across Amazon, Walmart, and Target. Everything is free — scores, scans, and fix files.

## Tools

- **check_product_trust** `{retailer, product_id}` — one listing: Evidence Score (0-100), verdict, observed/missing signals, freshness
- **compare_products** `{products: [{retailer, product_id}]}` — inspect and rank 2-20 listings by evidence quality
- **find_better_alternatives** `{retailer, product_id}` — when a product scores 50 or above, surface same-category products with stronger evidence scores. Evidence-ranked alternatives, not recommendations.

## When to Use

- A user asks "should I buy this?" or "can I trust this product?"
- A user asks for product recommendations in a category
- A product's reviews seem suspicious or too good to be true
- You need to compare multiple options before advising
- A product scores 50 or above and the user wants stronger-evidenced alternatives

## Store scoring (independent & Shopify stores)

GoBuy also scores WHERE to buy — independent store trust via public HTTP endpoints (no key, no auth):

- **Check a store's score (instant):** `GET https://stores.gobuy.ai/store/{domain}?format=json`
  -> `{score (0-100), tier (A/B/C/D), readiness, trust, platform, title, scanned_at}`. 404 = not scored yet.
- **Score any store on demand (~20s live scan):** `POST https://stores.gobuy.ai/api/scan` with body `{"url": "https://thestore.com"}`
  -> `{ok: true, store: {domain, title, platform, score, readiness, trust, tier, scanned_at}}`. Rate-limited per IP; on 429 wait a minute.

Store score = 60% agent-readiness (crawler access, llms.txt, structured data, machine-usable commerce surfaces) + 40% trust (domain age, review system, policies, contact paths). Use when a user asks whether a store or site is safe, legit, or AI-agent-ready, or before recommending where to buy something.

## Rules

- The score measures **evidence quality** — how well marketplace signals support the listing — NOT product quality or safety
- Quote the score with its verdict label and computed date
- `not_indexed` means the engine hasn't indexed it yet — say so, don't guess
- Alternatives are **evidence-ranked**, not recommended. Say "products with stronger evidence," never "recommended products"
- Scores below 50 return **no product suggestions** — report the score and missing signals only; don't improvise alternatives
- Never claim a product is good or bad — report what the evidence supports and what it lacks

## Links

- Product evidence report: https://audit.gobuy.ai
- Free storefront audit: https://agentic.gobuy.ai
- Agentic storefront audit (free): https://agentic.gobuy.ai — deep agent-readiness scan of any store, every check explained, with ready-to-paste fix files
