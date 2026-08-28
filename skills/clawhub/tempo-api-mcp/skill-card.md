## Description:

Access Tempo time-tracking data via MCP for worklogs, plans, teams, accounts, time logging, resource allocations, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo/Jira users use this skill to configure an MCP-backed agent for Tempo time tracking, resource planning, team/account lookups, and timesheet approval workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect team, account, worklog, and timesheet data while its instructions may understate that scope.

Mitigation: Install only for workflows where the agent may use the Tempo token for personal and permission-dependent team or admin actions.

Risk: The Tempo API token grants access according to the user's Tempo and Jira permissions.

Mitigation: Use the least-privileged token available, avoid shared chats or repositories for the token, and rotate the token if it is exposed.

Risk: Deletes, approvals, rejections, reopen actions, and actions involving another user can change business records.

Mitigation: Require explicit confirmation before destructive, approval-state, or other-user actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)
- [Tempo Terms of Use](https://www.tempo.io/terms-of-use)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, API calls]

**Output Format:** [Markdown with inline JSON and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Tempo API token and a registered tempo-api-mcp server; available actions depend on token permissions.]

## Skill Version(s):

2.3.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
