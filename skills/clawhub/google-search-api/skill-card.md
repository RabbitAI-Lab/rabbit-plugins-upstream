## Description:

Searches Google through Scavio and returns a structured JSON SERP with organic results, ads, knowledge graph, AI overview, related questions, related searches, top stories, videos, and pagination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and operators use this skill when they need current Google search results or SERP features such as organic links, AI overview, knowledge graph, related questions, and localized query results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and related request parameters are sent to Scavio.

Mitigation: Use the skill only for queries acceptable to share with Scavio and review organizational data-handling requirements before deployment.

Risk: The skill requires a Scavio API key and consumes Scavio credits per request.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store, keep it out of source code, and monitor usage limits.

## Reference(s):

- [Scavio Search API documentation](https://scavio.dev/docs/search-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/google-search-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON SERP data and inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and uses Scavio credits for each request.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
