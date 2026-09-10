## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab profile repository updated with monthly contribution charts and proof records for completed calendar months.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab authentication to enumerate accessible projects and update profile assets.

Mitigation: Scope the GitLab token, root group, and project list as narrowly as possible, and review generated assets before committing or pushing them.

Risk: The bootstrap includes a recurring cron configuration that could run unattended if enabled.

Mitigation: Leave the cron disabled or remove it unless recurring unattended profile updates are explicitly intended.

Risk: WebP conversion may run an unpinned npm package when ImageMagick is unavailable.

Mitigation: Preinstall and pin a trusted conversion dependency, or use ImageMagick or vetted Python packages instead.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance plus generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab authentication and configurable environment variables to select projects, users, month range, workspace, and output paths.]

## Skill Version(s):

1.91.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
