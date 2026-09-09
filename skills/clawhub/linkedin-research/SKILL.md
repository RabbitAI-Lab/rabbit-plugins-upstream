---
name: linkedin-research
description: Looks up LinkedIn company, product, and showcase pages by ID via the Crawlora API, returning clean JSON. Use when the user wants a company's LinkedIn profile info, a product page, or a showcase page — instead of scraping LinkedIn directly. Covers company/product/showcase pages only, not personal LinkedIn profiles.
---

# LinkedIn company research

Look up LinkedIn company, product, and showcase page info by ID — all as
normalized JSON from the Crawlora API, no browser automation or LinkedIn
login required.

## When to use this skill

- "What's <company>'s LinkedIn company info (industry, size, description)?"
- "Pull the LinkedIn product page for <product ID>."
- "Get details on this LinkedIn showcase page."
- Competitor company profiling or firmographic research using LinkedIn IDs.
- Enriching a company record with its LinkedIn company/product/showcase data.

## Setup (one-time)

- Get a free Crawlora API key (2,000 credits/mo, no card) at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- `export CRAWLORA_API_KEY=sk_your_key_here`
- All requests: `x-api-key: $CRAWLORA_API_KEY` against
  `https://api.crawlora.net/api/v1`. Missing/invalid key → `401`.

## How it works

Pick the page type, then call it by ID:

1. **Company** — `/linkedin/company/{id}` — detailed company info (industry,
   size, description, and related fields) by LinkedIn Company ID.
2. **Product** — `/linkedin/product/{id}` — detailed product info by LinkedIn
   Product ID.
3. **Showcase page** — `/linkedin/showcase/{id}` — detailed info about a
   LinkedIn showcase page by ID.

Full endpoint list, methods, and params: [`reference/endpoints.md`](reference/endpoints.md).

## Calling the API

```sh
# Company info:
scripts/crawlora.sh /linkedin/company/1035 | jq '.'

# Product info:
scripts/crawlora.sh /linkedin/product/urn:li:organizationProduct:123456 | jq '.'

# Showcase page info:
scripts/crawlora.sh /linkedin/showcase/1234567 | jq '.'
```

Raw `curl` fallback:

```sh
curl -fsS -H "x-api-key: $CRAWLORA_API_KEY" \
  "https://api.crawlora.net/api/v1/linkedin/company/1035" | jq '.'
```

## Endpoint reference

See [`reference/endpoints.md`](reference/endpoints.md) for the full LinkedIn
company/product/showcase endpoint list this skill uses.

## Examples

- **Company profiling:** `/linkedin/company/{id}` for a target company to
  pull industry, size, and description before an outreach or comparison doc.
- **Product-page audit:** `/linkedin/product/{id}` to check how a competitor
  positions a specific product line on LinkedIn.
- **Showcase-page check:** `/linkedin/showcase/{id}` to see how a company
  segments a sub-brand or business unit on its LinkedIn showcase page.

## Notes & limits

- **Credits / pay-on-success:** billed only on `2xx`; free tier 2,000 credits/mo.
  Key at [https://crawlora.net](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills).
- **Public data only** — public company/product/showcase pages; no login, no
  private content. Respect LinkedIn's terms.
- **Security:** key lives in `CRAWLORA_API_KEY` only — never hardcode, query-param, or commit it.
- **Scope: companies/products, not personal profiles.** This skill covers
  LinkedIn company, product, and showcase pages by ID only — there is no
  personal-profile lookup endpoint; don't imply one exists.
- All three endpoints take a LinkedIn ID as a path parameter — no search or
  discovery endpoint is available to find that ID, so it must come from the
  page URL or an upstream source.
