## Description:

Pulls prediction-market odds, order books, and forecast questions from Polymarket, Kalshi, and Metaculus via the Crawlora API and returns normalized JSON for market and forecasting research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve current and historical prediction-market data, order books, prices, and community forecasts for event research. It supports read-only research across Polymarket, Kalshi, and Metaculus through Crawlora-backed endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the helper script is broader than disclosed and can send arbitrary requests and payloads to Crawlora-backed endpoints.

Mitigation: Restrict use to the documented Polymarket, Kalshi, and Metaculus endpoints and avoid arbitrary POST bodies.

Risk: The security evidence says use requires a Crawlora API key and outbound Crawlora requests.

Mitigation: Provide the API key only through CRAWLORA_API_KEY, do not hardcode or commit it, and install only when outbound Crawlora access is acceptable.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/prediction-markets-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper output is raw JSON from read-only market-data requests.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
