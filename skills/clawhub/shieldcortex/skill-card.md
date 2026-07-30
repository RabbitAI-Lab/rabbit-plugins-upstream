## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph support, and memory-boundary security scanning to AI agent workflows. It is intended for workflows that need local memory capture, recall, auditing, and controls for prompt injection, credential leaks, poisoning, and related agent-memory risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read agent and project configuration files, scan .env files, and persist selected conversation-derived memories locally. <br>
Mitigation: Install only when persistent local memory and scanning are desired; review captured memories and disable auto-memory if automatic capture does not fit the workflow. <br>
Risk: Cloud sync can cause metadata or selected memories to leave the machine when explicitly enabled. <br>
Mitigation: Keep cloud sync disabled unless remote sync is needed, and review the selected memory and metadata sync settings before providing a cloud API key. <br>
Risk: The bundled OpenClaw integration can modify hook locations through documented setup and self-heal behavior. <br>
Mitigation: Use the documented setup flow deliberately and disable self-heal with configuration or SHIELDCORTEX_SKIP_SELF_HEAL when automatic hook repair is not acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [ShieldCortex Homepage](https://shieldcortex.ai) <br>
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex) <br>
- [Drakon Systems GitHub Profile](https://github.com/Drakon-Systems-Ltd) <br>
- [ShieldCortex Documentation](https://shieldcortex.ai/docs) <br>
- [ShieldCortex Changelog](https://shieldcortex.ai/changelog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide setup, local memory operations, scans, audits, cloud-sync configuration, and OpenClaw integration.] <br>

## Skill Version(s): <br>
4.47.17 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
