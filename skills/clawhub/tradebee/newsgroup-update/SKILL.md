---
name: newsgroup-update
description: Update one Tradebee news group after reading it and writing a local pre-update backup; supports name, tags, description, and SEO changes.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# newsgroup-update

## Overview

Update one exact news group after automatically reading and backing up its current state. Stop before mutation if capture or file writing fails.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only explicitly changed fields to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language matching the target group.

### `newsgroup` (object, **Required**)

| Field | Type | Rules |
|-------|------|-------|
| `newsgroup_id` | integer | Required positive ID selected from `newsgroup-read`. |
| `group_name` | string | 2–300 characters; omit if unchanged. |
| `tags` | array<string> | 1–6 items, each 1–50 characters; omit if unchanged. |
| `brief_description` | string | Up to 300 characters; omit if unchanged. |
| `seo` | object | Omit the object or unchanged nested fields. |

SEO limits are `title` 90, `description` 200, and comma-separated `keywords` 120 total characters and up to 6 values.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user approves the language, target ID, exact changes, and local backup. `summary` must restate that approval.

### Automatic Backup

- Reads the current group with `newsgroup-read`.
- Writes under `backups/newsgroup-update/` relative to the installed skill root.
- The backup includes the raw read response, snapshot, requested payload, and best-effort restore payload.
- If capture or file writing fails, the update does not run.
- Success returns `backup.storage.file_path`; this skill currently has no known restore limitations.

## Output Structure

Top level contains `status`, `msg`, `data`, and `backup`. `data` contains `newsgroup_id` and may contain `url`. Return the ID, preview URL, and backup path when present.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `newsgroup.newsgroup_id` | `newsgroup-read` | `list[].newsgroup_id` |

## Usage Example

```json
{"language":"en","confirmation":{"approved":true,"summary":"Update English news group 8 and write the backup first."},"newsgroup":{"newsgroup_id":8,"group_name":"Updated Company News","tags":["company"],"brief_description":"Updated description"}}
```

## Response Example

```json
{"status":true,"msg":"NewsGroup updated successfully","data":{"newsgroup_id":8,"url":"example.com/newsid8/updated-company-news.htm"},"backup":{"storage":{"file_path":"backups/newsgroup-update/example.json"},"restore_payload":{"language":"en","newsgroup":{"newsgroup_id":8}}}}
```
