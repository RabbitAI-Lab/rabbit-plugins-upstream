## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill when writing Go applications that need to call Roark's voice AI testing and monitoring API. It guides setup and use of the unofficial typed client for API resources such as agents, calls, transcripts, simulations, and metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials and private calls, transcripts, or recordings may be exposed.

Mitigation: Use a project-scoped key where possible, read credentials from ROARK_API_KEY, never hardcode or log them, and return only necessary private data.

Risk: Resource changes, simulation runs, metrics collection, and configuration changes affect the Roark project.

Mitigation: Perform these actions only when the user explicitly requests them.

Risk: The client is unofficial and its dependency may change.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go-Roark source and project documentation](https://github.com/psyb0t/go-roark)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Roark API](https://api.roark.ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, API calls]

**Output Format:** [Go code and concise Markdown setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use bearer authentication; avoid exposing credentials or unnecessary private call data.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
