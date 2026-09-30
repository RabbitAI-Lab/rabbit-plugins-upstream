## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let agents manage Instantly AI outreach workflows, including campaigns, leads, sending accounts, analytics, enrichment, webhooks, and workspace settings through superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Instantly workspace control can reach admin, billing, API-key, procurement, webhook, and credential-related operations beyond basic outreach tasks.

Mitigation: Install only when that scope is needed, use the narrowest possible account or key, and keep agent actions limited to the endpoints required by the user's request.

Risk: Destructive or outbound actions can delete or overwrite data, send email, change ownership or members, alter domains, create webhooks, expose password-related fields, or affect billing and purchases.

Mitigation: Require explicit user confirmation before purchases, outbound email, API-key changes, workspace/member/domain/owner changes, webhook creation, password retrieval, billing access, deletes, or overwrites.

## Reference(s):

- [superagnt Instantly AI documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [superagnt MCP server](https://mcp.superagnt.com/mcp)
- [MCP agent setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub skill listing](https://clawhub.ai/superagnt/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash code blocks, API endpoint tables, and tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Instantly AI account.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
