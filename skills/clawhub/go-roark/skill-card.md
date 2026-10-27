## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill from Go projects to access Roark agents, calls, chats, transcripts, simulations, metrics, and project resources through the typed API client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials and call or transcript data may contain private information.

Mitigation: Read the key from ROARK_API_KEY, never hardcode or log it, and return only the data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, and changing project configuration can affect the Roark project.

Mitigation: Use a project-scoped key where possible and perform project-changing operations only when the user requested them.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [go-roark project](https://github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
