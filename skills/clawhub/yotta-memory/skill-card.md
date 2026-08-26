## Description:

yotta-memory provides a file-based persistent memory workflow for agents, using local Markdown records for recall, context generation, profile summaries, and separated public or private memory types.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to give agents durable local memory across sessions, projects, and multiple agent clients. It helps agents recall prior context, write important facts or preferences, generate startup context, and manage memory lifecycle through the yotta-memory CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists agent memory as local plaintext files, which can include sensitive personal context.

Mitigation: Use it only for data the user intentionally wants stored, keep memory directories under user-controlled storage, and delete or forget sensitive entries when they should not persist.

Risk: LAN sharing can expose the memory service over the network.

Mitigation: Prefer local CLI or stdio mode, require bearer tokens for HTTP use, avoid --no-auth, and enable network access only on trusted networks.

Risk: MCP setup can modify agent connection configuration and may include bearer tokens.

Mitigation: Review MCP configuration changes before writing them and do not store or paste bearer tokens into persistent memory records.

Risk: Autostart can leave a background memory service running after setup.

Mitigation: Enable lan autostart only when an always-on shared memory service is intended, and use the documented status and disable commands to audit or remove it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol specification](references/protocol.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [Declared package repository](https://github.com/YottaMeta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run yotta-memory CLI and MCP setup commands when the user authorizes changes.]

## Skill Version(s):

0.6.5 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
