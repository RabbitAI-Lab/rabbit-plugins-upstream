## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go code that connects applications to Roark for agent, call, chat, transcript, simulation, metrics, and project workflows. It guides installation, authentication, choosing generated operations, and checking API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer keys, calls, transcripts, and recordings may contain private information.

Mitigation: Use a project-scoped key where possible, keep credentials in ROARK_API_KEY, never hardcode, commit, or log them, and return only data needed for the task.

Risk: The unofficial downloaded library is outside this artifact review.

Mitigation: Review and pin the library version before using sensitive credentials.

Risk: Resource changes, simulations, metrics collection, configuration changes, and revision promotion can affect the selected project.

Mitigation: Select the intended project explicitly and request confirmation from the user before performing those actions unless the user has already requested them.

## Reference(s):

- [Setup and API usage guide](references/setup.md)
- [go-roark source repository](https://github.com/psyb0t/go-roark)
- [go-roark package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use the ROARK_API_KEY environment variable for bearer authentication.]

## Skill Version(s):

0.8.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
