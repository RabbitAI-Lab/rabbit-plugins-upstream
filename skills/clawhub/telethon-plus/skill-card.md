## Description:

Controls an authorized Telegram user account through an existing Telethon HTTP or MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and users can connect an agent to an already-running, authorized Telegram account to read and manage chats, send messages or media, and receive incoming events through HTTP or MCP. The service acts with the account's full user permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API and MCP endpoint can expose full read, send, and administrative control of a real Telegram account, especially when the service is reachable without authentication.

Mitigation: Use an account you are authorized to operate, bind the service to localhost or protect it with TLS, configure a bearer key, and keep the endpoints away from untrusted clients.

Risk: A configured webhook forwards incoming message content, sender details, and account activity to its destination.

Mitigation: Leave the webhook disabled unless needed; when enabled, use only a trusted HTTPS endpoint you control.

Risk: A caller-supplied file_url is fetched by the server and may reach internal or private network addresses.

Mitigation: Do not forward arbitrary URLs; restrict fetches to HTTPS URLs on trusted public domains or upload a locally validated file.

Risk: ClawScan flags an unpinned Docker image and runtime shell use beyond the declared scope; its scan is partial and several references were unresolved.

Mitigation: Verify the Docker image before installing and review shell invocations against the documented setup-only scope.

## Reference(s):

- [Setup and deployment guidance](artifact/references/setup.md)
- [Project homepage](https://github.com/psyb0t/docker-telethon-plus)
- [Telethon](https://codeberg.org/Lonami/Telethon)
- [MCP Streamable HTTP transport specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http)

## Skill Output:

**Output Type(s):** [API calls, JSON, Text, Configuration guidance, Shell commands]

**Output Format:** [HTTP or MCP requests with JSON responses; setup guidance may include Markdown and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions operate on the authorized Telegram account; setup shell commands are for operator use.]

## Skill Version(s):

0.7.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
