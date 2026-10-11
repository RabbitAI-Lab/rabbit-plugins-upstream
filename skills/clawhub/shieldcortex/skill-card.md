## Description:

ShieldCortex gives AI agents persistent semantic memory and scans for prompt injection, credential leaks, and memory poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to recall and manage agent memories and to screen content for security threats. Optional integrations add lifecycle hooks and memory capture to supported agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent agent hooks and automatic memory capture can retain sensitive conversation content.

Mitigation: Review installation on machines with sensitive data; disable auto-memory when transcript capture is not wanted and review stored memories.

Risk: An OpenClaw fallback can fetch and run an unpinned package through npx.

Mitigation: Prefer a pinned local installation and set the configured binaryPath instead of relying on the npx fallback.

Risk: Cloud sync can transmit stored data when enabled, and hook self-heal can make automatic local changes.

Mitigation: Keep cloud sync disabled unless intended and disable self-heal if automatic hook repair is unwanted.

## Reference(s):

- [ShieldCortex on ClawHub](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Memory recall and security findings may depend on local stored data and configured integrations.]

## Skill Version(s):

5.6.0 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
