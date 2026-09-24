## Description:

Access Tempo time-tracking and resource-planning data through an MCP server for worklogs, plans, teams, accounts, projects, and timesheet approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Tempo/Jira users use this skill to query and manage Tempo worklogs, resource plans, teams, accounts, projects, and timesheet approvals from an agent with a configured Tempo API token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Tempo token may allow access to worklog, team, reviewer, account, and planning data beyond the immediate request.

Mitigation: Install with a least-privilege Tempo token and limit use to data the token holder is authorized to access.

Risk: The connector can modify Tempo data, including deletes, approvals, rejections, reopens, and account or team changes.

Mitigation: Require explicit user confirmation before any destructive, approval, reviewer, account, or team change is executed.

Risk: Team and colleague data may be exposed through the supplied token's permissions.

Mitigation: Confirm the intended scope before reading team or reviewer data and avoid bulk export or colleague-level reporting unless authorized.

## Reference(s):

- [tempo-api-mcp ClawHub skill page](https://clawhub.ai/chrischall/skills/tempo-api-mcp)
- [tempo-api-mcp npm package](https://www.npmjs.com/package/tempo-api-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with JSON and bash code blocks plus MCP tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools can return compact or full Tempo payloads; write tools return receipts or dry-run previews.]

## Skill Version(s):

3.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
