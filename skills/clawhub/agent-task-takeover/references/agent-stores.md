# Agent session stores

Where each agent keeps its conversations on disk, how the records are shaped, and what to read first. Paths are given for Windows; on macOS/Linux the same layouts apply under `~/` (Electron apps use `~/Library/Application Support/<App>` and `~/.config/<App>` respectively). "Verified" means the shape was confirmed against real files; anything else is marked as such — verify before trusting.

## Support matrix

| Agent | Type | Store | Reader script | Status |
|---|---|---|---|---|
| opencode | CLI | `~/.local/share/opencode/opencode.db` (SQLite) | `dump_opencode_session.py` | verified |
| ZCode | CLI | `~/.zcode/cli/rollout/model-io-session_*.jsonl` | `dump_jsonl_session.py` | verified |
| Codex CLI | CLI | `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` | `dump_jsonl_session.py` | verified |
| Claude Code | CLI | `~/.claude/projects/<cwd-dashes>/<uuid>.jsonl` | `dump_jsonl_session.py` | verified |
| Gemini CLI | CLI | `~/.gemini/tmp/<hash>/chats/session-*.json` | `dump_jsonl_session.py` (auto-detect) | location known; shape unverified on the reference machine |
| aider | CLI | `~/.aider.chat.history.md` (plain markdown) | read directly | location known; trivial format |
| Cursor | Electron | `AppData/Roaming/Cursor/User/**/state.vscdb` | `dump_vscdb_chat.py --app cursor` | verified |
| Trae | Electron | `AppData/Roaming/Trae/User/**/state.vscdb` | `dump_vscdb_chat.py --app trae` | verified |
| VS Code (Copilot chat) | Electron | `AppData/Roaming/Code/User/workspaceStorage/*/chatSessions/*.json` + `state.vscdb` | `dump_vscdb_chat.py --app code` | verified |
| Kiro / Windsurf / Antigravity | Electron | same VS Code-family layout under their app dirs | `dump_vscdb_chat.py --app <name>` | layout assumed from family; verify on first use |
| WorkBuddy (腾讯) | Electron | `~/.workbuddy/` (see section below) | discovery recipe | **store unconfirmed** |

---

## CLI agents

### opencode (sst/opencode)

- **Store**: `~/.local/share/opencode/opencode.db` (SQLite, WAL mode). Open read-only: `sqlite3.connect("file:<path>?mode=ro", uri=True)`.
- **Tables**:
  - `session`: `id` (`ses_...`), `title`, `directory`, `parent_id` (set for subagent sessions), `time_created`, `time_updated` (ms epoch), `summary_additions/deletions/files`, `tokens_*`.
  - `message`: `id` (`msg_...`), `session_id`, `data` (JSON with `role`, `time.created`, `agent`, `model`).
  - `part`: `id`, `message_id`, `session_id`, `data` (JSON; `type` is `text` for prose — other types are tool calls/steps you can skip).
- **Subagents**: rows in `session` with `parent_id` = main session id; titles look like `<task> (@general subagent)`. Read their final assistant message for their report.
- **Read first**: the **last substantial assistant message**. When opencode compacts an overflowing conversation, it writes a structured handoff there (`## Objective`, `## Work State` with Completed/Active/Blocked, `## Next Move`, `## Relevant Files`). That block is the best takeover input that exists.
- **Script**: `scripts/dump_opencode_session.py --list [--keyword X]` / `--id ses_... [--user-only] [--chars N]`.

### ZCode

- **Fast path (when ZCode is the taker)**: the built-in `ReadSessionContext` tool — `strategy='handoff'` for a continuation summary, `strategy='relevant'` for focused retrieval, `sessionId='sess_...'`. No file parsing needed.
- **On disk**: `~/.zcode/cli/rollout/model-io-session_<hash>.jsonl` — model I/O rollouts; each line is one API request. The conversation lives at **`request.messages`** (sibling of `request.body`, which holds model params/system prompt). The **last line's request contains the entire conversation** — extract from that single line rather than replaying every line. Caveat: when ZCode compacts the context, earlier turns are gone from the rollout for good.
- **Also**: `~/.zcode/cli/log/zcode-YYYY-MM-DD.jsonl` (app event log, not a clean transcript); `~/.zcode/v2/tasks-index.sqlite` (task metadata index).

### Codex CLI (OpenAI)

- **Store**: `~/.codex/sessions/YYYY/MM/DD/rollout-<timestamp>-<uuid>.jsonl` — one JSONL file per session.
- **Record shape**: `{"timestamp": ..., "type": ..., "payload": {...}}` where `type` is one of:
  - `session_meta` → `payload.id`, `payload.cwd`, `payload.originator` (session identity)
  - `user_message` → user turns; `payload` has `role` and `content: [{type: "input_text"|"output_text", "text": ...}]`
  - `response_item` → assistant turns; `payload.type == "message"`, `payload.content[].text`
  - `event_msg`, `turn_context`, `function_call*` — skip for storyline extraction.
- **Script**: `scripts/dump_jsonl_session.py <file>` handles this format.

### Claude Code

- **Store**: `~/.claude/projects/<cwd-with-dashes>/<session-uuid>.jsonl` (e.g. `C--Users-name-project/` for `C:\Users\name\project`). Honors `CLAUDE_CONFIG_DIR` when set.
- **Record shape**: JSONL with `type` in `user | assistant | summary | system`, plus `uuid`, `parentUuid`, `timestamp`, `sessionId`, `cwd`, `gitBranch`. Text lives in `message.content` blocks of `type: "text"`. A leading `summary` record often carries the session title.
- **Script**: `scripts/dump_jsonl_session.py <file>` handles this format.

### Gemini CLI

- **Store**: `~/.gemini/tmp/<project-hash>/chats/session-<name>.json` — one JSON document per session, `{"sessionId": ..., "messages": [{"id": ..., "timestamp": ..., "type": "user" | "gemini" | "info" | "tool_use" | ..., "content": ...}]}`.
- **Script**: `scripts/dump_jsonl_session.py <file.json>` auto-detects the single-JSON shape; `gemini`/`model` message types map to the assistant role.
- Not yet verified against a live store — if the shape differs on your machine, note the real keys and adjust `_GEMINI_ROLE_MAP`.

### aider

- **Store**: `~/.aider.chat.history.md` — plain markdown chat history (plus per-repo `.aider*` files). Read it directly; no parser needed.

---

## Electron agents (VS Code family)

Cursor, Trae, VS Code, Kiro, Windsurf and Antigravity are all VS Code forks and share the same storage layout under `<AppData>/<App>/User/`:

- **`workspaceStorage/<workspace-hash>/state.vscdb`** — per-workspace SQLite (table `ItemTable`, columns `key`/`value`). Chat-related keys observed:
  - `chat.ChatSessionStore.index` — index of stored chat sessions
  - `ChatStore` (Trae), `workbench.panel.chat`, `chat.toolsAgentMode` (Cursor), `workbench.panel.icube.aiChatSidebar` (Trae)
  - values are JSON; shapes vary by app/version — extract best-effort with `dump_vscdb_chat.py --db ... --key ...`
- **`globalStorage/state.vscdb`** — app-wide state; same reading rules.
- **`workspaceStorage/<workspace-hash>/chatSessions/<uuid>.json`** — VS Code Copilot chat sessions (verified shape):
  `{"version": ..., "sessionId": ..., "requesterUsername": ..., "requests": [{"message": {"text": ...}, "response": [{"value": ...}] }]}`.
  Dump with `dump_vscdb_chat.py --session <file.json>`.
- The workspace folder for each hash dir is recorded in `workspaceStorage/<hash>/workspace.json`.

### WorkBuddy (腾讯)

- **Root**: `~/.workbuddy/` (app shell: `~/.workbuddy-ai/`).
- **Known entries**: `workbuddy.db` (SQLite — schema was EMPTY on the machine where this registry was written; the app syncs much state remotely), `sessions/`, `tasks/`, `projects/`, `memory/`, `local_storage/`, `user-<uuid>/` per-account dirs, `traces/`, `audit-log/`.
- **Status**: no local conversation transcripts confirmed yet. When asked to take over a WorkBuddy task, run the discovery recipe from SKILL.md inside `~/.workbuddy/` — check `workbuddy.db` tables first, then `user-<uuid>/` and `projects/` subtrees. Update this section once the real location is found.

---

## Notes for all stores

- Epoch times in SQLite stores are **milliseconds**; divide by 1000 for `datetime.fromtimestamp`.
- Always open SQLite files read-only (`file:...?mode=ro`, `uri=True`) so a live agent's writer lock is never disturbed.
- Transcripts may embed secrets (tokens, cookies, auth headers captured from browser flows). Redact before quoting.
- A store file modified in the last few minutes usually means the owning agent is still alive — warn the user before taking over.

## Adding a new agent store

1. Find the store with `scripts/discover_stores.py` + the discovery recipe in SKILL.md.
2. Document the exact path pattern, record shape, and one verified example row in this file (redact sample content).
3. If the shape is JSONL or single-JSON, extend `scripts/dump_jsonl_session.py`; if it is SQLite, extend `dump_opencode_session.py` or `dump_vscdb_chat.py`; otherwise add a focused reader under `scripts/`.
4. Add a regression test with synthetic data in `tests/test_session_tools.py`.
