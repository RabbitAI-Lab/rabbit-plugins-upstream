# AstrMap API Reference

## Overview

This document provides detailed documentation for all AstrMap open API endpoints, request formats, response formats, and error codes.

> Source of truth: field names in this document are aligned with the server-side `server/src/api/v1/routes/route_external.py` and its underlying service implementations.

## Authentication

All API requests require authentication headers:

```
Authorization: Bearer {api_key}
Content-Type: application/json
```

> Note: API Key format is `sk_live_xxxxxxxxxxxxxxxx`

---

## Endpoint List

### 1. Endpoint Status Check

**Endpoint**: `POST /api/v1/external/device/status`

Check whether the user endpoint bound to the current API Key is online.

> Note (v2.2): The underlying model changed from `device` to `client_endpoint`.
> Field renames are reflected below (`online` → `is_alive`, `device_id` → `endpoint_id`,
> plus a new `endpoint_type`).

**Request Body**:
```json
{}
```

**Response (online)**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "is_alive": true,
    "endpoint_id": "endpoint_xxx",
    "endpoint_type": "desktop",
    "status": "idle"
  }
}
```

**Response (offline)**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "is_alive": false,
    "endpoint_id": null,
    "endpoint_type": null,
    "status": "offline"
  }
}
```

**Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| is_alive | bool | Whether the endpoint is online |
| endpoint_id | string \| null | Endpoint ID (null when offline) |
| endpoint_type | string \| null | Endpoint type: `desktop` / `extension` / `web_session` |
| status | string | Endpoint status: `idle` / `busy` / `offline` |

---

### 2. Create Task

**Endpoint**: `POST /api/v1/external/task/create`

Create a task and dispatch it to the device bound to the current account.

**Request Body**:
```json
{
  "platform": "amazon",
  "site": "US",
  "submit_content": "B09V3KXJPB",
  "is_auto": true
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| platform | No | amazon | Platform name |
| site | No | US | Site |
| submit_content | Yes | - | Input content, ASIN or product URL |
| is_auto | No | true | Auto-mode flag: `true` = auto analysis, `false` = collection only |

**Site Description**:
| site | Language |
|------|----------|
| US | English |
| CA | English |
| UK | English |
| DE | German |
| FR | French |
| IT | Italian |
| ES | Spanish |
| JP | Japanese |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "task_id": "TSK_xxx"
  }
}
```

> Note: This endpoint only returns `task_id`. For task name/status/other fields, call `POST /task/detail` afterwards.

---

### 3. Task Detail Query

**Endpoint**: `POST /api/v1/external/task/detail`

Query task details and status.

**Request Body**:
```json
{
  "task_id": "TSK_xxx"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": "TSK_xxx",
    "user_id": "user_xxx",
    "name": "Task name",
    "status": "SUCCESS",
    "platform": "amazon",
    "site": "US",
    "submit_content": "B09V3KXJPB",
    "parse_content": ["B09V3KXJPB"],
    "create_time": "2025-03-22 10:30:00",
    "update_time": "2025-03-22 10:35:00",
    "monitoring": false,
    "is_auto": true
  }
}
```

**Task Status Description**:
| Status | Description |
|--------|-------------|
| PENDING | Pending |
| DISPATCHING | Dispatching |
| COLLECTING | Collecting |
| COLLECTED | Collection complete (only `is_auto=false` stops here) |
| PROCESSING | Processing |
| ANALYZING | AI analyzing |
| SUCCESS | Completed |
| FAILED | Failed |
| CANCELLED | Cancelled |

---

### 4. Task List Query

**Endpoint**: `POST /api/v1/external/task/list`

Query task list.

**Request Body**:
```json
{
  "page": 1,
  "page_size": 20,
  "search_keyword": "B09",
  "filter_monitoring": false
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| page | No | 1 | Page number (equivalent to `current_page`) |
| page_size | No | 10 | Items per page (max 100) |
| search_keyword | No | "" | Search keyword (matches task name / ASIN) |
| filter_monitoring | No | false | Whether to return only monitoring tasks |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total": 100,
    "page_max": 5,
    "page": 1,
    "page_size": 20,
    "filter_monitoring": false,
    "search_keyword": "B09",
    "items": [
      {
        "id": "TSK_xxx",
        "name": "Task name",
        "status": "SUCCESS",
        "platform": "amazon",
        "site": "US",
        "asin_count": 1,
        "total_reviews": 335,
        "negative_reviews": 169,
        "create_time": "2026-07-05 22:33",
        "update_time": "2026-07-05 23:28",
        "monitoring": false
      }
    ]
  }
}
```

> Difference from `/task/detail`: list items are the **compact form** (includes counts `asin_count/total_reviews/negative_reviews`, **excludes** `submit_content / parse_content / is_auto / user_id`). Use `/task/detail` for full fields.

> ⚠️ **Common misread warning**: the semantic of `negative_reviews` **depends on `status`**:
> - `status="SUCCESS"`: `negative_reviews=0` means AI analysis confirmed **actually zero negatives**
> - `status="COLLECTED"` / `PENDING` / `DISPATCHING` / `COLLECTING`: AI has not run, the field is hard-coded `0`, which **does NOT** mean zero negatives
>
> AI Agents filtering / sorting by this field **must check `status` first**, otherwise "not-yet-analyzed" tasks will be misread as "zero-negative good products".

> Sort order (verified): default is `update_time` descending, NOT `create_time` — tasks with recent incremental / analysis / rename appear at the top.

---

### 4.1 Incremental Fetch

**Endpoint**: `POST /api/v1/external/task/incremental`

Create an incremental fetch for a **ready-state task** (`SUCCESS` / `CANCELLED` / `COLLECTED`), fetching new reviews since the last fetch. `FAILED` state is **NOT allowed**.

**Request Body**:
```json
{
  "task_id": "TSK_xxx"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID; must be in an allowed state: `SUCCESS` / `CANCELLED` / `COLLECTED` (**NOT `FAILED`**) |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "task_id": "TSK_xxx",
    "job_id": "JOB_xxx"
  }
}
```

**Use Cases**:
- Completed task needs latest review data
- Difference from creating a new task: input is the existing task ID (no need to re-enter ASIN), fetches incrementally
- Incremental fetch triggers full fetch + analysis; analysis deducts points

---

### 4.2 Task Rename

**Endpoint**: `POST /api/v1/external/task/rename`

Rename a task. Only updates the display name; does not change any other fields or state.

**Request Body**:
```json
{
  "task_id": "TSK_xxx",
  "name": "New task name"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |
| name | Yes | New task name |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "id": "TSK_xxx"
  }
}
```

> Note: The endpoint only returns the updated task ID. For full task fields, call `POST /task/detail` afterwards.

**Notes**:
- The task must belong to the caller's account (ownership is enforced server-side)
- Does not deduct points and has no prerequisites

**Error Codes** (server-side internal codes; on the wire they are wrapped as HTTP 400 with `detail.code = -1`; see "Error Handling Contract" at the end):
| Internal code | Typical msg |
|------|-------------|
| MissingRequiredParam | 未提供任务ID |
| VALIDATION_ERROR | 验证失败 (missing name or all update fields empty) |
| TaskNotFound | 找不到任务或权限不足 |
| TaskUpdateError | 更新任务失败 |

---

### 4.3 Manual Trigger Analysis

**Endpoint**: `POST /api/v1/external/task/{task_id}/trigger-analysis`

Manually trigger AI analysis for a collection-only task. Applicable to tasks with `is_auto=false` that stopped at `COLLECTED` status.

**Path Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID; status must be COLLECTED |

**Request Body**:
```json
{}
```

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "task_id": "TSK_xxx",
    "job_id": "JOB_xxx"
  }
}
```

**Status Flow After Trigger**: `COLLECTED` → `PROCESSING` → `ANALYZING` → `SUCCESS`

**Error Codes** (server-side internal codes; on the wire they are wrapped as HTTP 400 with `detail.code = -1`; see "Error Handling Contract" at the end):
| Internal code | Typical msg |
|------|-------------|
| MissingTaskId | 未提供任务ID |
| TaskNotFound | 任务不存在 |
| InvalidTaskStatus | 只有待分析状态的任务可以触发分析，当前状态: xxx |
| JobNotFound | 获取 Job 失败 |
| JobStatusUpdateFailed | 更新 Job 状态失败 |

---

### 4.4 Desktop Client Download Config

**Endpoint**: `GET /download-config.json`

A public config file (no API Key required) for retrieving desktop client download links.

**Response**:
```json
{
  "version": "1.0.0",
  "last_updated": "2026-04-27T14:31:08.795719Z",
  "downloads": {
    "macos": {
      "name_zh": "macOS Version",
      "name_en": "macOS Version",
      "url": "<actual download URL>",
      "version": "1.0.0",
      "size": "156MB",
      "requirements": {
        "min_version": "10.15",
        "recommended_memory": "8GB",
        "disk_space": "500MB"
      }
    },
    "windows": {
      "name_zh": "Windows Version",
      "name_en": "Windows Version",
      "url": "<actual download URL>",
      "version": "1.0.0",
      "size": "142MB",
      "requirements": {
        "min_version": "10",
        "recommended_memory": "8GB",
        "disk_space": "500MB"
      }
    }
  }
}
```

---

### 5. AI Insights Query

**Endpoint**: `POST /api/v1/external/analysis/insights`

Get AI insights. Returned as a flattened structure keyed by **three scenes** (competitor / improvement / marketing); each scene contains `insight_type → content(plain string)` pairs.

**Request Body**:
```json
{
  "task_id": "TSK_xxx"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "competitor_insights": {
      "<insight_type_a>": "<insight content string>",
      "<insight_type_b>": "..."
    },
    "improvement_insights": {
      "<insight_type_x>": "...",
      "<insight_type_y>": "..."
    },
    "marketing_insights": {
      "<insight_type_1>": "...",
      "<insight_type_2>": "..."
    }
  }
}
```

**Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| competitor_insights | object | Competitor-scene insights (key = insight_type, value = plain string content) |
| improvement_insights | object | Product-improvement-scene insights |
| marketing_insights | object | Marketing-copy-scene insights |

> When data is missing, all three fields return `{}` (empty objects). `insight_type` keys are defined by the server-side AI pipeline and may expand across versions; callers should read defensively (present → use, missing → skip) and not hard-code specific keys.

**Reference: typical `insight_type` keys** (observed as of 2026-07; **not guaranteed exhaustive or stable** — for structural understanding only):

| Scene | Common insight_type keys |
|-------|--------------------------|
| competitor_insights | `executive_summary` / `key_strength` / `key_problem` / `strategy_guide` |
| improvement_insights | `executive_summary` / `key_strength` / `key_problem` / `recommendation` / `priority_ranking` / `root_cause` |
| marketing_insights | `executive_summary` / `key_strength` / `word_of_mouth` / `material_library` |

---

### 6. Category-Tag Distribution

**Endpoint**: `POST /api/v1/external/analysis/category-tag-distribution/{task_id}`

Get category-tag distribution — a **three-level nested structure** (Dimension → Category → Tags). Supports `polarity` filter (negative/positive/all).

**Path Parameters**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |

**Request Body**:
```json
{
  "polarity": "negative"
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| polarity | No | negative | Polarity filter: `negative` / `positive` / `all` |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "category_tag_distribution": {
      "polarity": "negative",
      "dimensions": {
        "product": {
          "total_count": 42,
          "total_rate": "28.0%",
          "categories": {
            "quality": {
              "total_count": 20,
              "total_rate": "13.3%",
              "tags": [
                {"tag": "Workmanship issue", "count": 12, "rate": "8.0%"},
                {"tag": "Appearance defect", "count": 8, "rate": "5.3%"}
              ]
            }
          }
        },
        "service": { "total_count": 15, "total_rate": "10.0%", "categories": { "...": {} } },
        "experience": { "total_count": 8, "total_rate": "5.3%", "categories": { "...": {} } }
      }
    }
  }
}
```

> ⚠️ Note: `data` wraps a `category_tag_distribution` key at the top; actual data starts from `data.category_tag_distribution.dimensions`.

**Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| category_tag_distribution.polarity | string | Echoes back the requested polarity |
| category_tag_distribution.dimensions | object | Three dimensions (`product` / `service` / `experience`) → Category → Tags |
| dimensions.*.total_count | int | Comment count in this dimension |
| dimensions.*.total_rate | string | Dimension share (percent-string) |
| dimensions.*.categories | object | Category mapping |
| dimensions.*.categories.*.tags | array | Tag list under the category, each with `tag / count / rate` |

> When no data exists, `dimensions` is an empty object `{}`.

---

### 7. Basic Statistics

**Endpoint**: `POST /api/v1/external/analysis/statistics`

Get basic statistics (total counts, positive/negative counts and rates, last analysis time).

**Request Body**:
```json
{
  "task_id": "TSK_xxx"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "total_comments": 150,
    "negative_comments": 23,
    "negative_rate": "15.33%",
    "positive_comments": 120,
    "positive_rate": "80.0%",
    "last_analyzed_at": "2025-03-22 10:35"
  }
}
```

**Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| total_comments | int | Total comments |
| negative_comments | int | Negative count |
| negative_rate | string | Negative rate (percent-string) |
| positive_comments | int | Positive count |
| positive_rate | string | Positive rate (percent-string) |
| last_analyzed_at | string | Last analysis time (`YYYY-MM-DD HH:MM`, empty string if not analyzed) |

> If the task has never been analyzed, this endpoint does not fail — it returns an all-zero structure with `last_analyzed_at` as an empty string.

> ⚠️ **Positive and negative rates are NOT mutually exclusive (important semantic)**: `positive_rate + negative_rate` **may exceed 100%** (verified: 62.4% + 50.4% = 112.8%). AstrMap's semantic classification is **not a binary split** — a single review may **simultaneously** contain positive sentiment (e.g. "durable product") and negative sentiment (e.g. "slow shipping"), counted on both sides. **Therefore `total_comments - negative_comments ≠ positive_comments`** — do not derive one from the other via subtraction; read each field independently.

---

### 8. Representative Reviews

**Endpoint**: `POST /api/v1/external/analysis/representative-reviews`

Get representative reviews (top-N canonical reviews already selected per dimension).

**Request Body**:
```json
{
  "task_id": "TSK_xxx",
  "polarity": "negative",
  "limit": 5
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| task_id | Yes | - | Task ID |
| polarity | No | negative | Polarity filter: `negative` / `positive` |
| limit | No | 5 | Max per dimension (empirically ≤ 5) |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "AMAZON_R28FJKGLXXQJCQ",
        "content": "Review content...",
        "title": "Review title",
        "star": "1",
        "time": "2026-06-15",
        "reviewer": "Peyton",
        "avatar": "https://images-na.ssl-images-amazon.com/...",
        "region": "the United States",
        "is_purchase": true,
        "helpful_votes": 3,
        "images": [],
        "dimension": "product",
        "dimension_name": "Product",
        "rank_in_dimension": 1,
        "url": "https://www.amazon.com/..."
      }
    ]
  }
}
```

**items Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| id | string | Review ID |
| content | string | Review body |
| title | string | Review title |
| star | string | Star rating (string form of a number) |
| time | string | Review time |
| reviewer | string | Reviewer name |
| avatar | string | Reviewer avatar URL |
| region | string | Reviewer region |
| is_purchase | bool | Verified purchase |
| helpful_votes | int / string | Helpful vote count |
| images | array | Review image URLs |
| dimension | string | Dimension: `product` / `service` / `experience` |
| dimension_name | string | Dimension display name |
| rank_in_dimension | int | Rank inside the dimension (1 = top) |
| url | string | Original review URL |

> Note: `limit` is the max **per dimension**; when three dimensions are merged, items can contain up to `3 × limit` entries.

---

### 9. Sentiment Reviews List

**Endpoint**: `POST /api/v1/external/analysis/sentiment-reviews`

Get sentiment reviews list — **the same endpoint supports both negative and positive reviews** via the `polarity` parameter.

> Compatibility: `POST /api/v1/external/analysis/negative-reviews` is a legacy alias of this endpoint (auto-sets `polarity="negative"`), with identical behavior. **New code should use `/sentiment-reviews` + polarity.**

**Request Body**:
```json
{
  "task_id": "TSK_xxx",
  "polarity": "negative",
  "page": 1,
  "page_size": 20
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| task_id | Yes | - | Task ID |
| polarity | No | negative | Polarity: `negative` / `positive` |
| page | No | 1 | Page number |
| page_size | No | 10 | Items per page (max 100) |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "AMAZON_R28FJKGLXXQJCQ",
        "review_title": "Review title",
        "review_content": "Review content...",
        "review_star": "5",
        "review_time": "2026/06/15",
        "reviewer": "Peyton",
        "review_region": "the United States",
        "is_purchase": true,
        "review_vote": "0",
        "review_images": [],
        "review_videos": [],
        "asin": "B0C3L93F2Q",
        "tags": ["Great experience", "Good compatibility", "Nice looking"],
        "normalized_tags": ["good_experience", "good_compat", "good_looks"]
      }
    ],
    "total": 226,
    "page": 1,
    "page_size": 20,
    "page_max": 12
  }
}
```

**⚠️ Positive-side pitfall** (verified 2026-06-23):
- With `polarity="positive"` the items **may include a few 1★/2★ reviews** — the server side splits by AI sentiment rather than by `review_star` alone
- Before frequency counts / listing-copy extraction, **filter by `review_star >= 4`**
- Full V1 self-check + typical usage: see `references/positive-reviews-workflow.md`

**Python Usage**:
```python
from api_client import CustomerInsightsClient
client = CustomerInsightsClient(api_key="sk_live_...")

neg = client.get_sentiment_reviews(tid, polarity="negative", page=1, page_size=50)
pos = client.get_sentiment_reviews(tid, polarity="positive", page=1, page_size=50)
```

---

### 10. Review Trend

**Endpoint**: `POST /api/v1/external/analysis/trend`

Get daily review trend (anchored at the task's latest review date, looking back N days).

**Request Body**:
```json
{
  "task_id": "TSK_xxx",
  "filter_data": "30",
  "filter_polarity": "all"
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| task_id | Yes | - | Task ID |
| filter_data | No | 30 | Look-back days (`1-365`; out-of-range / invalid falls back to 30) |
| filter_polarity | No | all | Polarity: `all` / `negative` / `positive` (affects header columns) |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "trend_reviews": {
      "source": [
        ["Date", "Total reviews", "Negative reviews", "Positive reviews"],
        ["2025-03-01", 50, 8, 42],
        ["2025-03-02", 47, 6, 41]
      ],
      "filter_product_options": {"all": "All products"},
      "filter_data_options": {
        "30": "Last 30 days",
        "60": "Last 60 days",
        "90": "Last 90 days"
      }
    },
    "filter_product_options": {"all": "All products"},
    "filter_data_options": {
      "30": "Last 30 items",
      "60": "Last 60 items",
      "90": "Last 90 items"
    }
  }
}
```

**Header columns vary by `filter_polarity`**:
| filter_polarity | source header |
|---|---|
| all (default) | `["Date", "Total reviews", "Negative reviews", "Positive reviews"]` |
| negative | `["Date", "Total reviews", "Negative reviews"]` |
| positive | `["Date", "Total reviews", "Positive reviews"]` |

> When there is no data, `trend_reviews.source` contains only the header row.

> ⚠️ **Actual data points ≤ N days**: `filter_data=30` means "anchor at the task's latest review date, look back 30 days", but **days with no reviews are skipped** (no 0-count filler rows). In practice a 30-day window may contain only ~18 data points, depending on product review activity. If a continuous time axis is required for charting, callers must fill missing dates as 0 themselves.

---

### 11. Raw Comments Overview

**Endpoint**: `POST /api/v1/external/analysis/comments-overview`

Get raw-comments overview stats (star distribution, content-type distribution).

**Request Body**:
```json
{
  "task_id": "TSK_xxx"
}
```

**Parameter Description**:
| Parameter | Required | Description |
|-----------|----------|-------------|
| task_id | Yes | Task ID |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "task_id": "TSK_xxx",
    "total_reviews": 335,
    "average_rating": 4.2,
    "star_distribution": [
      {"rating": 5, "count": 200, "percentage": 60},
      {"rating": 4, "count": 60,  "percentage": 18},
      {"rating": 3, "count": 30,  "percentage": 9},
      {"rating": 2, "count": 25,  "percentage": 7},
      {"rating": 1, "count": 20,  "percentage": 6}
    ],
    "content_type_data": [
      {"type": "text_only",  "name": "Text only",  "count": 329},
      {"type": "with_image", "name": "With image", "count": 0},
      {"type": "with_video", "name": "With video", "count": 6}
    ],
    "last_update_time": "2025-03-22 10:35:00"
  }
}
```

**Field Description**:
| Field | Type | Description |
|-------|------|-------------|
| task_id | string | Task ID (echoed back) |
| total_reviews | int | Total reviews |
| average_rating | float | Average rating |
| star_distribution | array | Star-distribution array; each element has `rating / count / percentage` (**note: field is `rating`, not `star`; includes `percentage`**) |
| content_type_data | array | Content-type distribution **array** (not an object); each element has `type / name / count`; `type` values: `text_only` / `with_image` / `with_video` |
| last_update_time | string | Last update time |

**Error Codes** (server-side internal codes; on the wire they are wrapped as HTTP 400 with `detail.code = -1`; see "Error Handling Contract" at the end):
| Internal code | Description |
|------|-------------|
| TaskNotFound | Task not found |
| AccessDenied | No permission to access this task |
| GetReviewStatisticsError | Failed to get review statistics |
| GetContentTypeStatisticsError | Failed to get content-type statistics |

---

### 12. Raw Comments List

**Endpoint**: `POST /api/v1/external/analysis/comments`

Get raw comments list (supports star / content-type / product / verified filters).

**Request Body**:
```json
{
  "task_id": "TSK_xxx",
  "page": 1,
  "page_size": 20,
  "filter_star": "all",
  "filter_verified": "all",
  "filter_content_type": "all",
  "filter_product": "all",
  "search_keyword": "",
  "sort_field": "latest"
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| task_id | Yes | - | Task ID |
| page | No | 1 | Page number (equivalent to `current_page`) |
| page_size | No | 20 | Items per page (max 100) |
| filter_star | No | all | Star filter: `1` / `2` / `3` / `4` / `5` / `all` |
| filter_verified | No | all | Verified-purchase filter: `all` / `true` / `false` |
| filter_content_type | No | all | Content-type filter: `all` / `text_only` / `with_image` / `with_video` |
| filter_product | No | all | ASIN filter (exact ASIN or `all`) |
| search_keyword | No | "" | Keyword search |
| sort_field | No | latest | Sort field: `latest` or others supported by server |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "AMAZON_R28FJKGLXXQJCQ",
        "review_time": "2026-06-15",
        "asin": "B0C3L93F2Q",
        "reviewer": "Peyton",
        "is_purchase": true,
        "review_star": 5,
        "review_title": "Review title",
        "review_content": "Review content...",
        "content_type": "text_only",
        "review_url": "https://www.amazon.com/...",
        "review_vote": "0",
        "review_region": "the United States",
        "variant": ""
      }
    ],
    "total": 150,
    "page": 1,
    "page_size": 20,
    "page_max": 8,
    "filter_product_options": {"all": "All products", "B0C3L93F2Q": "B0C3L93F2Q"}
  }
}
```

> `filter_product_options` is only returned on **page 1** (for rendering an ASIN filter dropdown); subsequent pages omit it.

**`content_type` values**: `text_only` / `with_image` / `with_video`

**Error Codes** (server-side internal codes; on the wire they are wrapped as HTTP 400 with `detail.code = -1`; see "Error Handling Contract" at the end):
| Internal code | Description |
|------|-------------|
| InvalidPaginationParams | Invalid pagination params |
| TaskNotFound | Task not found |
| AccessDenied | No permission to access this task |
| GetCommentsListError | Failed to get comments list |

---

### 13. Get Related Comments

**Endpoint**: `POST /api/v1/external/analysis/related-comments`

Drill down to comments associated with a specific **tag** or **category**. `association_type` decides which sub-mode is used.

**Request Body (tag mode)**:
```json
{
  "task_id": "TSK_xxx",
  "association_type": "tag",
  "normalized_tag": "Shipping issue",
  "category": "service",
  "polarity": "negative",
  "current_page": 1,
  "page_size": 20
}
```

**Request Body (category mode)**:
```json
{
  "task_id": "TSK_xxx",
  "association_type": "category",
  "dimension": "product",
  "category": "quality",
  "polarity": "negative",
  "current_page": 1,
  "page_size": 20
}
```

**Parameter Description**:
| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| task_id | Yes | - | Task ID |
| association_type | Yes | - | Association type: `tag` / `category` (**`issue` is NOT supported**) |
| normalized_tag | tag mode | - | Normalized tag name |
| category | optional | - | Category; in `category` mode the server maps it internally to `issue_type` for filtering |
| dimension | category mode | - | One of `product` / `service` / `experience` |
| polarity | No | negative | Polarity: `negative` / `positive` / `all` |
| current_page | No | 1 | Page number (also accepts `page`) |
| page_size | No | 20 | Items per page |
| sort_field | No | - | Sort field (server-supported) |

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "items": [
      {
        "id": "AMAZON_R28FJKGLXXQJCQ",
        "content": "Review content...",
        "title": "Review title",
        "rating": 1,
        "review_time": "2026-06-15",
        "reviewer": "Peyton",
        "verified_purchase": true,
        "helpful_votes": 3,
        "total_votes": 5,
        "images": [],
        "videos": [],
        "tags": ["Chin strap issue"],
        "variant": "",
        "asin": "B0C3L93F2Q",
        "platform": "amazon",
        "dimension": "experience",
        "issue_type": null
      }
    ],
    "total": 50,
    "page": 1,
    "page_size": 20,
    "page_max": 3,
    "association_type": "tag",
    "task_id": "TSK_xxx"
  }
}
```

**items Field Description** (**note: naming differs from §12/§9** — this endpoint uses `rating / verified_purchase / content / title` instead of `review_star / is_purchase / review_content / review_title`):

| Field | Type | Description |
|-------|------|-------------|
| id | string | Review ID |
| content | string | Review body |
| title | string | Review title |
| rating | int / null | Rating (1-5, may be null) |
| review_time | string | Review time |
| reviewer | string | Reviewer name |
| verified_purchase | bool | Verified purchase |
| helpful_votes | int | Helpful vote count |
| total_votes | int | Total vote count |
| images | array | Image URLs |
| videos | array | Video URLs |
| tags | array | Raw tags |
| variant | string | Product variant |
| asin | string | ASIN |
| platform | string | Platform |
| dimension | string | Dimension (present in category mode) |
| issue_type | string / null | Issue type (may be present in category mode) |

> ⚠️ **Naming inconsistency (as-is)**: item fields here (`rating / verified_purchase / content / title`) differ from those in `/analysis/comments` and `/analysis/sentiment-reviews` (`review_star / is_purchase / review_content / review_title`). This is a legacy artifact (different underlying CRUD sources); the doc reflects reality — callers must use the naming that matches the endpoint being called. Both tag and category modes share the same item structure.

---

### 14. Points Balance

**Endpoint**: `POST /api/v1/external/account/points`

Query current account's available points across all sources (subscription + purchase + gift + compensation).

**Request Body**:
```json
{}
```

**Response**:
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "available_points": 1000
  }
}
```

---

## Error Handling Contract

### Unified failure response format

All business failures share this **real on-the-wire structure** (verified 2026-07-06):

- **HTTP status code**: always `400` (auth / not-found / validation — all HTTP 400)
- **Response body**: wrapped once by FastAPI's `HTTPException.detail`:

```json
{
  "detail": {
    "code": -1,
    "msg": "<error message, usually Chinese>",
    "data": null
  }
}
```

**⚠️ Key contract facts**:
1. **`code` is always `-1`** — the server-side string codes (`TaskNotFound / VALIDATION_ERROR / InvalidTaskStatus`, etc.) **do not appear in the response**; they live only in server logs
2. Callers **cannot programmatically distinguish error types via `code`** — you must match against `msg` substrings
3. Success responses are **flat** `{code, msg, data}`; failure responses are **nested** `{detail: {code, msg, data}}` — check HTTP status before parsing

### Recommended error-handling pattern

```python
import requests

resp = requests.post(url, headers=headers, json=payload)
if resp.status_code == 400:
    err = resp.json().get("detail", {})
    msg = err.get("msg", "")
    if "API Key" in msg or "认证" in msg:
        # Auth / authorization error
        ...
    elif "找不到任务" in msg or "任务不存在" in msg:
        # Task not found or unauthorized
        ...
    elif "状态" in msg:
        # Task state does not permit this op
        ...
    else:
        raise Exception(f"API call failed: {msg}")
elif resp.status_code == 429:
    retry_after = resp.headers.get("Retry-After", "60")
    ...
else:
    data = resp.json().get("data")
```

### Common error-msg keyword reference

Grouped semantically. These are the **server-side internal classifications** — the codes never appear on the wire, but the corresponding Chinese `msg` strings do:

| Internal code | Typical msg | When |
|---|---|---|
| MISSING_API_KEY | 认证失败: 缺少 API Key | Missing `Authorization: Bearer` header |
| INVALID_API_KEY | 认证失败: 无效的 API Key: API Key 不存在 | Wrong or deleted API Key |
| API_KEY_EXPIRED | API Key 已过期 | Key past `expires_at` |
| API_KEY_DISABLED | API Key 已禁用 | Disabled by user |
| API_KEY_READ_ONLY | API Key 为只读模式 | Read-only key attempted write (create/rename/incremental/trigger) |
| MISSING_REQUIRED_PARAM | - | Missing required param (e.g. task_id) |
| VALIDATION_ERROR | 验证失败 | Param validation failed (e.g. rename missing name) |
| INVALID_PARAMETER | 无效参数 | Illegal parameter value |
| TaskNotFound | 找不到任务或权限不足: TSK_xxx | Task does not exist or does not belong to current account |
| InvalidTaskStatus | 只有待分析状态的任务可以触发分析，当前状态: xxx | trigger-analysis when task is not COLLECTED |
| InvalidTaskStatus | 只有成功/已取消/待分析状态的任务才能进行增量获取 | incremental when task is not SUCCESS/CANCELLED/COLLECTED |
| InvalidPaginationParams | 无效的分页参数 | Bad page / page_size in comments list |
| AccessDenied | 无权访问该任务 | Task does not belong to current account (some endpoints) |
| INSUFFICIENT_POINTS | 积分余额不足 | Points-consuming op failed |
| DEVICE_NOT_FOUND | 设备未找到 | Endpoint not bound / offline (some endpoints) |
| API_RATE_LIMIT | 请求过于频繁，请稍后再试 | Rate-limit tripped (default 100/min) |
| UNKNOWN | 未知错误，请稍后重试 | Fallback |

> Full internal string constants are defined server-side in `configs/config_domain/infrastructure/config_error_codes.py`, **but they are not part of the public API contract**. The table above is only for understanding server-side error semantics.

---

## Rate Limits

- Default: 100 requests / minute
- On breach, `code` returns `API_RATE_LIMIT` and the `Retry-After` response header carries the backoff time

---

## FAQ

### Points System

- **Create task (auto mode)**: Amazon review collection is free; AI analysis deducts points
- **Create task (collection-only mode)**: Amazon review collection is free; no point deduction
- **Incremental fetch**: Fetch latest reviews and re-analyze; deducts points
- **Query results**: View analysis results of completed tasks; no point deduction, no prerequisites

### Prerequisites (only for creating tasks)

Before creating a task, ensure:

1. AstrMap desktop client is logged in
2. Desktop client is logged in with an Amazon buyer account (do not use your seller account)
3. Amazon access is working

### Error-handling Guidance
1. Endpoint offline (`is_alive: false` or msg contains "设备"): check if desktop client is logged in
2. Insufficient points (msg contains "积分"): prompt user to top up
3. Invalid API Key (HTTP 400 + msg contains "API Key"): verify the API Key
4. Write op rejected (msg contains "只读"): a read-only key cannot create task / trigger analysis / incremental / rename
5. **General rule**: all failures are `HTTP 400 + {detail: {code: -1, msg, data: null}}` — distinguish by `msg` keywords (see "Error Handling Contract" section)
