## Description: <br>
Structured Cloud lets MCP-capable assistants read, create, update, complete, and delete Structured tasks through the Structured Cloud MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[puppetjellyfish](https://clawhub.ai/user/puppetjellyfish) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to connect an MCP-capable assistant to Structured Cloud so the assistant can view schedules, create tasks, update task details, complete tasks, delete tasks, and manage recurring tasks when the account supports them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can enable an agent to change or delete Structured Cloud tasks. <br>
Mitigation: Install it only when task access is intended, and ask the agent to preview affected tasks before destructive or bulk changes. <br>
Risk: Task changes may be applied to the wrong date, title, label, or schedule when a request is ambiguous. <br>
Mitigation: Use the user's wording for task details and ask a clarifying question when the task cannot be resolved unambiguously. <br>
Risk: The assistant cannot perform task operations until the Structured Cloud MCP connection and authentication are available in the host app. <br>
Mitigation: Connect the host app to the Structured Cloud MCP endpoint and complete the Structured Cloud login flow before retrying task-management requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/puppetjellyfish/skills/structured-cloud-skill) <br>
- [Publisher profile](https://clawhub.ai/user/puppetjellyfish) <br>
- [Source repository](https://github.com/puppetjellyfish/structured-cloud-skill) <br>
- [Structured Cloud MCP endpoint](https://mcp.structured.app/mcp) <br>
- [OpenCode configuration schema](https://opencode.ai/config.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Text, Markdown] <br>
**Output Format:** [Markdown text with JSON configuration examples and short operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for connecting a host application to the Structured Cloud MCP server and for safely carrying out task-management requests.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
