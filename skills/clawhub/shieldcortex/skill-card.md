## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add local persistent memory, semantic recall, audit trails, and configurable memory-security controls to AI agent workflows. It is suited for users who want memory persistence while managing prompt injection, credential leak, poisoning, and cloud-sync risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read conversation transcripts, scan .env files, and persist memories across sessions.

Mitigation: Review auto-memory settings before sensitive work, disable auto-extraction when needed, and inspect stored local memories and audit previews.

Risk: Cloud sync can transmit memory content when explicitly enabled.

Mitigation: Keep cloud sync disabled unless required, review the Cloud API key and sync settings, and prefer local-only use for sensitive projects.

Risk: Local hooks and setup can write configuration, memory databases, and integration files.

Mitigation: Run setup deliberately, review requested filesystem changes, and use the documented self-heal and auto-memory opt-out settings when tighter control is needed.

## Reference(s):

- [ShieldCortex ClawHub listing](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Publisher profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex homepage](https://shieldcortex.ai)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and generated local memory/security actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local memories, audit previews, and configuration under the user's ShieldCortex-managed local storage; cloud sync is optional and user-configured.]

## Skill Version(s):

4.47.33 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
