# Governance Profiles And Files

Choose the lightest profile that controls risk. Do not use file count as a sign of rigor.

## Lite

Use for Small, reversible work with direct acceptance and no independent QA requirement.

Required:

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`

Keep target, scope, acceptance, stage, evidence summary, and next action in the Active Packet. A standalone agent may perform self-acceptance only when `qa_required: false`, evidence includes automatic and functional checks, and no Owner boundary is involved.

Do not create Program, Dispatch, per-stage handoff, status journal, or separate QA files.

## Standard

Use for Medium work, an important user flow, moderate uncertainty, or work needing independent evaluation.

Required:

- `Docs/ACTIVE_PACKET.md`
- `Docs/LOOP_RUNS.jsonl`
- one `Docs/QA_DECISION_{ID}.md`

Optional only when they own stable information:

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- one consolidated `Docs/WORK_ORDER_{ID}.md`

Do not split Work Orders unless ownership, dependency, rollback, or acceptance boundaries differ.

## Full

Use for Large, high-risk, multi-agent, architecture, migration, production, security, data-integrity, or release work.

Required as applicable:

- `Docs/TARGET.md`
- `Docs/ACCEPTANCE.md`
- `Docs/ACTIVE_PACKET.md`
- `Docs/PROGRAM_{ID}.md`
- ordered `Docs/WORK_ORDER_{ID}.md`
- `Docs/LOOP_RUNS.jsonl`
- independent `Docs/QA_DECISION_{ID}.md`
- `Docs/DECISIONS.md` for Owner decisions and risk debt

Create separate handoff or rebaseline files only at real authority boundaries.

## File Creation Test

Create a new file only when at least one is true:

- a new authority or ownership boundary starts;
- an independent QA decision must be durable;
- an Owner decision changes authorization;
- a cross-agent or cross-team handoff cannot rely on the Active Packet;
- a formal target rebaseline is approved;
- the canonical active file reaches its archive threshold.

Otherwise update the canonical file.

## Anti-Bloat Rules

- One fact has one authoritative home.
- Link to logs and artifacts; do not paste them into several Markdown files.
- Keep `ACTIVE_PACKET.md` under roughly 200 lines.
- Keep only one immediate next action.
- Archive closed Work Orders and old decisions by release or month.
- Do not append routine stage notes to `TARGET.md` or `ACCEPTANCE.md`.
- Do not create a new Milestone for a failed test or repair.
- Do not repeatedly copy the same target, status, pending list, and evaluation into separate files.

## Legacy Compatibility

Existing `STATUS.md`, `NEXT_ACTIONS.md`, `PENDING.md`, `COMPLETED.md`, `EVALUATION.md`, handoffs, and Milestone histories may remain. Treat them as compatibility inputs. Do not continue expanding all of them unless the project's established audit or regulatory process requires it.

When adopting v2:

1. Create one Active Packet as the current projection.
2. Link to existing authoritative target, acceptance, and Work Order files.
3. Mark stale or conflicting files as archived; do not rewrite history.
4. Write new execution evidence to `LOOP_RUNS.jsonl`.
