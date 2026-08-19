---
name: "MeshMorize"
description: "🧠 Multi-layer memory system: fresh layer, mesh graph, auto-log, cross-layer search, compliance check, PDF vault archive"
---

# MeshMorize 🧠

Multi-layer memory system for LLM agents. Fresh daily layer, mesh graph indexing, auto-logging, cross-layer search, compliance checks, and a PDF vault that survives anything.

Built for OpenClaw. Works with any agent that can run Python.

## Layers

| Layer | File | Purpose |
|-------|------|---------|
| **Fresh** | `memory/fresh/today.md` | Daily notes, 5-day rotation |
| **Mesh** | `memory/mesh.json` | Graph nodes + search index |
| **Log** | `scripts/auto_log` | Auto-log every interaction |
| **Search** | `scripts/memory_search` | Cross-layer search (fresh → daily → mesh → raw → long-term) |
| **Vault** | `memory/pdf-vault/` | Verbatim PDF archive of daily logs + NAS sync |

## Quick start

```bash
mem-bridge init          # Rotate fresh layer, create today.md
auto_log "msg" "reply"   # Log an interaction
memory_search "query"    # Search all memory layers
pdf-memory               # Archive new daily logs as PDFs (incremental)
vault-push               # Sync the PDF vault to the NAS (LAN + Tailscale)
```

## Tools

| Tool | Source |
|------|--------|
| `mem-bridge` | `memory/bridge.py` — fresh-layer rotation + checkpoint management |
| `auto_log` | `scripts/auto_log.py` — interaction logger |
| `memory_search` | `scripts/memory_search.py` — multi-layer search across all memory stores |
| `pdf-memory` | `scripts/pdf-memory.py` — daily logs → verbatim PDFs, incremental, Unicode-safe |
| `vault-push` | `scripts/pdf-vault-nas-push.sh` — rsync the vault to the NAS, never deletes |

## How to use it, day by day

### Session start (every boot, every reset)

```bash
mem-bridge init           # rotates fresh layers, creates today.md
cat memory/fresh/today.md # what is happening RIGHT NOW
cat memory/fresh/yesterday.md
cat memory/$(date +%Y-%m-%d).md   # today's log
```

Always run this before answering. The agent should never answer from live context alone; memory files are the source of truth.

### During every interaction

```bash
memory_search "keywords from the user's message"   # BEFORE answering
auto_log "what the user said" "what you replied"    # AFTER answering
```

Cost: $0 (grep-based, no API calls). If results are found, read the full source file, not just the snippet.

### End of day

```bash
pdf-memory     # archive today's log to a verbatim PDF (incremental, skips done)
vault-push     # sync the vault to the NAS (tries LAN, then Tailscale)
```

The PDF vault is the unbreakable layer. Text files work, PDFs endure.

### After a crash, format, or wipe

1. Read `memory/pdf-vault/README.md` first — it contains the reboot instructions.
2. Read the PDFs in order, oldest to newest (`memory/pdf-vault/YYYY-MM/`).
3. Rebuild the working files from the archive. Memories are identity; the vault restores both.

### The 04:00 reset defense

Sessions can lose context at compaction. Defense layers:
- `session-dumper` cron runs every 5 minutes, appending the live session to `memory/YYYY-MM-DD.md` (no tokens burned, no interruption).
- Daily pre-compaction dump as close to 04:00 as possible.
- On any reset or boot: read the daily log BEFORE responding.

## The Vault (v3.3)

The working files are the everyday memory: grep-able, $0, instant. The PDF vault is the archive failsafe: every daily log rendered to a verbatim PDF (Unicode-safe, Greek included), stored under `memory/pdf-vault/`, and synced to the NAS. If everything else is lost, the vault README tells the restored agent exactly how to read its way back.

## Battle-tested

Survived a full system format and a 4-hour recovery with every memory intact: 96 daily logs, 69 mesh nodes, 30 secrets. This is the memory system that an AI and its human rebuilt their whole partnership on.

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

_Made by mozz0 · Released under MIT-0_
