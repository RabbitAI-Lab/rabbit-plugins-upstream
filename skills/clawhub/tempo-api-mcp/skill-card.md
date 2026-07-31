## Description: <br>
Access Tempo time-tracking data via MCP for worklogs, plans, teams, accounts, resource allocation, and timesheet approval workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a registered Tempo MCP server for time logging, worklog review, resource planning, team and account lookup, and timesheet approval actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read or change sensitive Tempo and Jira time-tracking data according to the permissions granted to the configured token. <br>
Mitigation: Use a least-privilege Tempo token, obtain admin approval for corporate use, and restrict access to users who are allowed to view or change the affected worklogs, plans, teams, accounts, and timesheets. <br>
Risk: Mutation tools can delete worklogs, modify accounts or teams, and act on timesheet approvals. <br>
Mitigation: Require explicit human confirmation before destructive, account/team, or timesheet approval actions, and review requested identifiers and date ranges before execution. <br>
Risk: A leaked Tempo token could expose or alter organization time-tracking data. <br>
Mitigation: Keep TEMPO_API_TOKEN out of git and shared chats, store it in the local MCP environment, and rotate the token if it is exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/tempo-api-mcp) <br>
- [tempo-api-mcp npm Package](https://www.npmjs.com/package/tempo-api-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline JSON, shell commands, and MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a registered tempo-api-mcp server and a Tempo API token supplied outside source control.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
