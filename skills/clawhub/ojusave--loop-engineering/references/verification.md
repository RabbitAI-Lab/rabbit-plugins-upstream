# Verification and Validation

## Contents

- [Principle](#principle)
- [Verification versus validation](#verification-versus-validation)
- [Evidence fit](#evidence-fit)
- [Evidence states](#evidence-states)
- [Acceptance definition](#acceptance-definition)
- [Maker and checker separation](#maker-and-checker-separation)
- [Reproducibility](#reproducibility)
- [Failures](#failures)
- [Subjective quality](#subjective-quality)
- [Commodity-baseline verification](#commodity-baseline-verification)
- [Meta-change verification](#meta-change-verification)
- [Stop rules](#stop-rules)

## Principle

Evidence must observe the outcome contract, not merely a convenient artifact property.

Examples:

- Passing unit tests does not prove an onboarding flow is understandable.
- A screenshot does not prove a form submits correctly.
- A phrase linter does not prove an article has an argument or audience value.
- A polished abstract does not prove the talk delivers knowledge beyond a generic overview.
- Recent repository activity does not prove a library is appropriate.

## Verification versus validation

- **Verification:** confirm that the artifact, implementation, or analysis meets its specified requirements.
- **Validation:** confirm that it fulfills its intended purpose for the intended stakeholder in the intended context.

Examples:

- Unit and integration tests can verify code. A representative end-to-end task or observed production behavior validates intended use.
- Factual and editorial review can verify an article. A target reader accurately understanding and applying its promised idea validates the audience outcome.
- Source review can verify a research packet. A decision owner being able to make the named decision with bounded uncertainty makes it `DECISION READY`.

Do not demand unavailable post-use evidence when the scoped request is only to prepare an artifact. Set the required evidence state accordingly and disclose what remains unvalidated.

## Evidence fit

Choose evidence by how directly it observes the contracted outcome. Determinism is valuable, but a deterministic proxy is not stronger than direct observation of the intended result.

Use the relevant evidence family:

- **Artifact verification:** tests, builds, schemas, parsers, static analysis, factual checks, rendered inspection, and diff review
- **Behavior validation:** end-to-end scenarios, actual runtime behavior, representative users or operators, and production-like environments
- **Decision readiness:** primary evidence, reproducible observation, source-quality analysis, counterevidence, uncertainty bounds, and decision-owner needs
- **Subjective outcomes:** representative audience response, expert review, comparative alternatives, and explicit human judgment

Combine evidence when one source covers only part of the outcome. Record the environment, population, scenario, and limitation of every proxy.

## Evidence states

Report exactly one:

- `NO RELIABLE EVIDENCE`: required checks have not passed or evidence is insufficient
- `ARTIFACT VERIFIED`: the deliverable meets its specified requirements, but its intended external effect has not been observed
- `OUTCOME VALIDATED`: the target result is observed in the intended context at the contracted threshold
- `DECISION READY`: research or diagnosis has reduced uncertainty enough for the named owner to make the named decision

Evidence state is not assignment status. A task can be `BLOCKED / NO RELIABLE EVIDENCE`, `COMPLETE / ARTIFACT VERIFIED`, or `COMPLETE / OUTCOME VALIDATED` depending on its contract.

## Acceptance definition

Before acting, record:

- baseline and target state
- primary measure, threshold, and guardrails
- required evidence state
- scenario or behavior that must succeed
- invariants that must remain true
- edge and failure states
- exact evidence to collect
- exclusions

Avoid criteria such as `looks good`, `high quality`, `production ready`, `modern`, `robust`, or `user friendly`. Translate them into observable behavior or explicitly reserve them for human judgment.

## Maker and checker separation

Prefer a separate checker context or specialist when:

- the artifact is high impact
- the maker can overfit the metric
- subjective judgment is central
- security, accessibility, or factual accuracy matters

If separate contexts are unavailable, perform a cold review:

1. Reopen the original request.
2. Reopen the outcome contract and current acceptance criteria.
3. Inspect the actual artifact or diff.
4. Re-measure the target and guardrails using the strongest feasible evidence.
5. Run artifact verification again where relevant.
6. Ignore the maker's explanation until after recording findings.

## Reproducibility

Record:

- baseline
- hypothesis and predicted observation
- actual observation and measured delta
- command or scenario
- environment or population
- input
- expected result
- observed result
- artifact path, screenshot, log, or citation

Do not write `tests pass` without naming the relevant check. Do not write `users will understand` without representative evidence or an explicit proxy limitation.

## Failures

When a check or validation fails:

1. Preserve the failure evidence.
2. Identify the assumption the failure contradicts.
3. Fix the cause, not the check.
4. Rerun the narrow check.
5. Remeasure the contracted outcome when the fix can affect it.

Never delete, weaken, or bypass a legitimate check merely to reach `COMPLETE`.

## Subjective quality

For UI, writing, and strategy, avoid a single invented score. Use specific scenarios and findings.

Good:

- A first-time user cannot identify the primary action within the first screen.
- The article's second section repeats the thesis without evidence.
- The recommendation assumes a procurement model not supported by the source data.

Weak:

- UX score: 8.7/10
- Writing quality: excellent

## Commodity-baseline verification

When an artifact must earn attention, compare it with the strongest plausible generic answer available from common knowledge and the supplied public context.

Record:

- the baseline takeaways
- the artifact's additional takeaways
- which additional takeaways depend on verified evidence, access, demonstration, synthesis, or judgment
- whether those takeaways will actually be delivered

Do not treat unusual wording, a famous employer, proprietary-sounding nouns, or an invented framework name as evidence of added value. If the supported audience delta is empty, verification fails and the work returns to research, strategy, or the author before more editing.

## Meta-change verification

When a loop proposes changing its own persistent prompt, workflow, routing, rubric, tool, or evaluator:

1. Freeze the current outcome contract and guardrails.
2. Record the recurring failure pattern the change is meant to address.
3. Define the predicted improvement and plausible regressions.
4. Run representative success, failure, and adversarial cases before and after the change.
5. Use external checks or an independent reviewer; do not rely only on the authoring model's score.
6. Adopt the change only when the intended measure improves without weakening evidence, safety, scope, or authority boundaries.
7. Require human approval for consequential or persistent changes when the user did not already authorize them.

If the current strategy fails, change the strategy or stop honestly. Do not change the test so the failure becomes a pass.

## Stop rules

Stop with `COMPLETE` only when the scoped target and required evidence state are reached, guardrails pass, the result is usable for its named next step, and no required work remains.

Use `NEEDS HUMAN JUDGMENT` when evidence supports multiple choices and the remaining decision depends on taste, priorities, risk, values, or authority.

Use `BLOCKED` when a required external dependency, access, permission, or evidence source is unavailable.

Use `NOT FEASIBLE` when the outcome cannot be achieved safely or credibly within constraints.

Use `STAGNATED` when two consecutive parent cycles produce neither measurable progress nor decision-relevant learning, the hypothesis has changed at least once, and no credible next intervention remains.
