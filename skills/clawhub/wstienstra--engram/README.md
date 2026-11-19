# Engram

Local-first associative memory for OpenClaw agents. One command in, one command out.
SQLite only — no cloud, no API keys, no vector database.

## Why not just markdown files

Most agents remember by injecting `MEMORY.md` into every turn, or by grepping it. Engram
has to beat both, so it was measured against both.

74 questions, mined from 60 days of what a real agent was actually asked, labelled by hand
with the node that should answer each one, run against a 19,000-node workspace on
2026-09-18:

| arm | hit@3 | tokens per useful fact |
|---|---|---|
| `engram recall` | **86%** | 1,643 |
| `engram msgctx` (the per-message hook) | **62%** | 149 |
| grep over `MEMORY.md` + `memory/*.md` | 49% | 484 |
| injecting all of `MEMORY.md` every turn | 31% | 4,649 |

Two results matter. `recall` finds the right fact 37 points more often than a keyword search
does — and it does it while *falling silent* on 85% of the questions it has no answer for.
And the hook that runs on every message costs 149 tokens per useful fact against grep's 484
and the file dump's 4,649.

1.2.0 is where that stopped being a narrow win. On the same questions and the same database,
`recall` went from 74% to 86% at hit@3 and from 58% to **81%** on paraphrased questions — the
class that decides whether a memory is a memory or an index — at the same token cost, 1,421
per query. `msgctx` went from abstaining on 15% of unanswerable questions to **62%**.

Method, per-class results, and the parts that do not flatter Engram:
[docs/measurement.md](docs/measurement.md).

### Where it is weak

- `msgctx` abstains on 62% of questions it has no answer for, against `recall`'s 85%. So the
  per-message hook still answers about four unanswerable questions in ten with roughly 92
  tokens of noise. Much better than 1.1.x's 15%, still the biggest known defect.
- Every gain in this release lands hardest on `recall`, and `recall` is not the path that
  runs on every message. `msgctx` gained 9 points of hit@3 where `recall` gained 12.
- `recall` costs 6× more tokens per query than a markdown search (1,421 against 236). You
  buy the accuracy.
- The association channel adds +2 points at hit@3 for 234 extra tokens per query. It was
  +0.0 in 1.1.x, so the graph now earns its keep — narrowly, and it is still the least
  profitable part of the system per token.
- Tiering (`nodes.tier`, `recall --all`) ships but is **switched off**: it is the largest
  remaining token win and it is not safe yet. See [SKILL.md](SKILL.md).

## What it does

- **Recall** — hybrid retrieval: FTS5, semantic embeddings, tag and graph channels fused
  with weighted RRF, then reranked by a small CPU cross-encoder.
- **Abstention** — when nothing is genuinely grounded it says "no confident match" instead
  of confabulating. For an agent memory this is the feature everything else rests on.
- **Methods** — procedural memory. Store how a task was done right, get the steps and the
  pitfalls back when the same shape of task comes round again.
- **Intentions** — `engram intend "when X" "do Y"` arms a reminder that fires when the
  trigger appears in conversation. Keyword matching, about 50 ms, no model in the loop.
- **Time** — bi-temporal facts. `engram asof "office address" --date 2024-06-01` answers
  from that moment. Superseded facts are demoted, not deleted.
- **Tasks** — a durable ledger for work that outlives a session, with an evidence command
  whose exit code decides whether a task is really done.
- **Migration** — parses your `MEMORY.md`, `memory/*.md` and `AGENTS.md` into typed nodes.
  Dry-run report first, applied only when you say so.
- **Aliases** — `props.aliases` gives a node the words a person would actually use for it.
  Picked up free by full-text search, the vector index and the name channel. The single
  biggest share of the paraphrase gain in 1.2.0.
- **Hygiene** — `engram-hygiene.py` counts and (only when told) fixes duplicate nodes and
  orphans. Dry-run by default, on a read-only connection, and every applied step leaves a
  marker so a non-idempotent one cannot run twice.
- **Revert** — uninstall restores your workspace from a backup manifest.

## Install

```bash
./install.sh [workspace_dir]
```

Preflight degrades loudly: no flashrank means lexical rerank, no ONNX or ollama means
keyword-only. The installer then stages into `<workspace>/engram/`, creates the database,
stores and recalls one node to prove a fresh install works, and writes a migration dry-run
report for you to read.

```bash
python3 engram/engram-migrate.py --apply      # after reading the report
python3 engram/engram-seed-battery.py         # verify against your own content
python3 engram/engram-rewire.py               # optional: slim MEMORY.md, add crons
```

Then, whenever you like:

```bash
python3 engram/engram-hygiene.py engram/engram.db tier,merge,link   # count; add --apply to fix
cp engram/aliases.example.json engram/aliases.json                  # then edit it
python3 engram/engram-aliases.py engram/engram.db --spec engram/aliases.json --apply
```

## Daily use

```bash
engram recall "hosting setup"              # ask a question
engram msgctx "<incoming message>"         # per-message hook: short context, or silence
engram store --name N --type fact --content "..."
engram task add <name> --brief "..." --evidence "<shell command>"
engram startup                             # WIP and session briefing
```

`msgctx` is the one to wire into an agent loop. It reads the raw message, decides whether
there is anything worth saying, and returns roughly 200 tokens or nothing at all. `recall`
is the deeper lookup for when the agent knows it needs to dig.

## Uninstall

```bash
python3 engram/engram-uninstall.py          # restore and archive the db
python3 engram/engram-uninstall.py --purge  # also delete the archived db
```

Restores every touched file from the manifest, removes the managed cron lines, stops the
daemon. Safe to run twice.

## Configuration

Everything lives in `engram/engram.json`: workspace root, database path, socket, embedding
model, ollama URL, semantic mode. The engine hardcodes no paths. Point `ENGRAM_CONFIG`
elsewhere to run a second workspace from one install.

## Runtime cost

No cloud model is called anywhere in the runtime. The recurring pipelines are scripts, SQL
and embedding arithmetic. A small local model can phrase the nightly digest; without it the
digest is extractive.

## Contributing

The engine files are generated. Run `python3 build.py` to regenerate them, `--list` to see
what comes from where, `--check` to fail on a stale copy, and `bash ci/run-battery.sh` for
the four gates. See
[SKILL.md](SKILL.md#the-engine-files-are-generated-not-edited).

## License

MIT — see [LICENSE](LICENSE).
