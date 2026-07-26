---
name: engram
version: 1.1.1
description: >
  One-install associative memory graph for any OpenClaw workspace: stage,
  migrate markdown memory, rewire, verify with a seeded battery, and revert.
---

# Engram — Associative Memory as a Skill

## What This Does

Installs a fresh Engram associative memory engine into any OpenClaw workspace
with a single command. Migrates existing `MEMORY.md`, `memory/*.md`, and
`AGENTS.md` content into typed Engram nodes, rewires the workspace to use
Engram for context, and provides a full uninstall path.

## Install

```bash
./install.sh [workspace_dir]
```

Default workspace is the parent of this skill's directory.

## Flow

1. **PREFLIGHT** — Checks Python ≥3.10, pip deps (numpy, onnxruntime), optional
   flashrank (degrades to lexical rerank if absent), optional ollama (degrades
   to ONNX or FTS-only if absent). Disk space check.
2. **STAGE** — Copies engine files into `<workspace>/engram/`. Aborts if an
   existing engram/ is found (never overwrites). Writes `engram/engram.json`
   config with all paths.
3. **INIT** — Creates fresh `engram.db` with full schema (nodes, tags,
   associations, config, embeddings, methods, intentions, bi-temporal props).
   Starts warm daemon if ONNX is available.
4. **MIGRATE** — Parses `MEMORY.md` + `memory/*.md` + `AGENTS.md` into typed
   nodes (rule/lesson/contact/fact/project), each tagged with
   `source:<file>#<line>`. DRY-RUN first: emits `migration-report.md`.
   `--apply` after owner review. Originals NEVER modified.
5. **REWIRE** — Backs up `MEMORY.md` + `AGENTS.md` to
   `.engram-backup/<ts>/` with `manifest.json`. Slims `MEMORY.md` to an
   Engram pointer. Updates `AGENTS.md` startup section. Adds crons (backup
   03:15, sleep 03:45 dry-run, weekly battery) with `# ENGRAM-MANAGED`
   markers. Append-only.
6. **VERIFY** — Seeded mini-battery: 20 recall cases mined from migrated
   content + 3 negative controls. Gate: ≥18/20 + 3/3.

## Uninstall

```bash
python3 engram/engram-uninstall.py           # restore + archive
python3 engram/engram-uninstall.py --purge   # also delete archived db
```

Restores every file from manifest, removes crons by marker, stops daemon,
archives `engram.db` to `.engram-backup/`. Idempotent.

## Configuration

All paths and model settings live in `engram/engram.json`:
- `workspace` — workspace root
- `db_path` — engram.db location
- `socket_path` — daemon socket
- `embed_model` — ONNX embedding model name
- `ollama_url`, `ollama_embed_model` — ollama config (optional)
- `semantic_mode` — `onnx` | `ollama` | `fts`

Zero hardcoded paths in engine code — everything reads from config.

## Degradation

| Missing | Behavior |
|---------|----------|
| flashrank | Lexical rerank (RRF only, no cross-encoder) |
| onnxruntime | No ONNX semantic search, FTS-only mode |
| ollama | No ollama embeddings, uses ONNX or FTS |
| numpy | No semantic search, FTS-only mode |

All degradation is loud (warnings printed) and non-fatal.

## Engine Files

| File | Purpose |
|------|---------|
| `engram.py` | Core CLI — store, recall, link, tags, wip, startup, msgctx |
| `bq.py` | Thin client (daemon socket → CLI fallback) |
| `engram-serve.py` | Warm daemon (keeps ONNX model resident) |
| `embeddings.py` | Semantic engine (ONNX multilingual-e5-small) |
| `engram-migrate.py` | Markdown → Engram migration parser |
| `engram-rewire.py` | Backup + slim MEMORY.md + crons |
| `engram-uninstall.py` | Full revert from manifest |
| `engram-seed-battery.py` | Install verification battery |
| `engram-sleep.py` | Nightly consolidation pipeline |
| `engram-backup.py` | Nightly safe backup (sqlite3 .backup API) |
| `engram-battery.py` | Full recall battery (adversarial) |
| `bpconfig.py` | Shared config loader (single source of truth) |

## Runtime Cost

No cloud LLM in crons. Local model optional. Everything degrades to
deterministic scripts. Sleep consolidation uses local rules + heuristics.

## Constraints

- Never overwrites an existing `engram/` directory
- Migration dry-run is MANDATORY; `--apply` gated on human approval
- Never auto-rewrites md files without backup manifest
- Uninstall is idempotent and restores from manifest