## Description:

Provides a typed Go client for accessing Roark's voice AI agent testing and monitoring API, including agents, calls, chats, simulations, metrics, webhooks, and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use the skill to write Go code that integrates with Roark for voice AI agent testing, monitoring, simulations, and project management. It is intended for Go projects using or adopting github.com/psyb0t/go-roark.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A bearer credential can expose Roark project data or authorize project changes.

Mitigation: Read ROARK_API_KEY from the environment; never hardcode, commit, log, or print it or an Authorization header. Perform project-changing operations only when requested.

Risk: Calls, transcripts, and recordings may contain private data.

Mitigation: Return only the data needed for the task.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project homepage](https://github.com/psyb0t/go-roark)
- [Roark API](https://api.roark.ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go source code and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.17.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
