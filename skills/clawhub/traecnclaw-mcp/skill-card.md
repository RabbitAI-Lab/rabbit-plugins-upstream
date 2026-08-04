## Description: <br>
TRAECNclaw MCP lets MCP-capable agents operate TraeCN through focused stdio tools for task submission, workspace, model, mode and conversation selection, settings changes, conversation management, generation stops, and exceptional approvals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and MCP-capable agent users use this skill to connect an agent to a trusted local TRAECNclaw gateway for sending TraeCN tasks, managing TraeCN context and settings, and resolving command approvals or destructive actions with audit safeguards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gateway exposure could allow an agent or remote client to control TraeCN outside the intended local trust boundary. <br>
Mitigation: Install the matching TRAECNclaw server from a trusted source, keep the gateway bound to 127.0.0.1 unless remote access is secured, and set TRAECN_GATEWAY_TOKEN if exposed beyond local use. <br>
Risk: Settings changes, conversation deletions, generation stops, and command approvals can have high impact. <br>
Mitigation: Review those actions before allowing them; require exact command, title, or conversation matching plus the documented acknowledgement and audit reason where applicable. <br>
Risk: Mock output or non-terminal task states could be mistaken for completed live TraeCN results. <br>
Mitigation: Treat mock results and non-terminal task states as incomplete, and do not cite mock output as live TraeCN evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp) <br>
- [MCP Surface](artifact/references/mcp-surface.md) <br>
- [MCP Tool Contracts](artifact/references/mcp-tool-contracts.json) <br>
- [MCP Call Examples](artifact/references/mcp-call-examples.json) <br>
- [MCP Client Config](artifact/assets/mcp-client-config.json) <br>
- [Direct MCP Client Config](artifact/assets/mcp-client-config.direct.json) <br>
- [MCP Servers JSON Schema](https://json.schemastore.org/mcp-servers.json) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Configuration, Guidance, Shell commands] <br>
**Output Format:** [Markdown guidance with MCP tool calls and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and a matching TRAECNclaw gateway; uses optional TRAECN_GATEWAY_HOST, TRAECN_GATEWAY_PORT, TRAECN_GATEWAY_TOKEN, and TRAECN_MCP_CLIENT_ID environment variables.] <br>

## Skill Version(s): <br>
0.5.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
