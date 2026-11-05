## Description:

Guides Go developers in using the unofficial go-kalshi client for Kalshi REST APIs, WebSocket streams, and authenticated account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Kalshi market data, account operations, and WebSocket streams into Go projects, including setup, authentication, and safe handling of real-account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private key material could be exposed through source control or logs.

Mitigation: Load keys from environment variables or a user-provided file, and never hardcode, commit, or log them.

Risk: Order and account-management actions can affect a real Kalshi account.

Mitigation: Prefer the demo environment during development and perform each real-account change only when the user explicitly requests that action.

Risk: The external Go dependency was not included in this review.

Mitigation: Review and pin the dependency before production use.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go snippets and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use user-supplied credentials and a selected demo or production environment.]

## Skill Version(s):

0.9.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
