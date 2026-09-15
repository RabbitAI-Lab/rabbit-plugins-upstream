## Description:

Stock Ontology helps agents resolve ticker-related people, products, product families, peers, and organizations, then compare their SentiSense Scores over common windows using read-only SentiSense API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer stock-related entity, relationship, and sentiment-context questions for listed companies. It is intended for informational and educational analysis, not trading, purchasing, account writes, or personalized buy or sell recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SentiSense API key to make network requests.

Mitigation: Provide the key through the SENTISENSE_API_KEY environment variable and limit network access to app.sentisense.ai.

Risk: Financial sentiment and relationship outputs could be mistaken for trading advice or causal market-impact claims.

Mitigation: Present outputs as informational context only, include dated provenance, and avoid buy or sell recommendations.

Risk: Broad crawling or repeated fan-out could exceed quotas or collect more data than needed.

Mitigation: Use the documented bounded workflows, avoid enumerating the graph, respect rate limits, and preserve partial status when limits are reached.

Risk: Evidence lookups may retrieve document metadata, source URLs, and SentiSense-generated story records.

Mitigation: Report only returned metadata and source links, and clearly distinguish generated story records from publisher article text.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-ontology)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown tables and prose with optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API guidance with dated provenance; outputs should avoid investment recommendations and causal market-impact claims.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
