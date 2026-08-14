## Description:

blave-quant helps agents fetch Blave market alpha data, Taiwan market data, futures OHLCV, and selected crypto exchange account and trading information through documented API workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trading-system operators use this skill to let an agent retrieve market data, inspect exchange account state, and prepare exchange API actions. It is intended for data access and user-confirmed trading workflows, not unattended financial decision-making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers live trading, transfers, and funding actions across multiple exchanges.

Mitigation: Require explicit current-conversation CONFIRM for each write action, use least-privilege API keys, disable withdrawals unless needed, and prefer read-only keys for analysis.

Risk: The marketplace workflow can download and run Python strategy code while exchange credentials may exist on the same machine.

Mitigation: Independently review and sandbox downloaded strategy code before execution, and avoid running it in environments that contain live exchange credentials.

Risk: Market indicators and generated trade preparation can be incorrect or financially harmful.

Mitigation: Treat outputs as informational, verify data and order details manually, and do not treat the skill as financial advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave Homepage](https://blave.org)
- [Blave API Examples](references/blave-api.md)
- [Blave Indicator Interpretation Guide](references/blave-indicator-guide.md)
- [Hyperliquid API Reference](references/hyperliquid-api.md)
- [TradingView Signal Stream](references/tradingview-stream.md)
- [Blave Agent Strategy Marketplace API](references/marketplace.md)
- [BitMart Futures API Reference](references/bitmart-api-reference.md)
- [BitMart Spot Trading API Reference](references/bitmart-spot-api-reference.md)
- [OKX API Reference](references/okx-api-reference.md)
- [Binance API Reference](references/binance-api-reference.md)
- [TWSE / TPEX API Reference](references/twse-api-reference.md)
- [Taiwan Stock Fundamental Data](references/twstock-fundamentals-reference.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with API request examples, environment variable instructions, and code or shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to make authenticated third-party API calls using local user-provided credentials.]

## Skill Version(s):

1.22.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
