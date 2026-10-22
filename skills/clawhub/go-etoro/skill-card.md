## Description:

Unofficial Go clients for the eToro public API, generated from the specs eToro publishes. The root package `etoro` (`github.com/psyb0t/go-etoro`) is an oapi-codegen REST client for `https://public-api.etoro.com` with a typed `...WithResponse` method per endpoint (balances, market data, instruments, rates, candles, feeds, portfolios, transfers, posts). The `etorows` package (`github.com/psyb0t/go-etoro/ws`) is a typed WebSocket client for `wss://ws.etoro.com/ws` that authenticates, subscribes to topics and decodes instrument rate, candle and market status pushes and order and position updates through a `Handler`. Use when Go code needs to call the eToro API or stream eToro market data, or already imports go-etoro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to add typed Go REST or WebSocket integration with eToro's public API, including account and market data, live updates, and user-requested account actions. It also guides setup and safe handling of API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposed eToro API keys could compromise the user's account.

Mitigation: Keep both keys in protected environment variables or a secret store; never hardcode, commit, or log them, and send them only to the documented eToro hosts.

Risk: Transfer and publishing endpoints can cause consequential account actions.

Mitigation: Default to read-only calls and perform a money-moving or publishing action only when the user explicitly requests that exact action.

## Reference(s):

- [Setup and API reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [Project homepage](https://github.com/psyb0t/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup guidance for integrating the Go client into the current project.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
