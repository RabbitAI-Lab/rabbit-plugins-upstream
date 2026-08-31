---
name: news-read
description: Read Tradebee website news by language, optional exact news or news-group filter, selected fields, and pagination.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# news-read

## Overview

Read published news records. Omit both filters for all news, provide `news_id` for one exact record, or provide `newsgroup_id` for one group; never combine the two filters.

## Input Parameters

Authentication uses only `BEE_API_KEY`. Never expose the key. Send only the minimum requested site data to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`.

### `news_id` (integer, Optional)

Positive exact news ID. Mutually exclusive with `newsgroup_id`.

### `newsgroup_id` (integer, Optional)

Positive group ID selected from `newsgroup-read` under the same language. Mutually exclusive with `news_id`.

### `fields` (array<string>, Optional)

Omit or send `[]` for all fields. Supported values: `news_id`, `language`, `group`, `publisher`, `publication_date`, `source`, `title`, `images`, `tags`, `summary`, `description`, `seo`, `news_url`, `create_time`, `update_time`.

### `pagination` (object, Optional)

`current_page` defaults to 1 and must be at least 1. `page_size` defaults to 5 and must be 1–10. Continue only while `data.pagination.has_next_page=true`, using the exact returned `next_page`; never guess the next page.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.pagination` contains `current_page`, `page_size`, `total_page`, `total_count`, `has_next_page`, and `next_page`. `data.list` contains the records.

### `data.list[]`

| Field | Type | Description |
|-------|------|-------------|
| `news_id` | integer | News ID. |
| `language` | string | Site language. |
| `group` | object | `newsgroup_id` and `group_name`. |
| `publisher` | string | Publisher. |
| `publication_date` | string | Display publication date. |
| `source` | string | News source. |
| `title` | string | News title. |
| `images` | array<string> | Cover-image URLs. |
| `tags` | array<string> | Tags. |
| `summary` | string | Plain-text summary. |
| `description` | string | News HTML; submitted base64 image sources are returned as server URLs. |
| `seo` | object | `title`, `description`, and `keywords`. |
| `news_url` | string | Preview/detail URL. |
| `create_time` | string(datetime) | ISO 8601 creation time. |
| `update_time` | string(datetime) | ISO 8601 update time. |

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `newsgroup_id` | `newsgroup-read` | `list[].newsgroup_id` |

## Usage Examples

```json
{"language":"en","pagination":{"current_page":1,"page_size":5}}
```

```json
{"language":"en","news_id":8,"fields":["news_id","title","news_url","update_time"],"pagination":{"current_page":1,"page_size":5}}
```

```json
{"language":"en","newsgroup_id":8,"pagination":{"current_page":1,"page_size":10}}
```

When presenting a list, include an available `news_id` and `news_url`; do not tell the user that previewing is mandatory.
