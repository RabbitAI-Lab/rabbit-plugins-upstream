## Description:

Guidance for using the unofficial Go client to access Roark's voice AI testing and monitoring API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to connect projects to Roark, inspect calls and transcripts, and manage Roark resources or run simulations when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials and calls, transcripts, or recordings may contain private information.

Mitigation: Read the key from ROARK_API_KEY, never hardcode, commit, or log it, prefer a project-scoped read-only key when possible, and return only the data needed.

Risk: Resource changes, simulation runs, metric collection, and configuration changes can affect a Roark project.

Mitigation: Perform these operations only when the user requested them.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project repository](https://github.com/psyb0t/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated API operations; return only task-relevant data.]

## Skill Version(s):

0.4.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
