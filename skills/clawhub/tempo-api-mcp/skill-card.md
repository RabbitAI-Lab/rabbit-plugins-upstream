## Description:

Access Tempo time-tracking data via MCP for Tempo worklogs, plans, teams, accounts, resource allocations, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers who use Tempo with Jira can query and manage time tracking, resource planning, team, account, and timesheet approval data through a configured Tempo MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running an unpinned MCP package can execute code that changes between reviews.

Mitigation: Use a pinned, reviewed package version or reviewed commit before installing or registering the MCP server.

Risk: The Tempo API token can grant access to sensitive time-tracking, coworker, approval, or administrative data allowed by the user's account.

Mitigation: Use the least-privileged token available, keep the token out of project files and shared chats, and rotate it if exposed.

Risk: Write tools can create, update, delete, submit, approve, reject, reopen, or recall Tempo records and timesheets.

Mitigation: Review proposed write actions before confirmation and verify the affected account, period, issue, plan, or team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)
- [Source repository listed in artifact](https://github.com/chrischall/tempo-api-mcp)
- [Tempo Terms of Use](https://www.tempo.io/terms-of-use)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON configuration and shell command examples; MCP tool calls return Tempo API data, receipts, or diagnostics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact and full response views; write and timesheet actions return receipts and may require confirmation.]

## Skill Version(s):

2.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
