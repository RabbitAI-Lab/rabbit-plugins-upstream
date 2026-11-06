## Description:

Provides an unofficial typed Go client for Kalshi REST, WebSocket, and authenticated account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add Kalshi market data, account operations, or streaming support to Go applications using the go-kalshi client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A private API key could be exposed through source control or logs.

Mitigation: Keep the key ID and private key in environment variables or a user-provided file; never hardcode, commit, or log them.

Risk: Account-changing operations can place or cancel orders, accept quotes, or move funds.

Mitigation: Use the demo environment during development and perform real-account changes only when the user explicitly requests that exact action.

Risk: Downloaded Go dependencies are outside the supplied security review.

Mitigation: Review and pin external Go dependencies before production use.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Project repository](https://github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup, REST and WebSocket usage, request signing, and error-handling guidance.]

## Skill Version(s):

0.9.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
