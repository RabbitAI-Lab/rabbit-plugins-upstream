## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use ShieldCortex to add local persistent memory, semantic recall, knowledge graph context, and memory-write security controls to AI assistant workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can retain agent context, including content extracted from sessions.

Mitigation: Enable the skill only when persistent local memory is desired, review captured memories, and disable auto-memory when automatic retention is not appropriate.

Risk: Automatic hook repair can mutate OpenClaw hook files during bootstrap.

Mitigation: Disable self-heal when hook mutation is not desired by setting `SHIELDCORTEX_SKIP_SELF_HEAL=1` or the documented self-heal configuration.

Risk: Unpinned npm execution paths can download and run ShieldCortex when a local binary is not configured.

Mitigation: Install a trusted local `shieldcortex` binary and configure `binaryPath` before enabling the OpenClaw hook.

Risk: Custom or cloud endpoints can transmit configured sync or audit data when enabled.

Mitigation: Keep cloud sync disabled unless needed, and avoid custom cloud endpoints unless you control and trust the destination.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ClawHub Publisher Profile](https://clawhub.ai/user/jarvis-drakon)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex)
- [Publisher GitHub Profile](https://github.com/Drakon-Systems-Ltd)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local setup of MCP servers, OpenClaw hooks, and security scanning controls when the user runs the documented commands.]

## Skill Version(s):

5.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
