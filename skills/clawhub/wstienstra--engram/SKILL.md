---
name: engram
version: 1.2.0
description: >
  One-install associative memory graph for any OpenClaw workspace: migrate
  markdown memory into a graph, recall it by question, keep a task ledger,
  verify with a seeded battery, and revert cleanly.
---

# Engram — associative memory as a skill

## What this does

Engram gives an agent a memory that answers questions instead of a file it has
to re-read. It stores typed nodes in SQLite, links them, and retrieves them
with a hybrid of keyword search, embeddings, tags and graph hops. It migrates
the `MEMORY.md`, `memory/*.md` and `AGENTS.md` you already have, and it
uninstalls back to exactly what it found.

Everything runs locally. No cloud call is made at runtime.

## Install

```bash
./install.sh [workspace_dir]
```

The workspace defaults to the parent of this skill directory.

The installer stops after a migration dry-run. It does not change your
markdown, and it refuses to overwrite an existing `engram/` directory.

## Flow

1. **Preflight** — Python 3.10 or newer is required. numpy, onnxruntime,
   flashrank and ollama are optional; each one that is missing degrades one
   step, loudly, and never stops the install. With none of them Engram runs
   keyword-only.
2. **Stage** — copies twelve engine files into `<workspace>/engram/`, the three
   cron-driven tools into `<workspace>/scripts/`, and writes
   `engram/engram.json` with every path.
3. **Init** — creates a fresh `engram.db` with the full schema, and starts the
   warm daemon if ONNX is present.
4. **Smoke** — stores one node and recalls it. This is the first recall on a
   brand-new database, the exact path that crashed in v1.1.x. A failure here
   stops the install before it touches anything else.
5. **Migrate (dry-run)** — parses your markdown into typed nodes, each tagged
   `source:<file>#<line>`, and writes `migration-report.md`. Nothing is stored
   until you run `--apply`. The original files are never modified.
6. **Verify** — `engram-seed-battery.py` mines 20 recall cases from your own
   migrated content and adds 3 negative controls. It passes at 90% of the
   positives and 3/3 negatives. A non-zero exit or a traceback from the engine
   fails the whole run, whatever the score says.

Steps 5 and 6, and the optional rewire, are yours to run:

```bash
python3 engram/engram-migrate.py --apply
python3 engram/engram-seed-battery.py
python3 engram/engram-rewire.py     # optional
```

`engram-rewire.py` backs up `MEMORY.md` and `AGENTS.md` to
`.engram-backup/<timestamp>/` with a manifest, slims `MEMORY.md` to a pointer,
adds an Engram section to `AGENTS.md`, and appends three cron lines marked
`# ENGRAM-MANAGED`: backup at 03:15, sleep consolidation dry-run at 03:45, and
a weekly battery on Sunday at 09:00.

## Daily commands

```bash
engram recall "hosting setup"            # ask a question, get the answer
engram msgctx "<incoming message>"       # short context block for one message
engram store --name N --type fact --content "..."
engram startup                           # WIP plus session briefing
engram task add <name> --brief "..." --evidence "<shell command>"
engram task probe                        # what is open, what has gone stale
engram intend "when X happens" "do Y"    # fires when the trigger appears
engram asof "office address" --date 2024-06-01
```

(`engram` here is `python3 engram/engram.py`, or `python3 engram/bq.py` to go
through the warm daemon when it is running.)

### The per-message hook

`msgctx` is the command an agent should call on every incoming message, not
`recall`. It takes the raw message, decides whether the message is a question
worth answering from memory, and returns a short block — usually around 200
tokens — or nothing at all. `recall` is the deeper, more expensive lookup for
when the agent knows it needs to go digging.

```bash
python3 engram/bq.py msgctx "$USER_MESSAGE"
```

Inject the output ahead of the message. When it prints nothing, inject nothing.

### The task ledger

`engram task` is a durable ledger for work that outlives one session. A task
carries a brief that can respawn it, an evidence command whose exit code
decides whether it is really done, and a status. `engram task probe` reports
tasks that are open, stale, or finished but unclosed. `task done` refuses to
close a task whose evidence command fails, unless you pass `--force`.

## Uninstall

```bash
python3 engram/engram-uninstall.py           # restore and archive the db
python3 engram/engram-uninstall.py --purge   # also delete the archived db
```

Restores every file from the manifest, removes the marked cron lines, stops the
daemon, archives `engram.db`. Safe to run twice.

## Configuration

Every path and model setting lives in `engram/engram.json`: `workspace`,
`db_path`, `socket_path`, `embed_model`, `ollama_url`, `ollama_embed_model`,
and `semantic_mode` (`onnx`, `ollama`, or `off`). The engine reads all of them
from there and hardcodes none. Point `ENGRAM_CONFIG` at another file to run a
second workspace from the same install.

## Degradation

| Missing | What happens |
|---|---|
| flashrank | Lexical rerank (RRF only, no cross-encoder) |
| onnxruntime | No ONNX embeddings; ollama or keyword-only |
| ollama | No ollama embeddings; ONNX or keyword-only |
| numpy | Keyword-only mode |

Every step down prints a warning. None of them is fatal.

## Engine files

| File | Purpose |
|---|---|
| `engram.py` | The engine. store, recall, msgctx, task, link, tags, wip, startup. **Generated — see below.** |
| `bq.py` | Thin client: daemon socket, CLI fallback |
| `engram-serve.py` | Warm daemon, keeps the ONNX model resident |
| `embeddings.py` | Semantic engine (ONNX multilingual-e5-small) |
| `engram-migrate.py` | Markdown to nodes |
| `engram-rewire.py` | Backup, slim `MEMORY.md`, add crons |
| `engram-uninstall.py` | Full revert from the manifest |
| `engram-seed-battery.py` | Install verification battery |
| `engram-battery.py` | Larger adversarial recall battery |
| `engram-sleep.py` | Nightly consolidation |
| `engram-backup.py` | Nightly backup via the SQLite backup API |
| `engram-maintenance.py` | Weekly health job: junk, casing, stale vectors, orphans, duplicates. **Generated.** |
| `engram-hygiene.py` | `tier` / `merge` / `link` migration, dry-run by default. **Generated.** |
| `engram-aliases.py` | Writes curated aliases into `props.aliases` and re-embeds. **Generated.** |
| `aliases.example.json` | Template for your own alias spec. Copy to `aliases.json` and edit. |
| `bpconfig.py` | Config loader, single source of truth |

## Aliases

An alias is new vocabulary for a node whose real name uses your jargon while the
question uses the asker's words. "owner contact details" and a node called
"Alice Johnson" share no word, in any channel, so no amount of ranking finds it.
One alias does.

```bash
cp engram/aliases.example.json engram/aliases.json      # then edit it
python3 engram/engram-aliases.py engram/engram.db --spec engram/aliases.json
python3 engram/engram-aliases.py engram/engram.db --spec engram/aliases.json --apply
```

Keys are node ids and each entry names the node as a safety net, so a spec
pointed at the wrong database is refused rather than applied. Aliases are free to
carry: `props` is already in the full-text index, `embeddings.py` embeds them with
the name, and the name channel treats each one as an alternative name — which
makes an aliased node pin-eligible whatever its type. One rule: no alias repeats a
word the node's name already has. That is a ranking hack, not a vocabulary fix.

## Hygiene

```bash
python3 engram/engram-hygiene.py engram/engram.db tier,merge,link     # counts only
python3 engram/engram-hygiene.py engram/engram.db merge --apply       # writes
```

Without `--apply` the database is opened read-only. Merging is **not** idempotent
— a second pass merges the survivors of the first — so every applied step leaves a
marker in `config` and refuses to repeat itself without `--force`. Duplicates need
an identical normalised name and type, or cosine ≥ 0.97 *and* name-token Jaccard
≥ 0.6 *and* content lengths within 20%; pairs that clear the first two bars but
not the third go to a review file, because merging them would drop text.

## Tiering is experimental and ships OFF

`nodes.tier`, the archive rule and `recall --all` are all in 1.2.0, and **nothing
marks a node `archive`**, so the filter does nothing until you switch it on. That
is deliberate. Switching it on measured **16 points off the recall headline**,
because the ranking constants (`NAME_MATCH_MAX_DF`, `GATE_EVIDENCE_DF_MAX`, the
IDF floors) count document frequency over `nodes_fts`, which indexes archived
nodes too — so hiding half the graph changes what every threshold means without
changing any threshold.

**Make document frequency tier-aware before turning tiering on**: a tier-filtered
FTS index, or df computed over the visible corpus. On the workspace this was
measured against, 65% of the graph is transport exhaust, so this is the largest
remaining token win — which is why the mechanism ships rather than being held back.

## The engine files are generated, not edited

Five files under `engine/` are built by `build.py` from upstream sources, with a
rename map, replaced regions, and a leak gate that refuses to write if a name,
path, id or internal document reference from the source workspace survives. A
banner at the top of each generated file says so.

For contributors:

```bash
python3 build.py            # regenerate every target
python3 build.py --list     # which file comes from where
python3 build.py --check    # exit 1 if a checked-in file is stale
python3 build.py --diff     # what would change
bash ci/run-battery.sh      # build check, fixture + tools, smoke recall, battery
```

`build.py` and `engine/engram_extras.py` are build-time only. `install.sh` does
not copy them into a workspace.

Before 1.2.0 the engine was maintained by hand and drifted from its upstream. The
generated build is what ended that. The engine files that are *not* in
`build.py --list` — `engram-sleep.py`, `engram-serve.py`, `bpconfig.py` and the
rest — have no upstream twin and are still maintained by hand; that is the
remaining drift surface, and it shrinks each time a file moves into the table.

## Constraints

- Never overwrites an existing `engram/` directory.
- The migration dry-run is mandatory. `--apply` is a separate, human step.
- Markdown is never rewritten without a backup manifest.
- Uninstall restores from the manifest and is safe to repeat.
