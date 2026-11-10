## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab project owners use this skill to maintain a profile page with monthly contribution charts and a public proof file, including anonymized totals for private activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the skill suspicious because an update script can fetch and run an unpinned npm package; the scan is partial and does not cover all referenced paths.

Mitigation: Review the skill's tool access and the package it may download before running the update routine, and account for the GitLab credentials and files available to that process. Review the paths not covered by the partial scan.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance, Shell commands]

**Output Format:** [SVG and WebP charts, a JSON proof file, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The proof file contains public counted records and anonymized monthly totals for private or internal activity.]

## Skill Version(s):

1.135.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
