## Description:

An unofficial Go client for accessing Kalshi's REST and WebSocket APIs for market data and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this client to read Kalshi market data, access account information, manage orders, and consume market or account updates over WebSockets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated operations use a private API key, which could be exposed if mishandled.

Mitigation: Read credentials from the user's environment or provided file; never hardcode, commit, or log private keys or signed request headers, and use the signer only with Kalshi API hosts.

Risk: Order, quote, transfer, and API key operations can change a real Kalshi account.

Mitigation: Use the demo environment during development and require an explicit user request for each account-changing action.

Risk: The downloaded Go dependency's implementation was outside the artifact security review.

Mitigation: Pin and review the dependency before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-kalshi)
- [Project homepage](https://github.com/psyb0t/go-kalshi)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Setup and reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed REST and WebSocket clients; requires the Go toolchain, and authenticated operations require Kalshi API credentials.]

## Skill Version(s):

0.8.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
