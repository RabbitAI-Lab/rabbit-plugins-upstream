## Description:

Use when forecasting, estimating, or sizing risk by anchoring on base rates, giving ranges, updating priors with evidence, and bounding unmeasured quantities with order-of-magnitude estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and decision makers use this skill to make uncertain forecasts, size risks, update estimates when evidence changes, and express decision-relevant ranges instead of unsupported single-point estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Forecasts can appear calibrated when no valid base rate, alternative path, or countercase exists.

Mitigation: Label the estimate as a guess unless the agent can name a reference class, compare alternatives, and state what evidence would change the estimate.

Risk: Probabilistic framing can be over-applied to facts that should be measured, looked up, or skipped because the decision is unchanged across the plausible range.

Mitigation: Measure or look up checkable quantities, skip estimates that do not affect the decision, and reserve Fermi bounds for quantities that cannot be cheaply measured.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance with structured estimates, ranges, evidence updates, Fermi bounds when needed, and decision implications.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-stream reasoning guidance; no files, commands, credentials, tools, or API calls are requested.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
