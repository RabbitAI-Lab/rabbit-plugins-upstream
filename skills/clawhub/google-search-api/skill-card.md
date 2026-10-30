## Description:

Search Google through Scavio's API and receive structured SERP data, including organic results and available knowledge panels, AI Overviews, questions, and related content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve current Google search results for research and time-sensitive questions. It supports localized and filtered searches and can return a Custom Search JSON API-compatible response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and supplied locations are sent to Scavio and may contain sensitive information.

Mitigation: Do not include confidential information in queries or location parameters.

Risk: Requests consume API credits, and exposed API keys can be misused.

Mitigation: Track usage and store SCAVIO_API_KEY in an environment variable or secret store; prefer Authorization headers and redact keys from URLs and diagnostics.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Google Custom Search-compatible API documentation](https://scavio.dev/docs/google-custom-search-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Scavio API rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)

## Skill Output:

**Output Type(s):** [Search results, JSON data, Source URLs]

**Output Format:** [Structured JSON search results, suitable for concise Markdown summaries with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include organic listings, ads, knowledge graph data, AI Overview, related questions and searches, news, videos, and pagination, depending on query and request options.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata; skill frontmatter reports 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
