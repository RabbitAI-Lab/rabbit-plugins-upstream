# Mentionkit Public API v1 Reference

This file documents the stable public API v1 surface that is already exposed in the repo and public docs.

## Base URL

`https://api.mentionkit.com`

## Authentication

Send your Mentionkit API key as a Bearer token:

```bash
Authorization: Bearer YOUR_API_KEY
```

## What API v1 is for

Use API v1 for:

- mention feed access
- project reads
- keyword reads
- organization summary and usage reads
- mention review status updates
- generated comment requests

Do not treat API v1 as a replacement for Mentionkit MCP workflows. It does not expose:

- workflow context tools
- shortlist-first opportunity tools
- source fetch and verification flow
- public keyword creation in the documented API v1 surface

## Response conventions

Read endpoints return plain JSON objects.

Most common shapes:

- list responses return `items`
- mention lists also return `nextCursor`, `limit`, and `sort`
- collection endpoints like projects and keywords return `items` plus `total`
- error responses return `{ "error": "..." }`

Pagination rule:

- `GET /api/v1/mentions` returns `nextCursor`
- omit `cursor` for the first page
- pass the previous `nextCursor` value back unchanged

## Stable endpoints

### `GET /api/v1/mentions`

Purpose:

- list raw mentions
- page through the mention feed

Documented query fields:

- `sort`
- `cursor`
- `projectId`
- `category`
- `platform`
- `relevance`
- `keywords`
- `tags`
- `startdate`
- `enddate`

Documented category values:

- `brand`
- `industryinsights`
- `competitorkeywords`

Practical response:

- `items`
- `nextCursor`
- `limit`
- `sort`

Each mention item includes fields like:

- `id`
- `platform`
- `keywordValue`
- `projectId`
- `authorHandle`
- `text`
- `sourceCreatedAt`
- `createdAt`
- `relevance`
- `relevanceText`
- `tags`
- `comment`
- `commentStatus`

### `POST /api/v1/mentions/:id`

Purpose:

- update mention review status

Request body:

- `commentStatus`

Allowed values:

- `1`
- `-1`

Practical response:

- `id`
- `commentStatus`
- `commentStatusAt`

### `PUT /api/v1/mentions/:id/comment`

Purpose:

- generate a comment suggestion for a mention

Request body:

- optional `slug`

Practical response:

- mention DTO with updated comment content when generation succeeds

### `GET /api/v1/keywords`

Purpose:

- list tracked keywords

Practical response:

- `items`
- `total`

Each keyword includes fields like:

- `id`
- `value`
- `category`
- `englishOnly`
- `mentionCount`
- `projectId`
- `platforms`
- `createdAt`
- `updatedAt`

### `GET /api/v1/projects`

Purpose:

- list projects in the active organization

Practical response:

- `items`
- `total`

Each project includes fields like:

- `id`
- `name`
- `siteUrl`
- `siteDomain`
- `bizName`
- `description`
- `type`
- `faviconUrl`
- `createdAt`
- `updatedAt`

### `GET /api/v1/me`

Purpose:

- read organization summary, counts, limits, and usage

Practical response includes:

- `organization`
- `counts`
- `limits`
- `usage`

## Gotchas

- Public docs use the original mention query names: `platform`, `keywords`, `startdate`, and `enddate`.
- API v1 is closer to raw data access than to MCP workflow guidance.
- For shortlist-style review, use Mentionkit MCP instead of trying to recreate the workflow with API v1 only.
- API errors are simple string envelopes, not MCP-style structured tool errors.
