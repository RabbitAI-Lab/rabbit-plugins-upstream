## Description:

Unofficial Go clients for the eToro public API, generated from the specs eToro publishes. The root package `etoro` (`github.com/psyb0t/go-etoro`) is an oapi-codegen REST client for `https://public-api.etoro.com` with a typed `...WithResponse` method per endpoint (balances, market data, instruments, rates, candles, feeds, portfolios, transfers, posts). The `etorows` package (`github.com/psyb0t/go-etoro/ws`) is a typed WebSocket client for `wss://ws.etoro.com/ws` that authenticates, subscribes to topics and decodes instrument rate, candle and market status pushes and order and position updates through a `Handler`. Use when Go code needs to call the eToro API or stream eToro market data, or already imports go-etoro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers can use this skill to integrate applications with eToro's REST API or WebSocket streams for account and market data. It also documents endpoints that can transfer money or publish social content, which should only be called when specifically requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The client uses eToro API credentials that can expose account data if mishandled.

Mitigation: Use read-only keys where possible; load credentials from ETORO_API_KEY and ETORO_USER_KEY environment variables, and keep them out of logs and source control.

Risk: Some documented API operations can move money or publish public content.

Mitigation: Default to read-only endpoints and call transfers or publishing actions only when the user explicitly requests that exact action.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [Project homepage](https://github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with Go code examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
