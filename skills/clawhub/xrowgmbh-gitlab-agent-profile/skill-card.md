## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update GitLab profile assets with monthly contribution metrics, charts, and proof records from GitLab projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a GitLab token to update and push profile assets.

Mitigation: Use a dedicated least-privilege GitLab token, keep it out of logs, and review repository diffs before pushing changes.

Risk: Configurable output paths can write generated SVG, WebP, and JSON files outside the intended profile assets directory.

Mitigation: Keep output paths under the intended workspace assets directory and review path-related environment variables before execution.

Risk: The optional cron block can run recurring automation against GitLab projects.

Mitigation: Leave the cron disabled unless recurring updates are explicitly desired, and monitor scheduled runs when enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration]

**Output Format:** [Static SVG and WebP chart files, JSON proof records, and Markdown task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI authentication with GITLAB_TOKEN; output paths, project scope, owner, agent, and month count are configurable through environment variables.]

## Skill Version(s):

1.81.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
