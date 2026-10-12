## Description:

Guides users through configuring a self-hosted aircraft monitor that polls ADS-B sources and alerts on selected aircraft near named locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Aircraft spotters and developers use this skill to set up location-based monitoring for emergency squawks, watchlisted aircraft, and low-flying planes, with alerts sent to Telegram or webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup runs an unpinned Docker image that handles location data and notification credentials.

Mitigation: Review the image and pin it to a trusted version or digest before installation.

Risk: The configuration contains Telegram tokens or webhook credentials.

Mitigation: Keep config.yaml private and mount it read-only.

Risk: Configured locations leave the host during polling, and matched aircraft data leaves it in alerts.

Mitigation: Use only ADS-B sources, Telegram chats, and webhook endpoints you control or trust.

## Reference(s):

- [planesnitch on ClawHub](https://clawhub.ai/psyb0t/skills/planesnitch)
- [planesnitch project documentation](https://github.com/psyb0t/docker-planesnitch)
- [Setup and configuration reference](references/setup.md)
- [plane-alert-db aircraft watchlists](https://github.com/sdr-enthusiasts/plane-alert-db)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with YAML and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for Docker deployment and configurable Telegram or webhook alerts.]

## Skill Version(s):

1.8.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
