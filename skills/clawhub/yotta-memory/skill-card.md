## Description:

Yuanyi yotta-memory provides boundary-aware, file-based long-term memory for AI agents, with recall, remember, context generation, archival, semantic search, and permission boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to let AI agents preserve useful context across sessions, retrieve prior facts and commitments, and manage public versus private memory boundaries through the yotta-memory CLI or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and replays long-lived cross-agent context, which may preserve sensitive or stale information.

Mitigation: Install it only when persistent agent memory is intended, review remembered content regularly, and use the documented private memory boundaries.

Risk: Credential-like connection data could be captured in persistent memory guidance or memory entries.

Mitigation: Do not store tokens or agent_key values in memories; keep credentials in the configured secret or key-file paths instead.

Risk: MCP configuration, LAN mode, or autostart features can broaden exposure if enabled casually.

Mitigation: Use the core MCP tool profile where possible, review MCP configuration changes before applying them, pin the package version, and enable LAN or autostart only when the exposure is understood.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Publisher profile](https://clawhub.ai/user/yottameta)
- [Homepage](https://github.com/YottaMeta/yotta-memory)
- [Protocol reference](references/protocol.md)
- [FAQ](references/faq.md)
- [User guide](USER_GUIDE.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or CLI snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory operations and configuration guidance; no cloud service output is required by default.]

## Skill Version(s):

0.16.7 (source: frontmatter, package.json, skill-manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
