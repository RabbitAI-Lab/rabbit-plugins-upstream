# TokST Memory Skill

Start here. This README gives the shortest reliable path to TokST Cloud MCP.
Read `SKILL.md` for durable memory, shared context, knowledge governance, and
connected Runtime boundaries.

## Supports

- Cloud workspaces and Atlases shared by people and trusted agents
- Cloud MCP for durable memory, shared context, knowledge bases, files, and account status
- Connected Agent Runtime for device workflows, automatic sessions, and directed tasks
- Claude Code, Codex, Cursor, Pi, WorkBuddy, ZCode, Qoder, and Kimi Code

## Connect Cloud MCP

Configure the Agent with `https://api.tokst.com/mcp`. OAuth-capable clients
open a browser for approval. Static clients use a dedicated Dashboard API key
as a Bearer credential.

The MCP connection is ready when the Agent can call `tokst_context` or
`tokst_search`. Use the Cloud MCP endpoint directly for all memory operations.
Use `tokst_memory_archive` and `tokst_memory_restore` for the memory lifecycle.
Permanent cleanup stays in the Dashboard archive view and requires the user's
manual confirmation.

## Optional device CLI

Install the CLI only for local Agent endpoint connections, directed task
execution, diagnostics, or a desktop stdio MCP proxy:

```bash
curl -fsSL https://tokst.com/install.sh | bash
tokst setup
tokst connect
```

Configure a desktop stdio client with `tokst mcp`; it proxies the same Cloud
MCP toolset using the saved device credential.

## First memory

Configure your Agent for `https://api.tokst.com/mcp`, then use
`tokst_context`, `tokst_search`, and `tokst_remember` through MCP.

## Use This Skill

Place this directory in the client's Skills location. The entry point is
`SKILL.md`. Load relevant context with `tokst_context`, search before making
decisions, and use `tokst_remember` for information that should persist.

Full documentation: <https://tokst.com/docs>

Help and common fixes: <https://tokst.com/help>
