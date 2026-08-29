## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to refresh GitLab profile assets with monthly contribution statistics, including merged merge requests, owner direct commits to main, contribution scores, and a JSON proof record.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated GitLab operations can update remote profile assets if the token has broad permissions.

Mitigation: Use a least-privilege GitLab token scoped to the intended profile repository and review commits before pushing.

Risk: The bootstrap routine can create recurring scheduled execution.

Mitigation: Review the cron entry before enabling it and keep it disabled unless recurring profile updates are intended.

Risk: Configurable output paths and image conversion tools can affect files or process paths outside the intended asset workflow.

Mitigation: Keep output paths inside the intended assets directory and avoid attacker-controlled paths for ImageMagick, npm sharp-cli, or fallback image conversion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [files, json, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated SVG, WebP, and JSON asset files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; default outputs are written under assets/.]

## Skill Version(s):

1.84.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
