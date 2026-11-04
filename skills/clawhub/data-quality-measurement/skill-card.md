## Description:

Define and calculate dataset quality metrics, sampling plans and uncertainty, including completeness, verified correctness, coverage, precision and recall. Use for measurement questions rather than the whole delivery-acceptance or vendor-investment decision.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redrookai](https://clawhub.ai/user/redrookai)

### License/Terms of Use:

MIT-0

## Use Case:

Data practitioners and developers use this skill to define dataset quality measures, select and interpret samples, quantify uncertainty, and report findings that support a specific customer decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A biased or clustered sample can make population estimates misleading.

Mitigation: Document the sampling frame and selection, account for strata and clustering where appropriate, and state uncertainty and assumptions.

Risk: Incomplete or unreliable reference labels can distort verified-correctness and classification metrics.

Mitigation: Identify the source of truth, report assessed and unverified counts, and define how missing labels and abstentions affect each denominator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redrookai/skills/data-quality-measurement)
- [Worked example: sampling two cohorts](artifact/references/example.md)
- [Practice: define the metric](artifact/references/practice.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown text with metric definitions, counts, estimates, uncertainty, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States denominators, sampling assumptions, unverified counts, and supported next steps when relevant.]

## Skill Version(s):

1.0.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
