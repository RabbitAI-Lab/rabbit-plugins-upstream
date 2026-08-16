# AstroBrowse - Authenticated Agentic Browser Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `astrobrowse-authenticated-agentic-browser`

x402 availability: not enabled for this product.

## `close_browser`

Action slug: `close-browser`

Price: `5` credits

Release the session: it is wiped and destroyed. Always call this when finished.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```

## `download_file`

Action slug: `download-file`

Price: `5` credits

Persist a file the browser downloaded into the File Manager (size-capped, requires workflow budget context). Pass download_name from list_downloads, or omit it to save the most recent download.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `download_name` | `string` | no | For download_file: the download filename to persist (from list_downloads). Omit to persist the most recent completed download. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "download_name": "example download name"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "download_name": {
    "description": "For download_file: the download filename to persist (from list_downloads). Omit to persist the most recent completed download.",
    "required": false,
    "type": "string"
  }
}
```

## `extract_page`

Action slug: `extract-page`

Price: `5` credits

Extract visible text (or HTML) from the active page or a selector.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `include_html` | `boolean` | no | Whether extract_page should include capped outer HTML. |
| `selector` | `string` | no | Optional selector for extract_page or upload_file. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "include_html": true,
  "selector": "example selector"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "include_html": {
    "description": "Whether extract_page should include capped outer HTML.",
    "required": false,
    "type": "boolean"
  },
  "selector": {
    "description": "Optional selector for extract_page or upload_file.",
    "required": false,
    "type": "string"
  }
}
```

## `get_policy`

Action slug: `get-policy`

Price: `5` credits

Read the user's browsing policy (saved-only vs general browsing). The policy is set only by the human from their dashboard; there is no agent action to change it.

Parameters:

This action does not require parameters.

Sample parameters:

```json
{}
```

Generated JSON parameter schema:

```json
{}
```

## `initialize_browser`

Action slug: `initialize-browser`

Price: `5` credits

Start a fresh, single-use, isolated browser session. Pass a stable idempotency_key (required) so a retry never starts a second session. Provide account_id to resume a saved login, or omit account_id for a general-browsing session (allowed only when the user has enabled general browsing). Call list_accounts first.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `account_id` | `string` | no | Saved account id for an account-backed session. Omit it to start a general-browsing session (no saved login). |
| `idempotency_key` | `string` | yes | Caller-supplied idempotency key for initialize_browser (the agent/request id). |
| `initial_url` | `string` | no | Optional URL to navigate to after initialization. Must match the account's allowed origins. |
| `region` | `string` | no | Optional region override for a general-browsing session. |

Sample parameters:

```json
{
  "account_id": "example account id",
  "idempotency_key": "example idempotency key",
  "initial_url": "https://example.com",
  "region": "example region"
}
```

Generated JSON parameter schema:

```json
{
  "account_id": {
    "description": "Saved account id for an account-backed session. Omit it to start a general-browsing session (no saved login).",
    "required": false,
    "type": "string"
  },
  "idempotency_key": {
    "description": "Caller-supplied idempotency key for initialize_browser (the agent/request id).",
    "required": true,
    "type": "string"
  },
  "initial_url": {
    "description": "Optional URL to navigate to after initialization. Must match the account's allowed origins.",
    "required": false,
    "type": "string"
  },
  "region": {
    "description": "Optional region override for a general-browsing session.",
    "required": false,
    "type": "string"
  }
}
```

## `list_accounts`

Action slug: `list-accounts`

Price: `5` credits

List the user's saved AstroBrowse logins (accounts). Call this first to find a saved site before initialize_browser.

Parameters:

This action does not require parameters.

Sample parameters:

```json
{}
```

Generated JSON parameter schema:

```json
{}
```

## `list_downloads`

Action slug: `list-downloads`

Price: `5` credits

List files the browser has downloaded in this session (name, size, type) so you can pick one to save with download_file.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```

## `request_user_takeover`

Action slug: `request-user-takeover`

Price: `5` credits

Ask the human to take over the live browser (e.g. CAPTCHA, MFA, unusual login UI). Holds the session open past the idle timeout. Use ONLY when the agent cannot proceed automatically.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `reason` | `string` | yes | Reason to show the user when requesting browser takeover. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "reason": "example reason"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "reason": {
    "description": "Reason to show the user when requesting browser takeover.",
    "required": true,
    "type": "string"
  }
}
```

## `run_steps`

Action slug: `run-steps`

Price: `5` credits

Run bounded browser automation steps (goto/click/fill/press/select/wait/extract/screenshot) in an initialized session.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `steps` | `array` | yes | Browser automation steps for run_steps. Each request accepts 1-20 steps. Caller-supplied JavaScript is not supported. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "steps": [
    {
      "action": "goto",
      "blur": null,
      "key": null,
      "marker": null,
      "selector": null,
      "text": null,
      "timeout_ms": 10000,
      "url": null
    }
  ]
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "steps": {
    "description": "Browser automation steps for run_steps. Each request accepts 1-20 steps. Caller-supplied JavaScript is not supported.",
    "items": {
      "description": "",
      "properties": {
        "action": {
          "description": "",
          "enum": [
            "goto",
            "click",
            "fill",
            "press",
            "select",
            "wait_for_load_state",
            "wait_for_selector",
            "extract_text",
            "extract_html",
            "screenshot"
          ],
          "required": true,
          "type": "string"
        },
        "blur": {
          "default": null,
          "description": "CSS selectors to frost (blur) on the live page before this step acts, so secrets never appear in a recording. Persists until navigation. Fails closed: every selector must blur at least one element on the current page (a typo'd selector matching nothing is unverifiable), otherwise the step aborts with BROWSER_AUTOMATION_BLUR_FAILED instead of recording the secret unblurred. If the target renders later, wait_for_selector first.",
          "items": {
            "description": "",
            "type": "string"
          },
          "required": false,
          "type": "array"
        },
        "key": {
          "default": null,
          "description": "",
          "required": false,
          "type": "string"
        },
        "marker": {
          "default": null,
          "description": "Visual marker drawn on the page right before a step acts.",
          "properties": {
            "margin": {
              "default": 16,
              "description": "",
              "maximum": 60,
              "minimum": 4,
              "required": false,
              "type": "integer"
            },
            "shape": {
              "default": "oval",
              "description": "",
              "enum": [
                "oval",
                "circle"
              ],
              "required": false,
              "type": "string"
            }
          },
          "required": false,
          "type": "object"
        },
        "selector": {
          "default": null,
          "description": "",
          "required": false,
          "type": "string"
        },
        "text": {
          "default": null,
          "description": "",
          "required": false,
          "type": "string"
        },
        "timeout_ms": {
          "default": 10000,
          "description": "",
          "maximum": 60000,
          "minimum": 500,
          "required": false,
          "type": "integer"
        },
        "url": {
          "default": null,
          "description": "",
          "required": false,
          "type": "string"
        },
        "value": {
          "default": null,
          "description": "",
          "required": false,
          "type": "string"
        }
      },
      "type": "object"
    },
    "maxItems": 20,
    "minItems": 1,
    "required": true,
    "type": "array"
  }
}
```

## `screenshot`

Action slug: `screenshot`

Price: `5` credits

Capture a PNG screenshot and save it to your File Manager (requires workflow budget context). The image is NOT returned inline; the response has artifact.file_id and a fresh artifact.signed_url for viewing or analysis.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```

## `start_recording`

Action slug: `start-recording`

Price: `5` credits

Start an MP4 screen recording of the session. show_cursor controls whether the cursor appears in the video.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `show_cursor` | `boolean` | no | For start_recording: capture the real cursor in the video. Only human (takeover) interaction moves the real cursor; agent-driven motion uses the run_steps tutorial fake cursor instead. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "show_cursor": true
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "show_cursor": {
    "default": true,
    "description": "For start_recording: capture the real cursor in the video. Only human (takeover) interaction moves the real cursor; agent-driven motion uses the run_steps tutorial fake cursor instead.",
    "required": false,
    "type": "boolean"
  }
}
```

## `status`

Action slug: `status`

Price: `5` credits

Return the session's sanitized live status (no cookies).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```

## `stop_recording`

Action slug: `stop-recording`

Price: `5` credits

Stop the recording and save the MP4 to your File Manager (requires workflow budget context). The video is NOT returned inline; the response has artifact.file_id — fetch it from the File Manager to view the recording. Call before close_browser.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```

## `upload_file`

Action slug: `upload-file`

Price: `5` credits

Attach File Manager files to a visible page <input type=file>. Reveal the input with run_steps first, then pass its selector and file_ids.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |
| `file_ids` | `array` | yes | File Manager file_id values for upload_file. |
| `selector` | `string` | yes | Optional selector for extract_page or upload_file. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id",
  "file_ids": [
    "example file id"
  ],
  "selector": "example selector"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  },
  "file_ids": {
    "description": "File Manager file_id values for upload_file.",
    "items": {
      "description": "",
      "type": "string"
    },
    "required": true,
    "type": "array"
  },
  "selector": {
    "description": "Optional selector for extract_page or upload_file.",
    "required": true,
    "type": "string"
  }
}
```

## `wait_for_takeover`

Action slug: `wait-for-takeover`

Price: `5` credits

Poll the session status after request_user_takeover.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `browser_session_id` | `string` | yes | Opaque browser runtime session id returned by initialize_browser. |

Sample parameters:

```json
{
  "browser_session_id": "example browser session id"
}
```

Generated JSON parameter schema:

```json
{
  "browser_session_id": {
    "description": "Opaque browser runtime session id returned by initialize_browser.",
    "required": true,
    "type": "string"
  }
}
```
