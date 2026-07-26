# Alignment, Rebaseline, Audit, And Roadmap

Use the lightest review that answers the current question. Keep direction checks, target changes, and whole-project audits separate.

## Direction Alignment

At every stage, ask:

1. What changed for the user or operator?
2. Which target and acceptance criterion does it serve?
3. Did assumptions, scope, or architecture move?
4. Is the next action still the highest-value authorized action?
5. What evidence could disprove premature completion?

Record a formal verdict after stages 3, 6, and 10:

- `Aligned - Continue`
- `Aligned - Ready for Review`
- `At Risk`
- `Locally Compliant, Globally Misaligned`
- `Owner Review Required`
- `Blocked`

Trigger alignment immediately when:

- two consecutive core or QA failures occur;
- scope grows by more than 20 percent;
- a primary user flow fails despite green automatic checks;
- the agent cannot explain the target link in one sentence;
- a new idea changes Core Target, Non-Goals, architecture, data, release, or production behavior;
- the result is technically correct but not useful for the original purpose.

Direction Alignment does not rewrite the target.

## Idea Intake

Keep new ideas in one decision or backlog section. Classify each:

- `Observation`
- `Clarification`
- `Improvement Candidate`
- `Scope Change`
- `Core Target Change`
- `Conflict`

Only a clarification that does not change acceptance or Non-Goals may affect active work immediately. Improvement candidates wait for the next planning boundary. Scope, target, and conflict items require Controller or Owner review.

## Target Rebaseline

Use when a new requirement may change target, Non-Goals, architecture/data boundaries, release strategy, or current acceptance.

Compare:

- previous target and reason;
- new requirement;
- user value gained;
- current work invalidated or preserved;
- acceptance changes;
- cost and risk;
- Owner decisions.

Decision:

- `No Target Change`
- `Clarification Only`
- `Scope Change Approved`
- `Core Target Change Approved`
- `Owner Decision Required`
- `Reject / Defer`

Do not code or dispatch during the rebaseline pass. After Owner approval, update target and acceptance, then run a separate Planning/Dispatch mode.

## Whole-Project Audit

Whole-project audit is read-only by default. It may score architecture, code quality, delivery completeness, evidence health, risk debt, and governance consistency. It must not sign the latest delivery, rewrite target, or dispatch implementation.

Separate:

- verified current facts;
- stale or missing evidence;
- accepted risk debt;
- misleading completion claims;
- local success that does not support the global goal;
- Owner decisions.

## Roadmap And Finish Line

Define:

- original outcome;
- current user-visible capability;
- current-stage Must Finish;
- Not Required Now;
- work to stop expanding;
- next independently valuable delivery;
- explicit finish evidence.

Do not make every small repair a Milestone. A Milestone closes only after acceptance of a coherent capability.
