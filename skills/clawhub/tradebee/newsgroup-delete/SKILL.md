---
name: newsgroup-delete
description: Delete one or more empty Tradebee news groups by confirmed ID list and report successes and failures separately.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# newsgroup-delete

## Overview

Delete 1–100 news groups under one exact language. A group containing active news cannot be deleted.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only the exact IDs approved by the user.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`.

### `id_list` (array<integer>, **Required**)

Array of 1–100 positive IDs selected from `newsgroup-read`.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user approves the exact language and IDs. `summary` must restate them.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.success[]` and `data.fail[]` contain `{id, msg}`. Always inspect and report `fail`, even when top-level `status=true`.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `id_list[]` | `newsgroup-read` | `list[].newsgroup_id` |

## Usage Example

```json
{"language":"en","id_list":[8,9],"confirmation":{"approved":true,"summary":"Delete English news groups 8 and 9."}}
```

## Notes

- `The news group contains news` means active news must be moved or deleted first.
- Missing, unauthorized, or wrong-language IDs return `Data not found`.
- Report partial failures explicitly.

## Response Example

```json
{"status":true,"msg":"Deleted successfully","data":{"success":[{"id":8,"msg":"Deleted"}],"fail":[{"id":9,"msg":"The news group contains news"}]}}
```
