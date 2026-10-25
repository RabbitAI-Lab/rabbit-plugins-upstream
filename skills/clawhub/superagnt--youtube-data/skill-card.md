## Description:

YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and content or marketing teams can search YouTube and retrieve channel and video details, transcripts, comments, trends, and recommendations for content research and creator intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider API key is sent to superagnt and also authorizes other provider capabilities; API requests consume credits.

Mitigation: Store the key securely rather than pasting it into chat, and check the provider's credit balance and expected usage before running large requests.

Risk: Channel email lookup returns creators' business contact information that could be misused for unsolicited outreach.

Mitigation: Use contact details only for the user's stated purpose and do not use them for bulk unsolicited outreach.

Risk: The documented shell examples contain escaped quote entities that may need correction before execution.

Mitigation: Review and correct the shell quoting in each example before running it.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data API endpoint](https://api.superagnt.com/v1/data/youtube)
- [Scoped YouTube MCP server](https://mcp.superagnt.com/mcp/youtube)
- [MCP client installation instructions](https://www.superagnt.com/install?facet=youtube)
- [superagnt app and API keys](https://superagnt.com/r/ch-youtube-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/youtube-data)

## Skill Output:

**Output Type(s):** [JSON data, Guidance]

**Output Format:** [Structured JSON from YouTube data endpoints, with Markdown setup guidance and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Response fields vary by endpoint and may include video and channel details, search results, comments, subtitles, recommendations, and creator business contact emails.]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
