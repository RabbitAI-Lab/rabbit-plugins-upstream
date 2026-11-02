## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent memory, semantic recall, and knowledge-graph features to agent workflows. They can also use its documented scanning and hook integrations to identify and enforce against prompt injection, credential leaks, and poisoned memory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabled OpenClaw hooks can automatically download and execute unpinned packages, and the bootstrap self-heal can alter hook files without asking.

Mitigation: Review the hooks before enabling them, use reviewed exact package versions, prevent hook-time registry execution, back up customized hooks, and consider `shieldcortex config --self-heal false` before restarting the gateway.

Risk: Conversation capture and cloud sync can store or transmit conversation and memory content when enabled.

Mitigation: Keep automatic conversation capture and cloud sync disabled unless needed, and review what is captured before enabling either feature.

Risk: This release contains instructions only; the external executables and their security guarantees were not verified.

Mitigation: Review the external package and its behavior before installing or enabling its hooks.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ClawHub skill release](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [Project source (listed in skill metadata; provenance unavailable)](https://github.com/Drakon-Systems-Ltd/ShieldCortex)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructional content; executable tools are installed separately.]

## Skill Version(s):

5.17.2 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
