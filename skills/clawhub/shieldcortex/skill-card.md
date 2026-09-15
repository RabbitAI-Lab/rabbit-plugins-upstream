## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add persistent local memory, semantic recall, knowledge graph functions, and security scanning or gating to AI agent workflows. It is most relevant for teams that want agent memory with declared local storage, optional cloud sync, and controls for prompt injection, credential leaks, and memory poisoning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive agent memory, transcripts, MCP settings, configuration files, and .env scans.

Mitigation: Install only in environments where this access is acceptable, review or purge ~/.shieldcortex memory and audit data periodically, and disable auto-memory for sensitive sessions.

Risk: Fallback execution paths can use npx and may run unpinned npm code when a local ShieldCortex binary is not configured.

Mitigation: Use a pinned local ShieldCortex installation and set binaryPath so hooks and plugins do not depend on first-use npm resolution.

Risk: Bootstrap self-heal can write hook files automatically.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the ShieldCortex selfHeal configuration when automatic hook writes are not desired.

Risk: Cloud sync and custom cloudBaseUrl settings can introduce outbound data paths when enabled.

Mitigation: Keep Cloud sync off unless needed, provide API keys only intentionally, and use a custom cloudBaseUrl only for endpoints you control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Publisher Profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing memory context, security scan results, setup guidance, and configuration instructions.]

## Skill Version(s):

5.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
