## Description:

Yotta Memory is a boundary-aware, file-based memory system that helps AI agents restore cross-session context, record long-term memories, search them semantically, and preserve permission boundaries with local storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI-agent users use this skill to give agents persistent local memory across sessions, including start-of-work context recovery, memory capture during work, semantic recall, and end-of-session handoff. It is especially relevant for multi-agent workflows that need shared facts, private preferences, boundaries, commitments, and auditable local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory can retain sensitive, stale, or incorrect information across sessions.

Mitigation: Install only when long-term memory is desired, review stored memories regularly, and use the documented view, recall, and forget workflows to inspect or remove records.

Risk: Bearer tokens, agent keys, and MCP configuration changes can expose private memory if copied into searchable memory or unreviewed config files.

Mitigation: Do not store bearer tokens or agent keys in memory records; prefer key files or secret injection and review MCP configuration edits before enabling them.

Risk: LAN or remote MCP access expands the access surface for a local memory store.

Mitigation: Prefer loopback or stdio MCP, avoid --no-auth, and use TLS, VPN, or SSH tunnels when LAN access is required.

Risk: Optional background services and autostart registration can make the memory service persist beyond a single session.

Mitigation: Review autostart registration, runtime status, and managed service configuration before enabling or relying on background operation.

## Reference(s):

- [Yotta Memory Homepage](https://github.com/YottaMeta/yotta-memory)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and command-line guidance with local memory files managed by the yotta-memory CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions and command workflows for local persistent memory; memory records are stored as user-controlled files.]

## Skill Version(s):

0.16.2 (source: SKILL.md frontmatter, package.json, skill-manifest.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
