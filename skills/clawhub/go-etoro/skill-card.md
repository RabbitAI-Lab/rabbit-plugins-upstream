## Description:

Unofficial Go clients for the eToro public API, generated from the specs eToro publishes. The root package `etoro` (`github.com/psyb0t/go-etoro`) is an oapi-codegen REST client for `https://public-api.etoro.com` with a typed `...WithResponse` method per endpoint (balances, market data, instruments, rates, candles, feeds, portfolios, transfers, posts). The `etorows` package (`github.com/psyb0t/go-etoro/ws`) is a typed WebSocket client for `wss://ws.etoro.com/ws` that authenticates, subscribes to topics and decodes instrument rate, candle and market status pushes and order and position updates through a `Handler`. Use when Go code needs to call the eToro API or stream eToro market data, or already imports go-etoro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add typed Go REST or WebSocket access to eToro market and account data in a Go project. It also explains credential handling and when to require explicit instructions for transfers or publishing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account keys could be exposed through source code, logs, or printed authenticated requests.

Mitigation: Load keys from ETORO_API_KEY and ETORO_USER_KEY; do not hardcode, commit, log, or print requests with authentication headers.

Risk: Transfers and social actions can move funds or publish, change, or delete content.

Mitigation: Keep usage read-only by default and require explicit user instructions for each transfer or content-changing action.

Risk: This is an unofficial integration, and a clean scan does not certify its library or dependencies.

Mitigation: Pin and review the Go dependency before providing it with account keys.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-etoro)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-etoro)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-etoro)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and implementation guidance for the current Go project.]

## Skill Version(s):

0.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
