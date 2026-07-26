## Description: <br>
Access Telegram data via MCP using the telebiz-tt browser client. Lists chats, reads messages, searches, manages folders, and sends messages through an authenticated Telegram session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[acastellana](https://clawhub.ai/user/acastellana) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to an authenticated Telegram session for reading chats and messages, searching history, managing folders, and sending messages through Telebiz. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthenticated local network services can expose an authenticated Telegram session. <br>
Mitigation: Restrict ports 9716, 9717, and 9718 to loopback or firewall them, and add authentication before allowing any broader access. <br>
Risk: Destructive or administrative Telegram tools can delete data or change chats, folders, and memberships. <br>
Mitigation: Enable only the tools needed for the workflow and review each destructive or administrative action before execution. <br>
Risk: High-volume or heavy Telegram operations can trigger rate limits or accidental spam-like behavior. <br>
Mitigation: Keep batches small, honor the documented delays, and prefer narrow filters before sending, forwarding, deleting, or batch-processing messages. <br>
Risk: Known upstream issues can make some folder and CRM-linking operations unreliable. <br>
Mitigation: Use sequential addChatToFolder calls for multi-chat folder updates and avoid depending on linkEntityToChat until the upstream contract is stable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/acastellana/skills/telebiz-mcp-skill) <br>
- [Telebiz web client](https://telebiz.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON snippets, and MCP tool responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a local MCP/HTTP bridge backed by an authenticated Telegram browser session.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
