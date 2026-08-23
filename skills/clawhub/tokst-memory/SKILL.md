---
name: tokst-memory
description: Use TokST to retrieve, store, govern, and hand off durable context across cloud workspaces or Local SQLite.
slug: tokst-memory
displayName: TokST Memory
version: 0.8.0
summary: Durable memory and session workflows for AI agents, with cloud workspaces, Local SQLite, CLI, MCP, REST API, and trusted Agent collaboration.
license: MIT
---

# TokST Memory

TokST gives this agent durable memory across conversations. Use Cloud for shared
workspaces and cross-device collaboration. Use Local for private SQLite memory,
attachments, FTS5 search, and backups on the current device.

## Install and verify

Use the standalone installer. It supports macOS, Linux, and Windows and does
not require Bun, Node.js, npm, or a package manager.

```bash
# macOS / Linux
curl -fsSL https://tokst.com/install.sh | bash

# connect this machine to TokST Cloud
tokst setup

# optional: write Agent instructions for this repository
tokst init --agents codex

# verify the active version, account, spaces, quotas, and integration
tokst version --verbose
tokst status
tokst doctor
```

Windows PowerShell:

```powershell
irm https://tokst.com/install.ps1 | iex
tokst setup
```

`tokst atlas bind` is optional. Bind a directory only when it permanently maps
to one Atlas. Cloud reads search all accessible memories by default.

Use a dedicated API key for CI, servers, or clients without browser approval:

```bash
tokst login --key tk_live_your_api_key
```

## Select a storage profile

### Cloud

Cloud memory is shared according to workspace roles. The server records the
authenticated human or trusted `agt_...` Agent identity; clients do not supply
an authoritative Agent ID.

```bash
tokst context --json
tokst search "previous deployment decision" --json
```

### Local

Local data stays in the current device's SQLite profile. It begins with one
default workspace and Atlas; additional local spaces can be created later.

```bash
tokst setup --local
tokst local remember "Private research note" --type note --tags private --json
tokst local search "research" --json
tokst local backup create --name before-change
```

Local-to-Cloud sync is explicit. It binds one Local Atlas to one Cloud Atlas,
synchronizes content and metadata, retains attachments locally, and preserves
conflicting edits as separate memories.

```bash
tokst local connect --cloud-atlas-id <cloud-atlas-id>
tokst local sync
```

## Daily memory loop

1. Load context at the beginning of meaningful work.
2. Search before repeating a decision or recommending a direction.
3. Store confirmed long-term facts, decisions, preferences, tasks, and architecture.
4. Archive superseded information instead of silently overwriting history.

```bash
TOKST_AGENT=1 tokst context --limit 20 --json
TOKST_AGENT=1 tokst search "authentication design" --json
TOKST_AGENT=1 tokst remember "Use PKCE for OAuth authorization." \
  --type decision --tags auth,oauth --source-type agent --source codex --json
```

Use `--json` whenever another program parses output. `TOKST_AGENT=1` or
`--agent` produces bounded, compact output for Agent subprocesses. Use `--full`
only when the complete response is required.

### Memory types

| Type | Use |
|---|---|
| `fact` | Stable project or user facts |
| `decision` | Approved choices and rationale |
| `preference` | Durable human preferences |
| `task` | Open, actionable work |
| `architecture` | System design and data flow |
| `note` | Useful durable context outside the above |

Store Markdown when structure helps. Do not store secrets, access tokens,
private credentials, raw chain-of-thought, or transient tool output.

Use the same compact structure across dashboard, CLI, MCP, and REST: facts use
Conclusion / Source / Scope; decisions use Decision / Context / Rationale /
Impact; tasks use Goal / checklist / Done when; architecture uses Goal /
Components / Data flow / Constraints. Long CLI content can be supplied with
`tokst remember --type decision --stdin < decision.md`.

## Session memory for substantial work

Start a Session for multi-step work, context limits, or handoffs. Capture only
confirmed durable information. A checkpoint records progress. Finalize creates
a snapshot and compiles candidates into formal memories by default.

```bash
TOKST_AGENT=1 tokst session start --atlas-id <atlas-id> --task "Implement OAuth callback" --json
TOKST_AGENT=1 tokst session capture --session <ses-id> \
  "Use PKCE and validate the redirect URI." --kind decision --tags auth,oauth --json
TOKST_AGENT=1 tokst session checkpoint --session <ses-id> "Callback validation is complete." --json
TOKST_AGENT=1 tokst session finalize --session <ses-id> "OAuth callback implemented and verified." --json
```

Use `--no-compile` when a human review must precede promotion. Members can review
their own candidates with `tokst session candidates --scope mine --status pending`.
Workspace Owners and Admins can review managed Sessions and compile, dismiss, or revert candidates.
Reverting archives the linked formal memory and retains the audit trail.

```bash
tokst session list --scope managed --json
tokst session candidates --scope managed --status pending --json
tokst session candidate --session <ses-id> --candidate <candidate-id> --action revert --json
```

Local uses the same lifecycle with `tokst local session ...`.

### Observed Session Relay

Relay is an opt-in local companion for supported client adapters. It accepts normalized Session events, removes credentials and high-risk content before processing, retains raw event fragments on the current device for 24 hours, and creates reviewable candidates. Relay candidates complement explicit Session capture; confirmed decisions still require Agent capture.

```bash
tokst session monitor enable --mode observed \
  --endpoint https://api.openai.com/v1 --model <model-name> --provider-key <provider-key>
tokst relay doctor
tokst session monitor service status
```

Observed mode starts a user-level Relay service automatically. Codex uses native Hooks and Pi uses a global Pi Extension. Use `tokst session monitor pause` during sensitive work. Use `tokst relay logs` to inspect local redaction and queue results. Cloud MCP and REST can manage Sessions and accept events, while observed capture requires a local Relay or a client adapter.

## MCP

TokST Cloud MCP exposes 53 tools for memories, files, workspaces, Agent
collaboration, Sessions, Session Relay, and governance.

### Browser-authorized Streamable HTTP

Use this in MCP clients that can open a browser for OAuth approval.

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

### Static API-key Streamable HTTP

Use this for WorkBuddy, ZCode, Qoder, Kimi, CI, and other clients that need a
non-interactive connection. Create one dedicated key per client in the dashboard.

```json
{
  "mcpServers": {
    "tokst": {
      "type": "streamable-http",
      "url": "https://api.tokst.com/mcp",
      "headers": {
        "Authorization": "Bearer tk_live_your_api_key"
      }
    }
  }
}
```

Keep API keys in the client's protected settings. Keep them out of source code,
chat transcripts, URLs, and version control. Revoke an unused key in Dashboard
API Keys.

### Local stdio MCP

Use the installed standalone CLI for private Local SQLite tools:

```json
{
  "mcpServers": {
    "tokst-local": {
      "command": "tokst",
      "args": ["local", "mcp"]
    }
  }
}
```

Run `tokst setup --local` before starting Local MCP. The local server uses the
same memory and Session tool names against the local SQLite profile.

## Workspace and Agent collaboration

Use the workspace role model consistently:

| Role | Capability |
|---|---|
| `owner` | Members, ownership, billing, audit, and all content |
| `admin` | All workspace content and operational management |
| `member` | Create content; edit and delete content they created |

Use workspace governance only for a Team workspace. Invitations require the
recipient to accept before membership becomes active.

```bash
tokst workspace members <workspace-id> --json
tokst workspace invite <workspace-id> member@example.com --role member --expires-in-days 7 --json
tokst workspace invitations <workspace-id> --json
tokst workspace inbox --json
tokst workspace respond <invitation-id> --accept --json
tokst workspace revoke <invitation-id> --confirm --json
tokst workspace leave <workspace-id> --confirm --json
tokst workspace role <workspace-id> <user-id> --role admin --confirm --json
tokst workspace remove <workspace-id> <user-id> --confirm --json
tokst workspace transfer-owner <workspace-id> <user-id> --confirm --json
```

Trusted Agents have stable `agt_...` identities generated from their API-key or
OAuth channel. `source` remains a readable source label.

```bash
tokst agent list --json
TOKST_AGENT=1 tokst message inbox --json
TOKST_AGENT=1 tokst agent listen --json
```

Run `agent listen` alongside a long-running Agent for realtime handoffs. It
reconnects and re-synchronizes unread durable messages after interruption.
Acknowledge a message once work is accepted; close it after completion.

## Troubleshooting

| Symptom | Recovery | Verify |
|---|---|---|
| `tokst: command not found` | Open a new terminal after install. | `tokst version --verbose` |
| Old command still runs after update | Run `tokst update`; inspect source and duplicate paths. | `tokst doctor`; zsh/bash: `tokst doctor --fix-path` |
| Browser approval cannot complete | Keep the initiating terminal open and restart `tokst setup`; use a dedicated API key for unattended use. | `tokst connection test` |
| MCP has no tools | Restart the MCP client after OAuth approval or static configuration. | Connect to `https://api.tokst.com/mcp` |
| Static MCP returns unauthorized | Confirm the `Authorization: Bearer tk_live_...` header and key status. | `tokst login --key tk_live_your_api_key` |
| Cloud write or creation is rejected | Review the target workspace, role, plan, and remaining quota. | `tokst status` |
| Local write fails | Update, back up before repair, and collect profile status. | `tokst update && tokst local backup create --name before-repair && tokst local status --json` |
| Listener reconnects | Read the durable inbox after recovery. | `tokst message inbox --json` |

Cloud operations require a connection to `api.tokst.com`. Local mode remains
available on the current device and can be synchronized later by explicit Atlas
binding.

## References

- Documentation: https://tokst.com/docs
- Help Center: https://tokst.com/help
- MCP setup: https://tokst.com/docs/mcp
- Sessions: https://tokst.com/docs/sessions
- Local: https://tokst.com/docs/local
