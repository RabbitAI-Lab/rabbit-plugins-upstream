## Description:

Researches public cryptocurrency markets, coins, exchanges, categories, global metrics, news, NFTs, token unlocks, and treasuries through CoinGecko via the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve public CoinGecko-derived cryptocurrency market snapshots through Crawlora for coin discovery, market comparison, category and chain research, exchange review, news checks, token unlocks, and treasury snapshots. It is for market research and comparative reporting, not trading, wallet access, private account access, or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested crypto research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use only for public market research queries, keep CRAWLORA_API_KEY scoped and private, and avoid submitting private wallet, exchange account, or trading information.

Risk: Cryptocurrency prices, volumes, rankings, news, and unlock data are time-sensitive and can become stale quickly.

Mitigation: Include retrieval time, quote currency, requested filters, and source in reports, and avoid presenting snapshots as forecasts or investment advice.

Risk: Coin tickers, CoinGecko IDs, chain IDs, and exchange IDs can refer to different entities.

Mitigation: Resolve assets through search and use CoinGecko IDs as stable identifiers before comparing market data.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/crypto-market-research)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; requests are GET-only and limited to documented public CoinGecko-derived Crawlora routes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
