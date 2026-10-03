## Description:

ShieldCortex provides AI agents with persistent semantic memory, knowledge-graph recall, and security scanning for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and recall useful context across sessions, scan agent configurations and memories for threats, and manage local memory safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persisted conversation-derived memories may contain sensitive information.

Mitigation: Review stored memories and disable automatic capture when handling sensitive work.

Risk: Security scans can read agent configuration, transcripts, MCP settings, and .env files; cloud sync may transmit selected memories if enabled.

Mitigation: Review the data-access scope before installation and keep cloud sync disabled unless needed.

Risk: Automatic hook repair or an npx fallback can change local integration code or fetch a package at runtime.

Mitigation: Prefer a pinned local installation and consider disabling self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or selfHeal:false.

## Reference(s):

- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub skill release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown with inline commands and scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and security findings depend on the local configuration and agent integration.]

## Skill Version(s):

5.3.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
