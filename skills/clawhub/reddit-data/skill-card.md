## Description:

Reddit posts, comments, and subreddit data for agents — community research and sentiment as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and research, marketing, or product teams use this skill to search Reddit and gather subreddit, post, comment, and user data for community monitoring, content research, and sentiment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests send the Superagnt credential and may consume account credits.

Mitigation: Keep SUPERAGNT_API_KEY private and review expected credit usage before running requests.

Risk: Some documented shell examples contain escaped quotes that may need correction before execution.

Mitigation: Review and correct the shell command quoting before running an example.

## Reference(s):

- [Reddit Data documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Reddit Data MCP server](https://mcp.superagnt.com/mcp/reddit)
- [MCP installation guide](https://www.superagnt.com/install?facet=reddit)
- [API key and account](https://superagnt.com/r/ch-reddit-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/reddit-data)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [Structured Reddit API response data in JSON; Markdown instructions with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are retrieved from Reddit Data endpoints; requests may use cursor pagination.]

## Skill Version(s):

2.0.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
