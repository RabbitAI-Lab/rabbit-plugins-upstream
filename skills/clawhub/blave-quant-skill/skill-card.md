## Description:

Blave Quant gives agents access to Blave market data, Taiwan market data, futures and commodity OHLCV data, and guided trading workflows across multiple cryptocurrency exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-focused agent users use this skill to retrieve market data, analyze crypto and Taiwan market signals, and prepare or execute exchange trading actions through documented API workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exchange API keys may enable live trading if granted trading permissions.

Mitigation: Use read-only or tightly scoped API keys unless live trading is intentional, disable withdrawals, and prefer IP allowlisting where the exchange supports it.

Risk: Marketplace workflows may download and run remote Python strategies.

Mitigation: Review downloaded strategy code before execution and run it in an isolated environment without trading secrets.

Risk: Trading guidance and order workflows can cause financial loss if executed incorrectly.

Mitigation: Require explicit confirmation for write actions and verify balances, positions, limits, and resulting order status before and after each action.

## Reference(s):

- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [TradingView stream reference](references/tradingview-stream.md)
- [Marketplace reference](references/marketplace.md)
- [BitMart futures reference](references/bitmart-futures-skill.md)
- [OKX reference](references/okx-skill.md)
- [Bybit reference](references/bybit-skill.md)
- [Binance reference](references/binance-skill.md)
- [KuCoin reference](references/kucoin-skill.md)
- [Gate.io reference](references/gateio-skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with code snippets, shell commands, configuration values, and API request instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May cause an agent to call Blave and exchange APIs using user-provided credentials; write actions require explicit user confirmation according to the artifact documentation.]

## Skill Version(s):

1.23.8 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
