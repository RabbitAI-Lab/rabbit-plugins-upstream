## Description:

AI-powered read-only trading analysis coach that simulates alternative strategies against your Binance trade history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[acevod](https://clawhub.ai/user/acevod)

### License/Terms of Use:

MIT

## Use Case:

Traders and developers use this skill to analyze Binance Spot and Futures trading history, compare real results with simulated strategy alternatives, and generate coaching guidance for risk management and trading discipline.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Binance API credentials and may display sensitive balances and trading history locally.

Mitigation: Use read-only Binance API keys with trading and withdrawals disabled, apply IP restrictions where possible, and avoid sharing console output that contains account details.

Risk: Trading analysis and simulated strategy alternatives may be mistaken for financial advice or trading signals.

Mitigation: Treat generated reports as educational analysis only and review recommendations independently before making trading decisions.

## Reference(s):

- [Shadow Binance Bot on ClawHub](https://clawhub.ai/acevod/skills/shadow-binance-bot)
- [Project homepage](https://github.com/acevod/Shadow-Binance-Bot)
- [OpenClaw](https://openclaw.ai)
- [Binance OpenClaw AI Builder Contest recognition](https://x.com/binance/status/2041259653305114833)
- [Architecture diagram](assets/architecture.png)
- [Shadow strategy simulation diagram](assets/shadow-simulation.png)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Console text and Markdown documentation with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Binance read-only API credentials when configured; runs in demo mode with generated data when credentials are absent.]

## Skill Version(s):

1.5.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
