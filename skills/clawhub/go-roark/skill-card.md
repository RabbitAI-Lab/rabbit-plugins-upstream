## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using Go can add typed Roark API access to a project for agent, call, chat, transcript, simulation, metric, and project workflows. The skill provides integration guidance and Go examples for the unofficial client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Roark credentials and call or transcript data may be private.

Mitigation: Use a project-scoped API key, keep credentials out of source and logs, and return only the data needed for the task.

Risk: Writes, simulations, metric collection, and configuration changes can affect the Roark project.

Mitigation: Explicitly authorize live API actions before calling operations that create, delete, run, or change project resources.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-roark source repository](https://github.com/psyb0t/go-roark)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.11.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
