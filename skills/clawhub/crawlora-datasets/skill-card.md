## Description:

Queries Crawlora's hosted public datasets for searches, aggregate breakdowns, nearby records, and individual records, returning JSON without crawling each source live.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to search and analyze Crawlora's pre-indexed public datasets, compare populations through facets, and retrieve records by dataset ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the API key are sent to Crawlora's hosted API.

Mitigation: Use a dedicated Crawlora key and keep secrets out of query text.

Risk: Public-contact and business records may require careful handling.

Mitigation: Use returned data in accordance with applicable policy and law.

## Reference(s):

- [Crawlora dataset endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON API responses and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated results; hosted datasets are refreshed periodically rather than in real time.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
