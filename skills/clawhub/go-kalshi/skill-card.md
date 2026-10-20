## Description:

Guides Go developers in using an unofficial Kalshi client to read market data, stream updates, and work with account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Kalshi market data, account operations, and live streams into Go applications with an unofficial client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kalshi API keys or signed headers could be exposed in source control or logs.

Mitigation: Keep keys out of code and logs, and never print signed request headers.

Risk: Order, transfer, or account-management calls can change a real financial account.

Mitigation: Use demo endpoints during development and confirm the user's exact requested action before changing a live account.

## Reference(s):

- [ClawHub go-kalshi release](https://clawhub.ai/psyb0t/skills/go-kalshi)
- [Setup reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples may cover REST calls, WebSocket streams, and request signing.]

## Skill Version(s):

0.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
