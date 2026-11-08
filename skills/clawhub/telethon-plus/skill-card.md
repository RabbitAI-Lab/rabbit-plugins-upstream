## Description:

Controls the user's authorized Telegram account through a running Telethon service over HTTP or MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can use an agent or script to read and manage chats, send messages and media, and handle incoming Telegram events through an instance they own or are authorized to operate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service can be open to anyone who can reach it when bearer authentication is unset, and it grants full access to the configured Telegram account.

Mitigation: Set bearer authentication, bind to loopback or protect the service with TLS, restrict access to trusted clients, and operate only an account you own or are authorized to use.

Risk: ClawScan reports risks around unauthenticated account access, unpinned container images, and runtime shell use; its scan was partial and some referenced paths were missing.

Mitigation: Verify the container image source, pin a reviewed version, and review the complete referenced files and bundled shell wrapper before deployment.

## Reference(s):

- [Setup and deployment guide](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-telethon-plus)
- [Telethon](https://codeberg.org/Lonami/Telethon)

## Skill Output:

**Output Type(s):** [API calls, JSON, Text, Guidance]

**Output Format:** [HTTP or MCP requests with JSON responses and concise text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions operate as the authorized Telegram account; writes can change messages, chats, and membership.]

## Skill Version(s):

0.7.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
