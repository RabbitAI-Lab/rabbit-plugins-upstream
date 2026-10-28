## Description:

Provides Go developers with an unofficial typed client for Kalshi REST and WebSocket APIs, including request signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

External developers use this skill to build Go applications that read Kalshi market data, manage account operations, or stream market and account updates through REST and WebSocket APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order, quote, transfer, and API-key operations can change a real Kalshi account.

Mitigation: Use the demo environment while developing and perform a live account-changing action only when the user explicitly requested that action.

Risk: The client signs requests with a private API key.

Mitigation: Read credentials from an environment variable or user-provided file; never hardcode, commit, or log the key or signed request headers.

Risk: The client is unofficial and maintained outside Kalshi.

Mitigation: Review and pin the dependency before using it.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Project homepage](https://github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration guidance]

**Output Format:** [Go code and concise Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST and WebSocket integration; live account-changing actions require explicit authorization.]

## Skill Version(s):

0.5.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
