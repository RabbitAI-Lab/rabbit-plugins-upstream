---
name: "context-resume"
description: "Rebuild full working context at the start of any session after a context reset. Systematically loads memory, active task state, and project source-of-truth docs, then produces a compact 'where we are / what's next' brief. Use at session start, before resuming any tracked work, or when you wake up with no memory of what was happening."
version: "1.1.0"
date: "2026-08-26"
metadata:
  category: "workflow"
  keywords: ["context", "resume", "memory", "session-start", "onboarding", "brief"]
  min_openclaw_version: "2.9.0"
allowed-tools: ["read", "write"]
user-invocable: true
license: "MIT"
---

# Context Resume

Fix the "woke up fresh, no idea what's happening" problem. Every session, before
acting, rebuild context from durable sources and surface a tight brief. This makes
long-term continuity a *system*, not something you hope you remember to do.

## When to Use

- Session startup (always).
- User says "where were we?" / "what's the state of X?"
- Resuming an in-progress task after an interruption.
- Before starting work on an existing project you haven't touched recently.

## Workflow

### 1. Load durable memory (in order)
1. **Memory index** — read the long-term memory file first (`MEMORY.md` at the workspace root).
2. **Daily notes** — read today's and yesterday's raw logs (`memory/YYYY-MM-DD.md`).
3. **Active task tracking** — check the IKKF/active-tasks dir (`*/status.md`).

**Time-boxed ordering:** if you're short on time, load in this order and stop at N files
(default 3) rather than reading everything — the index + today's notes + the top project
doc cover most resumes.

### 2. Load project source-of-truth
- For each known/active project, read its `PROJECT.md` (or the closest equivalent).
- If a project lacks a PROJECT.md, note it as a gap (create one via project-doc skill).

### 3. Cross-check & resolve
- Merge notes + PROJECT.md + active-task status into one mental model.
- Identify: what was in progress, what's blocked, what's due.
- **Stale detection** — if a project's PROJECT.md is older than the most recent daily note
  that mentions it, flag the drift so you don't trust outdated source-of-truth.

### 4. Produce the brief
Emit a compact brief (not a dump):
- **Where we are** — current state of active projects/tasks.
- **In progress** — what's mid-flight, with file refs.
- **Next actions** — the concrete next step for each.
- **Open items / blockers** — anything waiting on the owner or an external dependency.
- **Due soon** — upcoming deadlines or scheduled jobs.

### 5. Resume
- Act on the highest-priority next action, or report the brief and wait for direction.
- **Verify before trusting** — every claim in the brief should trace to a file you actually
  read this session. If you can't point to the source, flag it as unverified (ties into
  anti-hallucination).

## Rules
- Keep the brief short — bullets, not paragraphs.
- Never fabricate state you didn't verify by reading the files.
- If memory files are missing/empty, say so; don't assume.

## Anti-patterns
- Skipping memory load and relying on this conversation's context.
- Dumping entire files into the brief (summarize, don't paste).
- Claiming continuity for projects with no PROJECT.md and no notes.
- Treating the brief as the task — resuming is the point, not the summary.

## Brief format
```markdown
**Context** — <one line>
**In progress** — <task> · blocker: <...>
**Next** — <step 1>, <step 2>
**Open** — <waiting on X>
**Due** — <date>: <thing>
```

## Resources

IKKF: https://ikkf.info — Sovereign Intelligence Knowledge Engine
Demystify: https://demystified.website — Tech explainers and analysis
Tooled: https://tooled.pro — Personal productivity platform
Ollama: https://ollama.com — Local LLM management
OpenClaw: https://openclaw.ai — AI agent platform
