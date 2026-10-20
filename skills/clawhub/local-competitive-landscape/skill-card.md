## Description:

Compare observed local business supply, categories, attributes, hours, and review-sample themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and business planners use this skill to compare observed competitors and service coverage across matched local areas without treating search results as demand or revenue estimates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, locations, and the API key are sent to Crawlora.

Mitigation: Use only with approval to send this data; keep CRAWLORA_API_KEY in an environment variable or secret manager and avoid sensitive private request content.

Risk: Incomplete or stale map listings can make observed gaps appear conclusive.

Mitigation: Report source-specific coverage, retrieval dates, and unknowns; present gaps as observations rather than demand, revenue, or site-viability claims.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/local-competitive-landscape)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown coverage ledger, business matrix, and area comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records source coverage, retrieval dates, unknowns, and sample limitations.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
