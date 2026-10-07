## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab maintainers use this skill to update an agent's profile charts and contribution records across a GitLab group, then review and publish changed assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitLab access can expose private or internal group activity.

Mitigation: Use the narrowest GitLab token and group scope possible; review generated JSON before publishing.

Risk: The WebP converter fallback can run an unpinned npm package.

Mitigation: Preinstall a trusted converter or review and remove the npm fallback before use.

Risk: Enabling the scheduled task permits periodic unattended GitLab access and asset updates.

Mitigation: Leave the cron disabled unless periodic unattended runs are intended.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [Markdown instructions and SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts cover completed months; public records and anonymized private/internal monthly totals support review before publication.]

## Skill Version(s):

1.105.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
