---
name: navigation-update
description: Update one Tradebee navigation item after reading and locally backing it up, while preserving its parent and enforcing hierarchy and child-mode constraints.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# navigation-update

## Overview

Update one navigation item after reading and backing up its current state. The parent relationship cannot be changed. Stop before mutation if capture or file writing fails.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only explicitly changed fields to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language matching the target item.

### `navigation` (object, **Required**)

| Field | Type | Rules |
|-------|------|-------|
| `navigation_id` | integer | Required positive ID selected from `navigation-read`. |
| `name` | string | 2–100 characters; omit if unchanged. |
| `url` | string | 1–500 characters; internal links start with `/` and omit domain, external links use HTTP(S). |
| `system_children_type` | integer | 0–7; values 1–7 are first-level only. |
| `open_in_new_window` | boolean | Omit if unchanged. |
| `sort` | integer | 1–999999; smaller values appear earlier. |

Do not send `parent_navigation_id`; this API does not move navigation items.

#### `navigation.content` (string, Optional)

First-level custom child-navigation HTML. Only when replacing this field, call `rule-get` with the exact selected `language` and exact `scene=navigation.content`; stop if the call fails. Follow the returned payload: use one root `<section>` with a unique scoped class and one embedded `<style>` block at the end. Inline `style="..."` attributes and external stylesheet links are forbidden. Do not include `<h1>`; prefer `<h2>`–`<h6>`. `<img src>` supports HTTP(S) URLs or `data:image/...;base64,...`, up to 50 images and 500 kB each. The 100,000-character check removes `<img>` tags first. The server uploads base64 images and replaces their `src` values with URLs. An empty string or omitted field leaves stored content unchanged; this update API cannot clear existing content with `""`.

### Child Mode Rules

System children use type 1–7, empty stored content, and no manual children. Custom HTML uses type 0, non-empty content, and no manual children. Manual children use type 0 and empty stored content. Second-level items always use type 0 and empty content. Before switching to system or manual mode, stored content must already be empty.

System type meanings: `0` disabled, `1` first-level product groups, `2` news groups, `3` FAQ groups, `4` certificate groups, `5` case groups, `6` all product groups without covers, `7` blog groups.

### `confirmation` (object, **Required**)

`approved` must be `true` only after approval of the language, target ID, exact changes, and local backup. `summary` must restate that approval.

### Automatic Backup

- Reads the current item with `navigation-read`.
- Writes under `backups/navigation-update/` relative to the installed skill root.
- If capture or file writing fails, the update does not run.
- Success returns `backup.storage.file_path`, `backup.raw_read_response`, `backup.snapshot`, `backup.restore_payload`, and `backup.restore_limitations`.
- `parent_navigation_id` cannot be restored because update cannot change the parent relationship.

## Output Structure

Top level contains `status`, `msg`, `data`, and `backup`. `data.navigation_id` is the updated ID and `data.is_leaf` reports whether manual children are forbidden.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `navigation.content` | `rule-get` | `scene=navigation.content` rule payload, only when replacing content |
| `navigation.navigation_id` | `navigation-read` | `list[].navigation_id` |

## Usage Example

```json
{"language":"en","navigation":{"navigation_id":101,"name":"Our Products","url":"/products.htm","sort":10},"confirmation":{"approved":true,"summary":"Update English navigation 101 and create the local backup first."}}
```

## Response Example

```json
{"status":true,"msg":"Navigation updated successfully","data":{"navigation_id":101,"is_leaf":false},"backup":{"storage":{"file_path":"backups/navigation-update/example.json"},"restore_limitations":["parent_navigation_id cannot be restored because navigation-update does not allow changing the parent relationship."]}}
```
