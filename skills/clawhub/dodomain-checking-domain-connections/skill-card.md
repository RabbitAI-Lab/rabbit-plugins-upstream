## Description:

Reviews existing doDomain connections for DNS health and queues user-confirmed rechecks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Team members use this skill to review custom-domain connection health across doDomain apps, identify broken connections, and request a DNS recheck for a selected connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access team domain-connection data through doDomain.

Mitigation: Review the connector's OAuth scopes before granting access.

Risk: A queued DNS recheck may be mistaken for a successful verification.

Mitigation: Confirm the target connection before queuing one recheck, and check its status later before reporting a result.

## Reference(s):

- [doDomain: Checking Domain Connections on ClawHub](https://clawhub.ai/bsalaeddin/skills/dodomain-checking-domain-connections)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports connection status, DNS provider and check times; a queued recheck is not a verification result.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
