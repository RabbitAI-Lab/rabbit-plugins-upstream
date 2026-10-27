---
name: catalog
description: Find published domains by project description or keywords and check their current prices. Use the anonymous public catalog interfaces when a user asks about domains for sale on this site.
---

# Read the Namegarage domain catalog

Read the [quickstart](https://namegarage.com/docs/quickstart.md) for request examples and the
[OpenAPI reference](https://namegarage.com/openapi.json) for exact parameters and response schemas.

## Choose an interface

- Use `GET https://namegarage.com/api/search?q=...` to search by project description or keywords.
- Use `GET https://namegarage.com/domains.json` when you need the complete public listing data.

- A remote Streamable HTTP MCP client can connect to `https://namegarage.com/api/mcp` and call `search_domains` or `get_domain`.


No authentication or SDK installation is required. Do not request credentials or guess package names.
For JavaScript or TypeScript, the optional official package is `@namegarage/sdk@0.1.0` on npm.
Its `searchDomains()` method accepts `maxPrice` and `maxLength`; response fields keep the API names.
Search supports a whole-USD `max_price`, `tier`, `tld`, `max_length`, and `limit` up to 50.

## Interpret results

Use the price returned by search or MCP; a null price means offer-only.
Follow the returned domain URL before a purchase decision. Results do not reserve names.
Absence from the catalog does not prove registration or availability elsewhere.
If `meaning` is unavailable, describe the returned matches as keyword matches.
Honor `Retry-After` and `retry_after_seconds` before retrying.

## Stay within the public service

Only use the documented public read interfaces. They cannot buy or reserve names, send messages,
create accounts, sign in, or access the private portfolio. Do not call other site API routes.
