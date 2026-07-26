## Description: <br>
Persistent structured memory - save, recall, and update facts, decisions, people, and projects across sessions via the xmemory MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xmemory](https://clawhub.ai/user/xmemory) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to configure and operate xmemory as persistent structured memory for durable facts, decisions, people, preferences, and project state across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent memory can store sensitive or unintended durable facts. <br>
Mitigation: Save only facts the user intends to retain, avoid secrets and sensitive personal data unless explicitly intended, and use separate instances for work and personal memory. <br>
Risk: The xmemory API key grants access to the configured memory service. <br>
Mitigation: Keep XMEM_API_KEY in the host environment, do not commit it into configuration, and rotate it if exposure is suspected. <br>
Risk: The optional admin connection exposes instance and schema administration, including destructive operations. <br>
Mitigation: Register the admin connection only when needed and confirm with the user before applying schema changes, migrations, or instance deletion. <br>


## Reference(s): <br>
- [xmemory homepage](https://xmemory.ai) <br>
- [xmemory console](https://console.xmemory.ai) <br>
- [ClawHub skill page](https://clawhub.ai/xmemory/skills/xmemory) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XMEM_API_KEY and XMEM_INSTANCE_ID for normal instance access; optional admin connection should be registered only when needed.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
