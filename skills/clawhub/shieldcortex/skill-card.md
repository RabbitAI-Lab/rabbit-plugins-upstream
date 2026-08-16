## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory and security checks to AI agent workflows, including semantic recall, knowledge graph recall, memory write filtering, and prompt-injection or credential-leak scanning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can retain conversation content and agent context locally.

Mitigation: Install only when persistent local agent memory is desired, review what auto-memory captures, and disable auto-memory or proactive recall when the retention scope is not acceptable.

Risk: Setup and hook behavior can modify agent hook or MCP configuration files, including documented bootstrap self-heal behavior.

Mitigation: Review quickstart prompts before accepting changes and disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the ShieldCortex self-heal configuration when bootstrap-time mutation is not acceptable.

Risk: Cloud sync can share selected memory or audit data when explicitly enabled.

Mitigation: Keep cloud sync off unless the intended sharing scope is understood, and provide a cloud API key only for workflows where sync is approved.

Risk: The npx fallback can download and execute the package when a local ShieldCortex binary is unavailable.

Mitigation: Install a trusted pinned ShieldCortex binary and configure the binary path to avoid first-use package fetching.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Publisher Profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, local memory recall, and security scan guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can persist local agent memory and produce security findings; cloud sync is opt-in and requires user-provided credentials.]

## Skill Version(s):

4.53.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
