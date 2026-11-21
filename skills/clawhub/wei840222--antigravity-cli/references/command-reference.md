# Command Reference

Source: <https://antigravity.google/docs/cli/reference/>. Recorded against `agy` 1.4.12 (`agy --help`, 2026-10-31). The installed `agy --help` wins. On any other version, say these flags are the 1.4.12 set and tell the user to upgrade before trusting them. Local-only notes: `references/cli-usage.md`.

## Slash commands

Type `/` for typeahead. Category: U utilities, T tools and tasks, R reasoning, C configurations, A account, V conversations, P planning, X core.

| Command | Alias | Cat | Purpose |
| --- | --- | --- | --- |
| `/add-dir <path>` | | U | Add a workspace directory |
| `/agents` | | T | Switch custom agents; monitor background subagents |
| `/artifact` | | T | Open Artifact Review |
| `/boost <task>` | | R | On-demand multi-agent deep reasoning |
| `/browser <task>` | | T | Browse, verify UI, debug in browser |
| `/btw <query>` | | U | Side question; main conversation keeps running |
| `/changelog` | | U | Release notes; headless mode prints CLI changes |
| `/clear` | `/new` | U | Clear terminal and reset conversation context |
| `/codesearch <query>` | `/cs`, `/search` | U | Search code across the workspace |
| `/config` | `/settings` | C | Settings editor |
| `/context` | | U | Context usage |
| `/copy [n\|btw]` | | U | Copy last response, n-th response, or latest `/btw` answer |
| `/credits` | | A | G1 credit balance and purchase links |
| `/diff` | | U | Diff viewer: changes, turns, commits |
| `/effort [level]` | | C | Reasoning effort, `low` through `max`, model-dependent |
| `/exit` | `/quit` | X | Close TUI |
| `/feedback` | | U | Feedback panel |
| `/fork` | `/branch` | V | Clone thread; workspace stays |
| `/goal <objective>` | | R | Run until the goal is verified; no intermediate pause |
| `/grill-me [task]` | | P | One question at a time, with a recommended answer, before work |
| `/help` | | U | Commands and shortcuts |
| `/hooks` | | T | Pre-flight and post-format hooks |
| `/keybindings` | | C | Shortcut editor |
| `/learn [instruction]` | | T | Propose rules or skills from session corrections |
| `/logout` | | A | Disconnect profile; purge keyring tokens |
| `/mcp` | | T | MCP server manager |
| `/model` | | C | Set preferred model. `/model <model> <prompt>` uses another model for one prompt only |
| `/open <path>` | | U | Open path in system editor |
| `/permissions` | | C | Tool permissions |
| `/plan [task]` | | P | Explore, clarify, draft a reviewable implementation plan |
| `/plugin` | `/plugins` | T | Plugin manager, or inline install, uninstall, enable, disable, list |
| `/rename <name>` | | V | Rename thread |
| `/remote-control [on/off]` | | U | Remote Control for this terminal session |
| `/resume` | `/switch`, `/conversation` | V | Conversation picker |
| `/rewind` | `/undo` | V | Roll history back to a previous message |
| `/schedule <when> <task>` | | T | One-shot timer or recurring cron |
| `/skills` | | T | Loaded skills. `/skills reload` reloads from disk |
| `/statusline` | | C | Status bar |
| `/tasks` | | T | Background shell logs |
| `/teamwork <task>` | | R | Multi-agent teams; paid plans |
| `/title [on/off]` | | C | Terminal window title |
| `/usage` | `/quota` | U | Model quota. Credits are `/credits` |
| `/voice` | `/record` | U | Microphone dictation |

`/fast` and `/planning` are absent from this table. Use `/effort` and `/plan` unless installed `/help` still shows the old names.

## Keybindings

Global keys stay active in every panel.

| Key | Command | Behavior |
| --- | --- | --- |
| `Esc` | `cli.escape` | Close panels, halt streams, or clear an empty prompt |
| `Ctrl+C` | `cli.exit` | Quit. Asks when the agent is working |
| `Ctrl+D` | `cli.exit` | Quit only when the prompt is empty |
| `Ctrl+L` | `cli.clear_screen` | Clear the visual buffer |

Prompt keys apply while typing.

| Key | Command | Behavior |
| --- | --- | --- |
| `Enter` | `cli.enter` | Submit prompt or menu selection |
| `Shift+Enter` / `Ctrl+J` | `prompt.insert_newline` | Newline; do not submit |
| `Shift+Tab` | `cli.cycle_mode` | default, accept-edits, auto, plan. `auto` only where available |
| `Ctrl+V` | `edit.paste` | Paste media or clipboard blocks |
| `Ctrl+O` | `view.toggle_trajectory` | Show or hide tool reasoning |
| `Ctrl+R` | `view.review_artifact` | Artifact Review |
| `Ctrl+G` | `edit.open_editor` | Compose in `$EDITOR` |
| `Alt+J` | `subagent.jump_to_waiting` | Next subagent awaiting confirmation |
| `Ctrl+K` | `subagent.approve_fast` | Approve the pending subagent action in the status alert |
| `Ctrl+A` / `Ctrl+E` | | Line start / line end |
| `Ctrl+_` / `Ctrl+Shift+-` | `edit.undo` | Undo last edit |
| `Ctrl+Shift+Z` | `edit.redo` | Redo |
| `Ctrl+D` | | Forward delete when the prompt is not empty |
| `F5` | `voice.start_dictation` | Start or stop dictation |

Navigation applies in panels and menus. `y`, `n`, and `A` apply at confirmation.

| Key | Command | Behavior |
| --- | --- | --- |
| `↑` / `↓` | `navigation.up` / `navigation.down` | Move one item |
| `PgUp` / `Shift+↑` | `navigation.page_up` / `navigation.half_page_up` | Scroll up |
| `PgDn` / `Shift+↓` | `navigation.page_down` / `navigation.half_page_down` | Scroll down |
| `←` / `→` | `navigation.left` / `navigation.right` | Change page, including the session picker |
| `Tab` | `navigation.tab` | Accept slash-command autofill |
| `y` | `confirm.yes` | Allow tool, command, or artifact |
| `n` | `confirm.no` | Reject tool, command, or artifact |
| `A` | | In the review panel, approve all artifacts |

`references/settings-and-tips.md` adds `Ctrl+Z` suspend, `Ctrl+Y` yank, `Ctrl+Home` / `Ctrl+End`, and `e` to edit a proposed command. Those are not in this table.

## Startup flags

Local 1.4.12 `--help` matches this set and adds `--settings`, which the public table omits. Launch from the task directory. The missing `--cwd` flag is in the skill gotchas.

| Flag | Default | Purpose |
| --- | --- | --- |
| `--mode` | `""` | `accept-edits`, `auto`, or `plan`. `auto` is Preview: v1.3.5+ macOS/Linux, v1.4.4+ Windows; needs the terminal sandbox; not for business or enterprise accounts |
| `--model` | | This session. List: `agy models` |
| `--effort` | | `low` through `max`, model-dependent |
| `--agent` | | This session. List: `agy agents` |
| `--add-dir` | `[]` | Extra workspace directory; repeatable. Does not change the process working directory |
| `-c`, `--continue` | `false` | Most recent conversation |
| `--conversation` | | Resume by ID |
| `-i`, `--prompt-interactive` | | Initial prompt, then keep the session |
| `-p`, `--print`, `--prompt` | | One headless prompt. `--prompt` aliases `--print` |
| `--output-format` | `text` | `text`, `json`, `stream-json` |
| `--input-format` | `text` | `text` or `stream-json`. `stream-json` is one NDJSON message per line and requires `--output-format stream-json` |
| `--json-schema` | | Schema string or file. For `stream-json`, final result only |
| `--print-timeout` | `0s` | `0` waits for the turn. Local 1.4.12 default is `0s` |
| `--disable-slash-commands` | `false` | Print mode: leave slash commands and skills unexpanded |
| `--sandbox` | `false` | Terminal sandbox. v1.4.4+: no effect when sandbox is unavailable |
| `--dangerously-skip-permissions` | `false` | Auto-approve every tool. Skill workflow leaves this off unless the user accepts the risk |
| `--remote-control` | `false` | Remote Control on startup |
| `--project` | | Project ID or name |
| `--new-project` | `false` | Create a project for this session |
| `--log-file` | | Override CLI log path |
| `--settings` | | Local 1.4.12 `--help` only: session JSON of `settings.json` keys, inline or a file. Never saved |

## Settings keys

File: `~/.gemini/antigravity-cli/settings.json`. A missing key uses its default. Object keys `permissions`, `statusLine`, `title`, `sandboxProxy`, `customModelsConfig`, and `gcp` stay on the CLI settings page. Schema: `"$schema": "https://antigravity.google/schemas/v1/settings.json"`.

| Key | Type | Default | Notes |
| --- | --- | --- | --- |
| `agentMode` | string | `""` | `""`, `accept-edits`, `auto`, `plan`. `--mode` overrides the session. `auto` constraints match `--mode` |
| `colorScheme` | string | `"terminal"` | `light`, `solarized light`, `colorblind-friendly light`, `dark`, `solarized dark`, `colorblind-friendly dark`, `tokyo night`, `terminal` |
| `altScreenMode` | string | `"default"` | `default`: inline, full-screen views use alternate screen. `always`. `never` is settings-only |
| `toolPermission` | string | `"request-review"` | `request-review`, `proceed-in-sandbox`, `always-proceed`, `strict`. Deny rules apply in every mode |
| `artifactReviewPolicy` | string | `"asks-for-review"` | `asks-for-review`, `agent-decides` (currently the same), `always-proceed`. Does not change file-edit approval |
| `notifications` | boolean | `false` | Bell and desktop notice for approval, a question, or turn completion |
| `showTips` | boolean | `true` | Tips while generating |
| `showFeedbackSurvey` | boolean | `true` | Quality survey after task completion |
| `editor` | string | `"auto"` | `$EDITOR`, then `vim`; Windows falls back to `edit` / `notepad`. Also `vim`, `emacs`, or another command |
| `editorMode` | string | `"default"` | `default` or `vim`. This is not the `editor` program |
| `vimInsertFirst` | boolean | `false` | Vim starts in Insert; bare Enter submits. Requires `editorMode` `vim` |
| `allowNonWorkspaceAccess` | boolean | `false` | Files outside workspace folders. Permission rules still apply |
| `enableTerminalSandbox` | boolean | `false` | OS containment. v1.4.4+: no effect when sandbox is unavailable |
| `useG1Credits` | boolean | `false` | Spend AI credits after plan quota. Not for business accounts |
| `verbosity` | string | `"medium"` | `high`, `medium`, `low` |
| `runningLightSpeed` | string | `"medium"` | `fast`, `medium`, `slow`, `off` |
| `copyOnSelect` | boolean | `true` | Alt-screen: copy on mouse release. `false`: artifact viewer uses terminal selection |
| `hideActiveItems` | boolean | `false` | Hide active subagents and background tasks under the prompt |
| `pickerGrouping` | string | `"none"` | `/resume`: `none`, or `grouped` by workspace |
| `queuedMessages` | string | `"queue"` | Message during a turn: `queue`, or `send-immediately` |
| `clearScrollbackOnResize` | boolean | `true` | Inline mode: clear scrollback on redraw |
| `disableSlashCommands` | boolean | `false` | Headless `-p`: send a leading `/` as typed. Same as the flag |
| `historySize` | integer | `2000` | Prompt history on disk. `-1` keeps all. `0` clears on exit |
| `model` | string | `""` | Label saved by `/model` |
| `modelProvider` | string | `""` | `"gemini"` uses `GEMINI_API_KEY` |
| `trustedWorkspaces` | string[] | `[]` | CLI writes a folder here when you trust it |
| `useTerminalCursor` | boolean | `false` | Terminal cursor shape instead of a block |

Enable Telemetry in `/config` has no `settings.json` key. The CLI stores it with the account.

The reference-page sample is not the default row: `agentMode` `auto`, `colorScheme` `tokyo night`, `altScreenMode` `always`, `toolPermission` `proceed-in-sandbox`, `notifications` `true`, `enableTerminalSandbox` `true`.
