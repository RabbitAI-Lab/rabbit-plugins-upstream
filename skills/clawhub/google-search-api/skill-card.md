## Description:

Searches Google through Scavio and returns structured SERP data, including organic results, ads, knowledge graph, AI overview, related questions, related searches, top stories, videos, and pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve current Google SERP information through Scavio when a task needs up-to-date web results, knowledge graph data, AI overview content, or related questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries are sent to Scavio's API, which may expose private or sensitive query text to the provider.

Mitigation: Avoid sending private or sensitive queries unless the user is comfortable sharing them with Scavio.

Risk: Requests consume API credits and require a valid SCAVIO_API_KEY.

Mitigation: Monitor API key usage, handle 401 and 402 responses, and rotate or revoke keys if misuse is suspected.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill listing](https://clawhub.ai/scavio-ai/skills/google-search-api)
- [Scavio publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, API calls, guidance]

**Output Format:** [Markdown response with cited URLs; Scavio API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search requests send query parameters to Scavio and consume API credits.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
