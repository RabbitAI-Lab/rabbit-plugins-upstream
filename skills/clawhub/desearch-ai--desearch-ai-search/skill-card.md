## Description:

AI Search searches X posts and the web and can return a summary. Supported AI Search source IDs are web and twitter. For web-only results, use the Search API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[desearch-ai](https://clawhub.ai/user/desearch-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can search the web and X for a query, retrieve links and posts, and optionally receive an AI-generated summary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and supplied parameters, including account identifiers or URLs, and the API key are sent to Desearch.

Mitigation: Send only information you are authorized to share with Desearch, keep secrets and confidential data out of queries and parameters, and consider whether you trust the service before providing its API key.

## Reference(s):

- [Desearch](https://desearch.ai)
- [Desearch API Reference: AI Search](https://desearch.ai/docs/api-reference/post-desearch-ai-search)
- [Desearch Search API Guide](https://desearch.ai/docs/guide/apis/search-api)
- [Desearch MCP Guide](https://desearch.ai/docs/guide/sdk/mcp)
- [Desearch Console](https://console.desearch.ai)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Search results and optional summaries as text or JSON printed to standard output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the query and selected source; AI Search supports web and X (Twitter).]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
