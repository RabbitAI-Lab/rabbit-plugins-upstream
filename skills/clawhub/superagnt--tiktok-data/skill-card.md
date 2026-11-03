## Description:

TikTok videos, creators, sounds, and trend data for agents — content and creator research as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketing teams, and researchers use the skill to retrieve TikTok video, creator profile, collection, and search data for social listening, creator research, and content monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service receives the API credential and research queries, and requests may incur credit charges.

Mitigation: Keep the API key in an environment variable rather than chat, and review expected usage and credits before making requests.

Risk: The optional remote MCP connection's consent permissions could not be independently verified.

Mitigation: Review the OAuth consent permissions before approving the connection.

Risk: The documented shell examples may need correction before execution.

Mitigation: Inspect and correct command quoting before running an example.

## Reference(s):

- [Documentation](https://superagnt.com/r/ch-tiktok-data-docs)
- [API key and credits](https://superagnt.com/r/ch-tiktok-data-key)
- [Scoped TikTok MCP server](https://mcp.superagnt.com/mcp/tiktok)
- [MCP installation instructions](https://www.superagnt.com/install?facet=tiktok)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/tiktok-data)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions]

**Output Format:** [Structured JSON data with Markdown guidance and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live TikTok data; requires a superagnt API key and may incur credit charges.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
