# Controller And QA

Keep planning authority, implementation authority, and acceptance authority separate.

## Dispatch

Before dispatch:

1. Confirm Goal Readiness is `Ready for Execution`.
2. Confirm size and governance profile.
3. Create or update the Active Packet.
4. Name allowed scope, protected boundaries, acceptance criteria, evidence, and stop conditions.
5. Set `execution_state: Ready`, `qa_decision: Not Reviewed`, and one first stage outcome.

Developer may continue through authorized stages without asking after every loop only when:

- the next action stays inside the same packet;
- evidence shows useful progress;
- no stop rule or Owner boundary is triggered;
- alignment remains `Aligned`;
- repeated failures stay below the limit.

Developer may set `execution_state: Ready for Review`. Developer may not set QA or project acceptance in Standard or Full governance.

## Latest Delivery Review

Review only:

- the active packet and current Work Order;
- files changed in the latest delivery;
- acceptance criteria affected by that delivery;
- submitted evidence;
- necessary regression surface.

Do not turn a latest-delivery review into a whole-project audit.

Check:

1. Scope stayed authorized.
2. Non-Goals and protected boundaries remained intact.
3. Each Must Pass criterion has reproducible evidence.
4. Automatic checks and functional/user-flow evidence agree.
5. Skipped checks have a material, explicit reason.
6. Known risks are traceable and genuinely non-blocking.
7. The result still serves the user-visible outcome.

## QA Decisions

- `Accepted`: Must Pass criteria and required evidence are sufficient.
- `Accepted With Risk`: Core outcome is usable; a non-blocking edge remains explicit, owned, and time-bounded.
- `Failed`: Actionable implementation or evidence defects remain.
- `Blocked`: Acceptance requires Owner authority, unavailable environment, credentials, protected access, or another hard gate.

`Accepted With Risk` is not a substitute for a failed core flow, missing primary environment, or absent functional evidence.

## Failed Work

When QA fails:

1. Keep the same Milestone and Work Order.
2. Set `qa_decision: Failed`.
3. Set `execution_state: Needs Fix` and `project_state: Needs Fix`.
4. Add a bounded repair tied to failed criterion IDs.
5. State required re-verification and affected regression.
6. Return to the next appropriate stage; do not reset to a new Milestone.

Use `{baseDir}/templates/en/QA_DECISION.md`.

## Self-Acceptance

Self-acceptance is allowed only in Lite governance when:

- `qa_required: false`;
- the change is local, reversible, and low risk;
- automatic and functional evidence both pass;
- no material known limit remains;
- the Active Packet authorizes standalone execution.

Otherwise require independent QA.
