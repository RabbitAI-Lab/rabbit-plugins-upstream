## Description:

Provides file-based, permission-aware long-term memory for AI agents, with cross-session recall and context restoration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to save, search, and restore local agent memories across sessions and projects while separating shared facts from private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable memory may retain sensitive information or credentials.

Mitigation: Review stored memories and access permissions; do not save raw tokens.

Risk: HTTP and LAN access can expose memory beyond the local machine.

Mitigation: Prefer local stdio/core mode; bind HTTP to localhost unless LAN access is intended, and do not disable authentication.

Risk: Setup can alter agent configuration or enable persistent services and optional providers.

Mitigation: Review MCP configuration edits and explicitly approve provider, embedding, LAN, and autostart setup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Memory protocol](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown, with optional JSON and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read and write durable local memory files.]

## Skill Version(s):

0.22.9 (source: ClawHub release metadata, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
