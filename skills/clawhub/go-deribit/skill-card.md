## Description:

Writes Go code with go-deribit, an unofficial client for Deribit crypto options and futures generated from Deribit's public specs. Root package `deribit` (`github.com/psyb0t/go-deribit`) covers all 186 REST paths for instruments, market data, accounts, positions, orders, transfers and account administration. Package `deribitws` (`/ws`) covers all 43 JSON-RPC subscription channels for order books, tickers, trades and account updates. Use when Go code needs Deribit REST calls or WebSocket subscriptions, or already imports go-deribit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go programs that call Deribit's REST API or consume WebSocket subscriptions for market data, account information, and trading operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private API calls use account credentials, and production trading or account changes can affect funds or account access.

Mitigation: Keep tokens out of source control and logs, develop on testnet, and use production credentials or perform account-changing actions only for explicitly requested tasks.

Risk: The security assessment covers the bundled documentation, not the downloaded Go dependency.

Mitigation: Review and pin the Go module version before using it.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-deribit source repository](https://github.com/psyb0t/go-deribit)
- [go-deribit API documentation](https://pkg.go.dev/github.com/psyb0t/go-deribit)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.2.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
