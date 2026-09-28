## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let agents manage Attio CRM records, lists, notes, tasks, meetings, call recordings, files, SCIM users and groups, and webhooks through a connected superagnt account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad Attio administrative capabilities, including SCIM user and group changes, webhook management, file access, transcript access, and create, update, or delete operations.

Mitigation: Use a least-privilege Attio or superagnt connection where possible and require explicit user confirmation before SCIM, webhook, file, transcript, or create, update, or delete actions.

Risk: Actions may run through the user's connected Attio credentials and affect workspace data or settings.

Mitigation: Keep actions scoped to the user's request and verify the target object, record, list, user, group, webhook, file, or meeting before execution.

## Reference(s):

- [superagnt Attio documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [superagnt API key dashboard](https://superagnt.com/r/ch-attio-crm-key)
- [superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)
- [Alternative MCP server](https://mcp.superagnt.com/mcp)
- [MCP client setup prompt](https://mcp.superagnt.com/agent-setup/prompt.md)
- [ClawHub listing](https://clawhub.ai/superagnt/skills/attio-crm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with curl commands, endpoint tables, and JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Attio account.]

## Skill Version(s):

2.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
