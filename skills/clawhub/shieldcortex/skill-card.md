## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use ShieldCortex to give AI agents persistent, searchable memory and to scan or filter memory and tool content for security threats. It also provides setup guidance for connecting the memory server and optional integrations to supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package resolution may fetch packages without pinned versions.

Mitigation: Review package sources and pin versions before installation; preinstall required packages where automatic npx resolution is not wanted.

Risk: The tool can inspect sensitive agent settings, memory, and conversation data.

Mitigation: Review the declared file access and enable only the integrations and transcript capture needed for the task.

Risk: The OpenClaw startup self-heal can remove named legacy hook directories without confirmation.

Mitigation: Inspect those directories before enabling the hook, or set SHIELDCORTEX_SKIP_SELF_HEAL=1 to make the self-heal warn-only.

Risk: The security analysis is partial because some referenced paths could not be resolved.

Mitigation: Review the relevant package sources and unresolved paths before installing.

## Reference(s):

- [ShieldCortex documentation](https://shieldcortex.ai/docs)
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex)
- [ShieldCortex changelog](https://shieldcortex.ai/changelog)
- [Dependency audit waivers](https://github.com/Drakon-Systems-Ltd/ShieldCortex/blob/main/docs/security/audit-waivers.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup and usage guidance for local memory, security scanning, and optional agent integrations.]

## Skill Version(s):

5.18.1 (source: server release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
