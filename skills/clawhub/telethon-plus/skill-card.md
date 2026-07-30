## Description: <br>
telethon-plus gives an agent HTTP and MCP access to a running Telethon userbot so it can read, send, edit, delete, forward, and manage Telegram messages and chats as the account owner. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate a user-owned Telegram account through an already-running telethon-plus server for messaging, chat administration, media transfer, dialog lookup, and incoming-message workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control a real Telegram account with full read, write, and admin authority. <br>
Mitigation: Install only for a user-owned or explicitly authorized account, keep session and API credentials private, and require confirmation before destructive or administrative actions. <br>
Risk: An exposed API or MCP endpoint can hand full account control to anyone who can reach it. <br>
Mitigation: Run the server on localhost or behind TLS, set TELETHON_AUTH_KEY, and avoid exposing /api/ or /mcp/ to untrusted agents or networks. <br>
Risk: Server-side file_url fetching can be misused to access internal or untrusted network resources. <br>
Mitigation: Use file_url only with trusted HTTPS endpoints under the operator's control, and prefer direct uploads when handling untrusted file sources. <br>
Risk: TELETHON_POST_TO_URL can continuously forward incoming Telegram content and account activity to another service. <br>
Mitigation: Configure webhook forwarding only to a trusted HTTPS endpoint controlled by the operator, or leave it disabled. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/telethon-plus) <br>
- [telethon-plus setup](references/setup.md) <br>
- [docker-telethon-plus project](https://github.com/psyb0t/docker-telethon-plus) <br>
- [Telethon](https://codeberg.org/Lonami/Telethon) <br>
- [MCP Streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl commands, JSON request and response examples, and setup configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runtime calls target TELETHON_PLUS_URL and may include TELETHON_AUTH_KEY when the server requires bearer authentication.] <br>

## Skill Version(s): <br>
0.5.6 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
