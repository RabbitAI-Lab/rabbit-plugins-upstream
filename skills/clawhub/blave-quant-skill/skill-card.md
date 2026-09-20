## Description:

blave-quant helps agents retrieve Blave market data and produce analysis, code, API calls, and trading workflow guidance for cryptocurrency, Taiwan market, futures, and supported exchange use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and trading users use this skill to guide agents through Blave market-data retrieval, indicator interpretation, Taiwan market workflows, and exchange trading operations that require explicit user confirmation for writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence rates the skill suspicious because it includes marketplace flows that can download Python strategy code and run it locally.

Mitigation: Review downloaded strategy code independently, scan it before execution, and isolate it from credentials, sensitive files, and unrestricted network access.

Risk: The skill can guide live trading, transfers, funding, and leveraged position actions through third-party exchange APIs.

Mitigation: Use least-privilege API keys, disable withdrawals unless required, prefer testnet or paper trading, and require an explicit CONFIRM for each write action.

## Reference(s):

- [Blave homepage](https://blave.org)
- [ClawHub skill page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Skill instructions](artifact/SKILL.md)
- [Blave API reference](artifact/references/blave-api.md)
- [Blave indicator guide](artifact/references/blave-indicator-guide.md)
- [Marketplace reference](artifact/references/marketplace.md)
- [TradingView stream reference](artifact/references/tradingview-stream.md)
- [TWSE workflow reference](artifact/references/twse-skill.md)
- [BitMart futures reference](artifact/references/bitmart-futures-skill.md)
- [Binance reference](artifact/references/binance-skill.md)
- [KuCoin reference](artifact/references/kucoin-skill.md)
- [Gate.io reference](artifact/references/gateio-skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown with code blocks, shell commands, configuration snippets, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to use local environment API keys and third-party exchange APIs; write operations require explicit user confirmation per skill instructions.]

## Skill Version(s):

1.23.6 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
