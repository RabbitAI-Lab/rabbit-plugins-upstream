## Description:

Reddit posts, comments, users, and subreddits for agents — no Reddit app or API approval needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, social listening agents, marketing and research teams can retrieve Reddit post, comment, user, and subreddit data for monitoring, creator intelligence, research, alerts, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests use a Superagnt API key, and the security guidance notes that benign scanner results do not mean risk-free use.

Mitigation: Keep the key in the intended environment and review the documented requests before use.

Risk: The security summary notes an apparent credits lookup outside the stated Reddit data purpose.

Mitigation: Review the documented /v1/credits verification request and confirm that it is acceptable before running it.

## Reference(s):

- [Superagnt Reddit Data documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Reddit Data MCP server](https://mcp.superagnt.com/mcp/reddit)
- [Superagnt client installation guide](https://www.superagnt.com/install?facet=reddit)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown instructions with HTTP GET requests and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; responses depend on the selected Reddit endpoint.]

## Skill Version(s):

2.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
