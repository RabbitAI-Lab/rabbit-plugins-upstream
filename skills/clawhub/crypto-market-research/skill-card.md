## Description:

Researches public cryptocurrency markets, coins, exchanges, categories, global metrics, news, NFTs, token unlocks, and treasuries through CoinGecko via the Crawlora API. Use for market snapshots and comparative research, not trading or financial advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to gather public CoinGecko market snapshots, compare coins, categories, chains, exchanges, NFTs, token unlocks, and treasuries, and produce time-stamped research summaries without connecting to wallets or trading accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and public crypto lookup queries sent through the helper.

Mitigation: Use a scoped Crawlora API key and avoid sending private account details, wallet secrets, or trading instructions as query values.

Risk: Crypto prices, volumes, rankings, news, trending assets, and token unlock information change quickly.

Mitigation: Include retrieval time, quote currency, source, requested filters, and stale or missing data notes in generated research.

Risk: Market snapshots or chart-derived metrics could be mistaken for financial advice or trading signals.

Mitigation: Present outputs as public market research only and avoid price targets, guaranteed-return claims, or manipulation claims without evidence.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/crypto-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve retrieval time, quote currency, source, requested filters, and missing or stale data notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
