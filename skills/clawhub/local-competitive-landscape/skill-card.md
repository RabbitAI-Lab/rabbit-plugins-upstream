## Description:

Compares observed local business listings, attributes, hours, and review themes across defined areas using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, and Yelp.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts and developers compare observed competitor coverage and services across matched local areas, with source-specific evidence and clear limits on what search results establish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, locations, and comparison data are sent to Crawlora using a Crawlora API key.

Mitigation: Use only if this data transfer is acceptable; keep the key in the environment and exclude secrets and unnecessary personal data from queries.

Risk: Bounded or stale listings can omit businesses and overstate apparent service gaps.

Mitigation: Record source coverage and retrieval dates, verify uncertain listings, and label conclusions as observations of the collected sample.

Risk: Default country or language settings can skew non-US or non-English comparisons.

Mitigation: Set matching country and language parameters deliberately for each compared area.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/local-competitive-landscape)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown coverage ledger, business matrix, and area comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports source, retrieval date, bounded coverage, unknowns, and match confidence; does not estimate demand or sales.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
