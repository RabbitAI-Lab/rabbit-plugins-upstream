## Description:

Blave Quant helps agents retrieve Blave market alpha, Taiwan and futures market data, and use supported exchange APIs for spot, futures, and funding workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and trading users use this skill to guide agents through authenticated market-data retrieval, alpha screening, backtesting support, and user-confirmed trading workflows across supported exchanges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to place trades, transfer funds, or submit funding actions through third-party exchange APIs.

Mitigation: Use read-only keys unless trading is required, disable withdrawals, apply IP allowlists where possible, and require an explicit per-action CONFIRM before any write operation.

Risk: Marketplace strategies may include untrusted Python strategy code.

Mitigation: Review and scan marketplace code before use, and run downloaded strategies only in an isolated environment that does not contain exchange keys or other secrets.

Risk: Supported exchange requests may include Blave broker or referral identifiers.

Mitigation: Disclose broker attribution to users before use and let them decide whether the attribution behavior is acceptable for their account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave homepage](https://blave.org)
- [Blave API reference](references/blave-api.md)
- [Blave indicator guide](references/blave-indicator-guide.md)
- [Hyperliquid API reference](references/hyperliquid-api.md)
- [Marketplace reference](references/marketplace.md)
- [Binance API reference](references/binance-api-reference.md)
- [BitMart futures reference](references/bitmart-futures-skill.md)
- [OKX API reference](references/okx-api-reference.md)
- [Bybit reference](references/bybit-skill.md)
- [KuCoin reference](references/kucoin-skill.md)
- [Gate.io API reference](references/gateio-api-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, API-call patterns, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Blave API credentials for market data; exchange credentials are optional and should be scoped to the requested workflow.]

## Skill Version(s):

1.23.1 (source: server release, frontmatter, clawhub.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
