---
name: tokst-memory
description: Use TokST to retrieve, store, govern, and hand off durable context across cloud workspaces or Local SQLite.
version: 0.8.2
license: MIT
---

<!-- skill-version: 0.8.2 -->

# TokST Memory Skill

Use TokST for durable memory across conversations. Cloud supports shared
workspaces, trusted Agents, and collaboration. Local keeps memory, attachments,
FTS5 search, and backups in a SQLite profile on the current device.

## Install once

macOS and Linux:

```bash
curl -fsSL https://tokst.com/install.sh | bash
tokst setup
tokst version --verbose
tokst status
tokst doctor
```

Windows PowerShell:

```powershell
irm https://tokst.com/install.ps1 | iex
tokst setup
```

The standalone installer supports macOS, Linux, and Windows. It requires curl
or PowerShell and does not require Bun, Node.js, npm, or a package manager.

`tokst atlas bind` is optional. Bind a directory when it permanently belongs to
one Atlas; searches and context otherwise cover all accessible memory.

## Install this Skill

Place this document as `SKILL.md` in the client Skill directory. The same
workflow works with MCP-only clients even when they have no Skill directory.

| Client | Skill directory |
|---|---|
| Claude Code | `~/.claude/skills/tokst-memory/` |
| Codex | `~/.codex/skills/tokst-memory/` |
| Cursor / Windsurf | `~/.cursor/skills/tokst-memory/` |
| Pi | `~/.pi/skills/tokst-memory/` |
| WorkBuddy | `~/.workbuddy/skills/tokst-memory/` |
| ZCode | `~/.zcode/skills/tokst-memory/` |
| Qoder | `~/.qoder/skills/tokst-memory/` |
| Kimi Code | `~/.kimi-code/skills/tokst-memory/` |
| Generic | `~/.agents/skills/tokst-memory/` |

For a repository-specific integration, generate the matching Agent guidance:

```bash
tokst init --agents codex,claude,cursor,opencode,pi
```

## Cloud and Local profiles

### Cloud

Cloud operations use your TokST account and workspace permissions.

```bash
tokst context --json
tokst search "previous deployment decision" --json
```

Run `tokst setup` for browser authorization. CI and unattended environments can
use a dedicated API key:

```bash
tokst login --key tk_live_your_api_key
```

### Local

Local data stays on this device. Start with a default local workspace and Atlas.

```bash
tokst setup --local
tokst local remember "Private research note" --type note --tags private --json
tokst local search "research" --json
tokst local backup create --name before-change
```

Cloud sync is explicit. Bind one Local Atlas to one Cloud Atlas; content and
metadata synchronize, attachments remain local, and concurrent changes remain
separate memories.

```bash
tokst local connect --cloud-atlas-id <cloud-atlas-id>
tokst local sync
```

## Agent operating rules

1. Read context before substantial work.
2. Search before repeating decisions or recommendations.
3. Capture only confirmed long-term knowledge.
4. Keep secrets, credentials, raw reasoning, and temporary tool output outside TokST.
5. Archive superseded memories so history remains traceable.

```bash
TOKST_AGENT=1 tokst context --limit 20 --json
TOKST_AGENT=1 tokst search "authentication design" --json
TOKST_AGENT=1 tokst remember "Use PKCE for OAuth authorization." \
  --type decision --tags auth,oauth --source-type agent --source codex --json
```

Use `--json` for machine-readable output. `TOKST_AGENT=1` or `--agent` gives
Agent subprocesses compact, bounded output.

| Memory type | Use |
|---|---|
| `fact` | Stable facts |
| `decision` | Approved choices and rationale |
| `preference` | Durable preferences |
| `task` | Open work |
| `architecture` | System design |
| `note` | Other durable context |

Use the same compact structure across dashboard, CLI, MCP, and REST: facts use
Conclusion / Source / Scope; decisions use Decision / Context / Rationale /
Impact; tasks use Goal / checklist / Done when; architecture uses Goal /
Components / Data flow / Constraints. Long CLI content can be supplied with
`tokst remember --type decision --stdin < decision.md`.

## Session memory

Use a Session for multi-step work or a handoff. A Session starts with scoped
context, records confirmed candidates, saves checkpoints, and finalizes a
snapshot. Finalize compiles candidates into formal memories unless `--no-compile`
is supplied.

```bash
TOKST_AGENT=1 tokst session start --atlas-id <atlas-id> --task "Implement OAuth callback" --json
TOKST_AGENT=1 tokst session capture --session <ses-id> \
  "Use PKCE and validate the redirect URI." --kind decision --tags auth,oauth --json
TOKST_AGENT=1 tokst session checkpoint --session <ses-id> "Callback validation is complete." --json
TOKST_AGENT=1 tokst session finalize --session <ses-id> "OAuth callback implemented and verified." --json
```

Members can review their own pending candidates with `tokst session candidates --scope mine --status pending`.
Owners and Admins can review managed Sessions:

```bash
tokst session list --scope managed --json
tokst session candidates --scope managed --status pending --json
tokst session candidate --session <ses-id> --candidate <candidate-id> --action compile --json
```

Local uses the same commands through `tokst local session ...`.

### Observed Session Relay

Relay is an opt-in local companion for supported client adapters. It accepts normalized Session events, removes credentials and high-risk content before processing, retains raw event fragments on the current device for 24 hours, and aggregates events at checkpoints, after five minutes of idle durable activity, or at session end. A durable completed Session writes a formal snapshot; extracted candidates remain reviewable in Dashboard → Sessions. Relay candidates complement explicit Session capture; confirmed decisions still require Agent capture.

```bash
# Pi default: routes to the first personal workspace and Atlas, then enables
# automatic candidate compilation. Keep review-first governance with --review-candidates.
tokst pi
tokst pi --review-candidates

tokst session monitor enable --mode observed \
  --endpoint https://api.openai.com/v1 --model <model-name> --provider-key <provider-key>
tokst relay doctor
tokst relay run
```

Use `tokst session monitor pause` during sensitive work. Use `tokst relay logs` to inspect local redaction and queue results. Cloud MCP and REST can manage Sessions and accept events, while observed capture requires a local Relay or a client adapter.

Native bridge Sessions include their client source and native session ID. Keep Relay diagnostics separate: `tokst relay ingest ... --test` records a diagnostic Session only. Automatic extraction creates one comprehensive candidate per window at confidence `0.6` or higher and ignores test procedures, Relay telemetry, versions, quotas, and model configuration. With automatic compilation, five minutes of durable idle activity closes the observed Session and writes one consolidated formal Markdown memory. When a Cloud Session was archived while its native client remains active, Relay creates one replacement Session and retries the event stream.

## MCP setup

TokST Cloud MCP exposes 53 tools across memory, files, workspaces, Sessions,
Session Relay, trusted Agent identity, and messages.

### Browser-authorized MCP

Use with clients that support an OAuth browser flow.

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

### Static API-key MCP

Use with WorkBuddy, ZCode, Qoder, Kimi, CI, and any static Streamable HTTP MCP
client. Create one dedicated key per client in Dashboard API Keys.

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

Store API keys only in a protected client setting or environment variable.
Never put one in source control, a URL, or a chat transcript. Revoke unused
keys from Dashboard API Keys.

### Local stdio MCP

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

Run `tokst setup --local` before starting Local MCP.

## Trusted Agents and handoffs

TokST assigns trusted calls a stable `agt_...` identity. The `source` field is a
readable source label. Use realtime listening for long-running Agent work and
durable inbox sync after restarts.

Team workspace governance remains explicit. Recipients accept an invitation
before membership becomes active.

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

```bash
tokst agent list --json
TOKST_AGENT=1 tokst agent listen --json
TOKST_AGENT=1 tokst message inbox --json
```

## Troubleshooting

| Problem | Recovery | Verify |
|---|---|---|
| `tokst: command not found` | Open a new terminal after installation. | `tokst version --verbose` |
| Older command remains after updating | Run `tokst update`, then inspect source and PATH. | `tokst doctor`; zsh/bash: `tokst doctor --fix-path` |
| Browser authorization fails | Keep the initiating terminal open and rerun `tokst setup`; unattended clients use a dedicated key. | `tokst connection test` |
| MCP tools do not appear | Restart the MCP client after authorization or configuration. | `https://api.tokst.com/mcp` |
| Static MCP is unauthorized | Check the `Authorization: Bearer tk_live_...` header and key status. | `tokst login --key tk_live_your_api_key` |
| Cloud write is rejected | Check workspace, role, plan, and quotas. | `tokst status` |
| Local write fails | Update, make a backup, then collect profile status. | `tokst update && tokst local backup create --name before-repair && tokst local status --json` |
| Agent listener reconnects | Read the durable inbox after recovery. | `tokst message inbox --json` |

Cloud operations require access to `api.tokst.com`. Local mode remains usable on
the current device and can synchronize later through an explicit Atlas binding.

## References

- https://tokst.com/docs
- https://tokst.com/help
- https://tokst.com/docs/mcp
- https://tokst.com/docs/sessions
- https://tokst.com/docs/local
