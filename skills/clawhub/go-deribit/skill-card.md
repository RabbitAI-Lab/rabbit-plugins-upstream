## Description:

Writes Go code that uses the unofficial go-deribit client for Deribit REST endpoints and WebSocket subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this skill to write code that calls Deribit REST endpoints or consumes Deribit WebSocket subscription updates for market data and account workflows. It is for projects that use the unofficial go-deribit client and should use testnet during development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private REST calls and subscriptions use OAuth credentials, and account operations can place or cancel orders, transfer funds, withdraw, or change account settings.

Mitigation: Keep tokens in environment-backed secret storage, use testnet during development, and run account-changing operations only when explicitly requested with credentials for the selected environment.

Risk: The security evidence is incomplete because three local references could not be resolved.

Mitigation: Review the setup reference and relevant provider documentation before installing or using private account features; the benign verdict is not a guarantee of safety.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-deribit source and project homepage](https://github.com/psyb0t/go-deribit)
- [go-deribit Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Shell commands, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST and WebSocket client usage; private calls require OAuth credentials.]

## Skill Version(s):

0.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
