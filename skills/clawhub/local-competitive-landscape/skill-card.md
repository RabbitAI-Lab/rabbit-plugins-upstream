## Description:

Compare observed local business supply, categories, attributes, hours, and review-sample themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp. Use for matched-area competitor landscapes and coverage comparisons; for user-supplied candidate-site screening with access and diligence gaps, use business-location-screening. Neither estimates demand, sales, or site viability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts and developers use this skill to compare observed businesses across defined areas and produce a traceable coverage ledger, business matrix, and area comparison. It supports matched-frame competitor and coverage analysis while keeping data gaps and search omission risk visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and locations used for a comparison are sent to Crawlora.

Mitigation: Use your own Crawlora API key and share only search terms and locations you are comfortable sending to that provider.

Risk: Bounded and ranked map or directory results can omit relevant businesses, so an observed gap may reflect search coverage.

Mitigation: Use matched comparison frames, disclose result bounds and search omission risk, and describe findings as observations from the collected sample.

Risk: Business listings, ratings, and review samples do not establish demand, revenue, or site viability.

Mitigation: Do not present observed counts or review themes as demand, sales, market share, or site-viability estimates.

Risk: Large collection limits can consume more Crawlora credits.

Mitigation: Set page and result limits to control credit usage.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Tables]

**Output Format:** [Markdown with concise narrative, a coverage ledger, and a business comparison matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-specific observations with retrieval dates, bounded-result context, unknowns, and match confidence.]

## Skill Version(s):

1.0.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
