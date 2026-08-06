## Description:

Timothe Growth Calendar helps agents plan, inspect, and generate SEO articles on a Timothe content calendar.

This skill is ready for commercial/non-commercial use.

## Publisher:

[timothe](https://clawhub.ai/user/timothe)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to inspect a Timothe workspace's content calendar, research SEO topics, plan article clusters, schedule or edit planned articles, and generate or edit article drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spend Timothe credits for planning, research, and article generation actions.

Mitigation: Check the credit balance, state the cost and expected result, and require clear user confirmation before expensive actions such as plan_cluster or generate_article.

Risk: The skill can schedule, edit, move, or delete planned content in the connected workspace.

Mitigation: List the affected articles or dates before changes, use batch operations deliberately, and require explicit confirmation before destructive changes.

Risk: Poorly researched plans can create duplicate or low-value SEO content that later incurs generation costs.

Mitigation: Run list_articles and use the research tools to check overlap, demand, market, and competition before planning a cluster or planting articles.

## Reference(s):

- [Timothe Growth Calendar ClawHub release](https://clawhub.ai/timothe/skills/growth-calendar)
- [Timothe publisher profile](https://clawhub.ai/user/timothe)
- [Growth Calendar product page](https://timothe.ai/growth-calendar)
- [Growth Calendar hosted MCP server](https://timothe.ai/mcp/growth-calendar)
- [Growth Calendar app](https://timothe.ai/tools/growth-calendar/app)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and structured MCP tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke hosted MCP tools that read or modify a Timothe workspace and may spend credits when authorized.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
