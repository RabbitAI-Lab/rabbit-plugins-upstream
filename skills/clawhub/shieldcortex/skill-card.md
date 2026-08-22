## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and memory-write security controls for AI agent workflows. It is most relevant when teams want agent memory with scanning for prompt injection, credential leakage, and memory poisoning risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist agent memory and conversation-derived content in a local memory database.

Mitigation: Review captured memories during sensitive work, disable auto-memory or proactive recall unless needed, and keep cloud sync off unless explicit team sync is required.

Risk: The bundled OpenClaw hook self-heal can repair hook files and remove stale legacy hook directories without a live prompt at gateway bootstrap.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the selfHeal:false configuration before running OpenClaw if automatic hook repair is not desired.

Risk: Cloud sync can transmit selected memory content when explicitly enabled with an API key.

Mitigation: Leave cloud sync disabled for local-only use, avoid syncing sensitive memories, and use the documented content controls when enabling team sync.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ClawHub Publisher Profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Text and Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-stream agent guidance, memory recall text, scan results, and local configuration instructions.]

## Skill Version(s):

4.54.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
