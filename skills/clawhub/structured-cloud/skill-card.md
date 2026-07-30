## Description: <br>
Use when a Hermes Agent, Open Claw, OpenCode, or other MCP-capable assistant needs to read, manage, or edit Structured tasks through Structured Cloud. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[puppetjellyfish](https://clawhub.ai/user/puppetjellyfish) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and users of MCP-capable assistants use this skill to connect an agent to Structured Cloud so it can view, create, update, complete, delete, and manage recurring tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected agent can delete tasks, complete tasks, move tasks in bulk, and edit recurring tasks. <br>
Mitigation: Ask the agent to preview intended deletes, bulk moves, completions, and recurring-task edits before applying them. <br>
Risk: The skill requires a Structured Cloud account and a connected MCP server before task operations can work. <br>
Mitigation: Authenticate through the host application's MCP flow and confirm Structured Cloud is connected before retrying task actions. <br>


## Reference(s): <br>
- [Structured Cloud MCP endpoint](https://mcp.structured.app/mcp) <br>
- [OpenCode configuration schema](https://opencode.ai/config.json) <br>
- [ClawHub skill page](https://clawhub.ai/puppetjellyfish/skills/structured-cloud) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP setup guidance and task-operation instructions for the host agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
