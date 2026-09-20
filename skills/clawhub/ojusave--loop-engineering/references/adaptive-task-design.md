# Adaptive Task Design

## Purpose

Keep the skill opinionated about reliability without freezing every task into a predefined checklist.

The shared contract is stable. The actual loop must be derived from the current task, repository, evidence, tools, risks, and user constraints.

## What is fixed

These rules do not change by task:

- activate when the user explicitly invokes it or an applicable active personal, workspace, or project instruction declares it the default; continue substantive follow-ups within that task and reset when the user clearly replaces the task
- inspect current state before acting
- establish a baseline-to-target outcome contract before selecting specialists
- make bounded, reversible changes
- prefer evidence over model confidence
- separate artifact verification from outcome validation
- require each meaningful cycle to predict an observable result and study the actual delta
- adapt strategy without autonomously weakening the outcome, verifier, evidence requirement, guardrails, or authority boundaries
- preserve compact state for multi-cycle work
- separate creation from verification when self-approval is risky
- require human approval for consequential or irreversible actions
- report one assignment status and one evidence state
- stop on completion, stagnation, blocked evidence, human judgment, or infeasibility
- never call failed or partial work `COMPLETE`

These are invariants, not a task checklist.

## What must be derived fresh

For every task, derive rather than assume:

- the real user outcome
- the outcome owner, class, baseline, target, intended context, measure, threshold, and guardrails
- the required evidence state and strongest feasible evidence now
- the next decision or use the result must enable
- non-goals and preservation constraints
- the important failure classes
- which specialist loops are necessary
- specialist order and handoff points
- what counts as evidence
- the commodity baseline and required audience delta when the artifact competes for attention
- the strongest feasible verifier
- currentness requirements
- source and incentive risks
- loop depth and budget
- stopping conditions specific to the artifact

Do not copy acceptance criteria from an unrelated example. Do not derive the outcome from the first solution that comes to mind.

## Design the loop from failure modes

Start with the artifact and ask:

1. What observable baseline-to-target change or decision does the user actually need?
2. How could the proposed output pass its checks while failing to cause that result?
3. Which outcome, guardrail, and failure observations would reveal that gap?
4. Which evidence is available now, and which real-world validation must remain pending?
5. Which specialist can collect each piece of evidence?
6. Must the specialist participate before work, after work, or both?
7. What can be omitted without creating a material blind spot?
8. If the artifact must earn attention, could it pass every planned check while remaining substitutable by generic knowledge?

Use the smallest specialist set that covers the material risks.

Examples are routing hints, not mandatory pipelines.

## Adapt during execution

The initial loop design is a hypothesis.

Revise routing when evidence reveals:

- a new failure class
- a dependency or platform decision
- a user-flow problem hidden by implementation
- source conflict or commercial bias
- a verifier that cannot observe the real outcome
- a required evidence state that cannot be reached in the current context
- a cycle whose actual observation contradicts the predicted mechanism
- a task that is simpler than initially believed

Do not add a specialist merely because it exists. Do not keep a specialist after its risk is proven irrelevant.

## Avoid checkbox theater

A checkbox is useful only when passing it provides evidence.

Reject checks that are:

- generic to every task
- impossible to observe
- duplicates of another check
- satisfied by producing a file rather than proving behavior
- self-scored without an external anchor
- inherited from a template without relevance

Replace `review quality` with a task-specific observation, such as:

- a first-time user completes the primary path without hidden knowledge
- the original bug reproduction no longer fails and a regression test passes
- each load-bearing market claim traces to current independent evidence
- the draft has one defensible thesis and no paragraph exists only for keyword coverage
- a public abstract names a supported finding, mechanism, demonstration, or decision that depends on the author's actual work or access

For every meaningful cycle, record a compact receipt:

```text
Hypothesis and mechanism:
Intervention or test:
Predicted observation:
Actual observation:
Delta from baseline or prior cycle:
Guardrail result:
Learning:
Next decision:
```

## Learn within the task

Use each cycle to update operational state:

- what evidence changed the direction
- which assumption failed
- which verifier was weak
- which specialist is now needed or no longer needed
- what acceptance gap remains
- how the evidence state changed

Do not turn one task's local finding into a permanent universal rule unless the user explicitly asks to update the skill.

## Completion test

Before `COMPLETE`, confirm that the target and required evidence state from the outcome contract were reached, the result is usable for its named next decision or context, guardrails pass, and remaining validation limits are explicit. Do not infer `OUTCOME VALIDATED` from artifact checks.

If the work changed a persistent loop, prompt, rubric, or evaluation method, also require representative before-and-after cases, regression evidence, and any necessary human approval. A loop cannot validate its own rule change solely with a score or judgment it authored.
