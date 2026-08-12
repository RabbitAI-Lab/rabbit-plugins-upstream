## Description:

Blave Quant guides agents to retrieve Blave market data and interact with supported crypto exchanges for spot, futures, margin, funding, and account workflows with explicit confirmation for write actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, traders, and analysts use this skill to access Blave market alpha, Taiwan market data, and exchange API workflows through an agent. It is intended for market analysis and guarded trading assistance where write actions require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through high-impact trading and account actions using live exchange credentials.

Mitigation: Use read-only or narrowly scoped API keys by default, avoid withdrawal permissions, prefer paper trading or testnet environments, and require explicit confirmation before any order, transfer, funding, leverage, or position action.

Risk: Marketplace workflows may fetch strategy code for local execution while trading credentials are present.

Mitigation: Independently review downloaded strategy code, isolate it from secrets and live accounts, and do not run marketplace strategy code unless it has been approved in a controlled environment.

Risk: Broker or affiliate attribution headers and fields are attached to several exchange workflows.

Mitigation: Review the disclosed broker and affiliate attribution before placing orders through supported exchanges.

## Reference(s):

- [Blave homepage](https://blave.org)
- [ClawHub skill page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [TradingView stream reference](references/tradingview-stream.md)
- [Marketplace reference](references/marketplace.md)
- [BitMart futures reference](references/bitmart-futures-skill.md)
- [BitMart spot reference](references/bitmart-spot-skill.md)
- [OKX reference](references/okx-skill.md)
- [Bybit reference](references/bybit-skill.md)
- [BingX reference](references/bingx-skill.md)
- [Bitget reference](references/bitget-skill.md)
- [Binance reference](references/binance-skill.md)
- [Bitfinex reference](references/bitfinex-skill.md)
- [KuCoin reference](references/kucoin-skill.md)
- [Gate.io reference](references/gateio-skill.md)
- [Taiwan stock fundamentals reference](references/twstock-fundamentals-reference.md)
- [Taiwan broker buy/sell reference](references/twse-bsr-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code, API request examples, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include credential setup, API signing examples, trading workflow checks, and exchange-specific request headers.]

## Skill Version(s):

1.21.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
