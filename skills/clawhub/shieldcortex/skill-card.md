## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and security scanning or enforcement against prompt injection, credential leaks, and memory poisoning in AI-agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist conversation-derived data and local memories under ~/.shieldcortex.

Mitigation: Review auto-memory captures before use in sensitive workspaces, delete unneeded memories, and disable auto-memory when persistent capture is not desired.

Risk: The skill can read agent transcripts, local agent configuration, and .env files while scanning for security issues.

Mitigation: Install only in workspaces where this local scanning is acceptable, and review the declared file access before enabling integrations.

Risk: Setup and hook behavior can modify MCP or hook configuration, including a self-heal path for OpenClaw hooks.

Mitigation: Run setup intentionally, inspect configuration changes, and disable self-heal with the documented setting or environment variable in sensitive environments.

Risk: Cloud sync can transmit metadata or selected memory content if explicitly enabled.

Mitigation: Leave cloud sync disabled unless team sync is required, and provide a cloud API key only after confirming the intended data-sharing mode.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ClawHub Publisher Profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex)
- [Drakon Systems GitHub Profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with CLI commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local memory recall, security findings, hook status, and setup or configuration commands.]

## Skill Version(s):

4.54.7 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
