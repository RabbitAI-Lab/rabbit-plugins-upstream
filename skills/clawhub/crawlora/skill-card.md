## Description:

Fetches structured public web data through the Crawlora REST API, returning JSON for searches, listings, reviews, transcripts, trends, financial data, and places.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve public website data for research, price comparisons, reviews, and summaries without parsing website HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-data queries are sent to Crawlora and may disclose sensitive search terms, addresses, locations, or private URLs.

Mitigation: Use only when comfortable sending the query to Crawlora; avoid sensitive or identifying details unless required for the task.

Risk: The Crawlora API key could be exposed if copied into prompts or logs.

Mitigation: Keep CRAWLORA_API_KEY in the environment and never paste it into prompts or logs.

## Reference(s):

- [Crawlora endpoint catalog](artifact/reference/catalog.md)
- [Crawlora](https://crawlora.net)
- [Crawlora skill on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured JSON API responses and agent-written summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be paginated; successful API requests use credits.]

## Skill Version(s):

1.0.30 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
