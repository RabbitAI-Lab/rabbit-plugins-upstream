## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jaencarrodine](https://clawhub.ai/user/jaencarrodine)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let agents manage Attio CRM data and workflows through Superagnt, including records, lists, notes, tasks, meetings, files, SCIM users and groups, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad Attio administration, file, recording, deletion, and webhook actions through one Superagnt API key.

Mitigation: Use the least-privileged Attio and Superagnt setup available, avoid production-wide credentials where possible, and require explicit review before destructive or administrative actions.

Risk: Deletes, overwrites, SCIM user or group changes, file downloads or deletions, recording or transcript access, and webhook creation can affect sensitive CRM data or account configuration.

Mitigation: Review proposed requests before execution and restrict use to trusted operators and connected workspaces.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/jaencarrodine/skills/attio-crm)
- [Superagnt Attio Documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [Superagnt MCP Server](https://mcp.superagnt.com/mcp)
- [Superagnt Agent Setup](https://mcp.superagnt.com/agent-setup/prompt.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline bash code blocks and JSON request schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SUPERAGNT_API_KEY and a connected Attio workspace.]

## Skill Version(s):

2.0.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
