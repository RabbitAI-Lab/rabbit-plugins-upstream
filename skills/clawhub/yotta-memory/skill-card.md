## Description:

Yuanyi yotta-memory provides boundary-aware, file-based persistent memory for AI agents, with shared factual memory, private agent-scoped memory, recall/context workflows, backup, rollback, and local or MCP access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to give AI agents persistent, auditable memory across sessions and projects. It supports saving important facts, preferences, boundaries, and commitments, then recalling or summarizing them through CLI or MCP workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can retain sensitive personal or project information across sessions.

Mitigation: Install only when persistent AI memory is intended, use encrypted stores, and avoid storing bearer tokens or agent keys in remembered profile text.

Risk: LAN serving or remote MCP access can expose private memories if enabled on untrusted networks or configured without strong authentication.

Mitigation: Prefer local or stdio use; for remote access use localhost, VPN, SSH tunnel, or a TLS-protected proxy, and do not use --no-auth.

Risk: Maintenance, archive, consolidate, and purge operations can alter or remove memory records.

Mitigation: Treat these as administrative operations, review previews where available, keep independent backups, and run doctor checks before destructive writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol specification](references/protocol.md)
- [FAQ](references/faq.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include recall results, context packages, memory write instructions, backup and doctor guidance, and MCP setup guidance.]

## Skill Version(s):

0.13.2 (source: frontmatter, package.json, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
