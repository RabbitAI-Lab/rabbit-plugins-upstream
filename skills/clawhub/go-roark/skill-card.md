## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API, with typed methods for agents, calls, chats, simulations, metrics, webhooks, and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill in Go projects to integrate with Roark for voice agent testing, monitoring, and project management. It provides setup and API usage guidance for the go-roark client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Two unresolved local references leave part of the security review incomplete.

Mitigation: Review the skill source and resolve the referenced material before installation.

Risk: The bearer credential and Roark calls, transcripts, recordings, and project data may be sensitive.

Mitigation: Read credentials from ROARK_API_KEY, never log or commit them, and return only the data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, changing configuration, or promoting revisions can affect a Roark project.

Mitigation: Perform these operations only when the user requested the action.

## Reference(s):

- [Setup and API usage reference](artifact/references/setup.md)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [go-roark project page](https://github.com/psyb0t/go-roark)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the ROARK_API_KEY environment variable; operations may read or change Roark project data.]

## Skill Version(s):

0.16.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
