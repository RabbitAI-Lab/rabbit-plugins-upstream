## Description:

Searches Crawlora's hosted datasets to find records, aggregate results, and retrieve items by dataset ID without running live crawls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill for bulk searches, filtered research, and aggregate questions across Crawlora's pre-indexed datasets. It can also retrieve an individual record by its dataset ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed.

Mitigation: Keep the Crawlora key private in the CRAWLORA_API_KEY environment variable; do not hardcode or commit it.

Risk: Search queries are sent to Crawlora and may contain confidential terms.

Mitigation: Avoid including confidential information in queries.

Risk: Bulk searches use credits, and results can include profile or contact details.

Mitigation: Set a credit budget before bulk searches and handle returned profile and contact details appropriately.

## Reference(s):

- [Dataset endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora Datasets on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON records and aggregate results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are paginated, and dataset freshness varies by source.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
