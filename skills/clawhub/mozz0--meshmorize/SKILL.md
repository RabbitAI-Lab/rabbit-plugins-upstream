---
name: "MeshMorize"
description: "🧠 Multi-layer memory system: fresh layer, mesh graph, auto-log, cross-layer search, compliance check"
---

# MeshMorize 🧠

Multi-layer memory system for LLM agents. Fresh daily layer, mesh graph indexing, auto-logging, cross-layer search, and full compliance checks.

Built for OpenClaw. Works with any agent that can run Python.

## Layers

| Layer | File | Purpose |
|-------|------|---------|
| **Fresh** | `memory/fresh/today.md` | Daily notes, 5-day rotation |
| **Mesh** | `memory/mesh.json` | Graph nodes + search index |
| **Log** | `scripts/auto_log` | Auto-log every interaction |
| **Search** | `scripts/memory_search` | Cross-layer search (fresh → daily → mesh → raw → long-term) |
| **Check** | `scripts/memory_check` | 10-point compliance check (`memcheck`) |

## Quick start

```bash
mem-bridge init          # Rotate fresh layer, create today.md
auto_log "msg" "reply"   # Log an interaction
memory_search "query"    # Search all memory layers
memcheck                 # Full 10-point compliance check
```

## Tools

| Tool | Source |
|------|--------|
| `mem-bridge` | `memory/bridge.py` — fresh-layer rotation + checkpoint management |
| `auto_log` | `scripts/auto_log.py` — interaction logger |
| `memory_search` | `scripts/memory_search.py` — multi-layer search across all memory stores |
| `memcheck` | `scripts/memory_check.py` — 10-point compliance check runner |

## Install

Put `bridge.py` in `memory/` and scripts in `scripts/` of your agent workspace. Symlink or add to `PATH`:

```bash
ln -s $(pwd)/scripts/* ~/.local/bin/
ln -s $(pwd)/memory/bridge.py ~/.local/bin/mem-bridge
```

On session start, run:
```bash
mem-bridge init
```

## Source

https://github.com/mozz0/MeshMorize

---

_Made by mozz0 · Released under MIT_
