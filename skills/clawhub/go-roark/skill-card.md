## Description:

An unofficial, typed Go client for the Roark voice AI testing and monitoring API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add the unofficial go-roark client to a project and access Roark agents, calls, chats, transcripts, simulations, metrics, and project resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer credentials and call data, transcripts, or recordings may expose private information.

Mitigation: Use a project-scoped key with only needed permissions, read the key from ROARK_API_KEY, never log it, and return only data needed for the task.

Risk: Resource changes, simulations, metric collection, and configuration updates can affect a Roark project.

Mitigation: Run these actions only when requested and state the requested change or simulation clearly.

Risk: The client is unofficial and depends on a downloaded Go module.

Mitigation: Pin and review the dependency before using it.

## Reference(s):

- [Setup and API usage reference](artifact/references/setup.md)
- [Project repository homepage](https://github.com/psyb0t/go-roark)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Roark API endpoint](https://api.roark.ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Go client setup, API request examples, and response handling guidance.]

## Skill Version(s):

0.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
