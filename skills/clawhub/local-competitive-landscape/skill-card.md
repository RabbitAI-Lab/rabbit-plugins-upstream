## Description:

Compare observed local business supply, categories, attributes, hours, and review-sample themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to compare local competitive coverage across matched areas while preserving source-specific counts, categories, attributes, hours, ratings, and review-sample themes. It is intended for traceable competitor landscape and coverage comparisons, not lead generation, demand forecasting, sales estimation, or site-viability claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business search terms, place identifiers, and the Crawlora API key are sent to Crawlora.

Mitigation: Use a scoped or disposable API key where possible and avoid confidential business plans or sensitive strategy terms in queries.

Risk: Directory coverage can be mistaken for proof of business population, demand, revenue, market share, or site viability.

Mitigation: Treat results as observed coverage, keep source and retrieval bounds visible, and label missing or bounded evidence as uncertainty rather than absence.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/local-competitive-landscape)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source, query, geometry, retrieval date, bounded or failed collection status, and uncertainty notes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
