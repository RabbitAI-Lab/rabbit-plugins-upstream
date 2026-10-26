## Description:

Helps agents access Tempo time tracking, resource plans, teams, accounts, and timesheet approvals through an MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Tempo users and teams use this skill to query worklogs and plans, log time, manage team or account information, and review timesheet approvals through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured token may access or change other users' worklogs, team data, and timesheet approvals; the documentation's own-account-only claim is inaccurate.

Mitigation: Review token permissions before installation and use a least-privilege Tempo token limited to the intended users, teams, accounts, and approval actions.

Risk: The Tempo token could be exposed if stored in shared repositories or chats.

Mitigation: Keep the token out of shared repositories and chats.

Risk: Create, update, delete, submit, approve, reject, reopen, or recall actions can alter Tempo records.

Mitigation: Require explicit user confirmation before each change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [Tempo MCP package (linked in skill documentation)](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Text or Markdown responses and Tempo tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may contain Tempo worklogs, resource plans, team information, or timesheet status.]

## Skill Version(s):

3.2.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
