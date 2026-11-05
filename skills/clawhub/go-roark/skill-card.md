## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that accesses Roark agents, calls, chats, transcripts, metrics, simulations, and project resources through the unofficial go-roark client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live API operations can create or delete resources, start simulations, collect metrics, or change project configuration.

Mitigation: Run these operations only when the user explicitly requests them, and use a project-scoped key where possible.

Risk: Bearer credentials and call, transcript, or recording data may be sensitive.

Mitigation: Read the key from ROARK_API_KEY, never hardcode, commit, or log it, and return only the data needed for the task.

Risk: The security assessment covers the bundled instruction files, not the downloaded client or linked repository files.

Mitigation: Review and pin the unofficial dependency before use.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Module homepage](https://github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the caller's Go project and Roark API credentials.]

## Skill Version(s):

0.9.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
