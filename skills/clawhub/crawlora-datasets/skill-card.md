## Description:

Queries Crawlora's hosted datasets for filtered records, aggregate breakdowns, nearby results, and individual items without live-crawling source platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to search public, pre-indexed datasets, compare populations with facets, and retrieve records for research or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataset requests send the API key and requested routes and query parameters to Crawlora.

Mitigation: Use a key stored in CRAWLORA_API_KEY and avoid putting secrets, private personal data, or confidential business details in queries.

## Reference(s):

- [Crawlora Datasets skill release](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)
- [Crawlora dataset endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON dataset responses or concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are paginated and drawn from periodically refreshed datasets, not live source pages.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
