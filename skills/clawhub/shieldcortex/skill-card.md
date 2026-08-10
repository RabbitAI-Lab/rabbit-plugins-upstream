## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add local-first persistent memory, semantic recall, knowledge graph support, and memory-boundary security checks to AI agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs durable agent hooks, can self-repair integrations, and can persist conversation-derived memory.

Mitigation: Review setup changes before enabling integrations, decide whether to disable self-heal and auto-memory, and periodically inspect stored memories.

Risk: The skill can inspect agent configuration and .env files and may retain selected conversation content locally.

Mitigation: Install only when a local-first memory and security layer is desired, keep sensitive projects under review, and disable capture paths that are not needed.

Risk: Cloud sync can transmit metadata and selected memories when explicitly enabled.

Mitigation: Leave Cloud sync disabled unless its data handling is acceptable, and enable it only with an intentional API key configuration.

## Reference(s):

- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Drakon Systems Ltd publisher profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local memory and security guidance for agent setup, recall, scanning, auditing, and optional cloud synchronization.]

## Skill Version(s):

4.47.35 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
