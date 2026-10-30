## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that accesses Roark for voice agent monitoring, testing, and project management, including running simulations when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials, calls, transcripts, and recordings may contain private information.

Mitigation: Use a least-privilege project-scoped key, read it from ROARK_API_KEY, never hardcode, commit, or log it, and return only data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, and changing project configuration can affect a live project.

Mitigation: Perform these actions only when the user requested them; otherwise use read-only operations or compile and test without live API requests.

Risk: The Go client is unofficial and its downloaded implementation is outside the scope of the bundled-instructions security review.

Mitigation: Review and pin the dependency version before use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Go client repository](https://github.com/psyb0t/go-roark)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-roark)
- [Roark API](https://api.roark.ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go 1.26.10 or newer and a ROARK_API_KEY are required.]

## Skill Version(s):

0.5.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
