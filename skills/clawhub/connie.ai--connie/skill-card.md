## Description:

Connects OpenClaw to Connie's hosted MCP server to search and update records and lists, import and export CSVs, run enrichment, and read workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[connie.ai](https://clawhub.ai/user/connie.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Connie workspace users use this skill to have an agent find and manage CRM records and lists, transfer CSV data, run enrichment, and check workspace information under their authorized account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can change or delete live workspace records and import data.

Mitigation: Confirm the intended workspace, records, and scope before writes, deletes, imports, or bulk actions.

Risk: Enrichment and some reads may consume workspace credits.

Mitigation: Get approval before credit-spending actions, especially across large selections.

Risk: Tool arguments and results pass through Connie's hosted service and may contain sensitive data.

Mitigation: Send only data needed for the Connie task; keep unrelated secrets out of tool arguments.

Risk: An OAuth grant continues to permit access to the authorized workspace until revoked.

Mitigation: Authorize the intended workspace and revoke the grant when access is no longer needed.

## Reference(s):

- [Connie MCP setup and tool documentation](https://connie.ai/docs/mcp)
- [Connie skill release on ClawHub](https://clawhub.ai/connie.ai/skills/connie)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language responses and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses and available actions depend on the live tool catalog and the user's authorized workspace.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
