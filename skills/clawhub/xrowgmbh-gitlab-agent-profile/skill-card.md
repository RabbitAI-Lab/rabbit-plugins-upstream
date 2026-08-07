## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep a GitLab profile repository updated with monthly contribution charts and proof records for owner and agent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can repeatedly update and publish GitLab profile assets.

Mitigation: Keep the cron disabled unless recurring updates are intentional, and review generated diffs before pushing changes.

Risk: The skill uses GitLab API access through GITLAB_TOKEN.

Mitigation: Use a dedicated GitLab profile repository and a least-privilege token.

Risk: Output environment variables can point generated assets outside the intended profile assets directory.

Mitigation: Keep chart, WebP, and records output variables pointed at the repository assets directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown instructions for running a Python helper that updates SVG, WebP, and JSON profile assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; output paths and GitLab project selection are controlled by environment variables.]

## Skill Version(s):

1.79.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
