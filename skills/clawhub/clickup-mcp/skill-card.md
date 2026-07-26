## Description: <br>
Manage ClickUp tasks, docs, time tracking, comments, chat, and search via official MCP. OAuth authentication required. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pvoo](https://clawhub.ai/user/pvoo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents with ClickUp workspaces use this skill to search workspace content and manage tasks, docs, comments, chat, time tracking, and workspace hierarchy through ClickUp's official MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad access to a ClickUp workspace, including changes to tasks, docs, time entries, files, comments, and chat messages. <br>
Mitigation: Use a least-privileged ClickUp account or workspace where possible, and require explicit confirmation before the agent performs workspace-changing actions. <br>
Risk: The setup asks users to copy a long-lived ClickUp token into an environment variable. <br>
Mitigation: Treat CLICKUP_TOKEN like a password, keep environment files private and out of source control, and refresh or rotate the token if it may have been exposed. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/pvoo/skills/clickup-mcp) <br>
- [ClickUp homepage](https://clickup.com) <br>
- [ClickUp MCP Documentation](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server) <br>
- [ClickUp MCP Supported Tools](https://developer.clickup.com/docs/mcp-tools) <br>
- [ClickUp API Reference](https://clickup.com/api) <br>
- [ClickUp Feedback and Allowlist Requests](https://feedback.clickup.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter and a CLICKUP_TOKEN environment variable; generated actions may read from or modify a connected ClickUp workspace.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
