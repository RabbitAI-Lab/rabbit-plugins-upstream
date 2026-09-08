---
name: news-create
description: Create and publish one Tradebee website news article under an exact enabled language and selected news group, after the user approves the final payload.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# news-create

## Overview

Use the Tradebee Website Builder Open API to create and publish one news article. Select the language with `languages-get` and the group with `newsgroup-read`, show the exact payload, and run only after explicit confirmation.

## Input Parameters

Authentication uses only the configured `BEE_API_KEY` environment variable. Never place API keys in inputs, prompts, examples, logs, or chat. Send only the site and business data needed for this request to the external Tradebee API.

### `language` (string, **Required**)

Copy one exact enabled language code returned by `languages-get`. Do not guess, translate, or normalize it.

### `news` (object, **Required**)

Complete news payload.

#### `news.newsgroup_id` (integer, **Required**)

Positive news-group ID selected from `newsgroup-read` under the same language.

#### `news.publisher` (string, Optional)

Publisher name, up to 100 characters.

#### `news.publication_date` (string, **Required**)

Valid display date in `yyyy/M/d` format, for example `2026/8/21`.

#### `news.source` (string, Optional)

News source, up to 100 characters.

#### `news.title` (string, **Required**)

Title containing 2–500 characters.

#### `news.cover_image` (object, Optional)

One optional cover image, decoded size at most 500 kB.

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Non-empty image label. |
| `base64` | string | Image data with MIME prefix, for example `image/jpeg;base64,...`. |

#### `news.tags` (array<string>, **Required**)

Provide 1–6 tags, each containing 3–50 characters.

#### `news.summary` (string, **Required**)

Plain-text summary containing 10–500 characters.

#### `news.description` (string, **Required**)

HTML fragment only. Before generating this field, call `rule-get` with the exact selected `language` and exact `scene=news.description`. Generate the description only after that call succeeds, and follow the complete returned rule payload instead of guessing its layout, styling, structure, theme, or link rules. The current rule requires one root `<section>` with a unique scoped class and one embedded `<style>` block at the end; do not use any inline style attributes or external stylesheet links. Do not include `<h1>` and prefer `<h2>`–`<h6>`. Each `<img src>` may use a normal HTTP(S) URL or `data:image/...;base64,...`. At most 50 `<img>` tags are allowed and each image must be 500 kB or smaller. The 100,000-character limit is calculated after removing `<img>` tags. The server uploads supported base64 images and replaces their `src` values with URLs. If `rule-get` fails, stop instead of generating or publishing an assumed layout.

#### `news.seo` (object, Optional)

| Field | Type | Description |
|-------|------|-------------|
| `title` | string | SEO title, up to 90 characters. |
| `description` | string | SEO description, up to 200 characters. |
| `keywords` | string | Comma-separated keywords, up to 6 values and 120 total characters. |

### `confirmation` (object, **Required**)

| Field | Type | Description |
|-------|------|-------------|
| `approved` | boolean | Must be `true` only after the user approves the exact language and news payload. |
| `summary` | string | Non-empty summary of the approved payload. |

## Output Structure

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean | Request status. |
| `msg` | string | Response message. |
| `data` | object/null | Created record information. |

`data.news_id` is the created ID and `data.url` is its preview URL. Return both when present; let the user decide whether to preview it.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `news.newsgroup_id` | `newsgroup-read` | `list[].newsgroup_id` |
| `news.description` | `rule-get` | `scene=news.description` rule payload |

## Usage Example

```json
{
  "language": "en",
  "confirmation": { "approved": true, "summary": "Create the approved English news article." },
  "news": {
    "newsgroup_id": 8,
    "publisher": "Marketing Team",
    "publication_date": "2026/8/21",
    "source": "Company website",
    "title": "New product launch",
    "tags": ["product", "launch"],
    "summary": "A concise news summary with enough detail.",
    "description": "<section class=\"news-detail-a1b2c3\"><h2>Launch</h2><p>Details.</p><style>.news-detail-a1b2c3{color:#333}</style></section>",
    "seo": { "title": "SEO title", "description": "SEO description", "keywords": "product,launch" }
  }
}
```

## Response Example

```json
{"status":true,"msg":"News created successfully","data":{"news_id":8,"url":"example.com/n8/new-product-launch.htm"}}
```
