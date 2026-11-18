## Description:

YouTube channels, videos, transcripts, and comments for agents — no Google API key or daily quota to manage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to search YouTube and retrieve video and channel details, transcripts, comments, recommendations, and trending content for research, monitoring, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an API key with the external superagnt service.

Mitigation: Use the skill only if you trust the API provider, and provide the key through SUPERAGNT_API_KEY.

Risk: The service includes channel email lookup, which can return creators’ business contact information.

Mitigation: Use returned contact data only for the stated purpose; do not use it for bulk unsolicited outreach.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data MCP server](https://mcp.superagnt.com/mcp/youtube)
- [YouTube Data API endpoint reference](https://api.superagnt.com/v1/data/youtube)

## Skill Output:

**Output Type(s):** [API calls, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown instructions with inline shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; returned data depends on the selected endpoint and available workspace credits.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
