## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and security scanning around agent memory writes and recalled context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks and local memory can capture conversation-derived content and keep it in local storage.

Mitigation: Install only when persistent memory is desired, periodically review or purge ~/.shieldcortex/ storage, and disable auto-memory or proactive recall before sensitive work unless explicitly needed.

Risk: The bundled hook includes automatic self-heal behavior that can mutate specific OpenClaw hook paths.

Mitigation: Set SHIELDCORTEX_SKIP_SELF_HEAL=1 or configure selfHeal:false to make self-heal warn-only, and use the documented install command for manual repair.

Risk: Cloud sync can transmit data when explicitly enabled with an API key.

Mitigation: Leave cloud sync disabled for local-only use and enable it only after confirming what metadata or memory content the selected sync mode sends.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [npm package](https://www.npmjs.com/package/shieldcortex)
- [Source repository](https://github.com/Drakon-Systems-Ltd/ShieldCortex)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local file, hook, memory database, MCP configuration, and optional cloud-sync setup.]

## Skill Version(s):

4.49.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
