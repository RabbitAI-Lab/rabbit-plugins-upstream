## Description: <br>
Memory and defence for AI agents: semantic recall, knowledge graph and decay, plus a memory firewall that scans and enforces against prompt injection, credential leaks and poisoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use ShieldCortex to add persistent local memory, recall, knowledge-graph support, and memory-boundary security checks to AI agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically modify agent hook installations and integration files. <br>
Mitigation: Review setup and self-heal behavior before use, keep changes user-initiated where possible, and disable self-heal with SHIELDCORTEX_SKIP_SELF_HEAL=1 or the ShieldCortex selfHeal configuration when automatic hook repair is not desired. <br>
Risk: The skill can persist sensitive conversation-derived data in local memory and audit stores. <br>
Mitigation: Review or disable auto-memory and lifecycle handlers for sensitive projects, audit stored memories regularly, and remove unwanted entries with the provided forget or purge workflows. <br>
Risk: Cloud sync can transmit selected data when explicitly enabled. <br>
Mitigation: Keep cloud sync disabled unless needed, provide an API key only after review, and use metadata-only or restricted sync settings where full memory content should not leave the local machine. <br>
Risk: Security evidence marks the release as requiring review because it reads transcripts and selected configuration files. <br>
Mitigation: Install only in trusted workspaces after confirming the declared read/write paths, lifecycle hooks, cloud settings, and memory retention behavior match the user's risk tolerance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jarvis-drakon/skills/shieldcortex) <br>
- [ShieldCortex Homepage](https://shieldcortex.ai) <br>
- [ShieldCortex Documentation](https://shieldcortex.ai/docs) <br>
- [ShieldCortex npm Package](https://www.npmjs.com/package/shieldcortex) <br>
- [Metadata Source URL](https://github.com/Drakon-Systems-Ltd/ShieldCortex) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local memories, audit records, and integration configuration under the user's ShieldCortex and agent configuration directories.] <br>

## Skill Version(s): <br>
4.47.27 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
