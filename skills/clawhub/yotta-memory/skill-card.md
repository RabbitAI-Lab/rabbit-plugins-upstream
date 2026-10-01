## Description:

Provides persistent, file-based memory for AI agents with cross-session recall, semantic search, and access boundaries for private records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use it to retain and retrieve project and personal context across sessions while keeping designated private memories separate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent private memories and credentials may be exposed through inappropriate storage or access.

Mitigation: Manage credentials securely and do not put bearer tokens in memory records.

Risk: The local viewer or LAN service may become reachable beyond the intended user.

Mitigation: Keep the viewer bound to 127.0.0.1; enable LAN access only with appropriate network controls.

Risk: Runtime installs, autostart, and package updates can change local services and executable code.

Mitigation: Prefer pinned package versions and enable runtime installs or LAN autostart only when a persistent local service is intended.

Risk: MCP configuration changes can alter agent access to the memory system.

Mitigation: Review MCP configuration changes before applying them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [Memory protocol](artifact/references/protocol.md)
- [Extension provider protocol](artifact/references/provider-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI output, with optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory retrieval respects configured identity and access boundaries; context selection can be budgeted.]

## Skill Version(s):

0.20.0 (source: skill frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
