## Description:

Writes Go code with go-deribit, an unofficial client for Deribit crypto options and futures generated from Deribit's public specs. Root package `deribit` (`github.com/psyb0t/go-deribit`) covers all 186 REST paths for instruments, market data, accounts, positions, orders, transfers and account administration. Package `deribitws` (`/ws`) covers all 43 JSON-RPC subscription channels for order books, tickers, trades and account updates. Use when Go code needs Deribit REST calls or WebSocket subscriptions, or already imports go-deribit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to write Go code that calls Deribit's REST API or subscribes to its WebSocket channels for market data and account operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client is unofficial, and private requests use account credentials or tokens.

Mitigation: Review and pin the dependency, keep credentials out of source code and logs, and start development on testnet with only the required token permissions.

Risk: Generated integrations can place orders or change account state, and the client does not enforce permissions or refresh tokens automatically.

Mitigation: Review generated code and API responses, and only authorize live trades, transfers, withdrawals, or account changes when explicitly requested.

## Reference(s):

- [Setup and usage reference](references/setup.md)
- [Skill release page](https://clawhub.ai/psyb0t/skills/go-deribit)
- [go-deribit project page listed in the skill](https://github.com/psyb0t/go-deribit)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance, Technical guidance]

**Output Format:** [Go source code and concise Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account or API integration code; review before use with live credentials or accounts.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
