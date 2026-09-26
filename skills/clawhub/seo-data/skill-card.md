## Description:

SEO and search intelligence for agents: live Google results, keyword research, competitor and backlink gaps, page audits and AI answer visibility.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and SEO operators use this skill to let agents query Superagnt SEO endpoints for live SERP results, keyword research, competitor gaps, backlink analysis, page audits, AI answer visibility, and technology stack research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEO targets, search queries, URLs, and related research terms are sent to Superagnt's service.

Mitigation: Use only approved targets and avoid confidential client domains, private URLs, or sensitive research terms unless the provider's data handling and billing terms have been reviewed.

Risk: The skill requires a Superagnt API key and uses priced API calls.

Mitigation: Store the key in SUPERAGNT_API_KEY, avoid exposing it in prompts or logs, and verify credits and billing terms before high-volume calls.

## Reference(s):

- [SEO Data documentation](https://superagnt.com/r/ch-seo-data-docs)
- [Scoped MCP server](https://mcp.superagnt.com/mcp/seo)
- [Agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/seo-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl examples, endpoint descriptions, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API responses are JSON and calls may be billed per request or returned row.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
