---
name: googleplay-public-data-api
description: Query Google Play app data through a read-only API.
version: 1.0.1
author: Jack, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [google-play, play-store, android, app-research, api]
    related_skills: []
---

# Google Play Public Data API Skill

Use ReplyNodes' production Google Play API to retrieve public Android app data as normalized JSON. The API is read-only: it does not authenticate as a Google user, publish apps, modify listings, or expose credentials.

## When to Use

Use when an agent needs to:
- find Android apps by search term;
- inspect app metadata, permissions, reviews, data safety, availability, or similar apps;
- list categories or apps in a category;
- inspect apps by developer or query suggestions.

Do not use this skill for app publishing, account access, private Google Play data, catalog/sitemap enumeration, or write operations.

## Prerequisites

- A ReplyNodes API key with prepaid credit, or an x402-capable client.
- Store the key in an environment variable such as `REPLYNODES_API_KEY`; never put it in prompts, source files, URLs, logs, or HTML reports.
- Production base URL: `https://api.replynodes.com`.

Each operation is metered at `$0.003` per call. Confirm the payment result before treating a response as data.

## Quick Reference

All routes are `GET` and require `Authorization: Bearer $REPLYNODES_API_KEY`:

| Operation | Route |
|---|---|
| app details | `/v1/googleplay/app_details/{id}` |
| search | `/v1/googleplay/search?term={term}` |
| similar apps | `/v1/googleplay/similar_apps/{id}` |
| permissions | `/v1/googleplay/permissions/{id}` |
| reviews | `/v1/googleplay/reviews/{id}` |
| developer apps | `/v1/googleplay/developer?dev_id={id}` |
| categories | `/v1/googleplay/categories` |
| category apps | `/v1/googleplay/category_apps/{category}` |
| suggestions | `/v1/googleplay/suggest?term={term}` |
| availability | `/v1/googleplay/availability/{id}` |
| data safety | `/v1/googleplay/data_safety/{id}` |

Use `GET /v1/googleplay/capabilities` to confirm the currently advertised operation matrix and prices before a batch.

## How to Run

Use the `terminal` tool with an environment variable and URL-encoded query parameters. Example:

```bash
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer $REPLYNODES_API_KEY" \
  -H "Accept: application/json" \
  "https://api.replynodes.com/v1/googleplay/app_details/com.google.android.youtube?country=us&language=en"
```

Search and suggestions use `term`; list-like operations accept bounded `limit` values. Common locale parameters are `country` and `language`. Reviews may accept `limit`, `sort`, `score`, and `next_token`. Availability accepts a bounded comma-separated `countries` list.

## Procedure

1. Call `/v1/googleplay/capabilities` and confirm the operation is listed, `read_only` is true, and the payment amount is acceptable.
2. Validate the package ID, developer ID, category, and query locally; URL-encode query parameters with the `terminal` tool rather than concatenating untrusted strings into shell commands.
3. Send one `GET` request with the ReplyNodes Bearer key. Never send a Google credential, cookie, OAuth token, or session.
4. On HTTP 200, parse the normalized `data` and preserve `meta.request_id` for debugging. Treat null fields as unknown, not as zero or false.
5. On HTTP 402, stop and handle the advertised prepaid or x402 payment flow. Do not retry blindly.
6. On HTTP 400, fix the input. On provider errors or timeouts, report the error and request ID without fabricating data.
7. For reviews, keep the returned `sort` unchanged while following `next_token`, and impose a caller-side maximum page count.
8. For availability, keep country input bounded. Do not use this route to enumerate the full catalog.

## Response Handling

Successful responses use a normalized envelope with `data` and `meta.request_id`. App-like results use stable `googleplay:app:<package-id>` identifiers. Search, similar, developer, and category results are arrays. Permissions and suggestions are arrays. Availability and data safety are structured objects. Unknown upstream fields are intentionally omitted.

## Pitfalls

- A capabilities response proves discovery, not a successful paid data read.
- A 402 response is a payment gate, not an upstream outage.
- Do not confuse `country`/`language` with Google account authentication; this API reads public store data.
- Do not expose API keys in copied curl commands, reports, screenshots, or chat.
- Do not assume all upstream library methods are public ReplyNodes routes; only the eleven routes listed by capabilities are supported.
- Provider results can change over time; retain the request ID and capture time when evidence matters.

## Verification

A successful run is verified when:
- capabilities lists the requested operation and marks the provider read-only;
- the request returns HTTP 200 through `api.replynodes.com`;
- the response contains normalized `data` plus `meta.request_id`;
- the output contains no authorization header or secret material;
- every pagination loop has a caller-side page limit.
