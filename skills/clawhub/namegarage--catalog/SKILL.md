---
name: catalog
description: Find published Namegarage domains, look up listing details, compare payment options, and suggest alternatives when a user is choosing a domain for a project.
---

# Read the Namegarage domain catalog

Read the [quickstart](https://namegarage.com/docs/quickstart.md) and
[OpenAPI contract](https://namegarage.com/openapi.json) for exact parameters and response schemas.
The [developer changelog](https://namegarage.com/developers/changelog/) records compatible interface versions.
No account, API key, cookie, or SDK installation is required.

## Choose the public read operation


A remote Streamable HTTP MCP client can connect to `https://namegarage.com/api/mcp`:

- `search_domains`: search by project description or keywords, optionally filtered by budget, suffix, length or tier.
- `get_domain`: look up a complete name. Use returned `description` and `use_cases`; keep empty or withheld copy empty. Potential uses are suggestions, not verified suitability or trademark rights.
- `get_purchase_options`: compare the current outright price and published standard zero-down lease-to-own schedules.
- `suggest_alternatives`: find other published names for a complete reference name. Add a project `query`, whole-USD `max_price`, and `limit` when useful. The reference need not be in our catalog; it is excluded before the result limit.


HTTP clients can use these canonical GET routes:

- `https://namegarage.com/api/search?q=...`
- `https://namegarage.com/api/domain?name=...`
- `https://namegarage.com/api/purchase-options?name=...`
- `https://namegarage.com/api/alternatives?name=...&query=...&max_price=3000&limit=5`

URL-encode parameter values. `/domains.json` is the full published catalog snapshot;
use the dynamic operations for current availability and prices.
For JavaScript or TypeScript, the optional official package is `@namegarage/sdk@0.3.0`.
It provides `getCatalog()` and `searchDomains()`, plus
`getDomain()`, `getPurchaseOptions()` and `suggestAlternatives()`.
Search uses `maxPrice` and `maxLength` in the SDK; wire responses retain the API field names.

## Interpret results and compare payments

A missing lookup returns `found: false` and `domain: null`. This does not prove
that the name is unregistered or unavailable elsewhere. Alternatives are published
Namegarage listings, not registrar availability checks.

A null price means offer-only, never free. For payment comparisons, use
`domain.purchase_options` from the server. Compare `buy_outright.total_usd` with
the lease's monthly payment, final payment, total and extra cost versus outright.
The monthly amount applies through the penultimate payment. A cash-only discount
may not reduce `lease_base_price_usd`. Empty `lease_to_own` means no standard
standalone plan is published; null `buy_outright` means offer-only.
Do not calculate replacement prices or invent payment plans. Send the buyer to
the returned page for current terms, other payment choices and additional checkout fees.

Search accepts whole-USD `max_price`, `tier`, `tld`, `max_length`, and `limit` up to 50.
`max_price` and SDK `maxPrice` cap the outright cash price, not a monthly payment.
For a monthly budget, compare the returned lease schedules rather than using
that monthly amount as a cash-price filter. A cash-budget filter excludes offer-only names. Honor `Retry-After` and
`retry_after_seconds`. If `meaning` is unavailable, describe matches as keyword matches.
Use general project descriptions: search text is sent to Namegarage, so omit
confidential project details unless the user chooses to disclose them.

## Stay within the public service

Use only documented public reads. They cannot buy or reserve names, create quotes,
start checkout, make offers, send messages, create accounts, sign in, or access the
private portfolio. Do not call other site API routes. Results never reserve a name;
follow the returned public page before a purchase decision.


## Delegate domain selection with A2A

The anonymous [A2A 1.0 Agent Card](https://namegarage.com/.well-known/agent-card.json)
advertises `select_domains` at `https://namegarage.com/api/a2a`. Read the
[A2A request guide](https://namegarage.com/docs/a2a.md) before calling it.
Use `SendMessage` and `A2A-Version: 1.0`, with one data part containing `query`
and typed `max_price`, `tld`, `max_length`, `tier` or `limit` (default 5, maximum 10).
Do not embed constraints in query prose. `clarification_required` means no search ran;
repeat a corrected full brief. Responses are direct Messages, with no persistent task.
Use only returned listings, prices, descriptions and potential uses; do not invent
names, relax filters or infer trademark clearance. This adapter cannot purchase or reserve.
If A2A is unavailable, use the documented anonymous MCP or HTTP search operation.



## UCP catalog and buyer handoff

Discover UCP only through `https://namegarage.com/.well-known/ucp`. If unavailable, use the HTTP or MCP catalog above. Protocol revision `2026-08-25` supports `dev.ucp.shopping.catalog.search`, `dev.ucp.shopping.catalog.lookup` and `dev.ucp.shopping.permalink` when advertised. Read the [UCP guide](https://namegarage.com/docs/ucp).

Use the advertised REST shopping endpoint for `/catalog/search`, `/catalog/lookup` and `/catalog/product`. POST reads require `UCP-Agent` with an exact reviewed HTTPS platform profile and a fresh RFC 9421 ES256 signature from its pinned key. Use the platform signing transport, or the SDK custom `fetch` option to sign requests. They do not authenticate the buyer. Search defaults to 10 results, caps pages at 20, and uses snapshot-bound cursor pagination. Lookup accepts at most 20 IDs. Follow pagination rather than guessing exhaustion. On recoverable `cursor_expired`, restart the same search without a cursor; on `invalid_request`, correct malformed or mismatched inputs.

Only available firm outright purchases are variants. Prices are explicit USD minor units; context and eligibility claims confer no discount or authority. Avoid personal or confidential query context. Check `ucp.status`, messages and `Retry-After`, including on HTTP 200. A missing product means unavailable in this catalog.

Use the returned ACE domain ID and quantity one with the advertised permalink endpoint. The `@namegarage/sdk@0.3.0` helpers `getUcpProfile()`, `searchUcpCatalog()`, `lookupUcpCatalog()`, `getUcpProduct()` and local `createPurchaseLink()` preserve this boundary. The buyer reviews the selected domain and current website terms and completes checkout on Namegarage. Opening a link grants no purchase authority or reservation. Do not call checkout, order, payment or identity endpoints as catalog operations.
