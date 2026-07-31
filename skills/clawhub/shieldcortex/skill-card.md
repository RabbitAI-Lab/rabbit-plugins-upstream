## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use ShieldCortex to add local persistent memory, semantic recall, knowledge graph support, and security checks around memory writes, recalls, agent instructions, MCP configuration, and optional OpenClaw realtime hooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Conversation-derived content and local audit previews can be retained under ~/.shieldcortex. <br>
Mitigation: Review auto-memory behavior before use, disable auto-memory or proactive recall for sensitive work, and remove stored memories when retention is not desired. <br>
Risk: Cloud sync can send selected memory or audit metadata when explicitly enabled. <br>
Mitigation: Keep cloud sync disabled unless remote synchronization is intended, and only configure a cloud API key for workflows where that data sharing is acceptable. <br>
Risk: Setup and hook behavior can register MCP/agent hooks and maintain OpenClaw hook files on the local machine. <br>
Mitigation: Run setup intentionally, inspect the declared paths, and disable self-heal with configuration or SHIELDCORTEX_SKIP_SELF_HEAL=1 when hook file maintenance is not desired. <br>
Risk: Security scans include agent configuration files and may inspect .env files for leaked secrets. <br>
Mitigation: Use the tool only in workspaces where local scanning of agent configuration and environment files is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [Publisher profile](https://clawhub.ai/user/jarvis-drakon) <br>
- [ShieldCortex homepage](https://shieldcortex.ai) <br>
- [npm package](https://www.npmjs.com/package/shieldcortex) <br>
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands, configuration snippets, and agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local setup, MCP registration, memory operations, security scans, dashboard/service commands, cloud-sync configuration, and OpenClaw hook/plugin behavior.] <br>

## Skill Version(s): <br>
4.47.18 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
