## Description:

YouTube channels, videos, transcripts, and comments for agents — content research and channel intelligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and marketing teams use the skill to search and analyze YouTube channels, videos, comments, subtitles, recommendations, and trends for content research and creator intelligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests are sent to Superagnt and consume account credits.

Mitigation: Keep the API key secret and check account credits before making requests.

Risk: Channel email lookups can return creators' personal contact data.

Mitigation: Use contact details only for the stated research purpose and avoid bulk unsolicited outreach.

Risk: An optional MCP connection may expose tools beyond YouTube when the workspace enables a broader set of tools.

Mitigation: Inspect enabled MCP tools before connecting and use a scope appropriate to the task.

## Reference(s):

- [YouTube Data documentation](https://superagnt.com/r/ch-youtube-data-docs)
- [YouTube Data listing](https://clawhub.ai/superagnt/skills/youtube-data)
- [Superagnt connection documentation](https://www.superagnt.com/docs/connect)
- [YouTube Data MCP server](https://mcp.superagnt.com/mcp/youtube)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured YouTube data in JSON, with Markdown instructions and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests require a SUPERAGNT_API_KEY and use account credits.]

## Skill Version(s):

2.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
