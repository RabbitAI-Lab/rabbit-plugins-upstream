## Description:

Provides Go guidance for using an unofficial Kalshi client to query markets, manage accounts, and stream market updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Kalshi's REST and WebSocket APIs through the unofficial go-kalshi client. It guides market data queries, account operations, request signing, and streaming updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposure of a Kalshi private key could enable unauthorized account access.

Mitigation: Keep credentials in environment variables or a user-specified file; do not hardcode, commit, log, or print signed request headers.

Risk: Account-changing operations can place or cancel orders, accept quotes, move funds, or change API keys.

Mitigation: Use the demo environment during development and require explicit authorization for each real-account change. Public market queries do not need a signer.

Risk: The Go client is unofficial and may change or behave differently from expectations.

Mitigation: Review and pin the dependency before using it with production credentials.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-kalshi package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Source repository](https://github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
