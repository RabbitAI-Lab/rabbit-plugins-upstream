## Description:

Pulls prediction-market odds, order books, price history, and forecast questions from Polymarket, Kalshi, and Metaculus through the Crawlora API, returning clean JSON for market and forecasting research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to query public prediction-market and forecasting data for current odds, order books, price history, trending markets, and community forecasts. It supports research comparisons across Polymarket, Kalshi, and Metaculus and does not place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora endpoints with arbitrary request bodies, beyond the advertised prediction-market scope.

Mitigation: Use documented Polymarket, Kalshi, and Metaculus paths and review requested paths and request bodies before execution.

Risk: Private or sensitive data could be exposed if included in API request bodies or prompts.

Mitigation: Avoid sending private data, keep CRAWLORA_API_KEY in the environment, and never hardcode or pass the key in query parameters.

Risk: Prediction-market prices and community forecasts may be mistaken for financial advice.

Mitigation: Present results as informational market or forecasting data, not as trading instructions or financial advice.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; intended for read-only public market and forecast data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
