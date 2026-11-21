## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External Go developers use this skill to integrate the go-roark client into a Go project for Roark voice AI agent monitoring, testing, and project management. It helps select API operations and handle authentication and responses safely.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automated security verdict is benign, but two unresolved local references leave scan coverage incomplete.

Mitigation: Treat the scan as partial and review the unresolved references before relying on the skill.

Risk: Credentials and call, transcript, recording, or project data handled through the API may be exposed if logged or returned unnecessarily; write operations can affect the project.

Mitigation: Read the bearer key from ROARK_API_KEY, never hardcode or log it, return only needed data, and make changes or start jobs only when requested.

## Reference(s):

- [go-roark setup and reference](artifact/references/setup.md)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [go-roark project homepage](https://github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and concise Markdown guidance, with shell commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide edits to a Go project and API calls; protect credentials and return only necessary private data.]

## Skill Version(s):

0.21.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
