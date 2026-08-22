## Description:

Blave Quant gives agents market-data and exchange-trading guidance for Blave alpha data, Taiwan equities and futures, CME/ICE futures, Hyperliquid tracking, and supported crypto exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch market data, inspect trading signals, and prepare exchange API workflows across multiple crypto, futures, and Taiwan market data sources. It also guides order, transfer, and funding workflows while requiring explicit user confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exchange API keys could authorize live trading or transfers if configured with broad permissions.

Mitigation: Use dedicated keys with withdrawals disabled, IP allowlisting, and the minimum permissions needed; prefer read-only keys unless trading is required.

Risk: Marketplace strategy code could run in an environment that also contains live exchange credentials.

Mitigation: Independently review and sandbox shared or purchased strategies, and do not run them in credential-bearing environments without isolation.

Risk: Trading, order, transfer, and funding workflows can create financial loss if executed incorrectly.

Mitigation: Require an explicit one-action confirmation before write actions and verify results through the corresponding read endpoint.

Risk: Broker or affiliate attribution is embedded in several exchange workflows.

Mitigation: Review exchange-specific attribution requirements before using the related trading flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave homepage](https://blave.org)
- [Blave API reference](artifact/references/blave-api.md)
- [Blave indicator guide](artifact/references/blave-indicator-guide.md)
- [TradingView stream reference](artifact/references/tradingview-stream.md)
- [Marketplace reference](artifact/references/marketplace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API call patterns, code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Blave API credentials for market data; exchange credentials are optional and should use least privilege.]

## Skill Version(s):

1.22.1 (source: SKILL.md frontmatter, artifact/clawhub.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
