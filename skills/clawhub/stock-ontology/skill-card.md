## Description:

Helps agents explore a company's people, products, and peer relationships and compare their SentiSense Scores over a shared time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to identify entities connected to a supplied stock ticker, inspect named relationships, and compare dated financial-discussion scores without making trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent sends the SentiSense API key to app.sentisense.ai and consumes API quota.

Mitigation: Use a dedicated API key, limit queries to the user's request, and monitor remaining quota.

Risk: Scores and entity relationships can be mistaken for investment advice or proof of market impact.

Mitigation: Present dated results as informational context and avoid buy-or-sell recommendations or causal claims.

Risk: Evidence views can include document metadata, source URLs, and SentiSense-generated story records.

Mitigation: Label generated stories and distinguish source metadata from original article content.

## Reference(s):

- [Stock Ontology on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-ontology)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables with dated scores, entity relationships, and source references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational output; not investment advice.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
