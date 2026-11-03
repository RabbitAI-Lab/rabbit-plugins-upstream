## Description:

Manage Attio CRM records, lists, notes, tasks, and meetings through the superagnt unified API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superagnt](https://clawhub.ai/user/superagnt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use the skill to let AI agents manage and automate work in an Attio CRM workspace, including records, lists, notes, tasks, meetings, and webhooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account can access sensitive CRM data and make destructive changes, modify users or groups, or configure webhook destinations.

Mitigation: Limit the connected account's permissions; review user and group changes, deletions, and webhook destinations, and require explicit confirmation before destructive or outbound actions.

Risk: The integration API key grants access through superagnt.

Mitigation: Supply the key through the environment and keep the connected account's permissions limited to the task.

Risk: The bundled verification command contains HTML-escaped quote characters.

Mitigation: Correct the example command quoting before running it.

## Reference(s):

- [Attio integration documentation](https://superagnt.com/r/ch-attio-crm-docs)
- [MCP server](https://mcp.superagnt.com/mcp)
- [Client installation guide](https://www.superagnt.com/install)
- [superagnt API key setup](https://superagnt.com/r/ch-attio-crm-key)
- [Attio Integration on ClawHub](https://clawhub.ai/superagnt/skills/attio-crm)
- [Attio connection setup](https://app.superagnt.com/dashboard/connections)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the connected Attio account through a SUPERAGNT_API_KEY.]

## Skill Version(s):

2.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
