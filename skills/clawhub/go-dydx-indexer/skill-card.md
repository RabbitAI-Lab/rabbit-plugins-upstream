## Description:

Provides a typed Go client for reading data from the dYdX v4 Indexer HTTP API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

AGPL-3.0-only

## Use Case:

Go developers use this skill to add the unofficial dYdX v4 Indexer client to applications that need market or account data. It guides endpoint selection, typed response handling, and mainnet or testnet configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some POST endpoints, including token registration, Turnkey sign-in, and affiliate code updates, act on the caller's identity.

Mitigation: Use these endpoints only when the user has requested the corresponding action.

Risk: Requests can send wallet addresses supplied by the user to the configured indexer.

Mitigation: Send user-provided addresses only to the indexer selected for the requested task.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [GitHub repository](https://github.com/psyb0t/go-dydx-indexer)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-dydx-indexer)
- [dYdX Indexer mainnet API](https://indexer.dydx.trade/v4)
- [dYdX Indexer testnet API](https://indexer.v4testnet.dydx.exchange/v4)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover typed API responses and HTTP status and transport error handling.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
