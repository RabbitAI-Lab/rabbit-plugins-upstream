## Description:

X posts, profiles, followers, and search for agents — audience research and social listening as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and data teams use this skill to search X and retrieve post, profile, follower, and engagement data for social listening, creator research, and analytics. It can also request sentiment, topic, entity, and translation analysis for supplied text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key grants access to superagnt capabilities, and requests or submitted analysis text are sent to superagnt; paid lookups may incur charges.

Mitigation: Keep the key in a protected environment variable, review each request and its cost before running it, and avoid sending sensitive text unless authorized.

Risk: The documented curl examples contain escaped quotes that may need correction before execution.

Mitigation: Review and correct shell quoting in the selected example before running it.

Risk: The optional MCP connection requires a separate authorization step.

Mitigation: Authorize the MCP connection only when needed and review the requested access during setup.

## Reference(s):

- [X (Twitter) Data documentation](https://superagnt.com/r/ch-x-twitter-data-docs)
- [Scoped X MCP server](https://mcp.superagnt.com/mcp/x)
- [API key and account setup](https://superagnt.com/r/ch-x-twitter-data-key)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/x-twitter-data)
- [Publisher profile](https://clawhub.ai/user/superagnt)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [Structured JSON results and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested X data endpoint and supplied query or identifiers.]

## Skill Version(s):

2.0.11 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
