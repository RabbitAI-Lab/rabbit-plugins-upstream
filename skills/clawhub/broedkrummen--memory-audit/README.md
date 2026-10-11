# memory-audit

A read-only OpenClaw skill for observing memory cost and recommending manual cleanup. It never edits memory, invokes OpenClaw maintenance, or writes a report file. Python 3.10+; no required third-party dependencies.

## Install and invoke

Copy this folder into your agent workspace's `skills/memory-audit/` directory, or into your OpenClaw shared skills directory (`~/.openclaw/skills/memory-audit/`). Then ask:

- "audit my memory"
- "analyze memory usage"
- "show memory optimization suggestions"

Provide the agent workspace and model context budget if they are not available to the agent. The analyzer also runs standalone:

```bash
python3 skills/memory-audit/audit.py \
  --workspace /path/to/agent/workspace \
  --context-budget 200000
```

`200000` is an example. Use your model's actual capacity. Reports go to stdout; no output path or apply mode exists. If saving stdout yourself, choose a location outside the audited memory files.

## Options and coverage

| Option | Behavior |
| --- | --- |
| `--workspace PATH` | Required agent workspace, not skill directory |
| `--context-budget N` | Required positive token capacity |
| `--days N` | Recent notes for duplicates/promotions; default 30, includes today and preceding 29 dates |
| `--frequency N` | Promotion threshold in distinct days; default 3 |
| `--today YYYY-MM-DD` | Reproducible date or agent-local date; default system date |
| `--format markdown\|json` | Human report or schema-versioned structured report |
| `--retrieval-log PATH` | Optional normalized JSONL; format below |
| `--encoding NAME` | Use already installed `tiktoken`; fails clearly if missing/invalid |
| `--max-comparisons N` | Near-match comparison cap; default 200000; reports partial coverage |

Scans core files, optional DREAMS.md, and all top-level valid dated Markdown notes, including slug variants. Recent notes feed line-based duplicate/promotion heuristics; all dated notes contribute stored size and old-note retrieval review. Future-dated notes and workspace symlinks are skipped with warnings. Does not inspect SQLite databases, recursively traverse archives, call models, or access the network. Inputs must be UTF-8. Missing memory files are reported, not created.

Lines shorter than four normalized words, headings, fenced code, blockquotes and Markdown tables are excluded from fact heuristics. Paraphrases, multiline facts and preferences without recognizable keywords can be missed. Related but differing claims can become low-confidence overlap/conflict candidates. Review neighboring text before editing.

## Context accounting

The default token estimate is `ceil(UTF-8 bytes / 4)` per file. It is approximate, especially for code and non-English text. `--encoding` counts exactly for the named encoding, which may differ from your model tokenizer. No dependency is installed by the tool.

The report separates:

- Stored memory: MEMORY.md, USER.md, DREAMS.md and all scanned dated notes.
- Memory bootstrap candidates: MEMORY.md, USER.md, today's and yesterday's dated notes.
- All bootstrap candidates: memory candidates plus existing AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, HEARTBEAT.md and BOOTSTRAP.md.

Percentages equal candidate tokens divided by the supplied context capacity. These are raw file budgets, not actual injected prompt measurements. Session type, provenance eligibility, startup behavior, file budgets and truncation can reduce injection. Wrappers, history, tools and later retrieval add overhead not counted here. Use OpenClaw `/context list` or `/context detail` to inspect actual injection. BOOTSTRAP.md is conditional; DREAMS.md is review-only by default.

## Retrieval log adapter

All example dates, preferences, decisions and events below are fictional documentation fixtures.

There is no assumed universal OpenClaw retrieval-log schema. Supply an existing log normalized into the following JSONL format outside memory files, or omit it. This script does not produce/modify logs. Only successful file retrievals qualify; a search query alone does not.

```jsonl
{"type":"coverage","since":"2025-08-01"}
{"type":"retrieval","timestamp":"2025-09-01T12:00:00Z","path":"memory/2025-08-01.md"}
{"type":"retrieval","timestamp":"2025-09-29T12:00:00Z","path":"MEMORY.md"}
```

Paths must be workspace-relative or absolute inside the workspace and identify scanned files. `type` defaults to `retrieval` on event rows. A `coverage` record is an assertion that **all successful retrievals since that date through the audit date are captured**. Do not declare coverage for incomplete logs. Timestamps are evaluated by their recorded calendar date; normalize to the agent's timezone beforehand when day boundaries matter.

A note older than 30 days is flagged only when complete declared coverage includes the last 30 days, every log row parses, and no retrieval occurred in that window. A file hit cannot establish that each fact in it was accessed. Missing logs/coverage leave no-hit access unknown. Malformed rows are counted and disable inactivity claims. File age comes from its dated name; filesystem atime is never used. Old age alone does not justify deletion.

## Report and manual-edit examples

JSON contains `schema_version`, `as_of`, `read_only`, `budget`, `files`, `retrieval`, `findings`, `warnings`, and `limits`. Each finding includes source evidence (`file`, `line`, `text`, note date), confidence, a manual action, before text and an illustrative after example. Suggestions do not change anything.

**Misplaced preference**

Before, MEMORY.md: `I prefer brief responses with bullet points.`

Manual action: verify this is the user's stable preference, then move its canonical directive to USER.md.

After, USER.md: `Use brief responses with bullet points. [observed: 2025-10-03; status: active]`

**Repeated durable decision**

Before, three distinct daily notes: `We decided to use PostgreSQL for billing data.`

Manual action: confirm the decision still stands and review DREAMS.md for prior consolidation; add one summary to MEMORY.md. Keep daily evidence as history if useful.

After, MEMORY.md: `Billing data uses PostgreSQL. Decision confirmed 2025-10-03; sources: memory/2025-09-20.md, memory/2025-09-24.md, memory/2025-09-28.md.`

**Expired temporary state**

Before, MEMORY.md: `Temporary staging freeze until 2025-08-10.`

Manual action: check whether the freeze ended. If confirmed, move the historical event into its dated note and remove the obsolete core statement. If unconfirmed, leave it pending verification rather than inventing current status.

After, dated note, only if verified: `Staging freeze ended 2025-08-10. [verified: 2025-10-03]`

## Architecture references

[OpenClaw memory overview](https://docs.openclaw.ai/concepts/memory) distinguishes user directives, durable memory, daily evidence and DREAMS.md review. [Memory architecture](https://docs.openclaw.ai/concepts/memory-architecture) describes injection and provenance tiers. [Skills](https://docs.openclaw.ai/tools/skills) documents skill discovery and `{baseDir}`.
