## Description:

Connects agents to Exa through Superagnt for web search, page content, similar links, and cited answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can research live web topics, retrieve page content, find related sources, and generate answers with citations through a connected Exa account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Superagnt proxies Exa queries under the user's connected account and billing limits.

Mitigation: Connect only an intended Exa account and review its access and billing limits before use.

Risk: Sharing the Superagnt API key in chat may expose account access.

Mitigation: Set SUPERAGNT_API_KEY as an environment variable rather than pasting it into chat.

Risk: The optional MCP server may request additional permissions.

Mitigation: Review MCP server permissions separately before approving that setup path.

## Reference(s):

- [Exa integration documentation](https://superagnt.com/r/ch-exa-search-docs)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [Text, API calls, Shell commands]

**Output Format:** [Markdown answers with citations, JSON search results, or curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a connected Exa account; queries use the user's vendor rate limits and billing.]

## Skill Version(s):

2.0.7 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
