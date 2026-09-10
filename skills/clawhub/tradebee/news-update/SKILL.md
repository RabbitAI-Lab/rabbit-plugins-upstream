---
name: news-update
description: Update one Tradebee news article after reading it and writing a local pre-update backup; supports content, metadata, group, image, and SEO changes.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# news-update

## Overview

Update one existing news record. Read and back up the current record before mutation; do not run if the read or backup write fails.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only requested fields to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language matching the target record.

### `news` (object, **Required**)

`news_id` is required. Every other field is optional and must be omitted when unchanged.

| Field | Type | Rules |
|-------|------|-------|
| `news_id` | integer | Positive ID selected from `news-read`. |
| `newsgroup_id` | integer | Positive replacement group from `newsgroup-read`; omit to keep current group. |
| `publisher` | string | Up to 100 characters; omit if unchanged. |
| `publication_date` | string | Valid date, normally `yyyy/M/d`; omit if unchanged. |
| `source` | string | Up to 100 characters; omit if unchanged. |
| `title` | string | 2–500 characters; omit if unchanged. |
| `cover_image` | object | Optional `{name, base64}` image up to 500 kB. |
| `tags` | array<string> | 1–6 items, each 3–50 characters. |
| `summary` | string | 10–500 characters. |

#### `news.description` (string, Optional)

New HTML fragment. Generate this field only when the user wants to replace the news body. Before generating it, call `rule-get` with the exact selected `language` and exact `scene=news.description`; continue only after that call succeeds and follow its complete rule payload instead of guessing layout, styling, structure, theme, or link rules. The current rule requires one root `<section>` with a unique scoped class and one embedded `<style>` block at the end; do not use any inline style attributes or external stylesheet links. Do not include `<h1>` and prefer `<h2>`–`<h6>`. `<img src>` supports HTTP(S) URLs or `data:image/...;base64,...`, up to 50 images and 500 kB each. The 100,000-character check removes `<img>` tags first. The server uploads base64 images and replaces their `src` values with URLs. If `rule-get` fails, stop instead of generating or publishing an assumed layout. An empty string or omitted field leaves the current description unchanged and does not require `rule-get`.

#### `news.seo` (object, Optional)

Omit the object or individual unchanged fields. Limits: `title` 90, `description` 200, and comma-separated `keywords` 120 total characters and up to 6 values.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user sees and approves the language, target ID, exact changed fields, and local backup. `summary` must restate that approval.

### Automatic Backup

- Reads the current record with `news-read`.
- Writes under `backups/news-update/` relative to the installed skill root.
- If capture or file writing fails, the update does not run.
- Success includes `backup.storage.file_path`, `raw_read_response`, `snapshot`, `restore_payload`, and `restore_limitations`.
- A changed cover image is not fully restorable because read returns URLs, not original base64.

## Output Structure

Top level contains `status`, `msg`, `data`, and `backup`. `data` contains `news_id` and may contain `url`. Return the ID, preview URL, and backup path when present.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `news.news_id` | `news-read` | `list[].news_id` |
| `news.newsgroup_id` | `newsgroup-read` | `list[].newsgroup_id` |
| `news.description` | `rule-get` | `scene=news.description` rule payload |

## Usage Example

```json
{"language":"en","confirmation":{"approved":true,"summary":"Update news 8 with the shown fields and create the local backup first."},"news":{"news_id":8,"title":"Updated news title","description":"<section class=\"news-detail-a1b2c3\"><h2>Update</h2><p>Details.</p><style>.news-detail-a1b2c3{color:#333}</style></section>"}}
```

## Response Example

```json
{"status":true,"msg":"News updated successfully","data":{"news_id":8,"url":"example.com/n8/updated-news-title.htm"},"backup":{"storage":{"file_path":"backups/news-update/example.json"},"restore_payload":{"language":"en","news":{"news_id":8}}}}
```
