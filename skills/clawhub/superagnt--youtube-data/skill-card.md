## Description:

YouTube channels, videos, transcripts, and comments for agents — no Google API key or daily quota to manage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing teams use agents to search YouTube and retrieve channel and video details, transcripts, comments, recommendations, and trending content for research and monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed, and lookup requests may consume credits.

Mitigation: Keep SUPERAGNT_API_KEY private and check expected credit use before making requests.

Risk: Channel email lookup returns business contact information.

Mitigation: Use returned emails only for the user's stated purpose; do not use them for bulk unsolicited outreach.

Risk: Shell examples or optional MCP permissions may not match the user's environment or intended access.

Mitigation: Review and correct shell commands before running them, and review the requested permissions before connecting the MCP server.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data API endpoint](https://api.superagnt.com/v1/data/youtube)
- [YouTube Data MCP server](https://mcp.superagnt.com/mcp/youtube)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON data, with text summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live YouTube data; requests may consume API credits.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
