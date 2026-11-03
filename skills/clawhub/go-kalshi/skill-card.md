## Description:

Provides guidance and examples for using an unofficial, typed Go client to access Kalshi REST APIs and WebSocket streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Kalshi market data, account endpoints, and WebSocket streams into their applications. It provides installation and usage guidance, including signed requests and account-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked API private key or signed request headers could expose account access.

Mitigation: Read credentials from the user's environment or an explicitly supplied file; never hardcode, commit, log, or print them. Attach the signer only to Kalshi API clients.

Risk: Order, quote, transfer, and API key operations can change a real account.

Mitigation: Use the demo environment during development and perform real-account changes only when the user explicitly requests that exact action.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [Project homepage](https://github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and integration guidance; no files are produced by the library itself.]

## Skill Version(s):

0.8.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
