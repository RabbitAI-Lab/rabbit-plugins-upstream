---
name: qqbrowser-use
description: "Browser automation CLI for AI agents. Use when: (1) the user asks to open, navigate, or interact with a website; (2) the user needs to fill forms, click buttons, take screenshots, download files, or inspect page state; (3) the user asks to extract structured data from web pages; (4) the user asks to record, save, or reuse a browser task, such as 保存为脚本, 录一下, or 下次还要用; (5) the user asks to run an existing playbook. Do NOT use for pure questions about HTML, CSS, or JavaScript without an actual browser task."
source: https://pypi.org/project/qqbrowser-skill/
homepage: https://browser.qq.com/
permissions:
  - network: Required for browser navigation and web page interaction
  - filesystem: Required for downloading files and saving screenshots to temporary directories
---

# qqbrowser-use

Browser automation CLI for AI agents. Wraps every task in an isolated Chrome Tab Group, supports both live automation and reusable playbook replay.

## Platform Support

Linux x86_64, Windows, macOS. Other Linux architectures (ARM, etc.) are not supported.

## Installation

```bash
# Linux / macOS
pipx install qqbrowser-skill
qqbrowser-skill install   # Download and install QQ Browser

# Windows
pip install qqbrowser-skill
qqbrowser-skill install
```

## Quick Start

```bash
qqbrowser-skill browser_start_session --sessionId task-demo-001 --initialUrl https://example.com
qqbrowser-skill playbook_list                          # Check existing playbooks first
qqbrowser-skill browser_snapshot                       # Get elements with encoded indices
qqbrowser-skill browser_click_element --index "<index-from-snapshot>"
qqbrowser-skill browser_end_session --sessionId task-demo-001
```

---

## Commands

### Session Management

```bash
browser_start_session --sessionId <id> [--title "<title>"] [--color <color>] [--initialUrl <url>]
browser_end_session --sessionId <id>
```

> `--initialUrl`: 启动会话时直接导航到指定 URL，省去单独调用 `browser_go_to_url` 的步骤。如果提供了该参数，会话创建后会自动打开对应页面。
>
> Isolation mode is fixed to `enforce` — `browser_start_session` does not accept an `--isolation` flag.

### Navigation

```bash
browser_go_to_url --url <url>
browser_go_back
browser_wait --seconds <n>              # Default 3s
```

### Snapshot & Screenshot

```bash
browser_snapshot                        # Element indices (for interaction)
browser_snapshot --markdown             # Markdown (for reading)
browser_screenshot [--full] [--annotate]
```

**`browser_snapshot --markdown`** returns clean Markdown of the page (ads/nav/scripts stripped, no element indices). Use it when AI needs to read/summarize page content in one-off tasks (Branch C). Do NOT use it inside `task_begin`/`task_end` (Branch B) or when you need structured data — use `browser_eval_content_js` instead.

### Click & Input

```bash
browser_click_element --index <id>
browser_dblclick_element --index <id>
browser_focus_element --index <id>
browser_input_text --index <id> --text "<content>"
```

### Scroll

```bash
browser_scroll_down [--amount <px>]
browser_scroll_up [--amount <px>]
browser_scroll_to_text --text "<text>"
browser_scroll_to_top
browser_scroll_to_bottom
browser_scroll_by --direction <dir> --pixels <n> [--index <id>]
browser_scroll_into_view --index <id>
```

### Keyboard

```bash
browser_keypress --key <key>
browser_keyboard_op --action type --text "<content>"
browser_keyboard_op --action inserttext --text "<content>"
browser_keydown --key <key>
browser_keyup --key <key>
```

### Dropdown & Checkbox

```bash
browser_get_dropdown_options --index <id>
browser_select_dropdown_option --index <id> --text "<option>"
browser_check_op --index <id> --value / --no-value
```

### Semantic Locators (Find and Act)

```bash
browser_find_and_act --by <role|text|label|placeholder|testid|css> --value "<v>" --action <click|fill|type> [--actionValue "<v>"] [--name "<n>"] [--nth <n>]
```

> `--nth`: 1-based index for list iteration (`--nth 1` = first match). Use `by: "css"` + `--nth` for loops.

### Get Information & State

```bash
browser_get_info --type <text|url|title|html|value|attr|count|box|styles|list_selector> [--index <id>] [--attribute <name>]
browser_check_state --state <visible|enabled|checked> --index <id>
```

> **`list_selector`**: Auto-detect CSS selector for list iteration. Pass any list item's index → returns `{"selector": "...", "count": N, "samples": [...]}`.

### JavaScript Evaluation

```bash
browser_eval_content_js --script "<js_code>"
browser_eval_content_js --script "<base64>" --base64
```

### Download

```bash
browser_download_file --index <id>
```

After a download succeeds, return the saved file path to the user or the next processing step. If the user asked to analyze the downloaded file, treat that path as the output of the browser sub-task and continue outside the browser workflow.

### Tab Management

```bash
browser_tab_open --url <url>
browser_tab_list
browser_tab_switch --tabId <n>
browser_tab_close --tabId <n>
```

### Dialog

```bash
browser_dialog --action <accept|dismiss> [--text "<input>"]
```

### Task Recording

```bash
task_begin --description "<desc>"
task_end
task_latest                                # Get most recent recording
```

> **When to use**: Only when user explicitly asks to record/save/reuse (trigger words: "record this", "save this", "保存为脚本", "录一下", "下次还要用"). Without explicit request, do NOT use these commands.
>
> **Before calling `task_begin`**: MUST read [references/playbook.md](./references/playbook.md) for recording quality rules — they are required to make the recording reusable.
>
> **After `task_end`**: Raw recordings are NOT replay-ready. Call `task_latest`, then follow [references/playbook.md → From Recording to Playbook](./references/playbook.md#from-recording-to-playbook) to generate, save, and verify the playbook JSON.

### Playbook & Replay

```bash
playbook_list                              # List available playbooks
browser_replay --script <path> [--variables '{"key":"value"}']
```

> **How to use**:
> 1. `playbook_list` returns available playbooks with `path`, `name`, `description`, and `params` (required variables).
> 2. Match the user's task against returned playbooks by name/description/URL.
> 3. Read the matched playbook's `params` to know which `--variables` keys are required.
> 4. Pass variables as JSON: `--variables '{"param1": "value1", "param2": "value2"}'`
>
> ⚠️ `browser_replay` can take **up to 10 minutes**. Wait patiently — do NOT interrupt, retry, or fall back to manual mode.
>
> For full output format (success/failure/step_results), see [references/commands-extended.md](./references/commands-extended.md#browser_replay-output-format).

### Utility

```bash
browser_done --success --text "<msg>"
status
list
```

> `browser_done` is a status/reporting utility only. It does **not** replace `browser_end_session`, and it does not release the session mapping.

---

## ⚠️ Core Workflow (MANDATORY)

> **Every automation MUST be wrapped in `browser_start_session` / `browser_end_session`, and you MUST run `playbook_list` before any `task_begin` or `browser_go_to_url`.** Never start manual automation without first checking for existing playbooks.

### Decision Flow

```
Step 0: Composite request?                    ← Multiple browser sub-tasks or browser → AI → browser flow?
        ├── YES → See references/session-lifecycle.md → Handling Composite Tasks.
        │         Start ONE session for the whole composite task,
        │         then run each sub-task through Step 2-3 independently,
        │         and call browser_end_session once after all sub-tasks.
        └── NO  → Continue as a single task ↓

Step 1: browser_start_session                 ← ⛔ MANDATORY: first command, no exceptions
Step 2: playbook_list                         ← ⛔ MANDATORY: ALWAYS call before any navigation, even if you think no playbook exists
Step 3: Match?
        ├── YES → browser_replay              ← Branch A: Replay
        └── NO  → Manual automation
                  ├── Recording mode          ← Branch B: user explicitly asks to record
                  │     task_begin
                  │     browser_* operations...
                  │     task_end
                  │     → then continue with references/playbook.md
                  └── Non-recording mode      ← Branch C: one-off task
                        browser_* operations...
Step 4: browser_end_session                   ← ⛔ MANDATORY: ALWAYS execute, even on failure or early exit
```

> **⛔ Non-Negotiable Rules:**
> 1. **`playbook_list` MUST be called every time** after `browser_start_session`, before any `browser_go_to_url` or other browser commands — no exceptions, no shortcuts.
> 2. **`browser_end_session` MUST be called at the end** regardless of outcome (success, failure, error, early exit, user interrupt). Think of it as a `finally` block — it always runs.

**Recording (Branch B) triggers only on explicit user request.** Trigger words: "record this", "save this", "make reusable", "保存为脚本", "录一下", "下次还要用". Without an explicit request, use **Branch C** (non-recording) — do **not** wrap the operations in `task_begin` / `task_end`.

### Human-in-the-Loop Verification Points

If the site requires CAPTCHA, SMS code, email code, MFA/2FA, QR login, device confirmation, or any other human verification step:

- Pause automation at that point.
- Keep the current session alive.
- Ask the user to complete the verification manually.
- Resume only after the verification step is finished.

Do **not** blindly retry replay or switch branches just because a human verification wall appears.

### Step 1: Start Session (REQUIRED)

```bash
qqbrowser-skill browser_start_session --sessionId task-<purpose>-<counter> [--initialUrl <url>]
```

`sessionId` must be unique per task (e.g. `task-form-001`). Use `--initialUrl` to navigate directly on session start, combining session creation and navigation into one step. Full flags and idempotency rules: [references/session-lifecycle.md](./references/session-lifecycle.md).

### Step 2: Check Playbooks (⛔ MANDATORY — DO NOT SKIP, NO EXCEPTIONS)

```bash
qqbrowser-skill playbook_list
```

**This step is non-negotiable.** You MUST call `playbook_list` every single time, even if:
- You are sure no playbook exists for this task.
- You have just completed a sub-task in a composite pipeline and are starting the next one.
- The user's request seems trivial or one-off.

Match returned playbooks against the user's task by `name`, `description`, keywords, target URL, and side-effect profile.

- For **read-only / low-risk tasks** (read, extract, summarize, inspect), a high-confidence partial match may still prefer replay.
- For **side-effecting tasks** (post, submit, message, purchase, delete, publish), replay is allowed only when the task intent, target site, entry page, and key side effects are clearly equivalent.
- If equivalence is uncertain, do **not** replay blindly — ask the user or fall back to a safer path.

### Step 3: Branch by Match Result

#### Branch A — Playbook matched → Replay

> ⚠️ **`browser_replay` may run for up to 10 minutes.** Wait for it to return — **NEVER interrupt, retry, or fall back to manual mode while it is still running.** Replayed operations are usually **not idempotent** (posting, submitting, messaging), so a premature retry will cause duplicate side effects.

```bash
qqbrowser-skill browser_replay --script <path> --variables '{...}'
```

#### Safety Gate for Side-Effecting Tasks

Before replaying a playbook that may cause real-world side effects — such as posting, submitting, sending messages, purchasing, deleting, or publishing — verify all of the following:

1. The target site/account/page matches the user's intent.
2. Required variables are complete and unambiguous.
3. The expected outcome is the same as the original playbook's outcome.
4. The user has clearly authorized executing the live action.

If any of the above is uncertain, do not replay blindly. Prefer draft mode, test data, manual review, or explicit user confirmation.

### If `browser_replay` Returns Failure

When replay finishes with `success: false`:

1. Inspect the failed step and its error details first.
2. Do **not** immediately retry the same replay on live targets.
3. Do **not** automatically fall back to manual execution for side-effecting tasks.
4. For read-only tasks, manual fallback is acceptable if the failure is clearly non-destructive.
5. For side-effecting tasks, require user confirmation or a safer environment before retrying or manually continuing.

#### Branch B — No playbook + user asked to record → Manual with recording

> **Before calling `task_begin`, MUST read [references/playbook.md](./references/playbook.md).** These rules are required to make the recording reusable; do not start recording from the short example alone.

```bash
qqbrowser-skill task_begin --description "描述任务"
qqbrowser-skill browser_go_to_url --url <url>
qqbrowser-skill browser_snapshot
# ... interact using indices ...
qqbrowser-skill task_end
```

**After `task_end`**, continue following [references/playbook.md](./references/playbook.md#from-recording-to-playbook) to generate the playbook JSON.

#### Branch C — No playbook + no recording request → Plain manual

Default fallback for one-off tasks. Do **not** call `task_begin` / `task_end`. **Still call `playbook_list` first** (Step 2 is mandatory for all branches).

```bash
qqbrowser-skill playbook_list                  # ⛔ MANDATORY — do not skip
qqbrowser-skill browser_go_to_url --url <url>
qqbrowser-skill browser_snapshot
# ... interact using indices ...
```

### Step 4: End Session (⛔ MANDATORY — always executed, like a `finally` block)

```bash
qqbrowser-skill browser_end_session --sessionId task-<purpose>-<counter>
```

**This step is non-negotiable.** `browser_end_session` MUST be called at the end of every task, regardless of outcome:
- ✅ Task completed successfully → call `browser_end_session`
- ❌ Task failed with an error → call `browser_end_session`
- 🛑 Task interrupted or early exit → call `browser_end_session`
- ⏸️ Human verification needed (CAPTCHA, etc.) → keep session alive during verification, then call `browser_end_session` after

**Never leave a session dangling.** If you called `browser_start_session`, you MUST call `browser_end_session` before finishing.

---

## Common Patterns

### Form Submission

```bash
qqbrowser-skill browser_start_session --sessionId task-form-001 --initialUrl https://example.com/signup
qqbrowser-skill playbook_list
qqbrowser-skill browser_snapshot
qqbrowser-skill browser_input_text --index "<name-index>" --text "Jane Doe"
qqbrowser-skill browser_input_text --index "<email-index>" --text "jane@example.com"
qqbrowser-skill browser_select_dropdown_option --index "<state-index>" --text "California"
qqbrowser-skill browser_click_element --index "<submit-index>"
qqbrowser-skill browser_wait --seconds 2
qqbrowser-skill browser_snapshot                    # Verify result
qqbrowser-skill browser_end_session --sessionId task-form-001
```

### Data Extraction

| Approach | When | Replayable? |
|----------|------|-------------|
| `browser_snapshot --markdown` | AI reads/summarizes a page once (Branch C only) | ❌ |
| `browser_snapshot` + `browser_get_info` | Read one specific element's text/attribute | ❌ |
| `browser_eval_content_js` | Structured JSON / multiple items / **only safe option in Branch B** | ✅ |

```bash
qqbrowser-skill browser_start_session --sessionId task-extract-001 --initialUrl https://example.com/products
qqbrowser-skill playbook_list
qqbrowser-skill browser_eval_content_js --script "JSON.stringify(Array.from(document.querySelectorAll('.product-item')).slice(0,10).map(el=>({name:el.querySelector('.name')?.textContent?.trim(), price:el.querySelector('.price')?.textContent?.trim()})))"
qqbrowser-skill browser_end_session --sessionId task-extract-001
```

### Infinite Scroll

```bash
qqbrowser-skill browser_start_session --sessionId task-feed-001 --initialUrl https://example.com/feed
qqbrowser-skill playbook_list
qqbrowser-skill browser_scroll_to_bottom
qqbrowser-skill browser_wait --seconds 2
qqbrowser-skill browser_snapshot
qqbrowser-skill browser_end_session --sessionId task-feed-001
```

---

## Key Concepts

- **Element Index**: Encoded string like `2_sfli_qp0u` (`highlightIndex_attrHash_xpathHash`). Generated by `browser_snapshot`, used to target elements. **Indices are regenerated on every snapshot** — always re-snapshot before reusing indices. **Never invent numeric indices like `1` or `2`; always copy the encoded index exactly from the latest `browser_snapshot` output.**
- **Snapshot**: Returns page content with indexed elements. Re-snapshot after any DOM change (navigation, form submit, modal, AJAX). Most `browser_*` commands executed inside an active session already return updated page state in their response. Use standalone `browser_snapshot` only when you truly need a fresh interactive view or the previous response is not sufficient.
- **Session**: AI tasks MUST be wrapped with `browser_start_session` / `browser_end_session` for tab group isolation.
- **Task Recording**: Manual browser tasks intended for replay MUST be wrapped with `task_begin` / `task_end` for playbook generation.
- **Playbook**: Parameterized JSON script that replays a recorded task without AI.

---

## Reference Files (Load On Demand)

| Reference | Load when… |
|-----------|-----------|
| [references/commands-extended.md](./references/commands-extended.md) | You need extended details on `browser_snapshot --markdown` usage, `browser_replay` output format, or advanced flag semantics |
| [references/session-lifecycle.md](./references/session-lifecycle.md) | You need full session rules, or the user's request is a **composite task** with multiple browser sub-tasks or browser → AI → browser flow |
| [references/playbook.md](./references/playbook.md) | User asks to **record/save/reuse**, generate/edit a playbook JSON, or run a reusable browser task |

---

## Notes

- Refs (element indices) are stable per snapshot but change on navigation — always re-snapshot after page changes.
- Use `browser_input_text` for form fields to ensure existing text is cleared.
- Use `browser_find_and_act` with semantic locators when element indices are unstable across sessions.
- For full `browser_replay` output format and consumption guide, see [references/commands-extended.md](./references/commands-extended.md#browser_replay-output-format).

---

## Evaluation Report

See the full skill evaluation report: [QQBrowserUse](https://bak.res.qq.com/nav/qqbrowser_skills/QQBrowserSkillReport.html)
