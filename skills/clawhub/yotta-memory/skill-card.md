## Description:

元忆 yotta-memory provides boundary-aware, file-based persistent memory for AI agents, with shared FACT memories, private PREF/BOUND/COMMIT isolation, recall/context workflows, and auditable local Markdown storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and end users use this skill to give AI agents persistent local memory across sessions, projects, and multiple agents while keeping public facts and private preferences, boundaries, and commitments separated by owner.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist long-lived local memory about a user and their work, including conversation-derived personal or sensitive information.

Mitigation: Use encrypted stores, keep private memory owner-scoped, review stored memories through the user view, and avoid retaining content the user does not want remembered.

Risk: Remote or LAN memory access can expose memory operations or access tokens if authentication or network settings are misconfigured.

Mitigation: Keep authentication enabled, avoid --no-auth except on a trusted isolated network, protect tokens, and review LAN autostart changes before approving them.

Risk: Installation and operation may edit host MCP configuration or add local autostart behavior.

Mitigation: Review proposed MCP configuration edits, install steps, and autostart changes before allowing the skill to apply them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [User Guide](USER_GUIDE.md)
- [Protocol Specification](references/protocol.md)
- [FAQ](references/faq.md)
- [Security Review v0.8.5](docs/SECURITY-REVIEW-v0.8.5.md)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory operations through the yotta-memory CLI or MCP tools; no fixed token cap is specified.]

## Skill Version(s):

0.10.1 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
