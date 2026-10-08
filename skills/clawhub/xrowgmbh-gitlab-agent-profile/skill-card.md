## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use this skill to track monthly owner and agent contributions across selected projects and update the agent's public profile charts and proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitLab access could expose more project activity than intended.

Mitigation: Use a minimally scoped token and restrict the root group or project list.

Risk: Published charts and proof records include aggregate private or internal activity.

Mitigation: Review generated assets and totals for disclosure before pushing profile changes.

Risk: Scheduled runs may repeatedly update and push profile assets without supervision.

Mitigation: Keep the cron disabled unless recurring unattended updates are explicitly wanted.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown instructions; SVG and WebP charts; JSON proof records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts cover completed calendar months; private and internal contributions appear as aggregate totals without identifying project details.]

## Skill Version(s):

1.106.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
