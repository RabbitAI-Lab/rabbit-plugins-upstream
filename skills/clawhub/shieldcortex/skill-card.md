## Description:

Provides persistent agent memory and security scanning to help detect prompt injection, credential leaks, and poisoned memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to retain and recall context across sessions, inspect agent files and memories for threats, and configure local memory and security integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security scans can read sensitive agent configuration, MCP settings, .env files, and session-derived content.

Mitigation: Review the requested file access and enable integrations only where that access is appropriate.

Risk: Persistent hooks and automatic memory capture can retain sensitive session context.

Mitigation: Review auto-memory settings and inspect or remove stored memories as needed.

Risk: Automatic hook self-heal can modify hook files without a prompt.

Mitigation: Set SHIELDCORTEX_SKIP_SELF_HEAL=1 if automatic hook changes are not acceptable.

Risk: The OpenClaw hook can run an unpinned npx fallback when ShieldCortex is not installed locally.

Mitigation: Use a trusted local installation and set its binary path instead of relying on the npx fallback.

Risk: Cloud sync can send stored memory content off the device when enabled.

Mitigation: Leave Cloud sync disabled unless sharing memory content is intended; review sync settings before enabling it.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Security findings, Shell commands, Configuration guidance]

**Output Format:** [Markdown text with inline commands and memory or scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local memory recall and security findings depend on configured integrations.]

## Skill Version(s):

5.7.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
