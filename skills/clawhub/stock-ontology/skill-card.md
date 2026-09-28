## Description:

Helps agents explore a company's people, products, peers, and typed relationships and compare their SentiSense Scores over a shared time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can resolve stock-related entities, inspect curated company relationships, and compare dated sentiment and attention readings for a selected ticker or supplied watchlist. Results provide informational context, not investment advice or evidence of market causation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent must use the SentiSense API key to access the service.

Mitigation: Provide the key only if comfortable with read-only requests to app.sentisense.ai; do not disclose it in responses.

Risk: Sentiment and relationship data could be mistaken for investment advice or proof of market impact.

Mitigation: Present dated readings as informational context, note sample and coverage limits, and avoid buy/sell or causal claims.

Risk: Large watchlists or repeated score lookups can consume request quota.

Mitigation: Bound requests to the supplied tickers, reuse identical reads, and report partial results when rate or quota limits are reached.

## Reference(s):

- [Stock Ontology ClawHub release](https://clawhub.ai/thesentitrader/skills/stock-ontology)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown tables and brief explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated observations with entity handles, sample and coverage notes, and an informational-use disclaimer.]

## Skill Version(s):

1.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
