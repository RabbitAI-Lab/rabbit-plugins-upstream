## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use this skill to publish monthly contribution charts and supporting records for an agent profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring runs may publish incorrect profile changes to GitLab.

Mitigation: Review the generated assets and repository diff before enabling the schedule or pushing changes.

Risk: GitLab credentials and broad project access may expose more data than intended.

Mitigation: Restrict token permissions and explicitly set project and output paths before running.

Risk: A fallback WebP converter may run an unpinned npm package.

Mitigation: Use a trusted preinstalled converter or remove the npm fallback.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands]

**Output Format:** [SVG and WebP charts with JSON proof records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows completed calendar months; public records and anonymized private monthly totals.]

## Skill Version(s):

1.96.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
