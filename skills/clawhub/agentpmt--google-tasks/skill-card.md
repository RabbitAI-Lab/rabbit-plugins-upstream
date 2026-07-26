## Description: <br>
Google Tasks: create, read, update, delete tasks and lists, including due dates, notes, subtasks, completion tracking, batch operations, and filtering through AgentPMT-hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill to manage Google Tasks through AgentPMT-hosted remote tool calls, including task and list creation, updates, completion tracking, search, filtering, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can delete tasks, delete task lists, and clear completed tasks. <br>
Mitigation: Require the agent to list the target task or task list first and get explicit confirmation before delete_task, delete_tasklist, or clear_completed. <br>


## Reference(s): <br>
- [Google Tasks marketplace page](https://www.agentpmt.com/marketplace/google-tasks) <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/google-tasks) <br>
- [Google Tasks generated schema](artifact/schema.md) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown instructions with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines 19 Google Tasks actions and points agents to live schema lookup when parameters or examples need confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
