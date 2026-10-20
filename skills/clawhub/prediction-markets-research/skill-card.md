## Description:

Retrieves prediction-market odds, order books, price histories, and community forecasts from Polymarket, Kalshi, and Metaculus through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to compare event odds, inspect market depth and historical prices, and review community forecasts without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries, IDs, and request bodies are sent to Crawlora using the user's API key.

Mitigation: Avoid secrets, personal data, and confidential research text in requests; keep the API key private.

Risk: Market odds and community forecasts can be mistaken for reliable financial advice.

Mitigation: Treat results as informational, verify consequential claims independently, and do not use them as financial advice.

## Reference(s):

- [Prediction-market endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/prediction-markets-research)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON market data with optional plain-language analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market data; a Crawlora API key is required.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
