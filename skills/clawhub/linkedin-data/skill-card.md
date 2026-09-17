## Description:

LinkedIn API integration with a single superagnt API key (Bearer token). Fetch company profiles, jobs, people, posts, and professional network insights. Use this skill when users want LinkedIn data for sales, recruiting, or enrichment. For other social data platforms, use the social-data skill (https://clawhub.ai/superagnt/skills/social-data).

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, sales teams, recruiting teams, and data-enrichment agents use this skill to retrieve structured LinkedIn company, people, jobs, posts, article, and professional-network data through Superagnt API or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP instructions may enable a broader Superagnt platform tool surface than the reviewed LinkedIn-only scope.

Mitigation: Use a pinned LinkedIn-only MCP or tool configuration, and avoid broader discovery or enablement instructions unless broader platform access is intentional.

Risk: The skill requires a Superagnt bearer token for curl-based API calls.

Mitigation: Provide the token through SUPERAGNT_API_KEY, limit credential exposure to trusted agent sessions, and rotate the key if it is shared accidentally.

## Reference(s):

- [LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [LinkedIn Data ClawHub listing](https://clawhub.ai/jaencarrodine/skills/linkedin-data)
- [Superagnt LinkedIn MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [Superagnt MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Dashboard and API keys](https://superagnt.com/r/ch-linkedin-data-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON tool schemas and inline bash curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY for curl use; MCP-capable clients can connect to the scoped LinkedIn MCP server.]

## Skill Version(s):

2.0.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
