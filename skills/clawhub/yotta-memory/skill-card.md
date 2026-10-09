## Description:

Provides persistent, boundary-aware local memory for AI agents, with cross-session recall, searchable records, and controlled sharing between agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to retain project facts, preferences, boundaries, and commitments across sessions, then recall relevant context while maintaining separate private memory for each agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory may contain sensitive personal or project information.

Mitigation: Enable encryption, review what is remembered, and keep tokens and agent keys out of remembered text.

Risk: LAN access or disabled authentication may expose memory to other users.

Mitigation: Bind services to localhost unless LAN access is necessary, and do not use --no-auth.

Risk: MCP configuration changes and autostart can expand the skill's ongoing access.

Mitigation: Review each MCP config change and approve LAN or autostart only after checking what will run.

Risk: Configurable provider and embedding commands can launch local subprocesses.

Mitigation: Inspect the exact commands before enabling provider or embedding integrations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage listed on ClawHub](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Memory protocol](references/protocol.md)
- [Provider protocol](references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text and Markdown memory context with CLI and MCP usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory records can persist locally across sessions and may include private user information.]

## Skill Version(s):

0.22.6 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
