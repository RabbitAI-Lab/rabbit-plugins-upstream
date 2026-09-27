## Description:

Provides persistent, access-controlled memory for AI agents across sessions, with recall, search, and locally stored memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to recall context across sessions, save important information, and maintain locally stored memories with access boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the memory viewer or remote access can disclose private memories.

Mitigation: Keep the viewer on 127.0.0.1; use --host or --no-auth only on trusted, isolated networks.

Risk: Storing access tokens in memories can expose credentials.

Mitigation: Do not save bearer tokens in memories.

Risk: Installation and MCP integration can change agent configuration or autostart behavior.

Mitigation: Review MCP configuration and autostart changes before approval, and pin npm package versions where possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [Memory protocol](references/protocol.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [CLI text and Markdown, with optional JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates locally stored Markdown memory files.]

## Skill Version(s):

0.18.1 (source: skill frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
