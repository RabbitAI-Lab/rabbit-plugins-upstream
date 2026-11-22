## Description:

Unofficial Go client for the Interactive Brokers Web API (Client Portal API v1), generated with oapi-codegen from the OpenAPI document Interactive Brokers publishes. Package `ibkr` (`github.com/psyb0t/go-ibkr`) has a typed `...WithResponse` method for each of the spec's endpoints, covering session status and keepalive, accounts, portfolio positions and summary, contract search and details, market data snapshots, order submission, status, modification and cancellation, and model portfolios. It works through a local Client Portal Gateway or against `https://api.ibkr.com` with an OAuth token. Use when Go code needs to read an Interactive Brokers account, look up contracts or market data, or place orders, or already imports go-ibkr.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that reads Interactive Brokers account, portfolio, contract, and market data through the Client Portal Web API. It also guides order submission and management when the user requests those actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth credentials and brokerage operations can expose account access or affect a real brokerage account; the security scan was only partially complete.

Mitigation: Use your own token through an environment variable or token code, and never hardcode, commit, or log it. Invoke order actions only when specifically requested, prefer paper trading during development, and follow the local gateway TLS guidance only for that gateway.

## Reference(s):

- [Setup and reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-ibkr)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, API usage guidance]

**Output Format:** [Go examples and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.1.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
