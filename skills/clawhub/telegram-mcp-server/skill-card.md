## Description: <br>
Guides agents in operating and diagnosing a Telethon/MTProto Telegram MCP server for listing chats, reading messages, sending messages, and handling authentication or lifecycle issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aihlp](https://clawhub.ai/user/aihlp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to help an agent call a Telegram MCP server, diagnose server or tool errors, manage multi-account labels, and explain when human QR login is required without exposing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP server can read chats and send messages through a real Telegram user account when an agent has access to the tool. <br>
Mitigation: Install it only for intended account operations, confirm the account label before sending messages, and limit tool access to agents that are allowed to act as that account. <br>
Risk: Telegram session strings and API credentials provide sensitive account access if exposed. <br>
Mitigation: Treat session strings and API credentials like passwords, never print them in responses or logs, and require human-attended QR login for session renewal. <br>
Risk: Manual process control can interfere with the supervised MCP server lifecycle and create conflicting Telegram sessions. <br>
Mitigation: Use the documented status and doctor diagnostics instead of manually starting or killing the server process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aihlp/skills/telegram-mcp-server) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include diagnostic steps, MCP tool names, account-label guidance, and credential-handling warnings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
