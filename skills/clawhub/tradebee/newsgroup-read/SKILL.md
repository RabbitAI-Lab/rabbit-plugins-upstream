---
name: newsgroup-read
description: Read Tradebee news groups by exact language, optional group ID, selected fields, and pagination for group selection or content operations.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# newsgroup-read

## Overview

Read all news groups under one language or one exact group selected by ID.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only requested site data to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`.

### `newsgroup_id` (integer, Optional)

Positive exact group ID. Omit it to list all news groups.

### `fields` (array<string>, Optional)

Omit or send `[]` for all fields. Supported values: `newsgroup_id`, `language`, `group_name`, `tags`, `brief_description`, `seo`, `newsgroup_url`, `create_time`, `update_time`.

### `pagination` (object, Optional)

`current_page` defaults to 1 and must be at least 1. `page_size` defaults to 5 and must be 1–10. Continue only when `has_next_page=true`, using the exact returned `next_page`.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.pagination` returns `current_page`, `page_size`, `total_page`, `total_count`, `has_next_page`, and `next_page`; `data.list` contains groups.

### `data.list[]`

| Field | Type | Description |
|-------|------|-------------|
| `newsgroup_id` | integer | News-group ID. |
| `language` | string | Site language. |
| `group_name` | string | Group name. |
| `tags` | array<string> | Group tags. |
| `brief_description` | string | Plain-text description. |
| `seo` | object | `title`, `description`, and `keywords`. |
| `newsgroup_url` | string | Group preview/detail URL. |
| `create_time` | string(datetime) | ISO 8601 creation time. |
| `update_time` | string(datetime) | ISO 8601 update time. |

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |

## Usage Rules

- Omit `newsgroup_id` for all groups; provide it only for one exact group.
- Omit `fields` for all supported fields.
- When returning choices, include `newsgroup_id` and `newsgroup_url` when available.
- Follow `next_page`; do not infer pagination.

## Usage Examples

```json
{"language":"en","pagination":{"current_page":1,"page_size":5}}
```

```json
{"language":"en","newsgroup_id":8,"fields":["newsgroup_id","group_name","newsgroup_url","seo"],"pagination":{"current_page":1,"page_size":5}}
```
