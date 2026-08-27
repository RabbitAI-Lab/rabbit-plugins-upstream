## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add persistent local memory, semantic recall, knowledge graph context, and memory-write security checks to supported AI agents. It is intended for local-first agent workflows where memory capture, recall, audit, and prompt-injection or credential-leak screening need to be managed together.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently capture agent context and store selected content in a local ShieldCortex database.

Mitigation: Review or disable auto-memory and proactive recall before sensitive work, and periodically inspect or purge the local database and audit logs under ~/.shieldcortex.

Risk: The skill can read session context and scan .env files while looking for prompt injection, credential leaks, and memory poisoning.

Mitigation: Install only in projects where this local inspection is acceptable, keep secrets out of agent transcripts where possible, and review scan results before relying on stored memory.

Risk: The bundled OpenClaw hook can modify hook files during its self-heal behavior.

Mitigation: Review the installed hook files and disable mutating self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the ShieldCortex self-heal configuration when automatic repair is not desired.

Risk: Optional cloud sync can transmit selected metadata and, for full memory sync, memory content when explicitly enabled.

Mitigation: Leave cloud sync disabled unless needed, require an explicit API key, and review content sync settings before enabling team or enterprise replication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local setup guidance, MCP memory operations, scan summaries, audit guidance, and OpenClaw hook or plugin configuration.]

## Skill Version(s):

4.54.13 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
