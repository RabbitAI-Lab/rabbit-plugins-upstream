## Description:

Access Tempo time-tracking data via MCP for worklogs, plans, teams, accounts, resource allocations, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo/Jira users use this skill to query and manage Tempo worklogs, resource plans, teams, accounts, and timesheet approvals through an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact Tempo actions can delete records or change timesheet approval state.

Mitigation: Use a least-privilege token and require explicit confirmation before delete, approval, rejection, reopen, or cross-user/team operations.

Risk: The connector can read or change team and colleague records when credentials permit it.

Mitigation: Confirm employer policy permits this automation and avoid reviewer or administrator tokens unless that access is required.

Risk: Tempo API tokens can expose worklog and account access if shared or committed.

Mitigation: Store TEMPO_API_TOKEN outside source control, do not paste it into shared chats, and rotate it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)
- [Source link from artifact](https://github.com/chrischall/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to call Tempo MCP tools that read or modify Tempo worklogs, plans, teams, accounts, and timesheet approvals.]

## Skill Version(s):

2.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
