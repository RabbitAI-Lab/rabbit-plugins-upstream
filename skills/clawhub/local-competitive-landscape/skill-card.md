## Description:

Compare observed local business supply, categories, attributes, hours, and review-sample themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp. Use for matched-area competitor landscapes and coverage comparisons; for user-supplied candidate-site screening with access and diligence gaps, use business-location-screening. Neither estimates demand, sales, or site viability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users can compare observed local business listings across defined areas to prepare a traceable competitor landscape, including source coverage, category and attribute mix, and sampled review themes. The comparison is bounded to collected listings and does not estimate demand, revenue, market share, or site viability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests consume account credits.

Mitigation: Use an API key you control and set a collection budget.

Risk: Search terms and target locations are sent to Crawlora.

Mitigation: Avoid confidential inputs.

Risk: Bounded map and directory results can omit businesses and do not establish complete market coverage.

Mitigation: Treat results as bounded observations, disclose coverage limits, and avoid interpreting them as demand, revenue, or site viability estimates.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Tables]

**Output Format:** [Markdown tables with a coverage ledger, business matrix, and area comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source-specific observations, unknowns, coverage limits, and retrieval dates.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
