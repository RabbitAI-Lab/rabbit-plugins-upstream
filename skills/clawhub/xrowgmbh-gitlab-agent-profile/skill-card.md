## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use this skill to summarize completed-month contributions, update profile charts and proof records, and publish changed assets after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad GitLab access may expose more projects than intended.

Mitigation: Use a least-privilege token and set an explicit project list where possible.

Risk: Publishing charts and proof records may reveal derived activity data.

Mitigation: Inspect generated records, project coverage, and totals before pushing assets.

Risk: Recurring runs may publish updates without active review.

Mitigation: Keep the recurring schedule disabled unless unattended publication is intended.

Risk: The optional WebP conversion fallback can fetch an unpinned package.

Mitigation: Avoid the npm sharp-cli fallback unless dependencies are pinned in a controlled environment.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [SVG and WebP charts, JSON proof records, and text update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Completed-month statistics; private and internal activity appears only as aggregate totals.]

## Skill Version(s):

1.110.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
