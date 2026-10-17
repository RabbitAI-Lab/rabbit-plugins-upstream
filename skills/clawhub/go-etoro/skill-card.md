## Description:

Guides Go developers in using unofficial typed REST and WebSocket clients for eToro account and market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate the unofficial Go clients with eToro REST endpoints and live WebSocket streams for account, portfolio, and market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: eToro account credentials could be exposed in code, logs, or requests to another host.

Mitigation: Read keys from environment variables, never log them, and send authenticated requests only to public-api.etoro.com or ws.etoro.com/ws.

Risk: Transfers and public-content actions can move money or publish on the user's behalf.

Mitigation: Default to read-only operations and perform transfers, posts, or other public-content actions only when explicitly requested.

## Reference(s):

- [Setup and API usage reference](references/setup.md)
- [go-etoro project homepage](https://github.com/psyb0t/go-etoro)
- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go-specific guidance for REST requests and WebSocket subscriptions.]

## Skill Version(s):

0.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
