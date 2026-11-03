## Description:

YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, and marketing teams can use the skill to search and monitor YouTube channels and videos, and gather metadata, transcripts, comments, and recommendations for content research and creator intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an API credential with requests, so exposure of the key could allow unauthorized use of the account and its credits.

Mitigation: Keep SUPERAGNT_API_KEY private and provide it through the agent's protected environment rather than embedding it in prompts or shared files.

Risk: API queries consume credits, and creator email lookup returns personal contact data.

Mitigation: Use queries for the user's stated purpose, check the account's credit balance, and use creator emails only for that purpose; do not use them for bulk unsolicited outreach.

Risk: The optional MCP server's live behavior and permissions were not verified.

Mitigation: Review the requested permissions before connecting the MCP server.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data MCP server](https://mcp.superagnt.com/mcp/youtube)
- [MCP client setup](https://www.superagnt.com/install?facet=youtube)
- [superagnt API key setup](https://superagnt.com/r/ch-youtube-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Research guidance]

**Output Format:** [Structured JSON API responses with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Superagnt API key and available API credits.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
