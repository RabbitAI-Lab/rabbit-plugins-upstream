## Description: <br>
HTTP and MCP control plane for operating a real Telegram MTProto user account through a Telethon-backed API, including message, media, dialog, chat administration, polling, webhook, and throttling workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent interact with an already running, user-owned telethon-plus server for authorized Telegram account workflows such as reading chats, sending messages, managing media, and performing chat administration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a real Telegram user account with read, write, and administration access. <br>
Mitigation: Use only with an account and telethon-plus instance the user owns or is explicitly authorized to operate, and require explicit confirmation before destructive or administrative actions. <br>
Risk: An exposed API or MCP endpoint can grant full account control to anyone who can reach it. <br>
Mitigation: Run the endpoint on a trusted local or TLS-protected surface and set TELETHON_AUTH_KEY before exposing it beyond a private environment. <br>
Risk: Session strings, API hashes, bearer tokens, phone numbers, and message contents are sensitive. <br>
Mitigation: Keep secrets private, avoid logging or echoing them, and limit message content disclosure to what the task requires. <br>
Risk: TELETHON_POST_TO_URL forwards incoming Telegram activity to a configured webhook. <br>
Mitigation: Enable webhook forwarding only for trusted HTTPS endpoints that the operator controls. <br>
Risk: Caller-supplied file_url values are fetched by the server and may reach destinations visible from the container. <br>
Mitigation: Avoid untrusted file_url values; prefer trusted HTTPS sources or local upload patterns when sending media. <br>
Risk: Automated high-volume messaging, joining, resolving, or scraping can violate platform rules or trigger account limits. <br>
Mitigation: Use the built-in throttling conservatively, prefer read-only or dry-run mode when possible, and avoid spam, mass outreach, or unauthorized scraping. <br>


## Reference(s): <br>
- [telethon-plus setup](references/setup.md) <br>
- [Telethon](https://codeberg.org/Lonami/Telethon) <br>
- [Model Context Protocol streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/telethon-plus) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, API calls] <br>
**Output Format:** [Markdown guidance with curl commands, shell commands, configuration examples, and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may act on a real Telegram account through the configured telethon-plus endpoint.] <br>

## Skill Version(s): <br>
0.5.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
