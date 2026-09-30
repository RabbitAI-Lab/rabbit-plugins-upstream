## Description:

Facebook pages, posts, and group data for agents - brand and market research without scraping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, research teams, and marketing teams use this skill to query Superagnt's Facebook data API for page, post, group, marketplace, video, seller, people-search, comment, and ad-research data for social listening, market research, alerts, dashboards, and analytics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Facebook-derived people, seller, group, comment, marketplace, and ad-research data through a third-party provider.

Mitigation: Use it only for approved Facebook-derived research workflows and review privacy, platform terms, consent expectations, and applicable legal requirements before invoking people or seller endpoints.

Risk: The skill requires a Superagnt API key and sends live requests to Superagnt endpoints.

Mitigation: Store SUPERAGNT_API_KEY as a secret, avoid exposing it in prompts or logs, and confirm the user intends to use Superagnt as the provider before running calls.

Risk: Returned social, marketplace, seller, and ad data may be incomplete, sensitive, or unsuitable for automated decisions without review.

Mitigation: Review outputs before downstream use, minimize collection to the task-relevant fields, and avoid identifying or acting on individuals unless the user has a clear authorization and purpose.

## Reference(s):

- [Superagnt Facebook Data documentation](https://superagnt.com/r/ch-facebook-data-docs)
- [Superagnt API key dashboard](https://superagnt.com/r/ch-facebook-data-key)
- [Scoped Facebook MCP server](https://mcp.superagnt.com/mcp/facebook)
- [MCP client setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/facebook-data)
- [Publisher profile](https://clawhub.ai/user/superagnt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl examples, endpoint descriptions, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and SUPERAGNT_API_KEY; API responses are JSON from Superagnt endpoints.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
