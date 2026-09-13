## Description:

元忆 yotta-memory is a boundary-aware, file-based memory skill and CLI that lets AI agents save, recall, isolate, back up, and maintain long-lived local memories across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and agent operators use this skill to give AI agents local persistent memory across sessions, with shared FACT records and private PREF, BOUND, and COMMIT records for multi-agent collaboration. It supports recall, context generation, memory writes, backups, diagnostics, and lifecycle maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores long-lived local memory that may contain sensitive personal or project information.

Mitigation: Install it only when persistent memory is desired, keep private memory encrypted, and review or delete stored records through the provided user review and CLI workflows.

Risk: Network, bearer-token, LAN, or no-auth modes can expose persistent memory beyond the local session.

Mitigation: Prefer local stdio or localhost operation, avoid --no-auth, avoid storing bearer tokens in memory, and use LAN mode only on a trusted network with TLS, VPN, or equivalent protection.

Risk: Automation and maintenance commands can mutate, archive, export, or purge memory.

Mitigation: Review autostart, scheduler, embedding_cmd, distill --model, export, maintain --apply, and --purge actions before allowing an agent to run them.

## Reference(s):

- [README](README.md)
- [User Guide](USER_GUIDE.md)
- [Protocol Reference](references/protocol.md)
- [FAQ](references/faq.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text guidance with shell command examples and local memory files generated through the yotta-memory CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include recalled memory context, saved Markdown memory records, diagnostics, backup status, and configuration instructions.]

## Skill Version(s):

0.13.0 (source: frontmatter, package.json, skill-manifest.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
