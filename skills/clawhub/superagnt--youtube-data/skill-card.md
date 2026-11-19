## Description:

YouTube channels, videos, transcripts, and comments for agents — no Google API key or daily quota to manage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research teams can use the skill to retrieve YouTube video, channel, search, transcript, comment, trend, and recommendation data for content research, monitoring, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's setup example checks Superagnt account credits; scanners flagged this as a possible mismatch with its YouTube purpose, while rating the skill benign with high confidence.

Mitigation: Before running the example, confirm that checking the Superagnt credit balance is relevant to your setup.

Risk: Channel email lookup can return creators' business contact emails.

Mitigation: Use contact results only for the user's stated purpose and avoid bulk unsolicited outreach.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data API key setup](https://superagnt.com/r/ch-youtube-data-key)
- [YouTube Data MCP server](https://mcp.superagnt.com/mcp/youtube)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)
- [Publisher profile](https://clawhub.ai/user/superagnt)

## Skill Output:

**Output Type(s):** [JSON, Text, Configuration instructions, Shell commands]

**Output Format:** [Structured JSON data with Markdown setup guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses depend on the requested YouTube data and supplied credentials.]

## Skill Version(s):

2.0.17 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
