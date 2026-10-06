## Description:

Maintains a GitLab agent profile page with monthly contribution statistics and a static performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GitLab project maintainers use this skill to track an agent's monthly contributions and update its public profile assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring agent runs can repeatedly access GitLab with the configured token.

Mitigation: Limit token permissions and the project list; leave the recurring schedule disabled unless needed.

Risk: Generated contribution records and charts may be published with incorrect or sensitive information.

Mitigation: Review records and totals before committing or pushing public profile assets.

Risk: A fallback converter may run through npm exec.

Mitigation: Use a pinned local converter instead of the npm exec fallback.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance; SVG and WebP charts and JSON contribution records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts summarize completed months; public records omit private project details.]

## Skill Version(s):

1.102.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
