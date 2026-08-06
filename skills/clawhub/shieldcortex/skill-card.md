## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to give AI agents persistent local memory, semantic recall, knowledge-graph support, and security scanning for memory writes, prompts, credentials, and agent configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ShieldCortex is a high-privilege local memory and security layer that can read agent sessions and configuration files, persist extracted memories, and modify OpenClaw or MCP integration files.

Mitigation: Install it only when that local memory/security behavior is desired, and treat ~/.shieldcortex/ data, including audit logs, as sensitive.

Risk: Automatic memory capture can store conversation context in the local memory database.

Mitigation: Disable auto-memory for sensitive projects and review stored memories before relying on or syncing them.

Risk: The bundled OpenClaw hook includes self-heal behavior that can repair or copy hook files during gateway bootstrap.

Mitigation: Disable self-heal when automatic hook repair is not acceptable.

Risk: Cloud sync can transmit selected memory data when explicitly enabled with a Cloud API key.

Mitigation: Keep Cloud sync off unless it is needed, and enable it only with an intentional API key configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP setup steps, local configuration guidance, and security-operation recommendations.]

## Skill Version(s):

4.47.31 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
