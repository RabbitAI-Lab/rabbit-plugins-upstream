## Description:

Provides unofficial typed Go clients for Kalshi's REST and WebSocket APIs, plus request signing, for market data and account workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Kalshi market data and account APIs, including real-time streams and explicitly authorized account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live account operations can place or cancel orders, accept quotes, transfer funds, or change API keys.

Mitigation: Use the demo environment during development and perform real-account changes only when explicitly requested by the user.

Risk: Exposure of the private API key or signed request headers could compromise account access.

Mitigation: Load credentials from environment variables or a user-specified file, never hardcode, commit, or log them, and attach signing only to Kalshi API clients.

Risk: This is an unofficial dependency that may change independently of Kalshi.

Mitigation: Review the dependency and pin its version before using live credentials.

## Reference(s):

- [Setup and API usage](references/setup.md)
- [Go-Kalshi project homepage](https://github.com/psyb0t/go-kalshi)
- [Go-Kalshi package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to the requested integration; live account operations require explicit user authorization.]

## Skill Version(s):

0.2.1 (source: target release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
