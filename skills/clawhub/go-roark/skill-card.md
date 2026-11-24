## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API, with typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects using a bearer key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External Go developers use the client to access Roark agents, calls, chats, transcripts, simulations, metrics and other project resources. It provides typed API methods and setup guidance for integrating those operations into Go projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete because two referenced paths were unavailable to scanners.

Mitigation: Review those paths in the release source before relying on guidance that depends on them.

Risk: Roark credentials and calls, transcripts or recordings may contain private data.

Mitigation: Read credentials from ROARK_API_KEY, never log or commit them, and return only the data needed for the task.

Risk: Creating or deleting resources, starting simulations, collecting metrics, changing configuration or promoting revisions can affect a Roark project.

Mitigation: Perform these operations only when the user requested the action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project homepage](https://github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration, Guidance]

**Output Format:** [Go code and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The client uses a bearer key supplied through ROARK_API_KEY.]

## Skill Version(s):

0.22.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
