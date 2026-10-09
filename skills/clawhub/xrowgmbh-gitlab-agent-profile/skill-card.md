## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to update a GitLab agent profile with monthly contribution charts and supporting records from accessible projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access can scan all accessible projects in the configured GitLab group, including private activity.

Mitigation: Use scoped GitLab credentials and review the group and project settings before running.

Risk: Publishing generated assets may disclose contribution totals and public project records.

Mitigation: Review the charts and proof records before committing or pushing them.

Risk: Bootstrap can enable recurring updates, and chart generation can invoke additional local conversion tools.

Mitigation: Leave the bootstrap schedule disabled unless needed; review available local tools and keep output paths within the intended workspace.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the update can produce SVG and WebP charts and JSON proof records.]

## Skill Version(s):

1.109.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
