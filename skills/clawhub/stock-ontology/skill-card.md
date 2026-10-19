## Description:

Helps agents explore companies' people, products, and peer relationships and compare their SentiSense Scores over a shared time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can resolve company-related entities, inspect typed relationships and compare dated sentiment and attention readings for a supplied ticker or watchlist. Results provide informational financial context, not trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key is sent to app.sentisense.ai for read-only lookups.

Mitigation: Use a dedicated API key and share it only with the disclosed SentiSense service.

Risk: Entity and score lookups can consume API quota.

Mitigation: Limit lookups to the requested tickers and check the available quota before large comparisons.

Risk: Sentiment and entity relationships can be mistaken for evidence of market impact or investment advice.

Mitigation: Present dated readings as informational context; do not infer causation, place trades, or provide personalized buy/sell decisions.

## Reference(s):

- [Stock Ontology on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-ontology)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes dated entity handles, relationship or score context, coverage notes, and an informational-use disclaimer.]

## Skill Version(s):

1.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
