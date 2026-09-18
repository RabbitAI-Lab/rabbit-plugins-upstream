# Foundations

## Contents

- [Purpose](#purpose)
- [Outcome contract](#outcome-contract)
- [Minimal anatomy](#minimal-anatomy)
- [Core cycle](#core-cycle)
- [Verification and validation](#verification-and-validation)
- [Productive results](#productive-results)
- [Why task-specific loops exist](#why-task-specific-loops-exist)
- [Stable contract, adaptive loop](#stable-contract-adaptive-loop)
- [Self-correction, recovery, and improvement](#self-correction-recovery-and-improvement)
- [Human role](#human-role)
- [Ground truth](#ground-truth)
- [State discipline](#state-discipline)
- [No-progress rule](#no-progress-rule)


## Purpose

Loop engineering turns a task into a feedback system. It is useful when fresh evidence from one attempt can change the next action.

The ideal result is a verified reduction in the gap between an observed starting state and a stakeholder-defined target state, demonstrated at the evidence level the task actually requires. A loop may also succeed by producing decision-quality learning that changes what should happen next.

A loop is not:

- a long checklist disguised as autonomy
- repeatedly asking the model to improve its own answer
- hidden chain-of-thought
- permission to keep working indefinitely
- a replacement for human product judgment

## Outcome contract

Before selecting specialists or drafting acceptance checks, establish the smallest useful outcome contract:

```text
Outcome owner or beneficiary:
Outcome class: state change | artifact | decision | knowledge | capability | risk reduction
Baseline:
Target state:
Intended context of use:
Primary measure and threshold:
Guardrails:
Required evidence state: ARTIFACT VERIFIED | OUTCOME VALIDATED | DECISION READY
Strongest feasible evidence now:
Next decision or use:
Constraints and non-goals:
```

Infer obvious fields for narrow tasks. Do not turn the contract into ceremony. Ask the user only when a missing field would materially change the work, risk, or meaning of success.

The outcome contract is not the proposed solution. Acceptance criteria describe whether an artifact matches its specification; the outcome contract describes the change or decision the artifact must enable.

## Minimal anatomy

Every loop needs:

- **Trigger:** why it starts
- **Outcome contract:** the baseline, target, context, measures, guardrails, and required evidence state
- **Scope:** what it may inspect or change
- **Observation:** fresh state and evidence
- **Hypothesis:** why a bounded action should change an observable measure
- **Action:** one bounded intervention, change, or information-gathering test
- **Measurement:** the predicted and observed result
- **Study:** the delta from baseline, contradicted assumption, or useful learning
- **Memory:** compact operational state
- **Stopping rule:** success, no progress, blocked, approval required, or infeasible

## Core cycle

1. **Observe:** Measure the current state or establish the strongest available baseline.
2. **Hypothesize:** State the expected observation and the mechanism: `If we do X, Y should change because Z.`
3. **Choose:** Select the smallest in-scope test or intervention that can resolve the highest-value uncertainty or reduce the target gap.
4. **Act:** Make one coherent, reversible change or collect one decisive piece of evidence.
5. **Measure:** Compare the actual observation with the prediction, baseline, target, and guardrails.
6. **Study:** Record what changed, what did not, which assumption was confirmed or contradicted, and what was learned.
7. **Decide:** Adopt, adapt, abandon, escalate, or stop. Repeat only when another cycle has a credible path to measurable progress or decision-relevant learning.

A failed intervention can be a successful cycle when it eliminates an important hypothesis or changes the next decision. A new artifact with no measured delta and no useful learning is not progress.

## Verification and validation

Keep these separate:

- **Verification:** confirm that the artifact, implementation, or analysis meets its specified requirements.
- **Validation:** confirm that it fulfills its intended purpose for the intended stakeholder in the intended context.

Use actual or representative users, operators, environments, and decisions whenever feasible. When real-world validation is unavailable within scope, use the strongest honest proxy and report `ARTIFACT VERIFIED`; do not claim the external effect was validated.

## Productive results

An assignment ends productively when one of these is true:

- the target outcome is observed in its intended context (`OUTCOME VALIDATED`)
- the requested artifact is verified and real-world effect is explicitly outside the assignment or still pending (`ARTIFACT VERIFIED`)
- research or diagnosis reduces uncertainty enough for a named decision (`DECISION READY`)
- human judgment, an external dependency, infeasibility, or genuine stagnation is reported honestly

Passing self-chosen checks is not sufficient by itself. The required evidence state must be declared in the outcome contract before work and matched at completion.

## Why task-specific loops exist

Different tasks fail in different ways:

- Code can be incorrect even when it compiles.
- A backend can be correct while the user flow is confusing.
- A page can look attractive while being inaccessible.
- An article can be factual while saying nothing original.
- A framework can work today while creating unnecessary lock-in.
- A prompt can be complete on paper while allowing the downstream agent to self-approve.

Use a shared operating contract, but specialize the cycle, evidence, and stop condition by failure class.

## Stable contract, adaptive loop

The skill fixes reliability rules, not the content of every loop. Derive the acceptance criteria, evidence, specialist order, and stop conditions from the current task.

The route may change as evidence arrives. The meaning of success may not drift merely because the current approach is failing.

## Self-correction, recovery, and improvement

Use three distinct behaviors:

- **Self-correction:** diagnose an observed failure, revise the strategy, and verify again within the existing outcome contract. This is required when another credible attempt exists.
- **Self-healing:** restore a known operational invariant after a transient or repairable failure. Use bounded retries, idempotent actions where possible, an action log, and an escalation condition.
- **Self-improvement:** change a persistent prompt, workflow, tool, rubric, routing rule, or evaluation method. Treat this as a separate change with its own outcome contract.

A working loop may propose a meta-improvement but must not silently adopt it when doing so changes what counts as success, weakens evidence, expands authority, or creates persistent behavior. Evaluate proposed improvements against representative success, failure, and regression cases. Compare before and after using externally anchored evidence. Keep the change only when the intended measure improves and guardrails remain intact.

Never allow the same agent's confidence or self-authored score to be the only approval for its own rule change. Require independent checking where feasible and human approval for consequential or persistent changes.

Do not run a protocol because it exists. Run it because it can observe a material failure. Treat examples as scaffolds and revise the loop when evidence changes the risk model.

## Human role

Keep the human at the boundary of:

- product taste
- values and priorities
- irreversible choices
- security and privacy
- production authority
- publication and external communication
- risk appetite

The agent may prepare options and evidence. It must not quietly convert a subjective or consequential choice into an invented default.

## Ground truth

Prefer evidence from the environment over model confidence:

- executed tests
- runtime output
- actual browser behavior
- screenshots
- source documents
- official release notes
- repository or package metadata
- user feedback

A self-written score is not ground truth.

## State discipline

State should be compact and operational. Record conclusions and evidence, not a transcript of internal reasoning.

Good state:

- outcome contract and baseline
- cycle hypothesis, predicted observation, and actual observation
- measured delta and evidence state
- acceptance criteria
- commands run and observed output
- selected direction and assumptions
- rejected direction and reason
- handoff artifact
- unresolved risk

Bad state:

- pages of speculative thinking
- copied secrets
- full source documents
- private user data
- unsupported confidence scores

## No-progress rule

Stop or change direction when:

- the same approach fails twice
- two parent cycles produce no measurable improvement
- the remaining issue requires human judgment
- the next iteration would only polish language or add speculative scope
- available evidence cannot resolve the question

When two consecutive parent cycles produce neither measurable progress nor decision-relevant learning, change the hypothesis. If no credible alternative remains, stop with `STAGNATED`. Never relabel stagnation as success or an external block.
