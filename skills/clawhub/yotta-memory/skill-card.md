## Description:

元忆 yotta-memory gives agents a local, file-based memory workflow with auditable Markdown records, recall/remember commands, public FACT memory, and private PREF/BOUND/COMMIT isolation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users use this skill to give AI agents durable local memory across sessions and projects. It helps agents restore context, save important facts and preferences, respect private memory boundaries, and manage memory lifecycle through CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles long-term personal memory and may capture sensitive user information or secrets.

Mitigation: Install only when durable local memory is desired, review what the agent saves, avoid pasting tokens into chat, and use the built-in review and encryption workflows for private memory.

Risk: The HTTP MCP service and LAN sharing features can expose memory access beyond the local machine if misconfigured.

Mitigation: Keep the service on trusted networks, use per-agent tokens, keep X-Agent-Id aligned with the registered token, and use --no-auth only in controlled environments.

Risk: The skill can guide edits to agent MCP configuration and can enable a persistent background memory service.

Mitigation: Review MCP configuration changes before applying them and enable LAN autostart only when a persistent memory service is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [README](README.md)
- [User guide](USER_GUIDE.md)
- [FAQ](references/faq.md)
- [Protocol specification](references/protocol.md)
- [Security review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI/MCP command examples and generated memory/context text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may guide agents to write local memory files through the yotta-memory CLI or MCP tools and to update agent configuration after user review.]

## Skill Version(s):

0.8.7 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
