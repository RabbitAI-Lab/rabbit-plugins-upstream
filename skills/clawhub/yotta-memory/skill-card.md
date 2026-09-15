## Description:

元忆 yotta-memory gives agents a local, file-based memory system with permission boundaries, recall and remember workflows, shared FACT memory, private PREF/BOUND/COMMIT memory, backups, rollback, and optional MCP access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to persist, recall, maintain, and back up agent memory across sessions and projects while separating public facts from private preferences, boundaries, and commitments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared or LAN memory deployments can expose private or multi-agent memory when the MCP service is unauthenticated or broadly reachable.

Mitigation: Keep the MCP service authenticated and bound to localhost unless LAN access is required; do not use --no-auth on untrusted networks.

Risk: Remote maintenance or destructive actions can affect shared memory stores.

Mitigation: Do not expose archive, maintain --apply, or purge to remote agents until ownership checks are reviewed, and rely on backup and doctor checks before destructive writes.

Risk: Bearer tokens stored in long-term memory can be exposed through later recall or storage access.

Mitigation: Avoid storing bearer tokens in memory and rotate credentials if they are accidentally recorded.

Risk: Autostart and scheduler setup can persist behavior on the host machine.

Mitigation: Enable autostart and scheduled backups only after reviewing what will persist and how to disable it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [npm package @yottameta/yotta-memory](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol reference](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with CLI commands and structured memory file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local memory records, indexes, backup artifacts, trash entries, and archive entries through the yotta-memory CLI or MCP tools.]

## Skill Version(s):

0.13.1 (source: frontmatter, package.json, changelog released 2026-09-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
