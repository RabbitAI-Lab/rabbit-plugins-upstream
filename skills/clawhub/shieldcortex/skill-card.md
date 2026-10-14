## Description:

Provides semantic memory, knowledge-graph recall, and a firewall that scans agent content for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to retain and recall useful context across sessions while scanning agent instructions, memory, and tool activity for security threats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks can access agent transcripts and store sensitive context in local memory.

Mitigation: Review captured memories and disable auto-memory for sensitive projects.

Risk: Cloud sync can upload selected memories when enabled.

Mitigation: Leave Cloud sync off unless remote memory storage is intended.

Risk: The OpenClaw hook can fetch and run the package through an npx fallback.

Mitigation: Install and pin a local ShieldCortex binary before enabling the hook.

Risk: Bootstrap-time self-heal can modify OpenClaw hook files.

Mitigation: Set self-heal to warn-only if automatic hook changes are not acceptable.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex on npm](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex ClawHub release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes memory recall and security scan findings where enabled.]

## Skill Version(s):

5.9.0 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
