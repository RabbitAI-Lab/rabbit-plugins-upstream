## Description: <br>
Slack Api Toolkit helps agents operate Slack workspaces through a Slack gateway for messages, channels, files, search, reactions, bookmarks, scheduled messages, batch actions, and audit logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, workspace administrators, and operations teams use this skill to automate Slack workflows such as channel management, message and file operations, workspace search, scheduled messages, and audit-oriented reporting. It is intended for agents that have an explicitly authorized Slack gateway connection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can drive workspace-changing Slack actions including deletes, archive operations, batch actions, and cross-workspace operations. <br>
Mitigation: Require human confirmation before delete, archive, bulk, or cross-workspace actions, and use explicit channel, file, message, and workspace connection identifiers. <br>
Risk: Slack gateway credentials and OAuth tokens could expose workspace access if mishandled. <br>
Mitigation: Use least-privilege Slack scopes, keep API keys and tokens out of code, store credentials through environment variables or the gateway login flow, and rotate credentials when needed. <br>
Risk: Multiple workspace connections can increase the chance of acting in the wrong Slack workspace. <br>
Mitigation: Use a dedicated workspace connection and require the agent or operator to specify the intended connection for every sensitive workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/slack-api-toolkit) <br>
- [Slack gateway API endpoint](https://api.slack-gateway.com/slack/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples, shell commands, Python snippets, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Slack API requests or CLI commands that modify workspace state when executed by an authorized agent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
