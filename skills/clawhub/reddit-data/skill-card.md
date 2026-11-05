## Description:

Reddit posts, comments, users, and subreddits for agents — no Reddit app or API approval needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, research teams, and marketers can use this skill to retrieve Reddit posts, comments, user activity, and subreddit information for social listening, research, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reddit queries and the service credential are sent to Superagnt, and requests may consume paid credits.

Mitigation: Keep the API key in the SUPERAGNT_API_KEY environment variable rather than chat, and check credit usage in the Superagnt app.

Risk: The documented verification curl command contains malformed quoting, and the optional MCP connection requests permissions.

Mitigation: Correct the curl quoting before running it; review the MCP connection's requested permissions before approving.

## Reference(s):

- [Reddit Data documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Reddit Data MCP server](https://mcp.superagnt.com/mcp/reddit)
- [Reddit Data ClawHub listing](https://clawhub.ai/superagnt/skills/reddit-data)
- [Superagnt API key access](https://superagnt.com/r/ch-reddit-data-key)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON data with Markdown setup guidance and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Reddit data; paginated endpoints may return cursors.]

## Skill Version(s):

2.0.13 (source: server-resolved release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
