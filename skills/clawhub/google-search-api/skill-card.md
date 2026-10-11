## Description:

Search Google through Scavio to retrieve structured results, including organic listings, ads, knowledge graph data, AI overviews, and related questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can look up current web information and summarize Google search results with source links, including organic results and available SERP features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and localization parameters are sent to Scavio, potentially exposing sensitive searches.

Mitigation: Avoid private queries unless Scavio's data handling terms meet your needs.

Risk: An exposed API key could permit unauthorized use, and requests may incur charges after the free allowance.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and monitor API credit usage.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Cited Markdown summaries and structured JSON search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available results may include organic links, ads, knowledge graph data, AI overviews, related questions, and pagination.]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
