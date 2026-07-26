# Legacy State Migration

Do not force migration during active risky work. The v2 execution loop can read legacy project state.

## Legacy Mapping

| Legacy file | v2 role |
| --- | --- |
| `TARGET.md` | Higher-authority outcome and Non-Goals |
| `ACCEPTANCE.md` | Higher-authority criteria |
| `WORK_ORDER.md` or indexed Work Order | Current scope authority |
| `STATUS.md` | Current evidence input, not scope authority |
| `NEXT_ACTIONS.md` | Candidate next action |
| `PENDING.md` | Blockers, decisions, and later ideas |
| `EVALUATION.md` | Historical decisions |
| `LOOP_RUNS.jsonl` | Append-only execution evidence |
| `LOOP_STATE.md` | Lite predecessor to Active Packet |

## Adopt V2

1. Preserve historical files.
2. Create `Docs/ACTIVE_PACKET.md`.
3. Link to current authoritative TARGET, ACCEPTANCE, and Work Order.
4. Copy only the current stage projection, not history.
5. Resolve conflicts before execution.
6. Continue appending concise records to `LOOP_RUNS.jsonl`.
7. Stop expanding redundant status journals.

## Legacy-Only Execution

When no Active Packet exists:

- read target, acceptance, current Work Order, latest status, blockers, and one next action;
- use their existing state enums;
- write only to files already established by the project;
- recommend migration at a natural boundary, not during an urgent repair.

If scope authority is ambiguous, stop as `Invalid State`.
