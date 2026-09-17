## Description:

Blave Quant helps agents retrieve Blave market data and use documented workflows for crypto trading venues, Taiwan market data, futures, commodities, and marketplace strategies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trading analysts use this skill to fetch market data, inspect alpha signals, prepare API calls, and manage supported exchange workflows with explicit user confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace strategy code may be unreviewed private or shared Python that runs near trading credentials.

Mitigation: Do not run marketplace strategies unless the source, provenance, and digest are independently reviewed; execute approved code in a sandbox without inherited Blave or exchange credentials.

Risk: Exchange API credentials can authorize trading actions if granted broad permissions.

Mitigation: Use dedicated exchange API keys with withdrawals disabled, minimum required permissions, and IP allowlisting.

Risk: Trading and funding actions can cause financial loss if executed unintentionally or with incorrect parameters.

Mitigation: Require a current-conversation explicit confirmation for each write action, then verify the resulting order, position, transfer, or funding state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Publisher profile](https://clawhub.ai/user/blave-wei)
- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
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
- [TWSE broker branch reference](references/twse-bsr-reference.md)
- [TradingView stream reference](references/tradingview-stream.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with API examples, code snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Blave credentials for market data and optional exchange credentials for trading integrations; write actions require explicit user confirmation.]

## Skill Version(s):

1.23.4 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
