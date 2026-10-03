## Description:

Guides Uptimely incident and alert response, including declarations, state changes, and on-demand monitor checks, one confirmed action at a time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Incident responders and operations teams use this skill to investigate Uptimely incidents and alerts, confirm individual response actions, and check monitored services on demand.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident and alert changes can notify responders or subscribers and change a public status page.

Mitigation: Review the project, target, action, and notification or status-page effects; explicitly approve each action separately.

Risk: On-demand monitor checks make real requests to monitored URLs.

Mitigation: Confirm the intended monitor before running a check and review the returned status.

Risk: Incident and alert text can become visible to responders or the public.

Mitigation: Keep incident and alert text factual and free of secrets.

## Reference(s):

- [Uptimely: Responding To Incidents on ClawHub](https://clawhub.ai/bsalaeddin/skills/uptimely-responding-to-incidents)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports action results, incident or alert state, and monitor-check outcomes.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
