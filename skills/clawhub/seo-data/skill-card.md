## Description:

SEO and search intelligence for agents: live Google results, keyword research, competitor and backlink gaps, page audits and AI answer visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

SEO practitioners, marketers, and developers use the skill to retrieve search, keyword, competitor, backlink, page audit, AI visibility, and technology stack data for research and planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted search terms, URLs, and prompts are sent to the provider API or optional MCP service and may contain sensitive information.

Mitigation: Review each input and omit sensitive content before making a request.

Risk: API calls consume credits, and larger result depths or row limits can increase cost.

Mitigation: Begin with default or small result limits and increase them deliberately.

Risk: The documented shell examples may need quote corrections, and an incorrectly expanded API key can prevent a request or expose credentials.

Mitigation: Keep SUPERAGNT_API_KEY secret; correct shell quoting and confirm the variable expands as intended before use.

## Reference(s):

- [SEO Data documentation](https://superagnt.com/r/ch-seo-data-docs)
- [Scoped SEO MCP server](https://mcp.superagnt.com/mcp/seo)
- [SEO Data ClawHub listing](https://clawhub.ai/superagnt/skills/seo-data)

## Skill Output:

**Output Type(s):** [API data, JSON, Analysis, Text summaries]

**Output Format:** [Structured SEO research results with agent-readable summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live, synchronous results; provider charges per call and costs can scale with returned rows.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
