## Description:

Neural web search, parsed page contents, find-similar discovery, and agentic Q&A over the live web through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add live Exa web search, page-content retrieval, similar-link discovery, and cited question answering to agent workflows through a connected superagnt account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, requested URLs, and selected content options are sent through Superagnt to the connected Exa account.

Mitigation: Use the skill only for data that is appropriate to send to the provider path, and avoid submitting sensitive queries or URLs unless approved for that account.

Risk: Optional MCP setup can expose the same Exa-backed actions as native client tools after approval.

Mitigation: Review the MCP server connection and requested permissions in the client before approving access.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP server](https://mcp.superagnt.com/mcp)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/exa-search)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with JSON schemas and inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Exa account; API responses may include web search results, parsed page text, summaries, highlights, citations, or structured answers.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
