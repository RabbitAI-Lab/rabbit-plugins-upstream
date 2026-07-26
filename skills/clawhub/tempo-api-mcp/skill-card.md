## Description: <br>
Access Tempo time-tracking, planning, team, account, and timesheet approval data through an MCP server backed by the Tempo API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Tempo/Jira users use this skill to query worklogs, plans, teams, accounts, and timesheet approvals, and to create or update Tempo records through MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose broad Tempo/Jira time, team, account, and organizational data. <br>
Mitigation: Use a least-privilege Tempo token and require explicit confirmation before cross-user, team, or account queries. <br>
Risk: Create, update, delete, and approval tools can change Tempo records. <br>
Mitigation: Require the agent to summarize the target record, action, and parameters and obtain user confirmation before any mutating operation. <br>
Risk: Tempo API tokens can be exposed if stored in shared project configuration or chat transcripts. <br>
Mitigation: Keep TEMPO_API_TOKEN out of committed files and shared chats, use local secret storage where available, and rotate the token if exposed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/tempo-api-mcp) <br>
- [tempo-api-mcp npm Package](https://www.npmjs.com/package/tempo-api-mcp) <br>
- [Tempo Terms of Use](https://www.tempo.io/terms-of-use) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and MCP tool calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a registered tempo-api-mcp server and a TEMPO_API_TOKEN supplied through MCP configuration or environment.] <br>

## Skill Version(s): <br>
2.1.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
