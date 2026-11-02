## Description:

Compare observed chain-store coverage using Crawlora Starbucks directories, live chain locators, and Google Maps business records. Use for branch counts, geographic overlap, amenity coverage, or footprint gaps within a defined area with source caps and identity uncertainty preserved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can compare observed store locations for selected chains within defined geographic boundaries. They use the results to review branch counts, geographic overlap, amenities, and coverage gaps while preserving source limits and uncertainty about location identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search locations and terms are sent to Crawlora, and requests consume credits.

Mitigation: Use a Crawlora key you control, define a geographic scope and credit budget, and share only locations and terms you are comfortable sending.

Risk: Capped or partial source results and uncertain chain matches can produce incomplete or incorrect footprint counts.

Mitigation: Track query boundaries, pages, caps, and crawl times; verify cross-source matches with address and coordinate evidence; report unknown and incomplete areas explicitly.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub release page](https://clawhub.ai/crawlora-org/skills/chain-store-footprint-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Tables]

**Output Format:** [Markdown report with a branch evidence ledger and deduplicated area/brand tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source IDs, URLs, dates, crawl times, result caps, and identity uncertainty; counts are scoped to the defined geography and available sources.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
