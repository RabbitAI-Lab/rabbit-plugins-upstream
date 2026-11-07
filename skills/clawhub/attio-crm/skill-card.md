## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect an Attio workspace to AI agents and workflows for managing CRM records, lists, notes, tasks, meetings, and related activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Attio account may be used to delete or change records, settings, access, or send outbound actions.

Mitigation: Use only endpoints needed for the user's request and require explicit confirmation before destructive, access-changing, or outbound actions.

Risk: The skill requires a superagnt API key to access a connected Attio workspace.

Mitigation: Store the API key securely and use the integration only when the user trusts superagnt with the connected Attio access and requested data.

Risk: The bundled-file review does not cover the hosted API or optional MCP server implementation.

Mitigation: Review and trust the service implementation before connecting sensitive workspace data through its API or MCP server.

## Reference(s):

- [Attio integration documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [MCP client setup](https://www.superagnt.com/install)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with endpoint descriptions, tool schemas, and inline curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents the Attio API surface and examples for agent use.]

## Skill Version(s):

2.0.13 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
