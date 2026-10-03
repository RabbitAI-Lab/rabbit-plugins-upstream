## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab profile maintainers use this skill to update contribution charts and supporting records for a GitLab agent profile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab credentials expose all projects visible to the login or token, and published totals include private/internal activity.

Mitigation: Restrict project scope with GITLAB_AGENT_PROFILE_PROJECTS and review the generated JSON before publishing.

Risk: A recurring schedule can repeatedly collect and publish profile data.

Mitigation: Keep the cron disabled until intentionally enabled and review changes before pushing.

Risk: WebP conversion can fall back to runtime npm execution.

Mitigation: Install a trusted local image converter so the npm exec fallback is not used.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance and SVG, WebP, and JSON assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts cover completed calendar months; public records and private/internal monthly aggregates support the totals.]

## Skill Version(s):

1.97.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
