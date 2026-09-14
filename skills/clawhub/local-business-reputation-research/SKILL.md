---
name: local-business-reputation-research
description: Researches public local-business profiles, ratings, reviews, complaints, scam reports, menus, and photos across Yelp, BBB, Trustpilot, and OpenTable using the Crawlora API. Use for vendor due diligence and reputation comparisons, with evidence and source boundaries kept explicit.
---

# Local business reputation research

Build an evidence-backed public reputation brief for a business or venue. Use
Yelp, BBB, Trustpilot, and OpenTable as distinct sources and keep profile data,
reviews, complaints, scam reports, menus, and photos separate.

## When to use this skill

- Compare local businesses or restaurants before hiring or visiting.
- Find a business profile, service area, rating history, or public complaints.
- Review recent customer themes and representative excerpts.
- Check public BBB scam reports or OpenTable restaurant details and menus.

## Research workflow

1. Resolve the business on each platform with its own search endpoint. Match by
   name, address, phone, domain, and service area; never merge on name alone.
2. Pull profile and review data from Yelp, BBB, or Trustpilot. Keep each site's
   rating scale, review count, date range, moderation labels, and sampling rules.
3. Use BBB complaints and Scam Tracker as reported records, not proof of legal
   wrongdoing. Use Trustpilot and Yelp reviews as platform-specific samples.
4. Use OpenTable for restaurant discovery, menu, and review context. Separate
   reservation metadata and menu availability from reputation evidence.
5. Report corroborated facts, conflicting records, unresolved identity matches,
   and a small set of linked excerpts. Do not infer fraud, safety, or service
   quality from a single review or rating alone.

## Examples

```sh
scripts/crawlora.sh /yelp/search term="plumber" location="Austin, TX" | jq '.'
scripts/crawlora.sh /bbb/search query="Acme Plumbing" location="Austin, TX" | jq '.'
scripts/crawlora.sh /trustpilot/business-units/search q="example.com" | jq '.'
scripts/crawlora.sh /opentable/search query="Italian Austin" | jq '.'
```

## Notes and limits

- Public pages only; no private customer records, account access, booking,
  payment, or review submission occurs.
- Ratings and complaints are platform-reported and may be incomplete,
  moderated, duplicated, or attached to a different branch.
- Preserve collection time, source URL or ID, business address, and platform
  when presenting a reputation comparison.
- Avoid identifying private individuals from review text; quote only what is
  needed to support the business-level finding.

See [`reference/endpoints.md`](reference/endpoints.md) for the complete generated endpoint list.
