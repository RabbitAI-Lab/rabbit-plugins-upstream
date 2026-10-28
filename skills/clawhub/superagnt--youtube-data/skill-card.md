## Description:

YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, and creator intelligence teams can use the skill to search YouTube and retrieve channel, video, transcript, comment, trend, and recommendation data for research, monitoring, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP setup may not enforce YouTube-only access as narrowly as its description suggests.

Mitigation: For YouTube-only access, use the documented REST operations or verify the dedicated MCP server's allowed tools before connecting; do not rely on the URL alone to restrict access.

Risk: An exposed API key or unmonitored usage can consume account credits.

Mitigation: Keep SUPERAGNT_API_KEY private and monitor credit spending.

Risk: Channel email lookup returns creators' business contact information.

Mitigation: Use creator email results only for the user's stated purpose and avoid bulk unsolicited outreach.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data listing](https://clawhub.ai/superagnt/skills/youtube-data)
- [Scoped YouTube MCP server](https://mcp.superagnt.com/mcp/youtube)
- [MCP client setup](https://www.superagnt.com/install?facet=youtube)
- [API key setup](https://superagnt.com/r/ch-youtube-data-key)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [Structured JSON API responses with Markdown instructions and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live YouTube data; API access requires SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.10 (source: frontmatter; server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
