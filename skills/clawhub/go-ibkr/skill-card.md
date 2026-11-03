## Description:

Provides a typed Go client for Interactive Brokers' Client Portal Web API, including account, portfolio, contract, market data, and order operations through a local gateway or OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Go developers use this client to access Interactive Brokers accounts, portfolios, contracts, market data, and order endpoints from Go applications. For real-account order changes, make only the specific change the user requested and prefer paper trading during development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Order submission, modification, cancellation, confirmation, and model-order operations can change a real brokerage account.

Mitigation: Use paper trading during development and make real-account changes only when the user explicitly requests that specific action.

Risk: Exposed OAuth tokens can grant brokerage access, and disabling TLS verification for a remote host weakens connection security.

Mitigation: Keep tokens in protected runtime sources and never hardcode, commit, or log them; keep TLS verification enabled except for the user's local self-signed gateway.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-ibkr package documentation](https://pkg.go.dev/github.com/psyb0t/go-ibkr)
- [go-ibkr project page](https://github.com/psyb0t/go-ibkr)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
