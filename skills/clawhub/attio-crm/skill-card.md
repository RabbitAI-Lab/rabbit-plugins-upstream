## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect agents to an Attio workspace and manage CRM records, lists, attributes, notes, tasks, meetings, files, webhooks, and SCIM resources through Superagnt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give agents broad access to CRM, identity, webhook, file, and call transcript data.

Mitigation: Use the least-privileged Attio and Superagnt access available, and scope connected accounts to the data needed for the task.

Risk: Delete, overwrite, SCIM, webhook, file, and transcript operations can affect sensitive workspace data or access controls.

Mitigation: Require explicit human approval before deletes, overwrites, SCIM user or group changes, webhook edits, file downloads or deletes, or transcript retrieval.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jaencarrodine/skills/attio-crm)
- [Superagnt Attio documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [Superagnt MCP setup instructions](https://mcp.superagnt.com/agent-setup/prompt.md)
- [Superagnt connections dashboard](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with curl command examples and JSON operation schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERAGNT_API_KEY and a connected Attio account; operations run against the user's Attio credentials.]

## Skill Version(s):

2.0.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
