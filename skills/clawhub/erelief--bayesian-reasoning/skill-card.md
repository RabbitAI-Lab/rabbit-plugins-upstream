## Description:

Guide users through Bayesian reasoning via multi-turn dialogue. Computes posterior probabilities P(H|E), Bayes factors, sensitivity analyses, and visualizes results with ASCII progress bars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erelief](https://clawhub.ai/user/erelief)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers use this skill to structure Bayesian probability updates, compare hypotheses against evidence, run sensitivity analysis, and preserve results for iterative review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved analysis files may contain sensitive hypothesis or evidence text.

Mitigation: Avoid saving sensitive material unless local JSON storage in the current working directory is acceptable.

Risk: Posterior probabilities depend on user-provided priors, likelihoods, and false-positive rates.

Mitigation: Review assumptions explicitly and use the skill's sensitivity analysis when estimates are uncertain.

## Reference(s):

- [Bayesian Analysis Result Schema](references/data_schema.md)
- [ClawHub skill page](https://clawhub.ai/erelief/skills/bayesian-reasoning)
- [Publisher profile](https://clawhub.ai/user/erelief)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON calculator results and optional saved JSON analysis files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local script output for posterior probabilities, Bayes factors, sensitivity ranges, and ASCII progress bars.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
