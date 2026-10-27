## Description:

Guides developers in using a typed Go client to read dYdX v4 Indexer market and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

AGPL-3.0-only

## Use Case:

Developers use this skill to add a Go client for dYdX v4 Indexer market and account data, including candles, orderbooks, positions and fills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adding an untrusted third-party Go module or using it under incompatible license terms.

Mitigation: Review the dependency before installation and confirm that its AGPL-3.0-only declaration and the conflicting release license metadata fit the project.

Risk: Wallet addresses or account identifiers are sent to an unintended indexer endpoint.

Mitigation: Choose the mainnet or testnet base URL deliberately and send user-provided identifiers only to the intended indexer.

Risk: Identity-related POST operations may be invoked without the user's intent.

Mitigation: Use push registration, sign-in or affiliate actions only when explicitly requested.

## Reference(s):

- [go-dydx-indexer setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-dydx-indexer)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-dydx-indexer)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
