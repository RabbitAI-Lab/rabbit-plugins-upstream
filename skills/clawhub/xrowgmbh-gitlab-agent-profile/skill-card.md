## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to update GitLab agent profile assets with completed-month contribution statistics, charts, and public proof records while summarizing private or internal activity without exposing project details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can be configured for recurring agent execution, which may repeatedly update and publish profile assets.

Mitigation: Keep the cron disabled unless automated updates are intended, and review generated assets before committing or pushing them.

Risk: GitLab API access depends on GITLAB_TOKEN and can reach private or internal project metadata available to that token.

Mitigation: Use a least-privilege GitLab token and set GITLAB_AGENT_PROFILE_PROJECTS to an explicit project list when broad group discovery is not needed.

Risk: Image conversion may fall back to an unpinned npm sharp-cli execution when local converters are unavailable.

Mitigation: Prefer preinstalled and pinned ImageMagick or Python image conversion dependencies in the execution environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)
- [ClawHub publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command guidance and generated SVG, WebP, and JSON profile assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GitLab CLI authentication through GITLAB_TOKEN and Python 3; optional image conversion uses ImageMagick, npm sharp-cli, or Python image packages.]

## Skill Version(s):

1.90.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
