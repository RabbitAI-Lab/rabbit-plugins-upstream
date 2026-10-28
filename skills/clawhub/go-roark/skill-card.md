## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Roark's voice AI testing and monitoring API into Go projects. It guides authenticated access to agents, calls, chats, transcripts, metrics, simulations, and project resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Go client is unofficial; its dependency and behavior may differ from Roark-maintained tooling.

Mitigation: Review and pin the dependency before use.

Risk: Bearer credentials and calls, transcripts, or recordings may contain sensitive information.

Mitigation: Use a project-scoped key where possible, keep credentials and transcripts out of logs, and return only the data needed.

Risk: Creating or deleting resources, starting simulations, collecting metrics, or changing project configuration can affect a live project.

Mitigation: Perform these operations only when the user requested them.

## Reference(s):

- [Setup and API usage reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Go-Roark project page](https://github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples, shell commands, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for use in the calling Go project; API operations that change project resources require user authorization.]

## Skill Version(s):

0.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
