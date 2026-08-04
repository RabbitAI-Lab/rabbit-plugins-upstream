## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph behavior, and security scanning to AI-agent workflows. It is suited for teams that want memory retention with reviewable controls for prompt injection, credential leakage, memory poisoning, and optional cloud sync. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can retain conversation content and agent memories locally. <br>
Mitigation: Review captured memories, disable auto-memory or proactive recall when working with sensitive content, and periodically purge or inspect ~/.shieldcortex/. <br>
Risk: The skill can scan sensitive local agent files and persistently modify agent hook or MCP configuration files. <br>
Mitigation: Install only after review, run setup intentionally, inspect the declared read/write paths, and keep self-heal warn-only with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the self-heal config when desired. <br>
Risk: Cloud sync can transmit memory data when explicitly enabled. <br>
Mitigation: Keep cloud sync disabled unless needed, provide a cloud API key only for approved workflows, and use the available metadata-only or classification controls for sensitive data. <br>


## Reference(s): <br>
- [ShieldCortex ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [ShieldCortex homepage](https://shieldcortex.ai) <br>
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex) <br>
- [Drakon Systems publisher profile](https://github.com/Drakon-Systems-Ltd) <br>
- [ShieldCortex documentation](https://shieldcortex.ai/docs) <br>
- [ShieldCortex changelog](https://shieldcortex.ai/changelog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, local MCP/tool responses, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local memory, configuration, hook/plugin files, and audit logs when installed and enabled by the user.] <br>

## Skill Version(s): <br>
4.47.30 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
