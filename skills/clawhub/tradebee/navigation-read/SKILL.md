---
name: navigation-read
description: Read the complete matching Tradebee two-level navigation tree without pagination, with optional exact-ID or parent filtering and field selection.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# navigation-read

## Overview

Read website navigation without pagination. Omit both filters for the complete tree, use `navigation_id` for one exact item, or use `parent_navigation_id` for one level. Never combine the filters.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only requested site data to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`.

### `navigation_id` (integer, Optional)

Positive exact navigation ID. Mutually exclusive with `parent_navigation_id`.

### `parent_navigation_id` (integer, Optional)

Use `0` for first-level navigation or a positive first-level ID for its children. Mutually exclusive with `navigation_id`.

### `fields` (array<string>, Optional)

Omit or send `[]` for all fields. Supported values: `navigation_id`, `parent_navigation_id`, `language`, `name`, `url`, `system_children_type`, `content`, `open_in_new_window`, `sort`, `create_time`, `update_time`, `is_leaf`, `children`.

Do not send `pagination`, `current_page`, or `page_size`.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.list` is the complete matching result. First-level items may contain second-level items in `children`; second-level `children` is always `[]`. Each level is ordered by ascending `sort`.

### `data.list[]`

| Field | Type | Description |
|-------|------|-------------|
| `navigation_id` | integer | Navigation ID. |
| `parent_navigation_id` | integer | `0` for first level; otherwise parent ID. |
| `language` | string | Site language. |
| `name` | string | Display name. |
| `url` | string | Navigation link. |
| `system_children_type` | integer | System mode 0–7; meanings below. |
| `content` | string | First-level custom HTML; base64 image sources are returned as URLs. |
| `open_in_new_window` | boolean | Window behavior. |
| `sort` | integer | 1–999999; smaller values appear earlier. |
| `create_time` | string(datetime) | ISO 8601 creation time. |
| `update_time` | string(datetime) | ISO 8601 update time. |
| `is_leaf` | boolean | Whether manual children are forbidden. |
| `children` | array<object> | Second-level items. |

System types: `0` disabled, `1` first-level product groups, `2` news groups, `3` FAQ groups, `4` certificate groups, `5` case groups, `6` all product groups without covers, and `7` blog groups. Values 1–7 occur only on first-level items.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |

## Usage Examples

Complete tree:

```json
{"language":"en","fields":["navigation_id","name","url","system_children_type","sort","is_leaf","children"]}
```

One exact item:

```json
{"language":"en","navigation_id":101}
```

Children of one first-level item:

```json
{"language":"en","parent_navigation_id":101}
```

## Response Example

```json
{"status":true,"msg":"Query successfully","data":{"list":[{"navigation_id":101,"parent_navigation_id":0,"language":"en","name":"Products","url":"/products.htm","system_children_type":0,"content":"","sort":10,"is_leaf":false,"children":[{"navigation_id":102,"parent_navigation_id":101,"name":"Industrial Equipment","url":"/products/industrial-equipment.htm","system_children_type":0,"content":"","sort":20,"is_leaf":true,"children":[]}]}]}}
```
