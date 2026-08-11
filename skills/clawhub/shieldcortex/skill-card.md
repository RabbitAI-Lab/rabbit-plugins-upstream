## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add persistent local memory, semantic recall, audit, and memory-write security controls to agent workflows such as OpenClaw, Claude Code, Cursor, and Codex.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist conversation-derived memories and audit previews across sessions under ~/.shieldcortex.

Mitigation: Use it only when persistent local memory is desired, and periodically review or purge stored memories and audit logs on sensitive projects.

Risk: The skill can hook agent sessions and automatically repair or install hook components.

Mitigation: Review the self-heal setting before first OpenClaw gateway startup, and disable self-heal when automatic hook repair is not wanted.

Risk: Security audits can read agent configuration files and .env files to check for leaks.

Mitigation: Run audits only in workspaces where that local inspection is acceptable.

Risk: Cloud sync can transmit selected data when explicitly enabled.

Mitigation: Keep cloud sync disabled unless it is required, and enable it only with an intended API key and sync policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [Declared Project Repository](https://github.com/Drakon-Systems-Ltd/ShieldCortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)
- [Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide installation or configuration steps that create local memory, audit, and hook state under ~/.shieldcortex and related agent configuration paths.]

## Skill Version(s):

4.47.38 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
