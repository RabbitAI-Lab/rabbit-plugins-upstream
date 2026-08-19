---
name: tokst-memory
description: Persistent memory for AI agents
version: 0.6.6
---

# TokST Memory Skill

TokST is a **cloud-first memory system**. Data lives in Supabase PostgreSQL
(with pgvector for semantic search); files attach via Cloudflare R2. Memories
are organized by **workspaces** → **atlases** (knowledge bases), scoped per user
via RLS, and shared across every agent and machine that logs in with the same
API key.

You (an AI agent) can use TokST as your long-term memory: load context at the
start of a session, search before deciding, and record durable knowledge after
doing work.

---

## Quick Install (run once per machine)

```bash
# 1. Install the checksum-verified standalone CLI and authorize in the browser
curl -fsSL https://tokst.com/install.sh | bash

# 2. Write local agent instructions (no cloud write and no Git requirement)
tokst init --agents codex

# 3. Optional: bind an existing Atlas to this directory
tokst atlas bind --atlas-id <atlas-id>

# 4. Verify — should show plan, usage, storage, quotas, workspaces, and Atlases
tokst status
tokst doctor
```

> `tokst setup` is the recommended interactive flow. It opens TokST once,
> confirms the signed-in account. Choose workspace and Atlas scope explicitly
> in commands; directory binding remains optional for a single-project folder.
> `tokst login --key tk_live_...` remains available for CI, servers, and
> unattended scripts.

### Platform install

```bash
curl -fsSL https://tokst.com/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://tokst.com/install.ps1 | iex
```

TokST publishes checksum-verified standalone binaries for macOS Apple Silicon, macOS Intel, Linux x64, Linux ARM64, Windows x64, and Windows ARM64. Installation requires `curl` on macOS/Linux or PowerShell on Windows; Bun, Node.js, npm, and a package manager are unnecessary.

---

## Agent Self-Registration

The first time you use this skill in a project, register yourself:

```bash
tokst init --agents <your-agent-name> --json
tokst doctor --json

tokst remember "I have the TokST Memory Skill available. Use 'tokst context' to load project memory before work, 'tokst search' to find specific memories, and 'tokst remember' to store new facts, decisions, and preferences." \
  --type fact \
  --tags skill,tokst,self-registration \
  --source-type agent \
  --source <your-agent-name> \
  --json

# Verify
tokst search "TokST Memory Skill" --json
```

Replace `<your-agent-name>` with your identity (e.g. `codex`, `claude`,
`opencode`, `cursor`, `gpt`). Be consistent across sessions.

In future sessions, run `tokst context --json` and check the `facts` section to
confirm this skill is active.

> **💡 One-link setup:** Share `https://tokst.com/skill.md` with any agent — it's a self-contained install guide that auto-detects the agent type and installs this skill.

WorkBuddy, ZCode, Qoder, and Kimi Code use this skill for the session workflow and MCP for TokST tool calls.

---

## Core Concepts

- **Workspace** — top-level container (`personal`, or a team workspace). Every
  user gets a `personal` workspace automatically.
- **Atlas** — a knowledge base inside a workspace (e.g. one per project).
  `remember` auto-routes to the best-matching atlas by keyword; you rarely
  switch manually.
- **Memory** — a single record: content + type + tags + optional file
  attachments. Identified by `mem_xxxxx`.
- **Attachment** — a file stored in R2, linked to a memory. Upload with
  `--file`, download with `memory download`.

`context`, `search`, and `memory list` read **all atlases** by default. Use
`--atlas-id <id>` only when you explicitly need one atlas.

---

## Read Context First

Before making project decisions, load existing memory:

```bash
tokst context --json
```

Use `--limit` for more than the default per-type results:

```bash
tokst context --limit 1000 --json
```

The output groups memories by type:

| Section | Use for |
|---------|---------|
| `facts` | Stable project facts (dependencies, config, setup) |
| `architecture` | Structural design, system topology, data flow |
| `decisions` | Chosen plans, architecture decisions, rationale |
| `preferences` | Human preferences, workflow habits |
| `tasks` | Open work, next actions, TODOs |
| `notes` | General useful context that doesn't fit above |

---

## Search

Hybrid search (keyword OR-matching + semantic vector similarity, fused via RRF):

```bash
tokst search "database choice" --json
tokst search "API design" --type decision --json          # filter by type
tokst search "auth" --tags security,backend --json        # filter by tag
tokst search "deployment" --atlas-id <atlas-id> --json    # scope to one atlas
tokst search "database choice" --search-mode auto --json  # adaptive fast path (default)
tokst search "related design" --search-mode semantic --json
```

Search defaults to **adaptive auto mode**: strong phrase or full-token matches return immediately;
weak and empty matches add semantic retrieval. `keyword`, `semantic`, and `hybrid` modes provide
deterministic control. Results
are sorted by relevance (matching tokens + recency + vector similarity).

---

## Store Memory

```bash
tokst remember "Decided to use PostgreSQL with pgvector for persistence" \
  --type decision \
  --tags database,architecture \
  --source-type agent \
  --source opencode \
  --json
```

Longer input via stdin:

```bash
cat notes.md | tokst remember --type note --tags notes --json
```

> **Format your content with Markdown** — headings (`##`), lists (`- `), code blocks (`` ``` ``), and tables render beautifully in the dashboard. Plain text works too, but Markdown makes memories more readable and structured. The dashboard renders your memory content as Markdown automatically.

### With file attachments

```bash
# Attach a file when creating the memory (repeatable)
tokst remember "Architecture diagram" --type architecture --file diagram.png --json

# Attach to an existing memory
tokst memory attach mem_xxxxx --file screenshot.png --json
```

Files upload directly to R2 via presigned URL; metadata is indexed in Supabase.
Storage quotas apply (see `tokst status`).

### Batch import

Import an entire folder of files as memories — text files (md, code, json, csv, etc.) are auto-extracted, binary files are uploaded as attachments:

```bash
tokst import ./docs --dry-run                    # preview what will be imported
tokst import ./docs --type architecture           # import with default type
tokst import ./code --tags imported --max 50      # limit to 50 files
tokst import ./large-dir --no-attach              # text only, skip file upload
```

---

## Manage Memories

```bash
tokst memory list --json                          # list all active memories
tokst memory list --atlas-id <id> --json          # scope to one atlas

tokst memory update mem_xxxxx --content "New content" --json   # replace content
tokst memory append mem_xxxxx --content "Addendum" --json      # append to content

tokst memory archive mem_xxxxx --json             # soft-hide (restorable)
tokst memory restore mem_xxxxx --json             # un-archive
tokst memory delete mem_xxxxx --json              # permanent delete
```

### Download attachments

```bash
tokst memory download mem_xxxxx                              # all attachments → ~/Downloads
tokst memory download mem_xxxxx --out ./files                # specify output dir
tokst memory download mem_xxxxx --attachment-id <att-id>     # one specific file
tokst memory download mem_xxxxx --json                       # machine-readable
```

Files stream from R2 via presigned GET URL; original filenames are preserved.
Cloud-only (requires `tokst login`).

---

## Atlases & Workspaces

```bash
# Atlases
tokst atlas init --name "My Project" --json                    # create
tokst atlas bind --atlas-id <id> --json                         # bind this directory
tokst atlas list --json                                        # list all
tokst atlas rename --atlas-id <id> --name "New Name" --json    # rename
tokst atlas profile --atlas-id <id> --keywords api,backend     # set auto-routing keywords
tokst atlas delete --atlas-id <id>                             # delete (and its memories)

# Workspaces
tokst workspace create --name "Team X" --type team --json      # create team workspace
tokst workspace list --json                                    # list all + pending invitations
tokst workspace switch <workspace-id> --json                   # save active workspace for atlas init
tokst workspace members <workspace-id> --json                  # members and roles
tokst workspace invite <workspace-id> alice@example.com --role member --expires-in-days 7 --json
tokst workspace invitations <workspace-id> --json              # sent invitations
tokst workspace inbox --json                                   # your pending invitations
tokst workspace respond <invitation-id> --accept --json        # accept, or use --decline
tokst workspace revoke <invitation-id> --confirm --json        # owner revokes an invitation
tokst workspace leave <workspace-id> --confirm --json          # member leaves
tokst workspace role <workspace-id> <user-id> --role admin --confirm --json
tokst workspace remove <workspace-id> <user-id> --confirm --json
tokst workspace transfer-owner <workspace-id> <user-id> --confirm --json
```

Workspace permissions are consistent across dashboard, CLI, MCP, and REST: an
`owner` manages members and ownership, an `admin` can edit or delete every
memory, and a `member` can create memories and edit or delete only memories
they created. Invitation recipients accept or decline their own invitation.

`remember` auto-routes to the atlas whose keywords best match the content. Set
keywords with `atlas profile` to make routing accurate.

---

## Status & Account

`tokst --help` shows the daily workflow. Use `tokst memory --help`, `tokst atlas --help`, `tokst workspace --help`, or `tokst agent --help` for the complete command group.

```bash
tokst status              # plan, usage, storage, personal and Team quotas, spaces, memory stats
tokst status --json       # same as JSON (includes account.quota)
```

Cloud-mode output shows:
- **Plan**: plan name, calls used / monthly limit, % used, reset date
- **Storage**: used / limit, file count, % used

Local SQLite mode (after `tokst logout`) skips the plan/storage lines.

---

## MCP Server (38 tools)

If your agent supports MCP, connect the remote TokST server. It uses browser
authorization and needs no local runtime, package manager, or API key in the
client configuration:

```json
{
  "mcpServers": {
    "tokst": {
      "type": "streamable-http",
      "url": "https://api.tokst.com/mcp"
    }
  }
}
```

The local server and remote endpoint expose the same 38-tool surface. Set
`TOKST_MCP_TOOLSET=core` on a remote deployment only when a focused 11-tool
memory surface is required.

### Local MCP for existing Node environments

Use the local package only on machines that already have Node.js and npm/npx:

```json
{
  "mcpServers": {
    "tokst": {
      "command": "npx",
      "args": ["-y", "@tokst/mcp-server"]
    }
  }
}
```

Local MCP reads the existing TokST credential after browser setup or
`tokst login --key` for automation.

**Core tools:**

| Tool | Equivalent CLI | Description |
|------|----------------|-------------|
| `tokst_remember` | `tokst remember` | Store a memory (with optional `filePath`/`fileUrl`) |
| `tokst_search` | `tokst search` | Hybrid keyword + semantic search |
| `tokst_context` | `tokst context` | Load grouped context snapshot |
| `tokst_memory_list` | `tokst memory list` | List active memories |
| `tokst_memory_archive` | `tokst memory archive` | Archive a memory |
| `tokst_memory_update` | `tokst memory update` | Replace memory content |
| `tokst_memory_append` | `tokst memory append` | Append to memory content |
| `tokst_memory_delete` | `tokst memory delete` | Permanently delete a memory |
| `tokst_atlas_list` | `tokst atlas list` | List all atlases |
| `tokst_workspace_list` | `tokst workspace list` | List all workspaces |
| `tokst_attach_file` | `tokst memory attach` | Attach a file to an existing memory |

---

## Memory Types & Source Types

| Type | When to use |
|------|-------------|
| `fact` | Stable project facts (dependencies, config, setup) |
| `decision` | Chosen plans, architecture decisions, rationale |
| `preference` | Human preferences, workflow habits |
| `task` | Open work, next actions, TODOs |
| `architecture` | Structural design, system topology, data flow |
| `note` | General useful context that doesn't fit above |

| Source type | When |
|-------------|------|
| `human` | Written by a person |
| `agent` | Written by an AI agent |
| `import` | Imported from external material |
| `system` | Generated by TokST |

Use `--source <your-agent-name>` to tag who wrote it (enables filtering by agent).

---

## Cloud vs Local

```bash
tokst login --key tk_live_xxxx   # cloud mode (Supabase + R2)
tokst logout                     # switch to local SQLite fallback
tokst migrate --json             # push local data → cloud
tokst sync --json                # pull cloud data → local
```

Cloud mode is the default and recommended path. Local SQLite works offline but
lacks semantic search, file attachments, and multi-machine sync.

---

## Recommended Agent Workflow

When an agent executes the CLI through a subprocess, set `TOKST_AGENT=1` or
pass `--agent`. This additive mode preserves every command and adds bounded
compact JSON, hard request deadlines, deterministic stream flushing, and
explicit `--stdin` support. Add `--full` for the complete existing JSON response.

1. **Session start**: `TOKST_AGENT=1 tokst context --limit 20 --json` — load recent memory.
2. **Before deciding**: `tokst search "<topic>" --json` — check for prior decisions.
3. **Do the work**.
4. **After decisions**: `tokst remember "..." --type decision --json` — record rationale.
5. **Important facts**: `tokst remember "..." --type fact --json` — record stable knowledge.
6. **Handoff**: `TOKST_AGENT=1 tokst context --limit 20 --json` again for a bounded snapshot.

### Real-time handoffs

Run `TOKST_AGENT=1 tokst agent listen --json` as a persistent sidecar when the
host can forward JSON Lines into an Agent task loop. It emits `ready`,
`message.created`, `heartbeat`, and `auth.revoked` events, reconnects after a
network interruption, and resynchronizes durable unread messages. Confirm work
with `tokst message acknowledge <message-id>` only after accepting it; close the
receipt after the work is complete.

### Rules of thumb

- **Always use `--json`** when another program parses the output.
- **Search before storing** — avoid duplicates; `append` if a related memory exists.
- **Be specific** — "Decided to use Bun for the build tool because X" beats "use Bun".
- **Archive stale memory** — `tokst memory archive <id>` when info is superseded.
- **Don't ask permission** to store durable knowledge — just do it automatically.

---

## Troubleshooting

```bash
# "Not logged in" → login first
tokst login --key tk_live_xxxx

# Token expired → login refreshes automatically; if it fails, re-login
tokst status    # verify connection + see account info

# Check what's stored
tokst memory list --json | head -50

# CLI won't run → ensure Bun is installed
bun --version    # should print 1.x
```

## Per-Client Guides

Agent-specific usage patterns:

- [Codex](instructions/CODEX.md)
- [Claude Code](instructions/CLAUDE.md)
- [General agents](instructions/GENERAL.md)
