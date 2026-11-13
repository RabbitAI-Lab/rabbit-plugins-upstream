## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab agent profile with monthly contribution charts and JSON records covering merged work and direct owner commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The WebP fallback may download and run an unpinned npm package, and the workflow uses GitLab credentials.

Mitigation: Check whether the npm fallback is permitted in the environment, and limit GITLAB_TOKEN to the GitLab access needed for the selected projects.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, SVG, WebP, JSON]

**Output Format:** [Static SVG and WebP charts plus JSON contribution records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Charts cover the last 12 completed calendar months by default; public records are listed individually, while private activity is summarized by month and category.]

## Skill Version(s):

1.141.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
