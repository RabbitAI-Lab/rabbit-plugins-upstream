## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update an agent's GitLab profile with monthly contribution charts and public proof records, including anonymized monthly totals for private activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A retained legacy updater can automatically download and run additional software with GitLab access.

Mitigation: Avoid running the legacy Python updater until its automatic npm fallback is removed or replaced with a reviewed, pinned renderer.

Risk: Published contribution charts and records can include aggregates derived from private or internal activity.

Mitigation: Confirm the target group and profile repository, and that publishing anonymized private activity totals is acceptable.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile on ClawHub](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [SVG charts, WebP images, JSON records]

**Output Format:** [Static SVG and WebP charts with JSON contribution records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers the last 12 completed calendar months by default; private and internal activity is published only as anonymized monthly totals.]

## Skill Version(s):

1.128.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
