## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add and call the unofficial Go client for Roark APIs, including operations for agents, calls, transcripts, simulations, metrics, and project resources. It guides installation, authentication, response handling, pagination, and safe use of project-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials and call, transcript, recording, or other project data may be exposed while using the API.

Mitigation: Use a project-scoped key, read it from ROARK_API_KEY, never hardcode, commit, or log it, and return only the data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, or changing project configuration can affect the user's Roark project.

Mitigation: Perform project-changing operations only when the user requested them.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-roark on GitHub](https://github.com/psyb0t/go-roark)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions and examples for integrating the Go client; no live API calls are made by the skill itself.]

## Skill Version(s):

0.7.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
