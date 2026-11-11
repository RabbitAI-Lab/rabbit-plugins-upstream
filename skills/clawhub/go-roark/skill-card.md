## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the Go Roark client to a Go project and look up typed operations for monitoring, testing, and managing Roark resources. It guides authentication, request and response handling, pagination, and care around actions that change project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because two references in the skill could not be resolved.

Mitigation: Review the unresolved references and installation guidance before relying on them.

Risk: Bearer credentials and calls, transcripts, recordings, or other project data may be exposed through code or output.

Mitigation: Read ROARK_API_KEY from the environment, never hardcode, commit, or log it, and return only the data needed for the task.

Risk: Some Roark API operations create or delete resources, start simulations, collect metrics, or change project configuration.

Mitigation: Use project-changing operations only when the user requested the action.

## Reference(s):

- [Setup and API usage guide](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project repository linked by the skill](https://github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions may use ROARK_API_KEY for authenticated API requests.]

## Skill Version(s):

0.14.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
