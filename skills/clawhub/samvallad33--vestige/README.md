# Vestige Skill for OpenClaw

Community skill wrapper for [Vestige](https://github.com/samvallad33/vestige) — local-first Rust MCP memory.

This skill wraps the official `vestige-mcp` binary. It is **not** OpenClaw default memory and **not** a `plugins.slots.memory` plugin. OpenClaw default is `memory-core`. Do **not** set `plugins.slots.memory` to vestige until a real OpenClaw plugin exists.

Most memory systems answer "what is like this?" Vestige answers **"what caused this?"** via backward-only causal Backfill (shared entities as the join key; similarity excluded from ranking).

Proof: no LLM in the memory path, exact FSRS-6 decay, local-first. Proven on local / synthetic traces. Not a production claim.

OpenClaw still has its own files and memory-core. Vestige sits beside them as an MCP server, not as a replacement.

## Install

Official Monday path is npm. Then copy the **absolute** path from `which` / `where` into OpenClaw MCP JSON. GUIs do not inherit shell PATH and do not expand `~`.

```bash
npm install -g vestige-mcp-server@2.7.1
which vestige-mcp          # macOS / Linux
where vestige-mcp          # Windows
```

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

Per-project store — `--data-dir` with an absolute directory. There is **no** `--project` flag (unknown args exit 1):

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

macOS and Linux are fine with the npm package. 2.7.1 is in on Ubuntu 22.04 / Debian 12 (glibc 2.35). Do not upgrade system glibc. Intel Mac still needs ORT_DYLIB_PATH in the MCP env block. Local/synthetic only. Do not use `npm install -g vestige-mcp-server@latest` as the Ubuntu 22.04 / Debian 12 path.

Helper `vmem` ships with this listing. It resolves `vestige-mcp` with `command -v`.

## Usage

```bash
vmem save "User prefers dark mode for all applications"
vmem recall "user preferences"     # search is a hidden alias of recall
vmem backfill                      # from the latest failure-like memory
vmem backfill <failure_id>
vmem stats                         # optional; needs vestige CLI
vmem health                        # optional; needs vestige CLI
```

## Advertised tools

These are the tools this skill tells agents to use. Prefer `recall`. `search` is a hidden v2.2 alias of `recall`.

| Tool | Arguments | Role |
|------|-----------|------|
| `recall` | `query` (mode `lookup` default) | Retrieve |
| `smart_ingest` | `content` | Store |
| `backfill` | `failure_id`, `manual`, `lookback_days`, `promote`, `scan_limit` | Backward causal trail from a later failure / symptom |

Live Backfill schema: [`crates/vestige-mcp/src/tools/backfill.rs`](https://github.com/samvallad33/vestige/blob/main/crates/vestige-mcp/src/tools/backfill.rs). The server also exposes other MCP tools; they are not this skill's advertised surface. Do not list `search` / `ingest` / `memory` / `codebase` / `intention` / `promote_memory` / `demote_memory` as primary tools.

## Default store

- **macOS**: `~/Library/Application Support/com.vestige.core/`
- **Linux**: `~/.local/share/vestige/core/`
- **Windows**: `%APPDATA%\vestige\core\`

## Credits

- [Vestige](https://github.com/samvallad33/vestige) by [@samvallad33](https://github.com/samvallad33)
- Skill wrapper by [@Belkouche](https://github.com/Belkouche)

## License

MIT
