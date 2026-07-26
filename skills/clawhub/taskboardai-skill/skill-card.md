## Description: <br>
Manage tasks and projects using the TaskBoardAI Kanban system with MCP server integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hyddd](https://clawhub.ai/user/hyddd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to create, move, block, and complete TaskBoardAI Kanban cards through an MCP server while preserving task context and final summaries in card content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Task context and final summaries can be retained in persistent TaskBoardAI cards outside the chat. <br>
Mitigation: Avoid saving secrets or sensitive business data in task cards, and install the skill only when external task retention is acceptable. <br>
Risk: The skill depends on a local npm package and MCP server path that may not match the user's environment. <br>
Mitigation: Verify the TaskBoardAI npm package and confirm the configured MCP server path before use. <br>
Risk: The suggested inferred-task trigger can create cards without an explicit task-tracking command. <br>
Mitigation: Remove or narrow the inferred-task trigger when cards should be created only after explicit user requests. <br>


## Reference(s): <br>
- [TaskBoardAI repository](https://github.com/taskboardai/taskboardai) <br>
- [TaskboardAI Skill on ClawHub](https://clawhub.ai/hyddd/skills/taskboardai-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with MCP task-board actions, setup commands, and status updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update persistent TaskBoardAI cards through the configured MCP server.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
