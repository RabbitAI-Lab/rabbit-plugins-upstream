## Description:

Access Tempo time-tracking data via MCP for worklogs, plans, teams, accounts, resource allocation, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo/Jira users use this skill to query time-tracking data, log or update work, manage resource plans, inspect teams and accounts, and handle timesheet approval workflows through a registered Tempo MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tempo permissions may expose team or colleague data despite the artifact's single-user wording.

Mitigation: Use a least-privilege Tempo token, confirm the token's accessible scope before use, and avoid sharing or committing the token.

Risk: Write, delete, and approval tools can change worklogs, plans, teams, accounts, or timesheet state.

Mitigation: Confirm every write, delete, submit, approve, reject, reopen, or recall action and verify target IDs, dates, and periods before execution.

Risk: Corporate Tempo or Jira automation may be subject to employer policy or administrative restrictions.

Mitigation: Check applicable IT, Jira, and Tempo policies before automating against an organization-managed workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [npm package](https://www.npmjs.com/package/tempo-api-mcp)
- [Tempo Terms of Use](https://www.tempo.io/terms-of-use)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool-call descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a registered Tempo MCP server and a Tempo API token.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
