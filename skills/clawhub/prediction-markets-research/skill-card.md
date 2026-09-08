## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API, returning clean JSON for market and forecasting research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and researchers use this skill to retrieve read-only prediction-market data, compare odds across Polymarket and Kalshi, and inspect Metaculus community forecasts for events and questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can expose the Crawlora API key if the API base is redirected.

Mitigation: Use a trusted environment, use a Crawlora key that can be revoked, and avoid setting CRAWLORA_API_BASE.

Risk: The bundled script is broader than the stated prediction-market purpose and can send arbitrary request bodies.

Mitigation: Limit use to the documented Polymarket, Kalshi, and Metaculus endpoints, and do not pass sensitive text or arbitrary request bodies through the helper.

Risk: Market odds and community forecasts may be incomplete, stale, or unsuitable as financial advice.

Mitigation: Treat retrieved data as read-only research input and verify important conclusions against primary market or forecasting sources before acting.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API output references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY for live API calls.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
