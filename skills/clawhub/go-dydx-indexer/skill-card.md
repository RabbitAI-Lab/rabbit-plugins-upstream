## Description:

Provides a typed Go client for querying dYdX v4 Indexer market and account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go calls for dYdX v4 market and account data to a project. It also provides install and usage guidance for the indexer client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identity-related endpoints can send wallet or account data to the configured base URL and can act on the caller's identity.

Mitigation: Use a trusted HTTPS indexer URL, send wallet addresses only to that indexer, and call identity-related endpoints only when the user requests the action.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-dydx-indexer source repository](https://github.com/psyb0t/go-dydx-indexer)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-dydx-indexer)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Go source code and shell commands with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install and build the Go dependency; runtime requests use the configured indexer base URL.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
