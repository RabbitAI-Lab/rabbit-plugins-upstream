## Description: <br>
Operate TraeCN through TRAECNclaw's focused stdio MCP tools for workspace, model, mode, conversation, settings, task, approval, and deletion workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and MCP-capable agent users use this skill to operate TraeCN through a focused stdio MCP surface, including sending work, selecting context, reading task results, changing settings, and resolving exceptional interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate TraeCN through a gateway, including settings changes, approvals, stops, and conversation management. <br>
Mitigation: Install it only when an MCP-capable agent is intended to operate TraeCN, and review command approvals or conversation deletions carefully before allowing them. <br>
Risk: A remote or exposed gateway, untrusted server path, or leaked gateway token could allow unintended access to TraeCN operations. <br>
Mitigation: Keep the gateway on loopback unless remote access is secured, set server paths only to trusted local TRAECNclaw servers, and protect the gateway token. <br>
Risk: Mock output or non-terminal task states can be mistaken for completed live TraeCN results. <br>
Mitigation: Use mock mode only for development and treat non-terminal task states as incomplete. <br>


## Reference(s): <br>
- [TRAECNclaw MCP Skill Page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp) <br>
- [MCP Surface](artifact/references/mcp-surface.md) <br>
- [MCP Tool Contracts](artifact/references/mcp-tool-contracts.json) <br>
- [MCP Call Examples](artifact/references/mcp-call-examples.json) <br>
- [MCP server configuration schema](https://json.schemastore.org/mcp-servers.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with MCP tool calls, JSON configuration examples, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing operational guidance for a 20-tool stdio MCP surface; requires Node and a trusted TRAECNclaw MCP server path when not installed in-repo.] <br>

## Skill Version(s): <br>
0.5.1 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
