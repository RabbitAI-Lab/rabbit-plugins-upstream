## Description:

Facebook pages, posts, and group data for agents - brand and market research without scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, marketing researchers, and data teams use this skill to query Facebook page, post, group, marketplace, video, and ad data through Superagnt APIs for social listening, content research, alerts, dashboards, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Facebook queries and returned data are sent through a third-party Superagnt API.

Mitigation: Review Superagnt privacy terms and use the skill only for Facebook data approved for third-party processing.

Risk: The MCP setup can expose broader Superagnt tool families beyond the Facebook endpoints.

Mitigation: Enable only the scoped Facebook MCP server or explicitly review and approve any additional tool families before use.

Risk: Security evidence flags ambiguity around scraping claims and sensitive investigative use.

Mitigation: Confirm the data-source method and avoid sensitive targets unless the use case has legal, privacy, and policy approval.

## Reference(s):

- [Superagnt Facebook Data Documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Superagnt Facebook MCP Server](https://mcp.superagnt.com/mcp/facebook)
- [Superagnt MCP Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub facebook-data Listing](https://clawhub.ai/jaencarrodine/skills/facebook-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands and JSON API schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl; API responses are structured JSON from Superagnt endpoints.]

## Skill Version(s):

2.0.2 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
