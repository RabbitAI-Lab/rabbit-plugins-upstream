## Description:

Gives AI agents file-based, cross-session memory with recall, semantic search, and access boundaries for shared and private information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to retain and retrieve local memory across sessions, organize shared facts and private preferences, and manage backups and recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent-wide memory access may expose or retain sensitive information longer than intended.

Mitigation: Install only when persistent local memory is needed, and review what agents may store and retrieve.

Risk: Connection tokens stored in long-term natural-language memory may be exposed through recall.

Mitigation: Keep bearer tokens and agent keys in a key file, password manager, or MCP secret mechanism, not in memory entries.

Risk: LAN access, autostart, runtime updates, or provider commands may expand the skill's authority.

Mitigation: Confirm exact configuration paths and commands before enabling these options.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol reference](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can read and write local Markdown memory files when enabled.]

## Skill Version(s):

0.22.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
