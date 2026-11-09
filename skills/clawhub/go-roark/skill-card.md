## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that integrates with Roark for voice agent monitoring, testing, and project management. It guides installation, authentication, endpoint selection, and safe handling of responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because two references could not be resolved.

Mitigation: Review the unresolved references and assess their contents before relying on the skill in a release.

Risk: Roark credentials and call, transcript, or recording data may be sensitive.

Mitigation: Read the bearer key from ROARK_API_KEY, never hardcode or log it, and return only data needed for the task.

Risk: Some API operations can change project resources, run simulations, collect metrics, or alter configuration.

Mitigation: Perform these operations only when the user requested the change.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-roark GitHub repository](https://github.com/psyb0t/go-roark)
- [go-roark Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific integration guidance; no fixed token cap.]

## Skill Version(s):

0.12.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
