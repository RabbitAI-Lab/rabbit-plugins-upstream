---
name: memory-lifecycle
description: "Structured memory management to resolve cliff-edge forgetting, false persistence, context blowup, contradictions, hallucinated recall, and stale accumulation. Use when the user states anything durable to carry across sessions — preferences, corrections, decisions, team/environment facts, or standing instructions ('from now on...', 'always X before Y', 'never...') even without saying 'remember'; for first-time setup, compaction flush, deep research or project work, recalling a past session missing from context, when MEMORY.md exceeds its size threshold, or on 'init memory' / 'promote memory' / 'compact memory' / 'workspace init'."
---

# Memory Lifecycle

Structured memory management built on openclaw's memory infrastructure. Provides structure for the pre-compaction memory flush (what to encode and how), defines promote rules for moving entries from daily files to MEMORY.md, compact rules for pruning stale entries, and project workspaces for detail that doesn't fit in MEMORY.md. Retrieval uses the platform's `memory_search` tool (hybrid BM25 + vector), which automatically indexes all `memory/**/*.md` files.

## Architecture

Three layers with progressive loading:

| Layer | File | Injected? | Managed by |
|-------|------|-----------|------------|
| Daily | `memory/YYYY-MM-DD.md` | Today + yesterday at session start | Flush prompt (auto) |
| Longterm | `MEMORY.md` | Always (full content) | Promote + Compact |
| Permanent | `SOUL.md` + `AGENTS.md` | Always (full content) | User only |

Supporting files:
- `memory/projects/{name}/` — project workspaces (loaded on-demand via pointers in MEMORY.md)
- `memory/.lifecycle.log` — operation audit log
- `memory/.memory-backup.md` — MEMORY.md backup before modification

### Progressive Loading

MEMORY.md is always in context but has a size ceiling (30K chars). For detailed knowledge — deployment runbooks, research reports, project architecture, recurring workflows — use project workspaces:

```
MEMORY.md (always in context):
  - Service A deployment | see memory/projects/service-a-deployment/

memory/projects/service-a-deployment/runbook.md (loaded when needed):
  Full step-by-step procedure, env vars, rollback steps, gotchas
```

Agent sees the pointer in MEMORY.md, reads the workspace file only when the task requires it.

## Flows

### 1. On first run

If `memory/.lifecycle.log` does not exist, run init. See [init.md](references/init.md).

### 2. On user remember request

Triggered when the user explicitly or implicitly states something lasting:

- **Explicit**: "remember that...", "save this...", "note that...", "from now on...", "always...", "never...", "the rule is..."
- **Implicit**: corrections ("no, we use X not Y"), preferences ("I prefer tabs"), decisions ("we're going with Postgres"), team facts ("Alice owns auth"), environment info ("staging is port 3001")

Do not compose your response yet. First write the entry to MEMORY.md in the appropriate section (`## User`, `## Knowledge`, `## Rules`, etc.):

```
- {content} | EXPLICIT | from:YYYY-MM-DD
```

If the content is detailed (multi-step procedure, analysis, etc.), create a project workspace instead and add a pointer to MEMORY.md.

Then respond to the user and confirm. Persistence before acknowledgment.

### 3. On compaction flush

The platform triggers a silent agentic turn when the session approaches the context window limit. The goal is to encode durable information from this session into today's daily file before compaction.

1. If the conversation was trivial (single-question lookup, no decisions, no new information), reply `NO_REPLY`.

2. Read `memory/YYYY-MM-DD.md` if it exists. Append a new session section (do not overwrite earlier sessions from today).

3. Write a session section with this structure:

```markdown
## Session {HH:MM}

### Key Events
- {event}

### Knowledge Learned
- {fact}

### User Preferences
- {preference} | EXPLICIT or INFERRED

### Decisions Made
- {decision}

### Unfinished
- {item}
```

Only record non-trivial, specific information. Skip filler.

4. Promote qualifying entries to MEMORY.md:
   - EXPLICIT entries: promote immediately with `from:YYYY-MM-DD`.
   - INFERRED entries: only promote if the same pattern appears in 3+ daily files from the last 7 days.
   - Unfinished items: add to MEMORY.md `## In Progress` as `- [ ] {task} | from:YYYY-MM-DD` (skip if already tracked).
   - Never promote credentials — replace with pointers.

   Before promoting, backup MEMORY.md to `memory/.memory-backup.md`. Log each promotion to `memory/.lifecycle.log`.

5. If MEMORY.md exceeds 30K chars after promotion, run compact. See [promote-compact.md](references/promote-compact.md).

See [flush-prompt.md](references/flush-prompt.md) for the openclaw.json memoryFlush configuration.

### 4. On past context retrieval

When the user asks about something from a previous session and the answer is not in MEMORY.md or current context:

Use the `memory_search` tool to search across daily files and MEMORY.md. The platform automatically indexes all `memory/**/*.md` files with hybrid BM25 + vector search.

If the search finds relevant entries in daily files, present findings to the user. If the information deserves long-term persistence, promote it to MEMORY.md with `from:YYYY-MM-DD`.

### 5. On promote (periodic or manual "promote memory")

Scan daily files from the last 7 days. For each entry, check against MEMORY.md — skip duplicates, promote qualifying entries, resolve conflicts. See [promote-compact.md](references/promote-compact.md) for the full checklist.

### 6. On MEMORY.md exceeds threshold (or manual "compact memory")

When MEMORY.md grows beyond 30K chars or contains visibly stale/redundant entries, run compact: decay old entries, merge duplicates, supersede contradictions. See [promote-compact.md](references/promote-compact.md) for the full checklist.

### 7. On deep research / project workspace creation

When the user asks for research, analysis, wants to create/work on a project, or teaches a multi-step procedure worth persisting:

1. Create `memory/projects/{name}/` (or append if exists). See [workspace-init.md](references/workspace-init.md) for structure.

2. Write findings, procedures, or analysis to workspace files.

3. Add a one-line pointer to MEMORY.md `## Projects`:
   ```
   - {name} | {one-line description} | memory/projects/{name}/
   ```

4. Present key findings in chat. The workspace holds the detail; MEMORY.md holds the index.

## Rules

### Promote (Daily → MEMORY.md)

| Entry type | Action |
|-----------|--------|
| EXPLICIT | Promote immediately with `from:YYYY-MM-DD` |
| INFERRED, 3+ daily files | Promote |
| INFERRED, 1-2 days | Leave in daily file |
| Credential | Reject — pointer only |
| Detailed procedure / analysis | Create project workspace + pointer instead |

### Compact (when MEMORY.md > 30K chars)

| Entry type | Action |
|-----------|--------|
| Non-`[perm]`, not relevant 60+ days | Delete |
| In Progress `[x]` older than 7 days | Delete |
| In Progress `[ ]` not updated 60 days | Delete |
| Same topic, multiple entries | Merge |
| `[perm]` | Never touch |

### Conflict Resolution

Newer > Older. EXPLICIT > INFERRED. User correction > all. AGENTS.md > everything.

### Verification

When a MEMORY.md entry is disputed: look up `from:YYYY-MM-DD`, use `memory_search` or read the daily file to find the original context. If wrong or stale, update MEMORY.md and log the correction.

### Safety

Never store credentials, API keys, tokens, or connection strings. Replace with location pointers. Always backup MEMORY.md before modifying. Always log operations to `memory/.lifecycle.log`.

## MEMORY.md Format

Entry format: `- {content} | EXPLICIT or INFERRED | from:YYYY-MM-DD | [perm]`

- `EXPLICIT` — user stated directly
- `INFERRED` — deduced from behavior
- `from:YYYY-MM-DD` — date of daily file with original context
- `[perm]` — immune to compaction decay (only the user tags this)

Project pointer format: `- {name} | {description} | memory/projects/{name}/`

In Progress format: `- [ ] {task} | from:YYYY-MM-DD` (open) → `- [x] {task} | from:YYYY-MM-DD` (done)

- Source: the `### Unfinished` items captured during flush become `[ ]` entries here.
- Mark `[x]` when the work completes. Compact then purges done items quickly (7 days) and reaps abandoned open items (60 days).

Sections: `## User` / `## Projects` / `## Team` / `## Knowledge` / `## Rules` / `## In Progress`

## Examples

### Remember request

User: "Remember that staging uses port 3001"

Write to MEMORY.md `## Knowledge`:
```
- Staging uses port 3001 | EXPLICIT | from:2026-05-08
```
Respond: "Recorded — staging uses port 3001."

### Flush encoding

Session discussed Redis migration and decided to switch packages:

Append to `memory/2026-05-08.md`:
```markdown
## Session 14:30

### Decisions Made
- Switch from ioredis to redis package for auth-service

### Unfinished
- Connection pooling not yet configured
```

Promote the decision to MEMORY.md:
```
- Switch from ioredis to redis for auth-service | EXPLICIT | from:2026-05-08
```

### Progressive loading

User: "Deploy service A"

Agent sees in MEMORY.md (already in context):
```
- Service A deployment | production deploy procedure | memory/projects/service-a-deployment/
```

Agent reads `memory/projects/service-a-deployment/runbook.md`, follows the steps.

### Project workspace creation

User explains a complex deploy procedure over a long conversation.

Agent creates `memory/projects/service-a-deployment/runbook.md` with full steps, adds pointer to MEMORY.md:
```
- Service A deployment | production deploy procedure | memory/projects/service-a-deployment/
```
