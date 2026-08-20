# TokST Memory Skill

TokST gives AI agents persistent memory across sessions, devices, and teams.
The Skill teaches an agent when to load context, search prior knowledge, and
record durable facts, decisions, preferences, and project updates.

## Supports

- Cloud workspaces and Atlases shared by people and trusted agents
- Local SQLite memory, attachments, search indexes, and backups
- TokST CLI, local MCP, remote MCP, and REST API workflows
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

## Use This Skill

Place this directory in the client's Skills location. The entry point is
`SKILL.md`. Start every relevant session with `tokst context`, search before
making decisions, and use `tokst remember` for information that should persist.

Full documentation: <https://tokst.com/docs>
