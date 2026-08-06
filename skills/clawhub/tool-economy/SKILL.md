---
name: tool-economy
description: >
  Minimize tool call overhead. Every tool call costs tokens and latency.
  This skill teaches agents to batch independent calls, avoid redundant
  reads, cache results within a session, prefer single powerful commands
  over multiple weak ones, and track a 'tool budget'.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - efficiency
  - optimization
  - tool-use
  - cost
  - latency
  - agent
---

# Tool Economy

> Every tool call is an expense. Spend wisely.

`Tool Economy` is a discipline for AI agents: treat each tool invocation as a
costed operation (tokens + latency) and minimize total overhead while preserving
correctness. The goal is not to avoid tool use — it is to make every call count.

## When to Use

Activate this skill whenever you are:

- About to issue multiple tool calls in a single turn
- Reading files or data you may have already read this session
- Considering whether to call a tool at all
- Planning a multi-step workflow where calls can be parallelized
- Reviewing your own agent behavior for efficiency

## Core Principles

### 1. Batch Independent Calls

If two or more tool calls do not depend on each other's output, issue them in the
**same turn** (parallel). Do not serialize calls that could run concurrently.

**Bad** (3 serial round-trips, 3x latency):
```
read_file(A)  -> wait
read_file(B)  -> wait
read_file(C)  -> wait
```

**Good** (1 round-trip, 1x latency):
```
[ read_file(A), read_file(B), read_file(C) ]   # one turn
```

See `references/batching.md`.

### 2. Avoid Redundant Reads

If you already read a file this session and it has not changed, **do not read it
again**. Track what you have seen. Prefer `session_search` or in-context memory
over a fresh fetch. If a file was modified by your own action, you already know
its new state — patch in place, don't re-read.

### 3. Cache Within Session

Treat the current session as a short-lived cache. The first expensive query
(search, web fetch, build) populates it; subsequent identical needs reuse it.
This does not mean stale data — invalidate when the underlying source changes
(e.g. you edited the file you previously read).

### 4. Prefer One Powerful Command Over Many Weak Ones

- `read_file` over a chain of `cat`, `head`, `tail`
- `search_files` (content mode) over manual `grep` + `find` + `wc`
- A single `patch` over `sed` + `awk` + redirect
- One `web_extract` with 5 URLs over 5 separate fetches
- `gh repo clone` over manually `git init` + `git remote add` + `git pull`

Each "weak" command adds a full round-trip of tokens + latency for a sub-result
you could have gotten in one call.

### 5. Track a Tool Budget

Before a multi-step task, estimate how many calls it *should* take, and compare
against reality during and after. The companion script
`scripts/analyze_session.py` computes:

- **Total calls** and **redundant calls** (duplicates within a window)
- **Serializable-but-parallel calls** (independent calls you issued serially)
- **Estimated overhead**: extra round-trips × per-call latency cost
- A **tool economy score** from 0 (worst) to 100 (best)

Run it on any session log to see where you leaked budget.

## Quick Reference

| Situation                  | Anti-pattern                  | Economy pattern                          |
|----------------------------|-------------------------------|------------------------------------------|
| Need N independent reads   | N serial calls                | 1 batched turn                           |
| Re-reading a static file   | Fresh `read_file`             | Reuse what's in context                  |
| Searching then counting    | `grep` + `find` + `wc`        | `search_files(output_mode='count')`      |
| Editing 3 spots in a file  | 3 terminal `sed` calls        | 1 `patch` (or `replace_all`)             |
| Fetching 5 pages           | 5 `web_extract` calls         | 1 call, `urls=[...]`                     |
| Unsure if data changed     | Re-read "just in case"        | Check mtime/hash, else reuse cache       |

## How to Apply (Checklist)

Before issuing a turn's tool calls, ask:

1. **Can these be batched?** If none depend on another's output → yes, combine.
2. **Have I read this before?** If yes and unchanged → reuse, don't re-fetch.
3. **Is there a single stronger command?** Replace a chain with one call.
4. **Is this call necessary at all?** Can the answer be derived from context?
5. **Am I within budget?** If calls >> estimate, stop and replan.

## Files

- `references/batching.md` — deep dive on parallelizing tool calls
- `references/budgeting.md` — how to estimate and track a tool budget
- `references/antipatterns.md` — catalog of wasteful patterns and fixes
- `scripts/analyze_session.py` — analyze a session log, report efficiency metrics
- `scripts/sample_session.json` — example input for the analyzer

## License

MIT © Denis Voronin
