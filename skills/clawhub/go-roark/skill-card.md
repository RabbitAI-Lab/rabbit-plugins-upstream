## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that accesses Roark's voice AI testing and monitoring API, including agents, calls, transcripts, chats, simulations, metrics, and projects. It guides dependency setup, authentication, operation selection, and safe handling of project-changing requests and private data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client is unofficial and may change independently of Roark.

Mitigation: Review and pin the dependency version before use.

Risk: Bearer credentials and calls, transcripts, or recordings may expose private data.

Mitigation: Keep ROARK_API_KEY out of source control and logs, prefer a project-scoped key, and return only data needed for the task.

Risk: Writes, simulations, metric collection, and configuration changes can affect a Roark project.

Mitigation: Run project-changing operations only when the user has requested them.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project homepage](https://github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and operation guidance for the Go client; outputs should avoid exposing credentials or unnecessary private API data.]

## Skill Version(s):

0.6.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
