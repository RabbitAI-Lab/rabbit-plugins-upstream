## Description: <br>
Search, read, and safely update one selected Trello workspace through Trello's official hosted MCP server for boards, members, cards, lists, checklists, and workspace search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maverick](https://clawhub.ai/user/maverick) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to work in one connected Trello workspace through allowlisted MCP tools. It supports Trello search and read workflows, plus approved updates to lists, cards, and checklists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth environment variables can grant access to the connected Trello workspace. <br>
Mitigation: Treat the refresh token, access token, and client id as secrets; rotate or reconnect Trello if credentials may be stale or exposed. <br>
Risk: Approved write or archive actions can change Trello boards, lists, cards, or checklists. <br>
Mitigation: Inspect current Trello state first, describe the intended change, and require explicit approval before every write or archive action. <br>
Risk: The skill is scoped to exactly one OAuth-connected Trello workspace. <br>
Mitigation: Do not claim or attempt access to another workspace without a separate connection. <br>
Risk: Rerunning setup with stale credential input can overwrite a newer rotated refresh token. <br>
Mitigation: Rerun setup only after a fresh connection or intentional credential rotation. <br>


## Reference(s): <br>
- [Trello MCP guide](https://support.atlassian.com/trello/docs/connect-trello-to-ai-assistants-with-trello-mcp/) <br>
- [Trello MCP endpoint](https://mcp.trello.com/v1) <br>
- [mcporter v0.12.3](https://github.com/openclaw/mcporter/tree/v0.12.3) <br>
- [ClawHub skill page](https://clawhub.ai/maverick/skills/maverick-trello-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown instructions with shell command examples and JSON MCP tool responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an allowlisted OAuth MCP server for Trello read, search, write, and archive workflows.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
