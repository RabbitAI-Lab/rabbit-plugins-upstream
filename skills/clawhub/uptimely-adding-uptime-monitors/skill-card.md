## Description:

Adds a confirmed uptime monitor to an Uptimely project without duplicating an existing monitor and can run an optional first check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and service operators use this skill to add an uptime monitor to a selected Uptimely project, avoid duplicate targets, and optionally check the new monitor once.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Uptimely through OAuth and creating monitors changes a selected project's configuration.

Mitigation: Review the connection permissions and confirm the project, target, and monitor creation before the write.

Risk: An optional first check sends a real request to the monitored URL.

Mitigation: Monitor only URLs you own or are responsible for, and run the first check only after separate confirmation.

## Reference(s):

- [Uptimely: Adding Uptime Monitors on ClawHub](https://clawhub.ai/bsalaeddin/skills/uptimely-adding-uptime-monitors)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the monitor configuration and, if requested, first-check status and response time.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
