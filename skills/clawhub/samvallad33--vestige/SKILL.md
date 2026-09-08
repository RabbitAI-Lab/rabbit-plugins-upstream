---
name: vestige
description: Local-first Rust MCP memory. Causal Backfill answers "what caused this?" (shared entities as join key; similarity excluded from ranking). Use for recall, smart_ingest, and backward-only Backfill — not as OpenClaw default memory.
---

# Vestige Memory Skill

Community skill wrapper around the official [`vestige-mcp`](https://github.com/samvallad33/vestige) binary.

Vestige is local-first Rust MCP memory. Most memory systems answer "what is like this?" Vestige answers **"what caused this?"** via backward-only causal Backfill: shared entities are the join key, and similarity is excluded from ranking.

Proof: no LLM in the memory path, exact FSRS-6 decay, local-first. Proven on local / synthetic traces. Not a production claim.

This skill is **not** OpenClaw default memory and **not** a `plugins.slots.memory` plugin. OpenClaw default is `memory-core`. Do **not** set `plugins.slots.memory` to vestige until a real OpenClaw plugin exists.

OpenClaw still has its own files and memory-core. Vestige does not replace them.

## Install

Official path is npm. Then resolve the **absolute** binary path — GUIs do not inherit shell PATH and do not expand `~`.

```bash
npm install -g vestige-mcp-server@2.7.1
which vestige-mcp          # macOS / Linux
where vestige-mcp          # Windows
```

Paste that path into OpenClaw MCP JSON:

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

Per-project store (absolute directory only). There is **no** `--project` flag — unknown args exit 1:

```json
{
  "mcp": {
    "servers": {
      "vestige": {
        "command": "<absolute path from which vestige-mcp>",
        "args": ["--data-dir", "<absolute dir>"]
      }
    }
  }
}
```

macOS and Linux are fine with the npm package. 2.7.1 is in on Ubuntu 22.04 / Debian 12 (glibc 2.35). Do not upgrade system glibc. Intel Mac still needs ORT_DYLIB_PATH in the MCP env block. Local/synthetic only.

Helper `vmem` ships with this listing. It resolves `vestige-mcp` with `command -v`.

## Advertised tools

Prefer `recall`. `search` is a hidden v2.2 alias of `recall`.

| Tool | Arguments | Use |
|------|-----------|-----|
| `recall` | `query` (mode `lookup` default) | Retrieve |
| `smart_ingest` | `content` | Store |
| `backfill` | `failure_id`, `manual`, `lookback_days`, `promote`, `scan_limit` | Start from a later failure / symptom; ranked trail of earlier operational records |

Backfill args are the live schema from [`crates/vestige-mcp/src/tools/backfill.rs`](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs). Omit `failure_id` to use the most recent failure-like memory. `manual=true` forces a run. `promote=false` is a dry run.

Do not treat `search` / `ingest` / `memory` / `codebase` / `intention` / `promote_memory` / `demote_memory` as the advertised surface.

## When to use

- Causal trail after a later failure ("what caused this?")
- Durable facts worth storing (`smart_ingest`)
- Session recall (`recall` with `query`)
- User preferences, bug fixes, project decisions

Never save API keys, passwords, or secrets.

## Trigger words

| User says | Action |
|-----------|--------|
| "Remember this" / "Don't forget" | `smart_ingest` |
| "I always..." / "I never..." / "I prefer..." | `smart_ingest` as a preference |
| "What caused this?" / "Why did this break?" | `backfill` |

## Session start

```bash
vmem recall "user preferences"
vmem recall "current project context"
```

## Helper

```bash
vmem recall "user preferences"     # search is an alias
vmem save "User prefers dark mode" # smart_ingest
vmem backfill                      # latest failure-like memory
vmem backfill <failure_id>
vmem stats                         # if vestige CLI is on PATH
vmem health                        # if vestige CLI is on PATH
```

## Data location

Default OS data dir (override with `--data-dir`):

- **macOS**: `~/Library/Application Support/com.vestige.core/`
- **Linux**: `~/.local/share/vestige/core/`
- **Windows**: `%APPDATA%\vestige\core\`

## Credits

- Official server: [Vestige](https://github.com/samvallad33/vestige) by [@samvallad33](https://github.com/samvallad33)
- Skill wrapper by [@Belkouche](https://github.com/Belkouche)
