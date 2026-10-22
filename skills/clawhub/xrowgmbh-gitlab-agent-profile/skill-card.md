## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to maintain a GitLab agent profile with monthly contribution charts and a JSON record of counted activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An undocumented fallback may download and run additional software with access to the agent’s credentials.

Mitigation: Provision a reviewed image converter or replace the automatic npm fallback with a pinned setup-time dependency. Confirm the GitLab account, project scope, output repository, and publication of private activity totals before running; review the recurring job before enabling it.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [Publisher profile: xrowgmbh](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Files, SVG, WebP, JSON]

**Output Format:** [SVG and WebP contribution charts plus a JSON activity proof file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers the last 12 completed calendar months by default; private/internal activity is represented only as anonymized monthly totals.]

## Skill Version(s):

1.117.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
