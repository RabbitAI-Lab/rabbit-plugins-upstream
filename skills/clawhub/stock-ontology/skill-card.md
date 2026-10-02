## Description:

Helps agents resolve a stock ticker to related people, products, and peer companies, inspect their relationships, and compare SentiSense Scores over a shared time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to explore the people, products, and peer relationships associated with a ticker and compare their dated sentiment scores for research context, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key is sent to the external SentiSense service.

Mitigation: Use a dedicated key and send it only to app.sentisense.ai over HTTPS.

Risk: Financial sentiment and relationship data can be mistaken for trading advice or proof of causation.

Mitigation: Present dated scores as research context, avoid personalized recommendations, and do not infer causation from co-movement.

Risk: Large ticker lists can exhaust API quotas or trigger rate limits.

Mitigation: Limit fan-out, respect rate limits, and report partial results when calls cannot complete.

## Reference(s):

- [Stock Ontology on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-ontology)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with dated entity comparisons and relationship summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research context; source links or document metadata when available.]

## Skill Version(s):

1.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
