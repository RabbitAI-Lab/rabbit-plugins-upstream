## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that integrates with Roark for project access, call and chat monitoring, transcripts, simulations, metrics, and resource management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because two local references could not be resolved.

Mitigation: Resolve and review those references before relying on the benign assessment.

Risk: Bearer credentials and call, transcript, recording, or project data may be exposed through generated code or output.

Mitigation: Read credentials from ROARK_API_KEY, never hardcode, commit, or log them, and return only data needed for the task.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Go module repository](https://github.com/psyb0t/go-roark)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.13.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
