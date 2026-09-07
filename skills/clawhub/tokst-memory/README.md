# TokST Memory Skill

Start here. This README gives the shortest reliable path to a working TokST
installation. Read `SKILL.md` after the checks below for Sessions, connected
Agent workflows, durable memory, explicit tasks, and team collaboration.

## Supports

- Cloud workspaces and Atlases shared by people and trusted agents
- Cloud Session capture, durable memory, and user-directed Agent Tasks
- TokST CLI and connected Agent workflows
- Local SQLite, local MCP, REST API, and remote MCP compatibility surfaces
- Claude Code, Codex, Cursor, Pi, WorkBuddy, ZCode, Qoder, and Kimi Code

## Install TokST

macOS and Linux:

```bash
curl -fsSL https://tokst.com/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://tokst.com/install.ps1 | iex
```

## Authorize and verify

```bash
tokst setup
tokst doctor --json
tokst connection test --json
```

Cloud is ready when the doctor and connection test pass. Local-only use starts
with `tokst setup --local`; Local remains in maintenance compatibility mode.

## First memory

```bash
tokst context --json
tokst remember "Use PKCE for OAuth authorization." --type decision --tags auth,oauth --json
tokst search "OAuth authorization" --json
```

## Use This Skill

Place this directory in the client's Skills location. The entry point is
`SKILL.md`. Start every relevant session with `tokst context`, search before
making decisions, and use `tokst remember` for information that should persist.

Full documentation: <https://tokst.com/docs>

Help and common fixes: <https://tokst.com/help>
