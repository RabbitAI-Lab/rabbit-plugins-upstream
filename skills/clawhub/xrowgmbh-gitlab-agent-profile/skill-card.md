## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update a GitLab agent profile with monthly contribution charts and a JSON record of public contributions plus anonymized private totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates the skill suspicious because its chart-generation fallback can download and run an unpinned package; five local references could not be resolved, leaving scan evidence incomplete.

Mitigation: Review the skill instructions and fallback behavior before installing, and resolve and inspect the unavailable references.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [SVG chart files, WebP chart files, JSON contribution records]

**Output Format:** [SVG, WebP and JSON files]

**Output Parameters:** [Monthly contribution statistics for completed calendar months]

**Other Properties Related to Output:** [Public counted records and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.147.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
