## Description:

Identifies overlooked QA risks and prioritizes testing by assessing changes, business impact, technical complexity, data, and integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this Chinese-language skill to identify high-risk functionality, prioritize limited test resources, and propose risk-based test depth and mitigations from requirements and project context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may invoke risk assessment when it is not needed.

Mitigation: Confirm that risk prioritization is requested and limit inspection to relevant requirements and project files.

Risk: Inconsistent scoring thresholds may produce misleading risk rankings or test-coverage recommendations.

Mitigation: Review risk scores and coverage recommendations against the actual requirements before allocating test resources.

## Reference(s):

- [Risk signals and checklist](references/risk-signals.md)
- [ClawHub skill release](https://clawhub.ai/kokxi/skills/qa-risk-intuition)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Chinese-language Markdown report with risk matrix, prioritized areas, test-case tables, and mitigation suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk IDs and requirement links; risk scores and proposed testing depth should be reviewed before use.]

## Skill Version(s):

1.7.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
