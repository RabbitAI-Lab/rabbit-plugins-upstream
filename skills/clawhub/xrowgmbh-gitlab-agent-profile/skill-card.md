## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update a GitLab agent profile with monthly contribution charts and supporting activity records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab credentials can expose project activity beyond the intended profile scope.

Mitigation: Use a GitLab token limited to the intended group and profile workflow; set explicit project paths.

Risk: Generated profile records or charts may publish unintended information or incorrect totals.

Mitigation: Set explicit output paths and inspect the generated JSON and charts before publishing.

Risk: Recurring automation can commit and publish profile changes without another manual run.

Mitigation: Enable the cron only when recurring automated commits are desired.

## Reference(s):

- [GitLab Agent Profile release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, Guidance]

**Output Format:** [SVG and WebP charts, JSON proof records, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Monthly totals cover completed calendar months; private activity is aggregated in public records.]

## Skill Version(s):

1.111.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
