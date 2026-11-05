## Description:

Instagram profiles, posts, reels, and hashtags for agents — influencer and brand research with no Instagram login, Business account, or Meta app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and research teams use agents to retrieve Instagram profile, post, Reel, location, and hashtag data for creator research, social listening, content monitoring, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to Superagnt, and API requests may use account credits.

Mitigation: Avoid sending sensitive query data, use the intended account, and monitor its credit balance.

Risk: The API key is a bearer credential, and the hosted service has not been independently verified.

Mitigation: Store the key securely, limit who and what can access it, and review the service before sending sensitive data.

Risk: The documented shell examples contain escaped quote entities that may need correction before execution; the MCP option requests OAuth permissions.

Mitigation: Correct and review the command quoting before running examples, and inspect the MCP permissions before authorizing access.

## Reference(s):

- [Instagram Data documentation](https://superagnt.com/r/ch-instagram-data-docs)
- [Instagram Data API](https://api.superagnt.com/v1/data/instagram)
- [Scoped Instagram MCP server](https://mcp.superagnt.com/mcp/instagram)
- [MCP installation guide](https://www.superagnt.com/install?facet=instagram)
- [API key and account credits](https://superagnt.com/r/ch-instagram-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/instagram-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON API responses with Markdown usage instructions and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Instagram data returned by the selected endpoint; access depends on the configured API key and account credits.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
