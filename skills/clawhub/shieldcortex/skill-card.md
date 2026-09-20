## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add local persistent memory, semantic recall, knowledge graph features, and security scanning to AI-agent workflows. It is intended for environments where agent memory writes and recalled context need prompt-injection, credential-leak, poisoning, and audit controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive local persistence and may read agent configuration, MCP configuration, .env files, and some conversation content.

Mitigation: Review before installation, use it only when a persistent memory and security layer is desired, and disable auto-memory when session capture does not fit the workflow.

Risk: Security evidence reports that supposedly blocked memory writes may not be prevented by default.

Mitigation: Wait for or apply a fix that makes BLOCK and QUARANTINE outcomes prevent memory writes before relying on enforcement.

Risk: Runtime package execution can occur through the npx fallback path.

Mitigation: Prefer a pinned local ShieldCortex installation or configured binary path instead of the npx fallback.

Risk: Cloud sync can transmit selected memory data when explicitly enabled.

Mitigation: Keep Cloud sync disabled unless needed, and enable it only with an intentional API key and appropriate data handling review.

Risk: The OpenClaw hook includes self-heal behavior that can write hook files unless disabled.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the documented configuration when automatic hook migration is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Project Homepage](https://shieldcortex.ai)
- [Documentation](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [GitHub Repository](https://github.com/Drakon-Systems-Ltd/ShieldCortex)
- [Issue Tracker](https://github.com/Drakon-Systems-Ltd/ShieldCortex/issues)
- [Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON configuration snippets; runtime tool outputs may be text or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent memory context, scan results, audit/status messages, and setup guidance; installed workflows may also create local memory, configuration, cache, and audit files.]

## Skill Version(s):

5.0.6 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
