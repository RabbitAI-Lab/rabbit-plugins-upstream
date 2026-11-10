## Description:

Unofficial Go client for Kalshi, generated from the API specs Kalshi publishes. The root package `kalshi` (`github.com/psyb0t/go-kalshi`) is an oapi-codegen REST client for the Trade API at `https://external-api.kalshi.com/trade-api/v2` with a typed `...WithResponse` method per endpoint (markets, events, series, orderbooks, trades, balance, positions, fills, orders, RFQs and quotes). `kalshiws` (`/ws`) streams market data (orderbook, ticker, trade, fill, lifecycle, RFQ and index pushes) through a typed `Handler`, `kalshiperpsws` (`/perpsws`) does the same for the perps channels, and `kalshiauth` (`/auth`) signs REST requests and WebSocket handshakes with an RSA-PSS or Ed25519 API key. Use when Go code needs to read Kalshi markets, manage a Kalshi account or stream Kalshi data, or already imports go-kalshi.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Kalshi through typed REST and WebSocket clients, including market data and account operations. It guides installation, request signing, endpoint discovery, and safe handling of account-changing calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release benign with medium confidence, but one scan was partial because two references in SKILL.md could not be resolved.

Mitigation: Review the unresolved references before installing; the available scan did not cover the full skill.

Risk: Order placement, cancellation, quote acceptance, subaccount transfers, and API key changes can affect a real Kalshi account.

Mitigation: Make these calls only when the user explicitly requests the exact action, and use the demo environment while developing.

Risk: Exposure of the Kalshi private key or signed request headers could compromise account access.

Mitigation: Read the private key from an environment variable or user-provided file path; never hardcode, commit, or log it, and never print signed headers.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [go-kalshi Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-kalshi)
- [go-kalshi project repository](https://github.com/psyb0t/go-kalshi)
- [go-kalshi ClawHub release](https://clawhub.ai/psyb0t/skills/go-kalshi)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go examples, shell commands, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.10.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
