## Description:

Provides unofficial, typed Go clients for Kalshi Trade API REST endpoints, market data and perps WebSockets, and API-key request signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Kalshi REST endpoints and WebSocket streams into a project, including authenticated account operations and market data streaming.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed API private keys can compromise a Kalshi account.

Mitigation: Read keys from environment variables or a user-provided file; do not hardcode, commit, or log them, and do not print signed request headers.

Risk: Order placement, cancellation, transfers, quote acceptance, and API key changes affect a real account.

Mitigation: Perform these actions only when the user requested the exact action, and prefer the demo environment during development.

Risk: The security assessment has incomplete evidence because two local references could not be resolved.

Mitigation: Review the unresolved references before installing the skill.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-kalshi)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, API integration guidance]

**Output Format:** [Markdown guidance with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST, WebSocket, and API key signing.]

## Skill Version(s):

0.11.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
