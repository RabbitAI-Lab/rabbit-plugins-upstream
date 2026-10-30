## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to maintain a GitLab agent profile with monthly contribution charts and supporting activity records. It guides scheduled updates across the last 12 completed calendar months.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chart generation may automatically download and run an undisclosed, unpinned software dependency.

Mitigation: Disable automatic npm downloads before enabling scheduled publishing, and use a reviewed renderer.

Risk: Published charts include totals for private and internal activity, even though identifying records are omitted.

Mitigation: Limit GitLab access to intended projects and review public assets, including private-activity totals, before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Static SVG and WebP contribution charts plus a JSON activity record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers completed calendar months; public records are listed, while private and internal activity is represented by anonymized monthly totals.]

## Skill Version(s):

1.123.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
