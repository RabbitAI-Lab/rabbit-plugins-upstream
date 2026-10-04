## Description:

Provides file-based, access-controlled long-term memory for AI agents, with cross-session recall, semantic search, and auditable rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to retain, search, and manage local memories across sessions while separating shared facts from private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Memory and access credentials can persist locally or be exposed through an improperly configured service.

Mitigation: Keep the view console bound to localhost, protect keys and tokens, and never store MCP tokens in memories.

Risk: Installation or remote access may change agent configuration or enable a persistent LAN service.

Mitigation: Review MCP configuration and autostart changes before allowing them; use authenticated access and pin npm package versions where possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage listed in release metadata](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Memory protocol](references/protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown memory files and textual recall or context summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local memory files can be reviewed and rolled back; shared and private memory have different access boundaries.]

## Skill Version(s):

0.22.1 (source: release metadata, SKILL.md frontmatter, package.json, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
