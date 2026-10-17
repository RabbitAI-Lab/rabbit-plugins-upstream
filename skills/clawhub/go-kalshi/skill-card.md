## Description:

Guides Go developers in using an unofficial Kalshi client for market data, account operations, and live streams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Kalshi market-data, trading-account, and WebSocket functionality to Go projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys and signed requests could expose access to a trading account.

Mitigation: Keep key material out of source code and logs, and use signed requests only with Kalshi endpoints.

Risk: Orders, transfers, quotes, or API-key changes can affect a real account.

Mitigation: Use demo endpoints during development and perform account-changing actions only when explicitly requested.

## Reference(s):

- [go-kalshi on ClawHub](https://clawhub.ai/psyb0t/skills/go-kalshi)
- [Setup and API reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover REST requests, WebSocket subscriptions, and API-key handling.]

## Skill Version(s):

0.1.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
