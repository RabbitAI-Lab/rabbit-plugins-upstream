## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update a GitLab profile with monthly contribution charts and proof records for owner and agent activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read GitLab group data, including private and internal projects available to the configured token.

Mitigation: Use a least-privilege GitLab token scoped only to the intended group or projects.

Risk: Generated records may publish aggregate counts for private or internal activity.

Mitigation: Review the generated JSON proof file and chart before committing or publishing profile assets.

Risk: The bootstrap section describes recurring automation that can repeatedly update profile assets.

Mitigation: Keep the cron disabled unless automated profile updates are explicitly desired and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python helper scripts that produce SVG, WebP, and JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated profile records include public counted records and anonymized private or internal monthly totals.]

## Skill Version(s):

1.94.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
