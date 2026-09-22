## Description:

元忆 yotta-memory gives AI agents a local, file-based long-term memory system with context recall, explicit memory writes, semantic search, access boundaries, diff, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to preserve useful context across sessions, store important facts or preferences, and retrieve task-relevant memory through the yotta-memory CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP full mode can expose or alter other agents' private memories in supported plaintext multi-agent stores.

Mitigation: Prefer encrypted stores, start MCP with `--tools core`, and avoid shared plaintext multi-agent stores until the cross-agent `explain` and maintenance authorization issues are fixed.

Risk: LAN or MCP access can expose persistent memory, keys, or tokens if authentication is weakened.

Mitigation: Avoid `--no-auth`, require the documented Authorization, `X-Agent-Id`, and `X-Agent-Key` controls, and enable LAN autostart only when it is needed.

Risk: The skill operates a local persistent memory engine that stores agent history, keys, tokens, and optional remote-access state.

Mitigation: Use encrypted stores, protect recovery keys and agent keys, and pin npm package versions for install and update workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol specification](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke local CLI or MCP workflows that read, write, recall, maintain, and configure local memory stores.]

## Skill Version(s):

0.16.3 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
