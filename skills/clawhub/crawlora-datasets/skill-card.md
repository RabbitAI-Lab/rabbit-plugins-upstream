## Description:

Queries Crawlora's hosted, pre-indexed public datasets through search, facet, item, and nearby endpoints so agents can return structured JSON for bulk research and aggregate analysis without live-crawling each source.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and research analysts use this skill to search and aggregate Crawlora's hosted datasets for market, product, hiring, app, social, housing, and company research. It is best suited for population-level questions, filtered lists, and dataset record lookup rather than real-time page scraping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataset searches, filters, coordinates, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, avoid unrelated secrets or sensitive personal data in query parameters, and keep the API key in the environment rather than files or shared outputs.

Risk: Hosted datasets refresh on a schedule and may not reflect real-time source state.

Mitigation: Use the skill for aggregate and bulk dataset analysis; verify time-sensitive results against current sources or a live lookup workflow when recency is critical.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; GET-only helper returns paginated API responses.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
