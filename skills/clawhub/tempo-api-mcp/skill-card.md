## Description: <br>
Access Tempo time-tracking, planning, team, account, and timesheet approval data through an MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to connect an agent to Tempo for worklog reporting, resource planning, account and team lookup, and timesheet approval workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Tempo token that may expose coworker, team, and organization data depending on the user's Tempo permissions. <br>
Mitigation: Install only when the agent should access Tempo data reachable by that token, and use a least-privilege token. <br>
Risk: The skill can guide create, update, delete, submit, approve, reject, reopen, or recall actions in Tempo. <br>
Mitigation: Require explicit confirmation before any write or approval action, and review the requested operation before execution. <br>
Risk: Running the MCP package through npm can introduce package supply-chain risk. <br>
Mitigation: Pin or review the npm package before use. <br>


## Reference(s): <br>
- [Tempo API MCP npm package](https://www.npmjs.com/package/tempo-api-mcp) <br>
- [Repository link declared in artifact](https://github.com/chrischall/tempo-api-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples and MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide authenticated Tempo API operations that read or change worklogs, plans, teams, accounts, and timesheet approvals.] <br>

## Skill Version(s): <br>
2.3.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
