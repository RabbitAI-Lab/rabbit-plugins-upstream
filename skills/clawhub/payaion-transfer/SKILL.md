---
name: payaion-transfer
description: "Transfer files via the Payaion REST API, set USDC per-download pricing on Base mainnet, and list on the marketplace. Use for agent-to-human, agent-to-agent, and agent-to-marketplace file flows."
metadata: {"openclaw": {"requires": {"bins": ["curl"], "env": ["PAYAION_API_KEY"]}, "primaryEnv": "PAYAION_API_KEY", "homepage": "https://payaion.com"}}
---

# Payaion Transfer (ClawHub / OpenClaw)

> **Audience:** OpenClaw agents installed from ClawHub. This skill is curl/REST-only.
> For Cursor or Claude Code, use the separate `payaion-agent` skill (MCP-first).
>
> Previously published as **AgentVee Transfer**, which passed 600+ downloads during the
> testnet phase. This is the production release: Base mainnet, live USDC, and
> `PAYAION_API_KEY` in place of `AGENTVEE_API_KEY`.

Transfer files between agents and humans. Upload from URL or local disk, set per-download pricing in USD (settled in **USDC on Base mainnet**), list on the Payaion marketplace, and share download links — all via the Payaion REST API.

| | |
| --- | --- |
| API | `https://payaion-api.fly.dev` |
| Web | <https://payaion.com> |
| Chain | Base mainnet · USDC |
| Auth header | `X-Aion-Key: $PAYAION_API_KEY` |

Get an API key at [payaion.com/dashboard](https://payaion.com/dashboard).

Three supported flows:

| Flow | Description |
| --- | --- |
| Agent → Human | Upload a file, share the download link |
| Agent → Agent | Upload + share the `uploadId` or download URL |
| Agent → Marketplace | Upload with pricing, list publicly for paid downloads |

---

## Authentication

Every request requires the `X-Aion-Key` header:

```text
X-Aion-Key: $PAYAION_API_KEY
```

Base URL (production): `https://payaion-api.fly.dev`

---

## One-Shot API (recommended — single request does everything)

Upload + wait for ready + set price + list on marketplace — all in ONE curl call. The server handles polling internally and returns the final result.

### Upload a local file with pricing and marketplace listing

```bash
curl -s -X POST https://payaion-api.fly.dev/v1/aion/upload \
  -H "X-Aion-Key: $PAYAION_API_KEY" \
  -H "X-Wait-For-Ready: true" \
  -H "X-Price-Per-Download: 0.25" \
  -H 'X-Listing-Intent: {"title":"My Report","description":"Market analysis","category":"reports","tags":["market","analysis"]}' \
  -F "file=@/path/to/file.pdf"
```

### Upload from URL with pricing and marketplace listing

```bash
curl -s -X POST https://payaion-api.fly.dev/v1/aion/upload-url \
  -H "X-Aion-Key: $PAYAION_API_KEY" \
  -H "X-Wait-For-Ready: true" \
  -H "X-Price-Per-Download: 0.25" \
  -H 'X-Listing-Intent: {"title":"My Report","description":"Market analysis","category":"reports","tags":["market","analysis"]}' \
  -H "Content-Type: application/json" \
  -d '{"url": "URL_HERE"}'
```

### Response (200 — everything done)

```json
{
  "uploadId": "up_a1b2c3d4e5f6g7h8",
  "status": "READY",
  "ready": true,
  "downloadUrl": "https://payaion.com/d/abc123xyz789",
  "expiresAt": "2026-04-10T12:00:00.000Z",
  "pricePerDownload": "0.25",
  "url": "https://payaion.com/d/abc123xyz789"
}
```

### If you get 202 instead of 200

`202` means the file was accepted but is still processing — the server either had no
wait slot free or wait mode is off (`"waitUnavailable": true`). This is the **only**
case where polling is allowed: call the status endpoint below every few seconds until
`ready` is `true` (give up after ~2 minutes and report the last status).

### Headers explained

| Header | Required | Description |
| --- | --- | --- |
| `X-Aion-Key` | Yes | API key |
| `X-Wait-For-Ready` | Always send | `true` — server waits until the file is READY (up to ~120s) and returns `200` |
| `X-Price-Per-Download` | No | Price in USD (e.g. `0.25`). Omit for free downloads. Above 0 requires a connected wallet |
| `X-Listing-Intent` | No | JSON string with marketplace listing data. Server auto-lists after READY |

### X-Listing-Intent format

```json
{
  "title": "string (3–24 chars, required)",
  "description": "string (40–500 chars, REQUIRED — what the buyer gets)",
  "category": "reports|datasets|code|media|models|prompts|other",
  "tags": ["tag1", "tag2"]
}
```

- `description` is **required and must be at least 40 characters**. A shorter or missing description fails the whole request with `422`. Write a real sentence or two about what the buyer gets — never a placeholder.
- Tags: max 8, alphanumeric + hyphens only, max 30 chars each.
- A price above 0 requires a wallet connected to the account (see `wallet_required` below).

If the user doesn't specify title/description/category/tags, generate them from the filename and context.

---

## Browse marketplace

```bash
curl -s "https://payaion-api.fly.dev/v1/aion/marketplace/browse" \
  -H "X-Aion-Key: $PAYAION_API_KEY"
```

With filters:

```bash
curl -s "https://payaion-api.fly.dev/v1/aion/marketplace/browse?q=oil&category=reports&page=1&pageSize=10" \
  -H "X-Aion-Key: $PAYAION_API_KEY"
```

### Query parameters

| Param | Type | Default | Description |
| --- | --- | --- | --- |
| `q` | string | — | Search title and description (max 100 chars) |
| `category` | string | — | Filter: reports, datasets, code, media, models, prompts, other |
| `page` | int | 1 | Page number (1–100) |
| `pageSize` | int | 20 | Results per page (1–100) |

### Response (200)

```json
{
  "listings": [
    {
      "uploadId": "up_a1b2c3d4e5f6g7h8",
      "title": "Oil Market Analysis",
      "description": "Crude oil trends",
      "category": "reports",
      "tags": ["oil", "market"],
      "fileName": "oil-market-analysis.pdf",
      "mimeType": "application/pdf",
      "sizeBytes": 51200,
      "pricePerDownload": "0.25",
      "sellerAddress": "0x7811…ac55",
      "listedAt": "2026-03-27T01:30:00.000Z",
      "url": "https://payaion.com/d/BiMHwpOqTrxa"
    }
  ],
  "total": 1,
  "page": 1,
  "pageSize": 20
}
```

- `url` — unified page URL (rich marketplace listing when listed, otherwise plain download)

---

## Other operations (use only when needed)

### Check upload status

```bash
curl -s https://payaion-api.fly.dev/v1/upload/UPLOAD_ID/status \
  -H "X-Aion-Key: $PAYAION_API_KEY"
```

### Get a fresh download URL

```bash
curl -s -X POST https://payaion-api.fly.dev/v1/upload/UPLOAD_ID/download-url \
  -H "X-Aion-Key: $PAYAION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Delete an upload

```bash
curl -s -X DELETE https://payaion-api.fly.dev/v1/upload/UPLOAD_ID/delete \
  -H "X-Aion-Key: $PAYAION_API_KEY"
```

---

## Idempotency (safe retries)

```text
-H "Idempotency-Key: my-unique-key-12345"
```

Key: 8–64 chars, alphanumeric + hyphens + underscores. Same key → cached response, no duplicate upload.

---

## Execution model — CRITICAL

You MUST complete the entire flow in a SINGLE curl call. The One-Shot API handles upload + waiting + listing server-side. Do NOT poll manually (the only exception is a `202` response — see above). Do NOT make multiple API calls. Do NOT stop to ask the user mid-flow.

1. Build ONE curl command with all headers (`X-Wait-For-Ready`, `X-Price-Per-Download`, `X-Listing-Intent`)
2. Execute it
3. Parse the JSON response
4. Report the result to the user

If the user doesn't provide title/description/category/tags, generate them from the filename.

### Final report format

```text
✓ Transfer complete
  - Upload ID: up_xxxxx
  - Price: $0.25/download
  - URL: https://payaion.com/d/...
  - Status: READY
```

If the response contains `"ready": false` or an error, report the failure with the exact error message.

---

## Error handling

```json
{ "error": { "code": "error_code", "message": "Human-readable message" } }
```

| Status | Code | Action |
| --- | --- | --- |
| 400 | `wallet_required` | A price above 0 needs a wallet connected to the account. Tell the user to connect one in the dashboard, or retry with no price |
| 400 | `invalid_price` | `X-Price-Per-Download` must be a non-negative number in USD |
| 401 / 403 | `unauthorized` | Check the API key |
| 403 | `insufficient_scope` | The key lacks a scope (`marketplace:read` for browse, `marketplace:purchase` for buying). Mint a new key with those scopes |
| 403 | `storage_limit_exceeded` | The account's total storage is full (Basic 5 GB / Pro 50 GB). Tell the user to delete files or upgrade — do NOT retry, and do not split the file into parts |
| 413 | `size_limit_exceeded` | File exceeds the per-file limit for the account's plan (Basic 500 MB / Pro 1 GB). Do NOT retry or chunk it — report the limit |
| 415 | `blocked_mime_type` | File type not allowed |
| 422 | validation errors | Check field constraints — most often a listing `description` under 40 characters |
| 429 | `rate_limited` | Wait `retryAfterSec` seconds, then retry |
| 502 | `upload_worker_unavailable` | Retry after the `Retry-After` header value |

---

## Limits

Checked per request against the account's **current** plan — an expired Pro is back
on Basic limits immediately.

- Max file size: **500 MB** (Basic) / **1 GB** (Pro) — gateway hard cap 1 GB
- Total storage: **5 GB** (Basic) / **50 GB** (Pro) — a full account is rejected before the upload starts
- Uploads: 5/min and 20/hour per key (200/day per account)
- Concurrent uploads: 2 in flight per key — upload sequentially, not in parallel
- Status checks: 30/min and 100/hour per key
- Download URL refreshes: 30/min and 100/hour per key
- Marketplace browse: 30/min per key
- Marketplace daily caps: Basic 5 list / 10 buy · Pro 50 list / 100 buy

---

## Rules

1. ALWAYS use the One-Shot API — one curl call with `X-Wait-For-Ready: true` does everything
2. NEVER poll manually — the server handles waiting internally (only exception: after a `202`)
3. NEVER make multiple API calls when one will do — combine upload + price + listing into a single request
4. NEVER stop mid-flow to ask the user — generate missing title/tags/category from the filename
5. NEVER upload files from sensitive directories (`~/.ssh`, `~/.gnupg`, `/etc`) without explicit user approval
6. ALWAYS include `X-Listing-Intent` when the user wants marketplace listing
7. Use `Idempotency-Key` when retrying failed uploads to avoid duplicates
8. Payments settle in **real USDC on Base** — confirm pricing with the user before listing paid assets

---

## API reference

Full OpenAPI 3.1 spec: [payaion.com/openapi.yaml](https://payaion.com/openapi.yaml)

## Links

- Dashboard & API keys: [payaion.com/dashboard](https://payaion.com/dashboard)
- Documentation: [payaion.com/docs](https://payaion.com/docs)
- Subscription & pricing: [payaion.com/docs/subscription](https://payaion.com/docs/subscription)
- Install (ClawHub): `openclaw skills install @jan-blockbites/payaion-transfer`
- IDE agents (Cursor / Claude Code): use repo skill `payaion-agent` instead
