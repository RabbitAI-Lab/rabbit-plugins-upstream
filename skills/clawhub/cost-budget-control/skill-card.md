## Description:

Cost Budget Control helps agents estimate token and cost usage, block over-budget calls, and suggest lightweight context compression before long-running or batch agent work proceeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to set token and cost budgets for long-running autonomous tasks, batch evaluations, and context-heavy workflows. It provides budget estimation, enforcement decisions, and compression guidance before expensive calls continue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner can retain local usage history, error patterns, and user preferences beyond the core budget-control workflow.

Mitigation: Review or disable the learner before installation when durable local history is not desired, and inspect or remove learned_patterns.json during operational reviews.

Risk: Budget estimates use static pricing supplied by the script or caller, so stale prices or mixed-model usage can produce inaccurate cost estimates.

Mitigation: Set price_per_1k and budget thresholds from the deployment's current billing data, and wrap the script with model-specific pricing when multiple models are used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/cost-budget-control)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell examples; script commands emit JSON or plain text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Budget estimation and enforcement depend on caller-provided token counts, cost limits, and static price settings.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
