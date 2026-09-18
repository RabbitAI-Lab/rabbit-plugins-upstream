## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to update GitLab profile assets that summarize completed monthly merge request, direct commit, and contribution score activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read private/internal GitLab activity and publish derived profile assets through recurring automation.

Mitigation: Review the configured root group, project list, token scope, and output repository before installation; require review before pushing generated assets when private/internal aggregates should not be published.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands and generated SVG, WebP, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces static profile chart assets and a JSON proof file when executed with GitLab CLI access.]

## Skill Version(s):

1.91.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
