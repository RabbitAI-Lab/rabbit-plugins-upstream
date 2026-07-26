## Description: <br>
API reference for CoinMarketCap market-wide endpoints including global metrics, fear/greed, indices, trending topics, and charts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to choose CoinMarketCap market API endpoints, shape authenticated requests, interpret response fields, and handle market-wide crypto data workflows such as sentiment, dominance, indices, charts, content, and API usage checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys can be exposed if users paste real CoinMarketCap credentials into chat, code, or saved examples. <br>
Mitigation: Keep the CoinMarketCap API key in an environment variable or secret manager and use placeholder values in prompts and examples. <br>
Risk: Community and content endpoints may return usernames, avatars, comments, posts, or other user-facing content that should not be overexposed. <br>
Mitigation: Review, minimize, and redact community content before displaying, logging, storing, or sharing it outside the intended workflow. <br>
Risk: API usage endpoints and rate-limit headers can reveal plan, quota, and consumption details. <br>
Mitigation: Treat usage and quota data as operationally sensitive and avoid including it in public outputs or persistent logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cmc.skills/skills/cmc-api-market) <br>
- [CoinMarketCap Pro API login](https://pro.coinmarketcap.com/login) <br>
- [CoinMarketCap Pro API base URL](https://pro-api.coinmarketcap.com) <br>
- [Global Metrics API Reference](references/global-metrics.md) <br>
- [Fear and Greed Index API Reference](references/fear-greed.md) <br>
- [Market Indices API Reference](references/indices.md) <br>
- [Community API Reference](references/community.md) <br>
- [Content API Reference](references/content.md) <br>
- [K-Line Charts API Reference](references/kline.md) <br>
- [Tools API Reference](references/tools.md) <br>
- [Common Use Cases](references/use-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Configuration guidance] <br>
**Output Format:** [Markdown guidance with endpoint tables, JSON response examples, and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a CoinMarketCap API key for live requests; outputs may include API plan, quota, and community-content details when those endpoints are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
