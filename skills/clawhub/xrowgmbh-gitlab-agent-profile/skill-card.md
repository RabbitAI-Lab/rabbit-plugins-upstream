## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to refresh a GitLab profile's contribution chart and proof records from configured GitLab projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab authentication to read configured project contribution data and generate profile proof records.

Mitigation: Use a GitLab token with the narrowest practical scope and install only when this access matches the intended profile maintenance workflow.

Risk: The routine can write SVG, WebP, and JSON assets and commit/push changed profile assets.

Mitigation: Review generated asset changes before publishing and confirm the target profile repository before enabling automated runs.

Risk: The bundled cron example is disabled, but its schedule is every 15 minutes if enabled.

Mitigation: Review the cron configuration before enabling it and adjust the cadence to the profile update requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with generated SVG, WebP, and JSON profile assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GitLab authentication and configured environment variables to update profile assets under assets/ by default.]

## Skill Version(s):

1.84.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
