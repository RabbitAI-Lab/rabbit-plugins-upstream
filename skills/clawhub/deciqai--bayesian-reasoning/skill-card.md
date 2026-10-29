## Description:

Guides agents to update beliefs with Bayesian reasoning by making priors, likelihood ratios, base rates, and evidence dependence explicit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deciqai](https://clawhub.ai/user/deciqai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users apply it to reason about uncertain decisions by stating a prior, assessing how diagnostic the evidence is, and updating a probability. It is especially useful when interpreting tests, security alerts, hiring signals, or benchmark results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An illustrative or poorly matched base rate, or an unsupported probability assumption, can distort a consequential conclusion.

Mitigation: Check the source and fit of the prior and likelihood assumptions before relying on the result for a consequential decision.

## Reference(s):

- [Sources](artifact/references/sources.md)
- [Bayesian search analysis of Air France Flight 447](https://doi.org/10.1214/13-STS420)
- [Bayesian Reasoning skill page](https://www.deciqai.com/c/bayesian-reasoning)
- [Machine-readable skill information](https://www.deciqai.com/s/bayesian-reasoning.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown with a structured Bayesian Update when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coach mode proceeds one question at a time; a completed update can state the hypothesis, prior, likelihood ratio, posterior, decision threshold, and next evidence.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
