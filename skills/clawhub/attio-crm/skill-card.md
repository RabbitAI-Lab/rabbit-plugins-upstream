## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to automate Attio CRM records, lists, notes, tasks, meetings, and related workflows through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad write and delete access can change or remove CRM records and list entries.

Mitigation: Use only endpoints needed for the request and obtain explicit confirmation before deletes or overwrites.

Risk: SCIM user and group operations can change workspace access.

Mitigation: Confirm requested provisioning changes with the user before modifying SCIM users or groups.

Risk: Webhooks and file uploads can initiate outbound actions.

Mitigation: Require explicit user confirmation before creating webhooks or uploading files.

## Reference(s):

- [Attio integration documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [MCP client setup](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Attio connection setup](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-connected Attio account and SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.7 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
