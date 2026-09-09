## Description:

Search Google and return the full structured SERP as JSON, including organic results, ads, knowledge graph, AI overview, related questions, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to run current Google searches through Scavio, tune search parameters, and return structured SERP data with source URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the Scavio API key are sent to Scavio's service.

Mitigation: Use SCAVIO_API_KEY from a secret store and avoid searches containing passwords, tokens, private customer data, internal project names, or other confidential material unless disclosure is acceptable.

Risk: Returned search results are external content and may be incomplete, stale, or misleading.

Mitigation: Return only API-provided results and URLs, cite sources when summarizing, and tell the user when no results are returned.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-search-api)
- [Scavio Google ClawHub page](https://clawhub.ai/scavio-ai/skills/google-search-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and Python or bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying API returns structured JSON and requires SCAVIO_API_KEY; normal requests cost 1 credit.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
