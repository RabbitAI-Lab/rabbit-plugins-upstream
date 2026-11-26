## Description:

ChatbotX provides an MCP server and CLI integration that lets agents work with a ChatbotX workspace for contacts, conversations, flows, broadcasts, sequences, and related omnichannel marketing operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sung17](https://clawhub.ai/user/sung17)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an AI agent or terminal workflow to a live ChatbotX workspace, discover workspace objects, and perform contact, messaging, broadcast, flow, and sequence tasks through MCP tools or CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote SSE operation and token handling could expose or misuse a ChatbotX workspace token.

Mitigation: Prefer stdio or local-only operation, bind servers to localhost, avoid putting workspace tokens in URLs, and use least-privilege short-lived tokens when available.

Risk: Publicly exposed MCP endpoints may be unsafe without authentication, session binding, origin validation, and resource limits.

Mitigation: Do not expose the MCP port publicly until those controls are in place and reviewed.

Risk: Self-signed certificate support can disable TLS verification for self-hosted instances.

Mitigation: Use valid TLS certificates for production and reserve disabled verification for controlled local or test environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sung17/skills/chatbotx)
- [Publisher profile](https://clawhub.ai/user/sung17)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [ChatbotX API base URL](https://app.chatbotx.io/api)

## Skill Output:

**Output Type(s):** [API Calls, Text, JSON, Shell commands, Configuration]

**Output Format:** [MCP tool responses and CLI-oriented Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CHATBOTX_API_KEY and CHATBOTX_API_URL for workspace access.]

## Skill Version(s):

0.1.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
