---
name: news-delete
description: Move one or more Tradebee news records to the recycle bin by confirmed ID list and report successes and failures separately.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# news-delete

## Overview

Move 1–100 news records under one exact language to the recycle bin. This high-impact mutation requires approval of the exact IDs.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only the exact IDs requested by the user.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`. Every target must belong to it.

### `id_list` (array<integer>, **Required**)

Array of 1–100 positive news IDs selected from `news-read`. Use an array even for one ID.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user approves the exact language and ID list. `summary` must restate them.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.success[]` and `data.fail[]` each contain `{id, msg}`. A top-level `status=true` means the batch was processed, not that every ID succeeded; always inspect `fail`.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `id_list[]` | `news-read` | `list[].news_id` |

## Usage Example

```json
{"language":"en","id_list":[8,9],"confirmation":{"approved":true,"summary":"Delete English news IDs 8 and 9."}}
```

## Notes

- Missing, wrong-language, or unauthorized IDs return `Data not found` in `fail`.
- A record already in the recycle bin returns `Already deleted` in `fail`.
- Report partial failures instead of describing the whole batch as successful.

## Response Example

```json
{"status":true,"msg":"Deleted successfully","data":{"success":[{"id":8,"msg":"Deleted"}],"fail":[{"id":9,"msg":"Already deleted"}]}}
```
