## Description:

Controls an authorized Telegram user account through HTTP or MCP for reading and managing messages, chats, media, polls, and account events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users use the skill to operate their own authorized Telegram account through an existing Telethon Plus service. It can read and send messages, manage chats and media, and relay incoming events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a suspicious, medium-confidence verdict, with concerns about unauthenticated access to full Telegram account control; the scan was partial.

Mitigation: Set TELETHON_AUTH_KEY and restrict access to trusted clients; bind locally or protect public access with TLS and a reverse proxy.

Risk: The security report raises concern about mutable Docker images.

Mitigation: Deploy a reviewed, pinned image version or digest.

Risk: Enabling the webhook forwards incoming message content and account activity to its configured endpoint.

Mitigation: Leave TELETHON_POST_TO_URL unset unless needed, and use only a trusted HTTPS endpoint you control.

Risk: A supplied file URL is fetched by the service and could reach private network addresses.

Mitigation: Use HTTPS URLs from trusted public domains; do not pass through untrusted or generated URLs.

## Reference(s):

- [Telethon Plus on ClawHub](https://clawhub.ai/psyb0t/skills/telethon-plus)
- [Project homepage](https://github.com/psyb0t/docker-telethon-plus)
- [Setup guide](references/setup.md)
- [Telethon](https://codeberg.org/Lonami/Telethon)

## Skill Output:

**Output Type(s):** [Text, JSON, Media data]

**Output Format:** [JSON API responses and MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned content depends on the requested Telegram operation.]

## Skill Version(s):

0.6.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
