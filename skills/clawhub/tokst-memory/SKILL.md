---
name: tokst-memory
description: Use TokST for durable memory, automatic Session capture, and user-directed Agent Tasks in cloud workspaces.
description_zh: 使用 TokST 管理长期记忆、自动会话整理和用户明确分派的智能体任务。
description_en: Give AI Agents durable memory, automatic Session capture, and user-directed task execution with auditable context.
display_name: TokST
display_name_en: TokST
category: tools
slug: tokst-memory
displayName: TokST
version: 0.8.5
author: TokST
summary: Durable memory, automatic Sessions, and user-directed Agent Tasks in cloud workspaces.
license: MIT
---

# TokST Memory

TokST gives this agent durable memory across conversations. Use Cloud for
shared workspaces, cross-device collaboration, automatic Session capture, and
user-directed tasks. The open-source Local runtime remains a maintenance-mode
compatibility option for private SQLite workflows.

## Start here

Read `README.md` before this full guide when TokST is being installed for the
first time. The README covers install, authorization, verification, and the
first memory operation. This file defines the complete operating rules for
Sessions, connected Agent workflows, durable memory, explicit tasks, and team
collaboration.

## Public references

Use these stable public resources when a client needs installation guidance,
API schemas, MCP discovery, or the complete machine-readable documentation:

- [TokST documentation](https://tokst.com/docs)
- [TokST Agent guide](https://tokst.com/llms.txt)
- [TokST full Agent context](https://tokst.com/llms-full.txt)
- [TokST OpenAPI contract](https://api.tokst.com/openapi.json)
- [TokST MCP manifest](https://api.tokst.com/.well-known/mcp)

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
3. Store confirmed long-term facts, decisions, preferences, rules, and architecture.
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
| `task` | Legacy compatibility type for historical open work; use a formal Task for new assigned work |
| `architecture` | System design and data flow |
| `note` | Useful durable context outside the above |

Store Markdown when structure helps. Do not store secrets, access tokens,
private credentials, raw chain-of-thought, or transient tool output.

Use the same compact structure across dashboard, CLI, MCP, and REST: facts use
Conclusion / Source / Scope; decisions use Decision / Context / Rationale /
Impact; architecture uses Goal / Components / Data flow / Constraints. A formal
Task retains its own goal, assignees, execution results, and history. Long CLI content can be supplied with
`tokst remember --type decision --stdin < decision.md`.

## Reliability and recovery rules

At the first Cloud operation in a new environment, verify the installation and
saved authorization before attempting memory writes.

```bash
tokst doctor --json
tokst connection test --json
tokst status --json
```

When a command fails, preserve the output and use the matching recovery path.
Retry only an operation that is safe to repeat.

| Failure | Agent action |
|---|---|
| `TIMEOUT`, a temporary network error, or a `5xx` response | Retry a read once. For a write with an unknown result, search or inspect the Session first to avoid a duplicate. |
| `429` or a quota response | Read `Retry-After` when supplied; wait for that duration, then retry once. Use `tokst status --json` to inspect remaining quota. |
| `UNAUTHORIZED` or expired browser approval | Run `tokst setup` in an interactive terminal, or replace the dedicated API key in the client configuration. |
| Permission or plan rejection | Confirm the workspace, Atlas, role, and limits with `tokst status --json`. Escalate the required access change to a workspace Owner or Admin. |
| Local profile or storage failure | Update the CLI, create a backup, then inspect Local status before another write. |

Use `--json` for tool-driven calls. A JSON failure includes a machine-readable
code and a `retryable` signal for timeout cases. Session starts accept
`--idempotency-key`; Session captures accept `--source-event-id` for stable
event de-duplication. For other interrupted writes, confirm the prior result
before repeating the mutation.

## Explicit Session capture for confirmed work

Connected Agents automatically create Session compilations for normal work.
Use explicit Session commands when a person or Agent needs to record a
confirmed decision, checkpoint, or final result. A Session compilation keeps
the working result and evidence; the compiler derives zero or more durable
memories when the content remains useful across future work.

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

Local keeps compatible `tokst local session ...` commands for existing private
SQLite workflows.

### Formal Tasks

Tasks are user-created work orders. A user creates a Task from the dashboard,
a Session compilation, or a long-term Memory, then assigns one or more
connected Agents. The Task retains delivery, execution steps, results, and
history on its own canvas. A normal Session never creates a formal Task by
itself. Read the [Tasks guide](https://tokst.com/docs/tasks) before assigning
work or accepting a delivery.

### Automatic Memory

TokST Automatic Memory is an opt-in local service. `tokst auto on --agent all` detects WorkBuddy, OpenCode, Pi, Codex, and Claude Code, installs their native bridges, and starts the local service. OpenCode uses a global plugin in the terminal and macOS App; Pi uses a global extension; Codex and Claude Code use TokST-managed Hooks that retain user Hooks. ACP Hosts use `tokst acp proxy`, `tokst acp opencode`, or `tokst acp pi --doctor`. A valid user request and final result create a Session compilation with evidence and diagnostics. The compiler may derive zero or more long-term memories. A formal Task exists after a user creates and assigns it. Explicit Session capture remains available for important decisions.

```bash
tokst auto on --agent all
tokst acp proxy -- <acp-agent-command> [args]
tokst auto status
tokst auto verify --agent all --json
tokst auto privacy --retain-raw 0
```

### OpenCode Terminal, App, and ACP

OpenCode Terminal and the macOS App load the generated global plugin from `~/.config/opencode/plugins/tokst-automatic-memory.ts`. A native OpenCode session, including one resumed with `opencode -s`, maps to the same TokST Session audit trail. Each completed work unit updates its matching Session compilation and may extract durable memories. An ACP Host can configure `command: "tokst"` and `args: ["acp", "opencode"]`.

```bash
tokst auto on --agent opencode
tokst acp opencode --doctor
```

Use `tokst auto repair --agent opencode` to regenerate the global plugin with the current absolute TokST executable path. `tokst acp opencode --repair` repairs ACP Host configuration.

Restart the client after bridge installation. `tokst auto status --agent <name>`, `tokst auto verify --agent <name>`, `tokst auto repair --agent <name>`, and `tokst auto logs --agent <name>` use the same status and diagnostic format for every bridge. Claude Desktop remains MCP-assisted and uses explicit Session tools. ACP clients launch through `tokst acp proxy -- <acp-agent-command> [args]`. Automatic Memory installs a user-level service after enablement. The queue contains sanitized event material and retries safe delivery when the network returns. Raw content is discarded by default; `tokst auto privacy --retain-raw 24h` enables a short local recovery window. MCP and REST retain the explicit Session workflow for clients outside automatic capture.

## MCP

TokST Cloud MCP exposes 57 tools for memories, files, workspaces, Agent
collaboration, Sessions, automatic memory, and governance.

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

Local stdio MCP remains available for existing private SQLite workflows. It
receives compatibility and security maintenance; choose Cloud for new shared
Agent workflows:

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

## Common questions

**Where should I start?** Read `README.md`, run `tokst setup`, then verify with
`tokst doctor` before giving an Agent memory instructions.

**Does TokST store every conversation automatically?** Automatic memory is
opt-in. A valid ACP or native session boundary produces a Session compilation
after local redaction. The compiler may derive zero or more durable memories.
Explicit Session capture records critical confirmed decisions. A formal Task
exists only after a user creates and assigns it.

**Which content belongs in memory?** Store confirmed facts, decisions,
preferences, rules, and architecture changes that remain useful across future
work. Keep task execution details in a formal Task and preserve credentials,
private keys, raw reasoning, and temporary tool output outside TokST.

**How do I repair a failed command?** Use the recovery table above, then consult
the Help Center for a guided resolution.

## References

- Documentation: https://tokst.com/docs
- Help Center: https://tokst.com/help
- MCP setup: https://tokst.com/docs/mcp
- Sessions: https://tokst.com/docs/sessions
- Local: https://tokst.com/docs/local
