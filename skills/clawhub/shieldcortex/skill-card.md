## Description:

Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph features, and security scanning against prompt injection, credential leaks, and memory poisoning across supported agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read conversation transcripts, agent configuration files, and optional environment files for memory capture and security scanning.

Mitigation: Install only where persistent local memory and security scanning are intended; review auto-memory settings, local audit logs, and environment scanning before use on sensitive projects.

Risk: Cloud sync is optional but can introduce data egress when enabled with an API key.

Mitigation: Keep cloud sync disabled unless needed, verify cloud-sync settings before use, and review which memory classes are eligible for sync.

Risk: The bundled OpenClaw hook includes a self-heal path that can copy hook files and remove named stale legacy hook directories.

Mitigation: Disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the skill's self-heal configuration when automatic hook maintenance is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex)
- [ShieldCortex Homepage](https://shieldcortex.ai)
- [ShieldCortex Documentation](https://shieldcortex.ai/docs)
- [npm Package](https://www.npmjs.com/package/shieldcortex)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local memory recall results, scan findings, audit records, and setup guidance when configured.]

## Skill Version(s):

4.54.9 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
