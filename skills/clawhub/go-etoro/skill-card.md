## Description:

Provides setup and Go integration guidance for the unofficial typed eToro REST and WebSocket clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the unofficial go-etoro client into existing projects, make typed eToro REST requests, and consume market or account updates over WebSockets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The integration uses API keys and sends authenticated requests to an external service.

Mitigation: Load both keys from environment variables, never hardcode, commit, or log them, and send them only to the documented eToro hosts.

Risk: Some documented API operations can transfer money or publish or modify public content.

Mitigation: Default to read-only operations and perform a money-moving or content-changing action only when the user explicitly requests that exact action.

## Reference(s):

- [Setup and API usage notes](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-etoro)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup and integration examples; the library itself does not read or write project files.]

## Skill Version(s):

0.4.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
