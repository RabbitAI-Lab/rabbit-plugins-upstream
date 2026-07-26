## Description: <br>
telethon-plus lets an agent control a user-owned Telethon MTProto account through JSON HTTP and MCP endpoints for reading, sending, editing, deleting, forwarding, media handling, chat administration, polls, and incoming-event forwarding. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent operate their own already-authorized Telegram account over HTTP or MCP for message, media, dialog, chat, admin, poll, and webhook workflows. It is appropriate only for accounts and actions the user is authorized to control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, write, delete, forward, and administer content as a real Telegram user account. <br>
Mitigation: Use only a user-owned or explicitly authorized instance, and require exact user confirmation before delete, admin, join, leave, or bulk actions. <br>
Risk: Exposing the HTTP API or MCP endpoint without controls grants full account control to anyone who can reach it. <br>
Mitigation: Keep the service on localhost or behind TLS, set TELETHON_AUTH_KEY before exposure, and do not expose /api/ or /mcp/ to untrusted agents or networks. <br>
Risk: Session strings, API hashes, bearer keys, phone numbers, and message contents are sensitive account data. <br>
Mitigation: Do not print, log, echo, or persist secrets or private message content beyond what the task requires. <br>
Risk: TELETHON_POST_TO_URL can forward every incoming Telegram event, including content and metadata, to an external endpoint. <br>
Mitigation: Leave TELETHON_POST_TO_URL unset unless needed, and use only a trusted HTTPS endpoint controlled by the operator. <br>
Risk: Server-side file_url fetching can probe network locations reachable from the container. <br>
Mitigation: Do not pass arbitrary caller-supplied URLs; restrict file_url to trusted HTTPS domains or prefer direct uploads after client-side validation. <br>
Risk: Spam, mass outreach, scraping, or aggressive joins can violate Telegram rules or trigger account rate limits. <br>
Mitigation: Use read-only or dry-run mode for testing, check account risk before bursts, respect throttling, and back off when flood risk rises. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/telethon-plus) <br>
- [telethon-plus setup](references/setup.md) <br>
- [Telethon](https://codeberg.org/Lonami/Telethon) <br>
- [MCP streamable HTTP transport](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON HTTP requests, shell command examples, and MCP usage; runtime calls return JSON, raw bytes, or base64 media payloads.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TELETHON_PLUS_URL and optionally TELETHON_AUTH_KEY; setup examples require docker and curl.] <br>

## Skill Version(s): <br>
0.5.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
