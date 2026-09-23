## Description:

Report helps an agent configure and manage user-defined recurring reports with schedules, local report files, formatting, and user-configured delivery channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to define data sources, schedules, output formats, and delivery channels for recurring reports managed by an AI agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External delivery channels such as Telegram, webhook, or email can send report contents off-device.

Mitigation: Review and explicitly configure each destination before use; choose local file delivery when report contents should stay on device.

Risk: Report configurations may reference API-backed data sources that require credentials.

Mitigation: Store only environment-variable names in report configs and keep secret values in the user's environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/report)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown instructions with YAML configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report content may be delivered locally or through user-configured external channels.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
