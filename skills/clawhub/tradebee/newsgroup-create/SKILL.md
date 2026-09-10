---
name: newsgroup-create
description: Create and publish one Tradebee news group under an exact enabled language with tags, description, and SEO metadata after explicit confirmation.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# newsgroup-create

## Overview

Create one news group under an exact enabled site language. Show the final payload and run only after the user approves it.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it in inputs, prompts, examples, logs, or chat. Send only required business data to the external Tradebee API.

### `language` (string, **Required**)

Select and copy one exact enabled code from `languages-get`; do not guess or translate it.

### `newsgroup` (object, **Required**)

#### `newsgroup.group_name` (string, **Required**)

Group name containing 2–300 characters.

#### `newsgroup.tags` (array<string>, **Required**)

Provide 1–6 tags, each containing 1–50 characters.

#### `newsgroup.brief_description` (string, Optional)

Plain-text description up to 300 characters.

#### `newsgroup.seo` (object, Optional)

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | SEO title, up to 90 characters. |
| `description` | string | SEO description, up to 200 characters. |
| `keywords` | string | Comma-separated keywords, up to 6 values and 120 total characters. |

### `confirmation` (object, **Required**)

| Field | Type | Description |
|-------|------|-------------|
| `approved` | boolean | Must be `true` only after the exact language and payload are approved. |
| `summary` | string | Non-empty restatement of the approved operation. |

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.newsgroup_id` is the created group ID and `data.url` is the group preview URL. Return both when present.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |

## Usage Example

```json
{
  "language":"en",
  "confirmation":{"approved":true,"summary":"Create the approved Company News group in English."},
  "newsgroup":{"group_name":"Company News","tags":["company","announcement"],"brief_description":"Latest company announcements.","seo":{"title":"SEO title","description":"SEO description","keywords":"company,announcement"}}
}
```

## Response Example

```json
{"status":true,"msg":"NewsGroup created successfully","data":{"newsgroup_id":8,"url":"example.com/newsid8/company-news.htm"}}
```
