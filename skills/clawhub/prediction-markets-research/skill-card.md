## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to retrieve read-only prediction-market and forecasting data for event research, odds comparison, price history, order-book inspection, and forecast aggregation. It supports research on public market signals and should not be treated as financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key with off-scope API requests.

Mitigation: Use a dedicated, low-privilege Crawlora key and verify agent calls stay within documented /polymarket, /kalshi, and /metaculus endpoints.

Risk: Changing CRAWLORA_API_BASE can redirect authenticated requests away from the expected API base.

Mitigation: Avoid setting CRAWLORA_API_BASE unless the destination is explicitly reviewed and trusted.

Risk: Market odds and forecasts can be mistaken for investment or trading advice.

Mitigation: Use the skill only for read-only research and clearly separate market data from financial advice or trading decisions.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and returns read-only public prediction-market or forecast data.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
