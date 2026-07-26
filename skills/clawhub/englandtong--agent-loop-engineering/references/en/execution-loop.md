# Execution Loop

## Loop Start

Read the minimum needed:

1. `Docs/ACTIVE_PACKET.md`.
2. Files linked by the current stage, acceptance criteria, or next action.
3. Relevant manifests and verification commands.
4. The last three to five loop records only when needed.

Confirm:

- contract version is supported;
- goal readiness is `Ready for Execution`;
- execution is `Ready`, `In Progress`, or authorized `Needs Fix`;
- alignment is not Misaligned or Owner Review Required;
- one next action exists;
- no stop condition is already active.

## Select A Bounded Action

A loop action should:

- fit inside the current stage;
- change one coherent behavior;
- link to at least one acceptance criterion;
- have an expected verification result;
- be reversible or protected by an explicit recovery plan.

If the action cannot be explained in one sentence as progress toward the desired outcome, stop for alignment.

## Implement

- Inspect existing patterns before editing.
- Prefer the smallest coherent vertical slice.
- Preserve unrelated user changes.
- Avoid speculative abstractions and unrelated cleanup.
- Keep protected files untouched.
- Record a newly discovered scope need as an idea or blocker, not an automatic expansion.

## Verify

Run the narrowest useful check first, then broaden:

1. focused test or reproduction;
2. typecheck/build/lint as relevant;
3. affected regression;
4. functional or user-flow check;
5. target-environment check when required.

Record command, exit code, concise result, timestamp, and evidence path.

## Evaluate

Use:

- `In Progress`: useful bounded next action remains.
- `Ready for Review`: authorized implementation is complete and evidence is sufficient for QA.
- `Needs Fix`: an actionable defect remains inside authorized scope.
- `Blocked`: a hard gate or unavailable authority prevents progress.
- `Invalid State`: project state conflicts or required authorization is missing.

At stages 3, 6, and 10, include:

```text
User-visible change:
Target / acceptance link:
Scope or assumption drift:
Evidence against premature completion:
Recommended alignment verdict:
```

## Progress And Failure Budget

Progress requires at least one:

- new passing verification;
- narrower failing scope;
- new root cause supported by evidence;
- completed authorized behavior;
- resolved acceptance criterion;
- reduced material risk with proof.

Do not count re-running the same failing command, rewriting plans, or producing documents as progress.

After two consecutive core failures without progress:

1. stop broad implementation;
2. summarize both failures and root-cause evidence;
3. set `Needs Fix` or `Blocked`;
4. recommend re-plan, environment action, or Owner decision.

## Stage Transition

Advance a stage only when:

- its intended outcome is satisfied or formally superseded;
- evidence is recorded;
- unresolved defects are not hidden;
- one next stage outcome is authorized.

Do not create a new Work Order just because the stage number changed.
