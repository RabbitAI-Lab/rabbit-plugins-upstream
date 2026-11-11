## Description:

Helps Go developers use an unofficial typed Deribit client for REST requests and WebSocket subscriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Deribit market data, account, order, and WebSocket subscription code to a project. It also guides dependency setup and endpoint type lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private requests and subscriptions can expose account data and require OAuth credentials.

Mitigation: Use a token only when private access is needed; load it from a protected environment or secret store and never hardcode, commit, or log it.

Risk: Orders, cancellations, transfers, withdrawals, and account or API key changes can affect a live account.

Mitigation: Use testnet during development and perform these actions only when the user explicitly requested that exact action.

Risk: The security review noted a credential-related alert and partial reference checks.

Mitigation: Review the setup guidance and apply normal credential safeguards before using private requests.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)
- [Project homepage](https://github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Go code, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Go code and concise Markdown guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and dependency setup for the current Go project.]

## Skill Version(s):

0.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
