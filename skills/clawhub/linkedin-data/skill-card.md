## Description:

LinkedIn API integration using a Superagnt Bearer token for fetching company profiles, jobs, people, posts, and professional network insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to add LinkedIn company, profile, job, post, and professional network data to sales, recruiting, enrichment, market intelligence, and CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn research queries and targets are sent to Superagnt.

Mitigation: Install only when that data sharing is acceptable, and avoid sending unnecessary sensitive targets or query details.

Risk: The skill describes dynamically expanding the Superagnt MCP tool surface beyond LinkedIn.

Mitigation: Prefer the documented LinkedIn endpoints unless broader Superagnt platform access is intentional, and review MCP tool expansion before enabling additional tool families.

## Reference(s):

- [Superagnt LinkedIn Data documentation](https://superagnt.com/r/ch-linkedin-data-docs)
- [Superagnt API key dashboard](https://superagnt.com/r/ch-linkedin-data-key)
- [LinkedIn MCP server](https://mcp.superagnt.com/mcp/linkedin)
- [MCP agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/linkedin-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with endpoint tables, JSON tool schemas, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY; API calls return structured JSON from Superagnt LinkedIn endpoints.]

## Skill Version(s):

2.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
