## Description:

Blave Quant equips agents to retrieve Blave market alpha, Taiwan market, futures, and crypto exchange data, and to prepare guarded spot, futures, margin, and funding workflows across supported exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, trading analysts, and external users use this skill to have an agent fetch market data, build trading analyses, and prepare exchange API actions. It is intended for users who manage their own API credentials and trading risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live trading, transfer, and funding workflows can expose users to financial loss or unintended account changes.

Mitigation: Use dedicated least-privilege API keys, disable withdrawals unless required, review proposed actions, and require one explicit confirmation for each write action.

Risk: Downloaded or shared marketplace strategy code may execute in an environment that can access exchange credentials.

Mitigation: Inspect strategy code before use and run it in an isolated environment without unnecessary credentials or host access.

Risk: Market data, scanner output, and generated analysis can be incorrect, stale, or misleading.

Mitigation: Validate important data against authoritative sources and treat all trading analysis as user-reviewed decision support, not financial advice.

## Reference(s):

- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [Hyperliquid API reference](references/hyperliquid-api.md)
- [TradingView signal stream](references/tradingview-stream.md)
- [Taiwan stock fundamentals reference](references/twstock-fundamentals-reference.md)
- [TWSE broker branch reference](references/twse-bsr-reference.md)
- [TWSE/TPEX reference](references/twse-skill.md)
- [BitMart futures guide](references/bitmart-futures-skill.md)
- [BitMart spot guide](references/bitmart-spot-skill.md)
- [OKX guide](references/okx-skill.md)
- [Bybit guide](references/bybit-skill.md)
- [BingX guide](references/bingx-skill.md)
- [Bitget guide](references/bitget-skill.md)
- [Binance guide](references/binance-skill.md)
- [Bitfinex guide](references/bitfinex-skill.md)
- [KuCoin guide](references/kucoin-skill.md)
- [Gate.io guide](references/gateio-skill.md)
- [Marketplace strategy reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with code, shell, configuration, and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Blave credentials and optional exchange credentials; write actions require explicit per-action user confirmation.]

## Skill Version(s):

1.22.3 (source: frontmatter, artifact metadata, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
