## Description:

Gives AI agents persistent semantic memory and a memory firewall that scans for prompt injection, credential leaks, and poisoned content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and retrieve conversation-derived context, scan agent environments, and protect memory reads and writes from unsafe content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation-derived memories may persist across sessions and become available to other agent interactions.

Mitigation: Review auto-memory settings and disable automatic capture where persistent recall is not wanted.

Risk: OpenClaw startup may automatically modify hook files.

Mitigation: Set SHIELDCORTEX_SKIP_SELF_HEAL=1 if startup file mutation is not acceptable.

Risk: An OpenClaw hook may fetch a package through npx when no local binary is available.

Mitigation: Install and pin a local shieldcortex binary instead of relying on the npx fallback.

Risk: Enabling Cloud sync can upload selected memory content.

Mitigation: Keep Cloud sync disabled unless the content and upload destination are acceptable.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub skill listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis]

**Output Format:** [Markdown with inline shell commands and scan findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and security scan results depend on local configuration and available agent integrations.]

## Skill Version(s):

5.3.1 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
