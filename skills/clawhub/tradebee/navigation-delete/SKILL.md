---
name: navigation-delete
description: Delete one or more Tradebee navigation items by confirmed ID list, cascading through children when a first-level item is deleted.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# navigation-delete

## Overview

Delete 1–100 navigation IDs. Deleting a first-level item recursively deletes all of its second-level children, so confirmation must explicitly acknowledge that consequence.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only the exact IDs approved by the user.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`. Every target must belong to it.

### `id_list` (array<integer>, **Required**)

Array of 1–100 positive navigation IDs selected from `navigation-read`.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user approves the exact language and IDs and acknowledges cascading child deletion. `summary` must record all of that.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.success[]` and `data.fail[]` contain `{id, msg}`. A top-level success does not imply every ID succeeded; inspect `fail`.

If both a parent and one of its children appear in `id_list`, deleting the parent may delete the child first; the child is still reported as successfully deleted rather than deleted twice.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `id_list[]` | `navigation-read` | `list[].navigation_id` |

## Usage Example

```json
{"language":"en","id_list":[101],"confirmation":{"approved":true,"summary":"Delete English navigation 101 and all of its child navigation."}}
```

## Notes

- Missing, unauthorized, or wrong-language IDs return `Data not found`.
- Child deletion failure prevents successful deletion of that parent.
- Report every entry in `fail` and do not hide partial failure.

## Response Example

```json
{"status":true,"msg":"Deleted successfully","data":{"success":[{"id":101,"msg":"Deleted"}],"fail":[]}}
```
