# Task Breakdown Guide — PRD → Execution-Ready Tasks

Purpose: turn a finished PRD's requirements into a task list a coding agent (Claude Code, opencode CLI, or a human) can pick up and execute one task at a time, without needing to re-read and re-interpret the whole PRD for every step.

This file is tool-agnostic on purpose. It does not assume any particular agent framework, memory system, or naming convention beyond plain Markdown — so it works whether the user runs it through Claude Code, opencode, or manually.

## 1. Structure of the output file

`.project/prd/TASKS-[product-slug]-v[version].md`, with this shape:

```markdown
# Implementation Tasks — [Product Name]

Source PRD: .project/prd/PRD-[product-slug]-v[version].md
Generated: [date]
Status legend: [ ] pending · [~] in progress · [x] done

## Phase 0 — Foundation
- [ ] TASK-001 — ...

## Phase 1 — Core Features
- [ ] TASK-010 — ...

## Phase 2 — Non-Functional Hardening
- [ ] TASK-030 — ...

## Phase 3 — Polish & Release Readiness
- [ ] TASK-040 — ...
```

Leave gaps in numbering between phases (001, 010, 030...) so tasks can be inserted later without renumbering everything.

## 2. Anatomy of one task

Each task is a self-contained brief — a coding agent should be able to start a fresh session, read only this one task block plus the linked PRD sections, and know exactly what to build and how to know it's done.

```markdown
### TASK-011 — Book registration (create/edit)
- **Implements**: REQ-F-001, REQ-F-002
- **Depends on**: TASK-001 (DB schema), TASK-005 (auth/roles)
- **Scope**: Prisma model `Book` (isbn, title, author, category, stock_count); API route `POST /api/books` and `PATCH /api/books/:id`; admin form UI for create/edit.
- **Out of scope for this task**: bulk CSV import (separate task, TASK-014), barcode scanning UI (TASK-012).
- **Acceptance**: satisfies AC-001, AC-002 in the PRD. Specifically verify: duplicate ISBN is rejected with a clear error; stock_count cannot go negative.
- **Suggested files/modules**: `prisma/schema.prisma`, `app/api/books/route.ts`, `app/(admin)/books/*`.
- **Notes/risks**: none identified / [call out anything uncertain here].
```

Fields that must always be present: **Implements**, **Depends on** (or "none"), **Scope**, **Acceptance**. The rest (Out of scope, Suggested files, Notes) are included whenever they add clarity — don't pad every task with boilerplate if there's nothing to say.

## 3. Sizing a task correctly

A task is sized right when it's roughly **one focused agent session/turn** — not "build the whole checkout module" (too big, will drift and lose acceptance-criteria tracking) and not "add one field to a form" (too small, adds coordination overhead for no benefit). Rules of thumb:

- If a task implements more than ~4–5 requirement IDs, split it by sub-feature.
- If a task has zero acceptance criteria to point to, it's either not a real unit of work yet (merge it into a neighboring task) or the PRD is under-specified at that point (flag it back rather than inventing acceptance criteria that don't exist in the PRD).
- Cross-cutting non-functional requirements (security, performance) usually get their own tasks in Phase 2 rather than being silently folded into every feature task — this keeps them visible and testable rather than "implicitly assumed."

## 4. Ordering and dependencies

1. **Phase 0 — Foundation**: schema/data model setup, auth/role scaffolding, core infrastructure (DB connection, base API structure, base UI shell) — everything else depends on this.
2. **Phase 1 — Core Features**: the Must-have functional requirements (MoSCoW) from the PRD, ordered so that a task never depends on a task listed after it. Build the dependency graph explicitly (even just as the "Depends on" field) rather than relying on reading order alone.
3. **Phase 2 — Non-Functional Hardening**: security review items, performance tuning, accessibility passes, observability/logging — these usually need the core features to exist first to have something to harden.
4. **Phase 3 — Polish & Release Readiness**: Should/Could-have items, edge-case handling, rollout mechanics (feature flags), final QA pass against the PRD's Definition of Done (Section 18).

Should-have and Could-have requirements can be interleaved earlier if they're cheap and low-risk, but default to placing them in Phase 3 so a minimum viable Phase 0–1 slice is always shippable on its own.

## 5. Handoff notes for the coding agent

At the top of the generated `TASKS-*.md` file, include a short "How to use this file" block so whichever tool picks it up (Claude Code, opencode, a human) knows the convention without guessing:

```markdown
> Work through tasks in order within each phase; respect "Depends on." 
> Mark a task [x] only after its Acceptance criteria are verified, not just after code is written.
> If a task's scope turns out to be wrong or too large once you're in it, stop and split it into sub-tasks rather than silently descoping.
```

## 6. What NOT to do

- Don't invent requirement IDs or acceptance criteria that aren't in the source PRD — if a task needs an AC that doesn't exist yet, that's a signal the PRD itself has a gap (flag it back to the user, don't quietly patch it in the task file only).
- Don't collapse the whole PRD into one giant "implement everything" task — that defeats the purpose of the breakdown.
- Don't hardcode a specific agent framework's task-ID convention (e.g. `HB-###`) unless the user has told you this project already uses that convention elsewhere — default to the plain `TASK-###` scheme so the file stays portable across tools.
