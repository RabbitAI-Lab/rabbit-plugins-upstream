## Description:

Provides unofficial, typed Go clients for Kalshi's Trade API and WebSocket feeds, with request signing for authenticated access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Kalshi market data and account workflows into Go applications through typed REST and WebSocket clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of a Kalshi API private key or signed request headers could compromise account access.

Mitigation: Read credentials from environment variables or a user-specified file; never hardcode, commit, log, or print private keys or signed headers.

Risk: Order, quote, transfer, cancellation, and API key operations can affect a real account.

Mitigation: Use the demo environment while developing and perform real-account actions only when the user explicitly requests that exact action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Project repository](https://github.com/psyb0t/go-kalshi)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code with setup guidance and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed REST and WebSocket clients, with optional authenticated access.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
