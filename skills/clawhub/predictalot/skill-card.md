## Description:

Guides agents in using a self-hosted service for time-series forecasts, ensembles, and trained tabular predictions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to request time-series forecasts with intervals or sample paths, combine models, and train tabular predictors on their own features through a trusted predictalot server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Forecast and training data are sent to the configured server.

Mitigation: Use a server you trust, prefer HTTPS, and avoid sharing sensitive data with untrusted instances.

Risk: An exposed service may accept requests from unauthorized users.

Mitigation: Bind to localhost or protect external access with TLS or VPN and a strong bearer token.

Risk: A mutable Docker image tag may change between deployments.

Mitigation: Pin the image to a reviewed version or digest rather than using latest.

Risk: Deleting a stored tabular model is irreversible.

Mitigation: Confirm the model identifier from the server and obtain explicit user approval before deletion.

## Reference(s):

- [predictalot on ClawHub](https://clawhub.ai/psyb0t/skills/predictalot)
- [predictalot setup guide](references/setup.md)
- [predictalot project homepage (declared by skill)](https://github.com/psyb0t/docker-predictalot)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API requests]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Forecast responses may include quantile intervals, sample paths, or tabular predictions.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
