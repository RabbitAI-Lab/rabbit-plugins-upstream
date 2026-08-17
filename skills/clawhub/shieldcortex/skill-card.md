## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and memory-write security checks to supported AI agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read agent configuration files, inspect conversation content, scan .env files, and store extracted memories locally.

Mitigation: Review auto-memory and scanning settings before enabling it, periodically inspect or purge ~/.shieldcortex, and disable auto-extraction when working with highly sensitive content.

Risk: Automatic hook self-heal behavior can persist or refresh OpenClaw hook files without an interactive prompt during gateway bootstrap.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or selfHeal:false, or remove the hook entirely when persistent memory integration is not needed.

Risk: Cloud sync is optional, but enabling it can sync eligible stored memory content depending on license and configuration.

Mitigation: Keep cloud sync off unless it is required, review what memory categories may sync, and use metadata-only or exclusion settings where appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Declared project source](https://github.com/Drakon-Systems-Ltd/ShieldCortex)
- [Declared publisher profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text with CLI commands, configuration snippets, and MCP/tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce memory recall context and security decisions such as allow, quarantine, or block.]

## Skill Version(s):

4.54.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
