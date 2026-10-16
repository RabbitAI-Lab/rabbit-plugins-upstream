---
name: vestige
description: Vestige 4.2.0, an agent-agnostic guard for your AI agent. It judges the whole chain of steps, stops it before it does damage, keeps a hash-chained receipt of every decision, and saves that chain to memory so an old yes is never permission to act now. Local Rust MCP server, exact-handle recall, causal_walk from a failure back to its cause.
---

# Vestige Skill

Vestige is an agent-agnostic guard for your AI agent. It judges the whole chain of steps, not just one command, and stops it before it does damage, keeping a receipt of every decision. It works with Claude Code, OpenClaw, any agent, and it saves that chain to memory so an old yes is never treated as permission to act now.

This skill wraps the official [`vestige-mcp`](https://github.com/samvallad33/vestige) server, version 4.2.0. Memory lives on Strata, an append-only hash-chained log: every write returns a receipt, and nothing is found by similarity. A memory is found by its exact id or an exact tag.

This skill is **not** OpenClaw default memory and **not** a `plugins.slots.memory` plugin. OpenClaw's `memory-core` stays as it is; Vestige runs beside it as an MCP server.

## Install

```bash
npm install -g vestige-mcp-server@4.2.0
which vestige-mcp          # macOS / Linux
where vestige-mcp          # Windows
```

Put the **absolute** path in OpenClaw's MCP config (GUIs do not inherit your shell PATH or expand `~`):

```json
{
  "mcp": {
    "servers": {
      "vestige": {
        "command": "<absolute path from which vestige-mcp>",
        "args": []
      }
    }
  }
}
```

For a per-project store add `"args": ["--data-dir", "<absolute dir>"]`.

## Tools to use

| Tool | Use |
|------|-----|
| `session_start` | Open intentions, status and code memories at the start of a session |
| `smart_ingest` | Save a memory (`content`, `node_type`, `tags`); returns a receipt |
| `recall` | Find by exact `handle`: a full memory id or an exact, case-sensitive tag. Free text returns `similarity_disabled` |
| `causal_walk` | Walk back from a failure along recorded causal edges: `start_points=[{kind:"logged_write", node_id:"<failure memory id>"}]`. Results are hypotheses, not proven causes |
| `forgotten_lesson` | From a failure memory, find earlier lessons on recorded edges that are fading |
| `receipt` | `get` shows what a write did; `replay` re-derives it from the log |
| `codebase` | `ingest_repo` records a checkout's commits, reverts, cherry-picks and `Fixes:` trailers as change records; `remember_decision` / `remember_pattern` anchor decisions to files |
| `selftest` | Planted-cause selftest on a throwaway log |

Tag every memory on purpose: tags are the index.

## When to use

- A decision, correction or verified fact worth keeping: `smart_ingest` with a narrow topic tag
- "What did we decide about X?": `recall` with that tag
- "Why did this break?": save the failure as an `event`, then `causal_walk` and `forgotten_lesson` from its id
- "Prove that write": `receipt` with the memory id

Never save API keys, passwords or other secrets.

## Helper

`vmem` ships with this listing and resolves `vestige-mcp` with `command -v`. It needs `jq`.

```bash
vmem recall <tag-or-id>            # exact handle
vmem save "text" [tag]             # smart_ingest, optional tag
vmem walk <failure-memory-id>      # causal_walk from a logged write
vmem receipt <memory-id>           # receipt get
vmem selftest
```

## Data location

Default data directory (override with `--data-dir`):

- **macOS**: `~/Library/Application Support/com.vestige.core/`
- **Linux**: `~/.local/share/vestige/core/`
- **Windows**: `%APPDATA%\vestige\core\`

## Credits

- [Vestige](https://github.com/samvallad33/vestige) by [@samvallad33](https://github.com/samvallad33)
- Original skill wrapper by [@Belkouche](https://github.com/Belkouche)
