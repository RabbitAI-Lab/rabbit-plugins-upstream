## Description:

Manage cold email campaigns, leads, and outreach analytics via Instantly AI through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let agents manage Instantly AI outreach workflows through Superagnt, including campaigns, leads, sending accounts, account settings, warmup, webhooks, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent broad administrative control over an Instantly outreach workspace.

Mitigation: Use a dedicated least-privilege Superagnt and Instantly connection where possible, and avoid owner or admin credentials for routine outreach.

Risk: Agent actions can send email, delete or bulk-change records, create webhooks, manage API keys, change workspace members, set domains, or transfer ownership.

Mitigation: Require explicit human confirmation before executing sensitive, destructive, bulk, or ownership-changing operations.

Risk: The integration handles operational secrets such as API keys, IMAP or SMTP passwords, and webhook headers.

Mitigation: Treat all credentials and webhook headers as secrets, and create webhooks only for trusted destinations.

## Reference(s):

- [Superagnt Instantly Outreach Documentation](https://superagnt.com/r/ch-instantly-outreach-docs)
- [Superagnt MCP Server](https://mcp.superagnt.com/mcp)
- [MCP Client Setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Dashboard and API Keys](https://superagnt.com/r/ch-instantly-outreach-key)
- [ClawHub Listing](https://clawhub.ai/jaencarrodine/skills/instantly-outreach)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with curl examples, endpoint tables, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and curl for direct API examples; MCP-capable clients can connect to the Superagnt MCP server.]

## Skill Version(s):

2.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
