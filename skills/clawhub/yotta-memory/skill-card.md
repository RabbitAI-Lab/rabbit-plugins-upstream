## Description:

Yotta-memory gives AI agents durable, file-based memory across sessions, with shared facts and per-agent private preferences, boundaries, and commitments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use it to save, recall, and maintain context across conversations and projects, while keeping shared facts separate from each agent's private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with high confidence, and the scan was incomplete.

Mitigation: Treat the verdict as unresolved; review the complete scan and release source before installation.

Risk: The security guidance flags memory-console access and unsafe import paths for particular attention.

Mitigation: Review those paths and restrict access to the intended users, files, and memory stores.

Risk: The security guidance flags unencrypted remote examples and token storage.

Mitigation: Use authenticated encrypted transport for remote access and keep tokens in protected secret storage.

## Reference(s):

- [Project page](https://github.com/YottaMeta/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [Memory protocol](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Files]

**Output Format:** [Natural-language guidance, CLI or MCP commands, Markdown memory files, and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory reads and writes depend on the configured agent identity and authorization.]

## Skill Version(s):

0.24.0 (source: frontmatter, package.json, CHANGELOG, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
