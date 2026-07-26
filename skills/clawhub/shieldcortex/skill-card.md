## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use ShieldCortex to add persistent local memory, semantic recall, knowledge graph features, and security scanning or enforcement around memory writes and tool output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist conversation-derived data in local memory. <br>
Mitigation: Review auto-memory and proactive recall settings before enabling; disable auto-memory for sensitive projects and regularly inspect or purge ~/.shieldcortex. <br>
Risk: The hook can automatically change or delete hook files during bootstrap. <br>
Mitigation: Review self-heal behavior before use; set SHIELDCORTEX_SKIP_SELF_HEAL=1 or disable self-heal in config when automatic file changes are not acceptable. <br>
Risk: Optional cloud sync can transmit selected memory content when explicitly enabled. <br>
Mitigation: Keep cloud sync disabled unless needed; if enabling it, review API key, memory classification, and content-mode settings first. <br>


## Reference(s): <br>
- [ShieldCortex ClawHub page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [Publisher profile](https://clawhub.ai/user/jarvis-drakon) <br>
- [ShieldCortex homepage](https://shieldcortex.ai) <br>
- [ShieldCortex documentation](https://shieldcortex.ai/docs) <br>
- [ShieldCortex source link from metadata](https://github.com/Drakon-Systems-Ltd/ShieldCortex) <br>
- [ShieldCortex npm package](https://www.npmjs.com/package/shieldcortex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with command examples and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local CLI commands, MCP configuration, and security guidance for the user's agent environment.] <br>

## Skill Version(s): <br>
4.47.16 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
