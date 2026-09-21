## Description:

Company firmographics, tech stack, headcount, and intelligence from a domain - agent-ready account research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, sales operations teams, and go-to-market agents use this skill to enrich company domains or names with account intelligence for account research, ICP filtering, target discovery, and market mapping.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company and domain queries, domain email results, and the Superagnt API key are sent to Superagnt.

Mitigation: Use a scoped API key where possible, avoid submitting sensitive account lists unless approved, and handle domain email results as personal data.

Risk: The skill describes broader Superagnt MCP platform tools beyond the advertised company-enrichment scope.

Mitigation: Keep the agent limited to the company-enrichment endpoints unless a human explicitly approves enabling additional Superagnt tool families.

Risk: Bulk enrichment and discovery can process large account lists through a third-party service.

Mitigation: Confirm data-sharing approval and credit usage expectations before running bulk operations.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/jaencarrodine/skills/company-enrichment)
- [Superagnt company enrichment documentation](https://superagnt.com/r/ch-company-enrichment-docs)
- [Superagnt MCP company enrichment endpoint](https://mcp.superagnt.com/mcp/company-enrichment)
- [Superagnt agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt API key dashboard](https://superagnt.com/r/ch-company-enrichment-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON endpoint schemas and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API usage; MCP-capable clients can connect to the scoped Superagnt MCP server.]

## Skill Version(s):

2.0.5 (source: SKILL.md frontmatter, artifact metadata, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
