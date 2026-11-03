## Description:

Reddit posts, comments, and subreddit data for agents — community research and sentiment as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research, and marketing teams can use agents to retrieve Reddit posts, comments, subreddit details, and user activity for community research, sentiment analysis, and social listening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup parameters and the Superagnt API key are sent to the third-party provider, and requests may consume credits.

Mitigation: Review the data sent and expected usage; keep the key in the environment and avoid exposing it in commands or logs.

Risk: The documented shell examples contain quoting and variable expansion that may fail when copied verbatim.

Mitigation: Correct shell quoting and variable expansion before running the examples.

Risk: The MCP option requires OAuth approval.

Mitigation: Review the permissions shown during OAuth approval.

## Reference(s):

- [Reddit Data documentation](https://superagnt.com/r/ch-reddit-data-docs)
- [Reddit Data API endpoint](https://api.superagnt.com/v1/data/reddit)
- [Reddit Data MCP server](https://mcp.superagnt.com/mcp/reddit)
- [API key setup](https://superagnt.com/r/ch-reddit-data-key)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON responses with Markdown instructions and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Reddit data varies with query parameters and available service credits.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
