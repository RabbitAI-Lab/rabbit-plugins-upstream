## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers maintaining a GitLab agent profile can use this skill to summarize monthly merge request and direct commit activity in static charts and a supporting JSON record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The legacy renderer may automatically download and run extra software while GitLab credentials are available.

Mitigation: Prefer a preinstalled renderer and remove automatic package fetching.

Risk: Scheduled publishing depends on a separately supplied production plugin.

Mitigation: Verify the production plugin before enabling scheduled publishing.

Risk: The public output includes aggregated activity from private and internal projects.

Mitigation: Restrict GitLab access to intended projects, confirm the destination repository, and review generated assets before publishing.

## Reference(s):

- [GitLab Agent Profile release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile: xrowgmbh](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, SVG charts, WebP charts, JSON records, Guidance]

**Output Format:** [SVG and WebP charts, a JSON proof file, and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly contribution totals and categories for the last 12 completed months; public records and anonymized private activity totals.]

## Skill Version(s):

1.130.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
