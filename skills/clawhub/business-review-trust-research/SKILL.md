---
name: business-review-trust-research
description: Researches software/SaaS products and business reputation via the Crawlora API — Product Hunt launches/makers/alternatives, Trustpilot business reviews, TrustMRR revenue-verified startups, and Capterra software reviews — returning clean JSON. Use when the user wants a product's launch/review history, a company's Trustpilot reputation, a startup's verified revenue, or software alternatives/reviews before buying.
---

# Business & software review research

Look up product launches, business reputation, verified startup revenue,
and software reviews across four platforms as normalized JSON from the
Crawlora API — no scraping review-site pages.

## When to use this skill

- "What did this product launch as on Product Hunt? Who made it?"
- "What are people saying about <company> on Trustpilot?"
- "How much revenue does this startup actually make?" (TrustMRR — payment-provider-verified)
- "What are the reviews / alternatives for this software?" (Capterra)
- Vendor due-diligence before buying or partnering.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

1. **Product Hunt** — `/producthunt/search` (`query`) to find a product
   `id`; `/producthunt/product/{id}` for detail (+ `/about`, `/makers`,
   `/launches`, `/reviews`, `/alternatives`, `/customers`).
   `/producthunt/leaderboard` and `/producthunt/category/{slug}/products`
   cover browsing/trending.
2. **Trustpilot** — `/trustpilot/business-units/search` (`q`) to find a
   business `slug`; `/trustpilot/business/{slug}` for the profile (+
   `/reviews`, `/related`). `/trustpilot/categories` / `/categories/search`
   browse by industry.
3. **TrustMRR** — `/trustmrr/startups` to browse, or `/trustmrr/startup/{slug}`
   for one company's payment-provider-verified revenue profile (see also
   the `crawlora-datasets` skill's `trustmrr` dataset for bulk/aggregate
   queries). `/trustmrr/leaderboard` ranks by MRR; `/trustmrr/categories`
   browses by category.
4. **Capterra** — `/capterra/search` (`q`) to find a `product_id`, then
   `/capterra/product` for detail and `/capterra/product/reviews` for user reviews.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Product Hunt:
scripts/crawlora.sh /producthunt/search query="AI coding assistant" | jq '.'

# Trustpilot:
scripts/crawlora.sh /trustpilot/business-units/search q="acmecorp.com" | jq '.'
scripts/crawlora.sh /trustpilot/business/acmecorp.com/reviews | jq '.'

# TrustMRR:
scripts/crawlora.sh /trustmrr/leaderboard | jq '.'

# Capterra:
scripts/crawlora.sh /capterra/search q="project management software" | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/producthunt/leaderboard" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for every Product
Hunt, Trustpilot, TrustMRR, and Capterra endpoint this skill uses.

## Examples

- **Vendor due diligence:** `/trustpilot/business/{slug}` (reputation) +
  `/capterra/product` + `/capterra/product/reviews` (feature-level
  feedback) before signing a software contract.
- **Launch retrospective:** `/producthunt/product/{id}` + `/launches` +
  `/makers` to see how a product performed and who built it.
- **Bootstrapped-revenue research:** `/trustmrr/startup/{slug}` for one
  company's verified MRR trend, or `/trustmrr/leaderboard` for the top
  earners in a category.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public listing/review pages.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **Trustpilot's `slug` is usually the business's domain** (e.g.
  `acmecorp.com`), not a display name — resolve via
  `/trustpilot/business-units/search` if unsure.
- Reviews/lists are paginated — pass `page` to walk beyond the first page.
