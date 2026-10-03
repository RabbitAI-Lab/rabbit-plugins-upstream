## Description:

Reports current and historical Uptimely project health, including monitors, incidents, alerts, on-call coverage, and maintenance windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Service operators and developers use this read-only skill to check project uptime, identify active incidents and alerts, review monitor history, and see who is on call or whether maintenance is scheduled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to incidents, monitor history, alerts, and on-call schedules may expose sensitive operational information to the agent.

Mitigation: Confirm the requested project and OAuth scopes before connecting; grant only the access needed for the status check.

## Reference(s):

- [Uptimely: Checking Uptime Status on ClawHub](https://clawhub.ai/bsalaeddin/skills/uptimely-checking-uptime-status)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown status summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only findings based on accessible project data; times reported in the user's timezone.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
