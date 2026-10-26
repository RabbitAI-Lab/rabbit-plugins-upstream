## Description:

Provides typed Go clients for Kalshi REST APIs, WebSocket streams, and API-key request signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to integrate Kalshi market data and account operations into Go projects, including REST requests and WebSocket streams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account operations such as orders, transfers, quote acceptance, and API-key changes can affect a real Kalshi account.

Mitigation: Use the demo environment during development and require explicit user authorization for each financial or API-key action.

Risk: Compromised or exposed API private keys could enable unauthorized account access.

Mitigation: Keep keys out of source control, logs, and hardcoded values; load them from protected environment variables or a user-provided path.

Risk: The security assessment does not certify downloaded dependency code.

Mitigation: Pin and review dependency versions before use.

## Reference(s):

- [go-kalshi documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Project homepage](https://github.com/psyb0t/go-kalshi)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code examples, shell commands, and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes guidance for private-key handling and explicit authorization of real-account actions.]

## Skill Version(s):

0.3.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
