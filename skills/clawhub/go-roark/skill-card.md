## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use the skill to add typed Roark API access to an existing Go project, including agent management, call and chat monitoring, simulations, and metrics. It guides setup, operation selection, authentication, and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rated the skill benign with medium confidence, but its analysis was partial because two references could not be resolved.

Mitigation: Review the unresolved references and current package documentation before relying on the guidance.

Risk: Bearer credentials and calls, transcripts, or recordings may contain sensitive information.

Mitigation: Read the key from ROARK_API_KEY, never hardcode, commit, or log it, and return only the data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, changing configuration, and promoting revisions affect the Roark project.

Mitigation: Perform project-changing operations only when the user has requested them.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project homepage](https://github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may use bearer authentication; keep credentials private and request authorization before project-changing operations.]

## Skill Version(s):

0.19.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
