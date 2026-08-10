## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to keep GitLab profile assets current with monthly contribution statistics, including generated chart images and proof records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run recurring unattended updates that use GitLab access to commit and push generated profile assets.

Mitigation: Keep the bundled cron disabled unless unattended updates are intentional, and review generated assets before pushing.

Risk: A broadly scoped GitLab token could expose more repository access than the profile update workflow needs.

Mitigation: Use a minimally scoped GitLab token dedicated to this profile-maintenance workflow.

Risk: Configurable output paths could write generated files outside the intended profile repository assets directory.

Mitigation: Keep output paths inside the intended assets directory and review path-related environment variables before running.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and configuration details for generating SVG, WebP, and JSON profile assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, python3, and GITLAB_TOKEN; generated assets should be reviewed before committing or pushing.]

## Skill Version(s):

1.81.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
