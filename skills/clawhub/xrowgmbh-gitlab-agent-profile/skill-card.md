## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab maintainers use this skill to collect monthly contribution statistics and maintain a profile chart with public proof records and anonymized private activity totals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WebP fallback can silently fetch and run an unpinned npm package with access to inherited credentials and files.

Mitigation: Review the suspicious verdict before installation, inspect and pin the fallback package, and limit the credentials and filesystem access available during execution.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Charts, JSON]

**Output Format:** [SVG and WebP charts with JSON proof records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly statistics for completed calendar months (12 by default); public records and anonymized monthly totals for private activity.]

## Skill Version(s):

1.144.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
