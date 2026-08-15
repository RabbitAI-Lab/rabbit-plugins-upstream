## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and engineers use ShieldCortex to add persistent local memory, semantic recall, knowledge graph tooling, and memory-write security checks to supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can store conversation-derived content, including sensitive project context.

Mitigation: Review captured memories, disable openclawAutoMemory or proactive recall for sensitive work, and purge stored memories when needed.

Risk: Cloud sync can upload metadata and selected memory content when explicitly enabled.

Mitigation: Keep cloud sync disabled unless needed, and enable it only after accepting the API key and memory-content handling.

Risk: Setup and self-heal behavior can maintain OpenClaw hook files and MCP or plugin configuration.

Mitigation: Run quickstart or setup deliberately, review prompts and config, and set selfHeal false or SHIELDCORTEX_SKIP_SELF_HEAL=1 if automatic hook repair is not acceptable.

Risk: Agent config and .env scans may read files that contain secrets.

Mitigation: Avoid scans and auto-memory in secret-heavy projects unless prepared to review and purge stored memories.

## Reference(s):

- [ShieldCortex ClawHub listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Drakon Systems GitHub profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or update local memory, audit, hook, plugin, and MCP configuration files when setup or memory actions are run.]

## Skill Version(s):

4.52.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
