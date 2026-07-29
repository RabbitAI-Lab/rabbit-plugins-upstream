# HTTP Gateway automation actions

## Contents

- Request and success contract
- Observation
- Navigation and apps
- Element and coordinate interaction
- Text and keyboard
- Waiting and swiping
- Reliable execution patterns

## Request and success contract

The client builds the synchronous Gateway request. Use:

```bash
python3 scripts/duoplus_ai.py --api-key 'API_KEY' action IMAGE_ID ACTION_NAME --params '{...}'
```

A successful action must satisfy all three checks:

1. HTTP request completed successfully.
2. Outer result has `state: "SUCCEEDED"`.
3. Parsed `result_json` has `success: true`, followed by an observed UI state matching the requested outcome.

`wait_before` and `wait_after` can be included in any action's `params` in milliseconds.

## Observation

Get formatted UI state and a screenshot:

```bash
python3 scripts/duoplus_ai.py --api-key 'API_KEY' ui-state IMAGE_ID --screenshot-out screen.png
```

The script removes large base64 data from stdout and writes decoded screenshot bytes to the requested path. Use the UI tree for selectors and the screenshot for visual/WebView/canvas targets.

## Navigation and apps

| Action | Required/important params | Example |
|---|---|---|
| `GO_TO_HOME` | none | `{}` |
| `PAGE_BACK` | none | `{}` |
| `OPEN_APP` | `package_name` | `{"package_name":"com.android.settings"}` |
| `KEYBOARD_OPERATION` | `key`: `enter`, `delete`, `tab`, `escape`, `space` | `{"key":"enter"}` |

## Element and coordinate interaction

| Action | Params |
|---|---|
| `CLICK_ELEMENT` | One or more of `text`, `resource_id`, `class_name`, `content_desc`; optional zero-based `element_order`. |
| `LONG_ELEMENT` | Same selector fields; optional `duration` in milliseconds. |
| `CLICK_COORDINATE` | `x`, `y`. |
| `LONG_COORDINATE` | `x`, `y`, optional `duration`. |
| `DOUBLE_TAP_COORDINATE` | `x`, `y`. |
| `GET_SINGLE_ELEMENT_TEXT` | Selector fields such as `text`, `resource_id`, `class_name`. |

Coordinates sent through the AI handler are relative integers from `0..1000`. The service converts them to physical display pixels. Use a screenshot taken immediately before the action; never reuse coordinates after navigation or rotation without observing again.

Selector examples:

```json
{"text":"Log in"}
{"resource_id":"com.example:id/login"}
{"content_desc":"Search"}
{"text":"Item","element_order":1}
```

Prefer stable `resource_id`, then content description/text. If multiple elements match and the intended one is not clear, ask the user instead of guessing.

## Text and keyboard

`INPUT_CONTENT` requires a focused input:

```json
{"content":"ads","clear_first":true}
```

Reliable sequence:

1. Observe.
2. Click the input field.
3. Send `INPUT_CONTENT`.
4. Send `KEYBOARD_OPERATION` with `{"key":"enter"}` if submission is required.
5. Observe and verify.

## Waiting and swiping

| Action | Params |
|---|---|
| `WAIT_TIME` | `wait_time` in milliseconds. |
| `WAIT_FOR_SELECTOR` | `text` and/or `resource_id`; optional `timeout`, default 10 seconds. |
| `SLIDE_PAGE` | `direction`: `up/down/left/right`; optional `start_x`, `start_y`, `end_x`, `end_y`. |

For scrolling down content, the finger moves up: use `direction: "up"`. Prefer the default gesture first. When specifying coordinates, keep them inside the content area and vary them slightly between attempts. Stop after three ineffective swipes unless the user requested exhaustive scrolling.

## Reliable execution patterns

### Open an app

```bash
python3 scripts/duoplus_ai.py --api-key 'API_KEY' action IMAGE_ID OPEN_APP \
  --params '{"package_name":"com.android.chrome","wait_after":1200}'
python3 scripts/duoplus_ai.py --api-key 'API_KEY' ui-state IMAGE_ID --screenshot-out after-open.png
```

### Click an accessibility element

```bash
python3 scripts/duoplus_ai.py --api-key 'API_KEY' action IMAGE_ID CLICK_ELEMENT \
  --params '{"text":"Continue","wait_after":800}'
python3 scripts/duoplus_ai.py --api-key 'API_KEY' ui-state IMAGE_ID --screenshot-out after-click.png
```

### WebView/canvas fallback

If `CLICK_ELEMENT` fails and the target is visible in the screenshot but absent from the UI tree:

1. Measure its center in the normalized screenshot coordinate space.
2. Convert to relative `0..1000` if needed.
3. Call `CLICK_COORDINATE` once.
4. Observe before retrying.

### Stop a stuck task

Use the task ID returned/recorded for the running request:

```bash
python3 scripts/duoplus_ai.py --api-key 'API_KEY' stop IMAGE_ID TASK_ID --reason 'operation timeout'
```
