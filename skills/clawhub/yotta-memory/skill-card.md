## Description:

元忆 yotta-memory provides boundary-aware, file-based long-term memory for AI agents, with shared FACT memories, private PREF/BOUND/COMMIT memories, recall/context workflows, lifecycle management, backup, and local or LAN access modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to give AI agents durable local memory across sessions, projects, and multiple agent identities while keeping private memory scoped by owner. It is intended for storing, recalling, maintaining, backing up, and reviewing agent memory through the yotta-memory CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores long-lived personal memory and can expose local persistence, network access, and cross-agent controls.

Mitigation: Install it only when a durable local memory system is intended; prefer local CLI or stdio mode and avoid LAN serving unless it is protected by TLS or a trusted tunnel.

Risk: Memory entries may contain sensitive information or bearer tokens if users or agents store them.

Mitigation: Do not store bearer tokens or other secrets in memory entries; use the skill's owner scoping, private-memory encryption, and user review workflow for sensitive data.

Risk: Autostart and backup scheduler changes can affect persistence and local system behavior.

Mitigation: Review autostart and backup scheduler changes before enabling them, pin the npm package version, and confirm backups are written to an independent trusted location.

Risk: Server evidence flags unresolved concerns for multi-agent private-memory maintenance and view-server session behavior.

Mitigation: Multi-agent private-memory users should wait for fixes or restrict use to trusted local workflows until those issues are resolved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package @yottameta/yotta-memory](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [YottaMeta yotta-memory repository](https://github.com/YottaMeta/yotta-memory)
- [User Guide](USER_GUIDE.md)
- [Protocol Specification](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include memory recall/context text, CLI commands, MCP configuration guidance, backup guidance, and maintenance recommendations.]

## Skill Version(s):

0.12.1 (source: frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
