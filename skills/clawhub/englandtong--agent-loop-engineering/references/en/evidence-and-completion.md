# Evidence And Completion

## Evidence Classes

Automatic evidence:

- focused tests;
- regression tests;
- typecheck;
- build;
- lint or static analysis;
- schema or migration validation;
- deterministic artifact checks.

Functional evidence:

- browser or UI workflow;
- API request and response;
- CLI behavior;
- generated file inspection;
- install/start/restart flow;
- device or target-environment smoke;
- operator workflow.

Independent evidence when required:

- QA rerun;
- reviewer reproduction;
- clean environment;
- separate agent with only task-local artifacts;
- release or production-like gate.

## Evidence Quality

Evidence must state:

- what was run or observed;
- environment;
- timestamp;
- result and exit code when applicable;
- artifact or log path;
- material limits.

Claims such as "tests pass", "looks good", or "implemented" without reproducible detail are insufficient.

## Conflicting Evidence

Use the weaker result:

- build passes, user flow fails -> not complete;
- unit tests pass, target environment unavailable -> keep the environment criterion open;
- screenshot looks correct, interaction fails -> not complete;
- self-round-trip passes, external consumer fails -> not complete;
- Developer says complete, QA fails -> `Needs Fix`.

## Ready For Review

Report `Ready for Review` only when:

- all authorized Must Pass criteria are checked;
- required automatic evidence passes;
- required functional evidence passes;
- regression scope is appropriate;
- known limits are explicit;
- no stop rule is active;
- the outcome still aligns with the original purpose.

## Accepted With Risk

Use only when:

- the core user outcome works;
- remaining risk is non-blocking;
- impact and owner are explicit;
- follow-up and deadline/boundary are recorded;
- the missing check is not the primary user flow or required environment.

Repeated Accepted-With-Risk items must trigger governance review.

## Standalone Completion

For Lite standalone work with `qa_required: false`, the execution agent may set:

- `qa_decision: Accepted`
- `project_state: Accepted`

only after both evidence classes pass and all acceptance criteria are checked.

Otherwise leave `qa_decision: Not Reviewed`, set `execution_state: Ready for Review`, and hand off.

## Completion Is Not Activity

Do not use as completion evidence:

- time spent;
- number of loops;
- files or lines changed;
- number of Markdown records;
- green checker output alone;
- a plan or handoff without working behavior.
