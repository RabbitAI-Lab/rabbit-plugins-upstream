---
name: navigation-create
description: Create a first- or second-level Tradebee website navigation item under an exact enabled language while enforcing hierarchy and child-mode constraints.
metadata: {"clawdbot":{"emoji":"bee","requires":{"env":["BEE_API_KEY"]},"primaryEnv":"BEE_API_KEY"}}
---

# navigation-create

## Overview

Create one website navigation item. Navigation supports at most two levels and at most 20 first-level items per language. For a second-level item, select a first-level parent from `navigation-read` where `is_leaf=false`.

## Input Parameters

Authentication uses only `BEE_API_KEY`; never expose it. Send only the required site data to the external Tradebee API.

### `language` (string, **Required**)

Exact enabled language selected from `languages-get`.

### `navigation` (object, **Required**)

#### `navigation.parent_navigation_id` (integer, Optional)

Defaults to `0`. Use `0` for first level. For second level use one positive first-level ID returned by `navigation-read`; never use a second-level ID.

#### `navigation.name` (string, **Required**)

Display name containing 2–100 characters.

#### `navigation.url` (string, **Required**)

Link containing 1–500 characters. Internal links must start with `/` and omit scheme and domain. External links must be absolute HTTP(S) URLs.

#### `navigation.system_children_type` (integer, Optional)

Defaults to `0`. Values 1–7 are first-level only.

| Value | Meaning |
|-------|---------|
| `0` | Disable system-generated children; use for custom HTML, manual children, and all second-level items. |
| `1` | First-level product groups. |
| `2` | News groups. |
| `3` | FAQ groups. |
| `4` | Certificate groups. |
| `5` | Case groups. |
| `6` | All product groups without cover images. |
| `7` | Blog groups. |

#### `navigation.content` (string, Optional)

First-level custom child-navigation HTML. Before generating this field, call `rule-get` with the exact selected `language` and exact `scene=navigation.content`; stop if the call fails. Follow the returned payload: use one root `<section>` with a unique scoped class and one embedded `<style>` block at the end. Inline `style="..."` attributes and external stylesheet links are forbidden. Do not include `<h1>`; prefer `<h2>`–`<h6>`. `<img src>` supports HTTP(S) URLs or `data:image/...;base64,...`, up to 50 images and 500 kB each. The 100,000-character check removes `<img>` tags first. The server uploads base64 images and replaces their `src` values with URLs.

#### `navigation.open_in_new_window` (boolean, Optional)

Defaults to `false`. `true` opens the URL in a new window or tab.

#### `navigation.sort` (integer, Optional)

Defaults to `999999`; valid range is 1–999999. Smaller values appear earlier.

### Child Mode Rules

A first-level item must use exactly one child mode:

| Mode | `system_children_type` | `content` | Manual second-level items |
|------|------------------------|-----------|---------------------------|
| System children | `1`–`7` | `""` | Forbidden |
| Custom HTML | `0` | Non-empty | Forbidden |
| Manual children | `0` | `""` | Allowed |

Every second-level item requires type `0` and empty content. Omitting content during create is equivalent to `""`.

### `confirmation` (object, **Required**)

`approved` must be `true` only after the user approves the exact language and payload. `summary` must restate them.

## Output Structure

Top level contains `status`, `msg`, and `data`. `data.navigation_id` is the created ID. `data.is_leaf=true` means manual children cannot be added; `false` means a second-level child may be added.

## Dependencies

| Parameter | Dependency skill | Field source |
|-----------|------------------|--------------|
| `language` | `languages-get` | `list[].language` |
| `navigation.content` | `rule-get` | `scene=navigation.content` rule payload |
| `parent_navigation_id` | `navigation-read` | `list[].navigation_id`, with `is_leaf=false` |

## Usage Examples

System children:

```json
{"language":"en","navigation":{"parent_navigation_id":0,"name":"Products","url":"/products.htm","system_children_type":1,"content":"","open_in_new_window":false,"sort":10},"confirmation":{"approved":true,"summary":"Create the approved English system navigation."}}
```

Manual second-level item:

```json
{"language":"en","navigation":{"parent_navigation_id":101,"name":"Industrial Equipment","url":"/products/industrial-equipment.htm","system_children_type":0,"content":"","sort":20},"confirmation":{"approved":true,"summary":"Create the approved child under navigation 101."}}
```

## Response Example

```json
{"status":true,"msg":"Navigation created successfully","data":{"navigation_id":101,"is_leaf":false}}
```
