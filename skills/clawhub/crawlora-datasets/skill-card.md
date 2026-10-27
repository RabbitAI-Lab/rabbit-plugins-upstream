## Description:

Searches Crawlora's pre-built datasets for records, filtered populations, facets, and nearby results, returning JSON for bulk or aggregate research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use the skill to search Crawlora's periodically refreshed public datasets, retrieve individual records, and inspect aggregate facets for population-level questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or sensitive research queries could be exposed to the hosted service.

Mitigation: Keep the API key in CRAWLORA_API_KEY and avoid sending confidential search terms.

Risk: Large paginated searches can consume API credits.

Mitigation: Limit page sizes and pagination to the records needed.

## Reference(s):

- [Crawlora dataset endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net/)
- [Crawlora Datasets on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON dataset records, search results, and facet aggregates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are paginated and come from periodically refreshed datasets.]

## Skill Version(s):

1.0.25 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
