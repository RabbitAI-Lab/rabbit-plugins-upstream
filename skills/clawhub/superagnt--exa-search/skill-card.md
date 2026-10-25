## Description:

Connects an Exa account through the superagnt unified API for neural and keyword web search, page content retrieval, similar-link discovery, and cited Q&A.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the connected Exa account to search the live web, retrieve and summarize page content, find similar links, and answer questions with citations. The integration uses the user's Exa connection and API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and URLs are routed through superagnt, and Exa usage may incur charges on the user's account.

Mitigation: Use the integration only for requested queries and URLs, and account for applicable Exa charges.

Risk: The documented shell examples contain HTML-escaped characters and authorization-header quoting that need correction before use.

Mitigation: Review and correct the command quoting and escaped characters before running any example.

Risk: The integration requires an API key, and the optional MCP connection requires a permission review.

Mitigation: Configure the key through the environment and review the requested permissions before approving an MCP connection.

## Reference(s):

- [Exa Integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP server](https://mcp.superagnt.com/mcp)
- [MCP installation instructions](https://www.superagnt.com/install)
- [API keys](https://superagnt.com/r/ch-exa-search-key)
- [Exa connections page](https://app.superagnt.com/dashboard/connections)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/exa-search)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or structured API responses with source citations and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Exa operation and may include page text, highlights, summaries, or cited answers.]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
