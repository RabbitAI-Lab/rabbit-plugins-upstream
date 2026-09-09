## Description:

Accesses Tempo time-tracking, resource planning, teams, accounts, projects, and timesheet approval workflows through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo/Jira users use this skill to ask an agent to read or manage Tempo worklogs, resource plans, teams, accounts, projects, and timesheet approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Tempo token may allow the agent to read or change Tempo data beyond a single user's own entries, including team or colleague data when permissions allow it.

Mitigation: Use a least-privilege per-user Tempo token, avoid shared or admin tokens, and confirm the token's effective permissions before enabling the connector.

Risk: Mutation tools can delete worklogs or change plans, teams, accounts, and timesheet approval states.

Mitigation: Require explicit user confirmation for delete, approval, reject, reopen, account, team, and plan operations, and review target IDs and date ranges before execution.

Risk: Scripted Tempo/Jira automation may conflict with organizational policy even when API access is technically available.

Mitigation: Confirm that the organization permits Tempo/Jira automation before using the connector against corporate workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Tempo API token and a registered tempo-api-mcp server.]

## Skill Version(s):

2.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
