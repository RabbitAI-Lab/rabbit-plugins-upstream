---
name: x-dm-auto-chat
description: "X (Twitter) DM automated chat end-to-end Skill: scan DM inbox to identify pending-reply conversations, read message history, generate persona-based replies and send; also supports searching users and starting new conversations. Built-in E2E passcode unlock, DM permission filtering, and rate control. Use when user mentions X auto-reply DMs, Twitter DM automated chat, auto-handle unread DMs, reply to X private messages with persona, X DM outreach campaign, batch send DMs to Twitter users, auto-process pending DM replies, Twitter DM bot, automated Twitter outreach, X direct message automation."
---

# X (Twitter) — DM Auto Chat (End-to-End)

> Full X DM automation Skill: inbox scan → conversation read → persona-based reply → send; also supports search-and-outreach. The calling Agent generates reply text based on persona; this Skill handles all mechanical operations.

## Language

All process output to user (progress updates, process notifications) follows the user's language.

## Objective

Encapsulate "refresh DM list → identify pending replies → read context → reply with persona → send" and "search user → enter chat → send first message" into callable end-to-end capabilities.

## Prerequisites

- X account is logged into the browser (`[aria-label="Account menu"]` visible on x.com)
- The 4-digit DM passcode is provided by the caller before execution starts, if the account has E2E encryption enabled; if no passcode is set on the account, this can be omitted
- Caller has prepared a persona description string (used by the calling Agent to generate replies), e.g.: `"You are a friendly community manager. Tone: warm and concise. End every reply with a question."`
- Optional: list of target user search queries (for outreach scenario)

## Pre-execution Checks

### 1. Tool Readiness

If browser-act has been confirmed available in the current session → skip this step.

Invoke `browser-act` via Skill tool to load usage. If installation or configuration issues arise, follow its guidance to resolve then retry.

### 2. Login Verification

If login status for X has been confirmed in the current session → skip this step.

Discover the browser and verify login state — **selection is fully automatic, do not ask the user interactively**:

1. `browser-act browser list` — find browsers with `url` containing `x.com`
   - No X.com browser found → report error and stop: "No browser with X.com open. Please open X.com in a browser first."
   - One X.com browser found → record its `id` as `BROWSER_ID`
   - Multiple X.com browsers found → run `eval "$(python scripts/check-page-state.py)"` on each in order; use the first with `logged_in: true`. If none are logged in → report error and stop.

2. `navigate https://x.com/i/chat` → `wait stable --timeout 15000`

3. `eval "$(python scripts/check-page-state.py)"` — check `logged_in`
   - `logged_in: false` → inform user that login is required; wait; retry this step
   - `logged_in: true` and `need_passcode: true` → run **AI Workflow: DM passcode unlock** before proceeding
   - `logged_in: true` and `need_passcode: false` → ready for business flow

> **BROWSER_ID** resolved here is used as `--browser <BROWSER_ID>` prefix for all subsequent browser-act commands in this execution. No fixed session name is used; BROWSER_ID is resolved fresh each execution.

## Capability Components

> This Skill's operational boundary = what the user can manually do in their browser. It only reads data already displayed to the user on the page, never bypassing authentication or access controls. JS code is encapsulated in Python files under the `scripts/` directory, invoked via `eval "$(python scripts/xxx.py {params})"`. `$(...)` is bash syntax; it is recommended to use the bash tool for execution. All `eval`, `navigate`, `wait`, `state`, `input`, and `screenshot` commands require `browser-act --browser <BROWSER_ID>` prefix at runtime; commands below omit this prefix for clarity.

### Composite: Scan DM inbox (API metadata + DOM preview merged)

`eval "$(python scripts/scan-inbox-merged.py)"`

Output example:
```json
{
  "my_user_id": "123456",
  "count": 14,
  "unread_count": 3,
  "items": [
    {
      "conversation_id": "123:456",
      "conversation_url": "/i/chat/123-456",
      "peer_user_id": "456",
      "peer_screen_name": "username",
      "peer_display_name": "Display Name",
      "peer_avatar_url": "https://pbs.twimg.com/...",
      "peer_is_blue_verified": false,
      "peer_can_dm": true,
      "peer_can_dm_reason": "Allowed",
      "is_muted": false,
      "is_deleted_by_viewer": false,
      "latest_message_timestamp": "6:25 PM",
      "latest_message_preview": "Hello there",
      "latest_message_from_self": false,
      "unread": true
    }
  ],
  "next_cursor": null,
  "message_requests_count": 2
}
```

### API: Fetch DM inbox metadata (with pagination)

`eval "$(python scripts/fetch-inbox-api.py --cursor-id '{cursor_id}' --graph-snapshot-id '{snapshot_id}' --limit {N})"`

Parameters:
- `--cursor-id`: pagination cursor_id from previous response; omit for first page
- `--graph-snapshot-id`: pagination graph_snapshot_id from previous response; omit for first page
- `--limit`: conversations per page, default 20

Output example:
```json
{
  "my_user_id": "123456",
  "count": 20,
  "items": [
    {
      "conversation_id": "123:456",
      "is_muted": false,
      "is_deleted_by_viewer": false,
      "has_more": false,
      "peer_user_id": "456",
      "peer_screen_name": "username",
      "peer_name": "Display Name",
      "participants": []
    }
  ],
  "next_cursor": {"cursor_id": "abc", "graph_snapshot_id": "xyz"},
  "message_requests_count": 2
}
```

### DOM: Read conversation messages

`eval "$(python scripts/read-conversation.py)"`

Output example:
```json
{
  "conversation_id": "123:456",
  "url": "https://x.com/i/chat/123-456",
  "peer_display_name": "Display Name",
  "my_user_id": "123456",
  "message_count": 10,
  "messages": [
    {
      "message_id": "abc123",
      "direction": "peer",
      "text": "Hello there",
      "timestamp_text": "6:25 PM",
      "links": ["https://t.co/..."],
      "images": []
    }
  ]
}
```

### DOM: Scroll to load message history

`eval "$(python scripts/scroll-load-history.py)"`

Output example:
```json
{
  "before_count": 10,
  "after_count": 20,
  "loaded_more": true,
  "reached_top": false
}
```

### DOM: Check composer state

`eval "$(python scripts/check-composer.py)"`

Output example:
```json
{
  "conversation_id": "123:456",
  "url": "https://x.com/i/chat/123-456",
  "composer_ready": true,
  "current_value": "",
  "has_send_button": true,
  "has_voice_button": true,
  "message_count": 10,
  "last_message_id": "abc123"
}
```

### DOM: Verify message sent

`eval "$(python scripts/verify-sent.py '<expected_text>' --prev-last-id '<last_id>')"`

Parameters:
- `expected_text`: the message text that was sent — pass in **single quotes** to prevent shell `$` expansion
- `--prev-last-id`: `last_message_id` recorded before sending, used to detect the newly appeared message

Output example:
```json
{
  "sent": true,
  "composer_cleared": true,
  "current_message_count": 11
}
```

### API: Search X users (with DM permission)

`eval "$(python scripts/search-users.py '<query>')"`

Parameters:
- `query`: name, screen_name, or partial search string

Output example:
```json
{
  "query": "content creator",
  "count": 5,
  "users": [
    {
      "user_id": "456",
      "name": "Display Name",
      "screen_name": "username",
      "avatar_url": "https://pbs.twimg.com/...",
      "is_blue_verified": false,
      "is_verified_organization": false,
      "verified_type": null,
      "can_dm": true,
      "can_dm_on_xchat": true,
      "can_dm_reason": "Allowed",
      "protected": false,
      "suspended": false
    }
  ]
}
```

### JS: Calculate conversation URL from user_id

`eval "$(python scripts/open-conversation-by-user.py '<user_id>')"`

Parameters:
- `user_id`: target user's numeric rest_id

Output example:
```json
{
  "my_user_id": "123456",
  "peer_user_id": "789",
  "conversation_url": "/i/chat/123-789",
  "conversation_id": "123:789",
  "next_step": "navigate to conversation_url then verify composer_ready"
}
```

### JS: Check page state

`eval "$(python scripts/check-page-state.py)"`

Output example:
```json
{
  "url": "https://x.com/i/chat",
  "logged_in": true,
  "need_passcode": false,
  "on_inbox": true,
  "on_conversation": false,
  "has_panel": false,
  "has_composer": false,
  "inbox_count": 14
}
```

### AI Workflow: DM passcode unlock

Triggered when `check-page-state` returns `need_passcode: true`. The passcode must have been provided by the caller as a prerequisite:

1. `state` — locate 4 consecutive `<input maxlength=1 pattern=[0-9]*>` elements; record their indexes `<idx1>` `<idx2>` `<idx3>` `<idx4>`
2. Enter each digit: `input <idx1> "<d1>"` → `input <idx2> "<d2>"` → `input <idx3> "<d3>"` → `input <idx4> "<d4>"` (**must use CDP real keyboard events via `browser-act input`; eval setting value is ignored by X**)
3. `wait stable --timeout 10000`
4. `eval "$(python scripts/check-page-state.py)"` — verify `need_passcode: false` and `on_inbox: true`
5. 3 consecutive failures still showing `need_passcode: true` → report error and stop: "DM passcode may be incorrect."

### AI Workflow: Scenario A — scan unread DMs and reply with persona

**Full flow**: scan inbox → filter pending-reply conversations → per-conversation: read context → calling Agent generates reply → send → delay

1. `eval "$(python scripts/scan-inbox-merged.py)"` — get `items[]`

2. Filter pending-reply conversations: select items where all conditions are met:
   - `unread: true` OR `latest_message_from_self: false`
   - `peer_can_dm: true`
   - `is_muted !== true` AND `is_deleted_by_viewer !== true`

3. For each pending-reply conversation (strictly serial, **random sleep 8–15s between each**):

   a. `navigate https://x.com<conversation_url>` → `wait stable --timeout 15000`

   b. `eval "$(python scripts/check-page-state.py)"` — if `need_passcode: true` → run **AI Workflow: DM passcode unlock** first

   c. `eval "$(python scripts/read-conversation.py)"` — get `messages[]`

   d. *(Optional)* If full history needed: loop `eval "$(python scripts/scroll-load-history.py)"` until `reached_top: true`, then re-read with `read-conversation.py`

   e. [AI Intervention] **Generate reply**: calling Agent combines persona + recent messages (typically last 6) + `peer_display_name` to produce `reply_text`. Max 10,000 characters. Reply content is entirely the caller's decision; this Skill does not participate in generation.

   f. **Send reply**:
      - `eval "$(python scripts/check-composer.py)"` → record `last_message_id`
      - `state` — find `<textarea placeholder=Message>` or `[data-testid="dm-composer-textarea"]` index `TA_IDX`
      - Shell-escape `reply_text` before passing to `input` — prevents `$N`, backtick, `!` from being expanded by the shell:
        ```python
        safe_text = reply_text.replace('\\', '\\\\').replace('$', r'\$').replace('`', r'\`').replace('!', r'\!')
        ```
      - `input <TA_IDX> "<safe_text>"` (**must use CDP real keyboard, cannot use eval**)
      - `wait --selector '[data-testid="dm-composer-send-button"]' --state attached --timeout 5000`
      - `eval "document.querySelector('[data-testid=\"dm-composer-send-button\"]').click(); 'clicked'"`
      - `wait stable --timeout 15000`
      - `eval "$(python scripts/verify-sent.py '<reply_text>' --prev-last-id '<last_message_id>')"` — pass original `reply_text` in single quotes
        - `sent: true` and `composer_cleared: true` → success, record result
        - `sent: false` → record failure, **do not retry** (prevents duplicate sends); proceed to next

   g. Random sleep 8–15s

4. Report batch results (success count / failure count / per-item status)

### AI Workflow: Scenario B — search users and send first message

**Full flow**: search candidates → filter sendable → open conversation → calling Agent generates first message → send

1. For each search query (1–2s interval between searches):
   `eval "$(python scripts/search-users.py '<search_query>')"`

2. Filter: `can_dm: true` AND `can_dm_reason: "Allowed"` AND NOT `suspended` AND NOT `protected`; skip `screen_name` values already in send history

3. For each target user (strictly serial, **random sleep 10–20s between each**):

   a. `eval "$(python scripts/open-conversation-by-user.py '<user_id>')"` → get `conversation_url`

   b. `navigate https://x.com<conversation_url>` → `wait stable --timeout 15000`

   c. `eval "$(python scripts/check-page-state.py)"` — if `need_passcode: true` → run **AI Workflow: DM passcode unlock**

   d. `eval "$(python scripts/check-composer.py)"` — if `composer_ready: false` → skip this user; otherwise record `last_message_id`

   e. [AI Intervention] **Generate first message**: calling Agent produces `first_text` based on persona + target user info (`screen_name`, `name`, verification type). Recommended < 500 characters (shorter first messages reduce spam detection risk).

   f. **Send**: follow the same send sub-steps as Scenario A step 3f, substituting `first_text` for `reply_text`

   g. Random sleep 10–20s

4. Report batch results

## Pagination

**API Pagination** (`fetch-inbox-api.py`): cursor type, start with empty params. Next page value source: `next_cursor.cursor_id` + `next_cursor.graph_snapshot_id` from response. Termination: `next_cursor === null`.

## Success Criteria

- Scenario A: `sent: true` rate ≥ 90% across processed pending-reply conversations
- Scenario B: `composer_ready: true` confirmed for each target user before send; `sent: true` rate ≥ 90%
- Per-item failures have a recorded reason (wrong passcode, composer unavailable, 429, etc.)

## Known Limitations

- **E2E passcode required**: `browser-act input` (CDP real keyboard) is the only working input method for passcode digits — eval setting value is ignored by X
- **Message bodies are E2E encrypted in API**: GraphQL API returns encrypted binary; plaintext only available from the already-unlocked DOM. This Skill must run in an already-logged-in and unlocked browser
- **DM permission enum** (`can_dm_reason` observed values): `Allowed` = can send; `InboxClosed` = recipient closed DM; other values treat as cannot send
- **Non-follower DMs go to Message Requests**: first message to a non-follower goes to their Message Requests; they must accept before it moves to Primary
- **Send rate** (empirical, no official docs): ~5–10 messages/minute max; 8–15s random delay between messages; exceeding triggers HTTP 429 or UI block
- **Message length cap**: 10,000 characters per message (X official limit)
- **Timestamp precision**: DOM only gives X display format (`"30m"` / `"6:25 PM"` / `"May 8"`); no ISO datetime available
- **Text-only**: sending images / GIFs / voice / video / quote tweets not implemented
- **Reply content generation not included**: persona application and context understanding are entirely the calling Agent's responsibility
- **No cross-session state**: per-run reply history, blocklists, and progress must be recorded by the caller in external files (JSONL)
- **Group conversations**: `peer_*` fields take only the first non-self member; fine-grained group replies not supported
- **Message Requests sub-inbox**: only scans Primary inbox; Message Requests sub-inbox scanning not implemented

## Execution Efficiency

- **Batch processing**: one run processes one batch then returns; no resident loop — let the caller decide scheduling cadence
- **Strictly serial**: all DM operations for the same account must be serial — parallel operations accelerate anti-abuse triggering
- **No retry on failure**: DM send failures are usually permission / rate / network issues; retrying risks duplicate sends — record and skip
- **Resume from breakpoint**: use JSONL to record `{target, status, timestamp, error?}` per item; resume from breakpoint on interruption
- **Small-scale validation first**: before bulk runs, validate the full pipeline with 1–2 items; only then run the full batch
- **Reuse browser connection**: use the same `--browser <BROWSER_ID>` throughout the batch; login state persists within the browser instance, no need to re-unlock for each item

## Experience Notes

Path: `{working-directory}/browser-act-skill-forge-memories/x-dm-auto-chat-x-dm-auto-chat.memory.md` (working directory is determined by the Agent running the Skill)

**Before execution**: If the file exists, read it first — it records unexpected situations encountered during past executions (e.g., a strategy has become ineffective, a selector changed, a rate threshold discovered); adjust strategy order accordingly.

**After execution**: If an unexpected situation is encountered (strategy became ineffective, page redesigned, anti-scraping upgraded, better path discovered, new `can_dm_reason` enum values), append a line:
`{YYYY-MM-DD}: {what happened} → {conclusion}`

Normal execution does not write to the file. Do not record what keywords were used, which conversations were replied to, or how many messages were sent — those are task outputs, not experience.
