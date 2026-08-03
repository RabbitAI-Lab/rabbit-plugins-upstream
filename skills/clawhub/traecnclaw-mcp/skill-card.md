## Description: <br>
TRAECNclaw MCP lets MCP-capable agents operate TraeCN through focused stdio tools for task submission, context selection, settings changes, conversation management, and exceptional interaction resolution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect an MCP-capable agent to a local TraeCN gateway, send or stop work, choose workspace/model/mode/conversation context, inspect or change Trae settings, manage conversations, and resolve exceptional questions or command approvals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An unsecured or remote gateway could expose TraeCN control to unintended clients. <br>
Mitigation: Keep TRAECN_GATEWAY_HOST bound to 127.0.0.1 unless remote access is explicitly secured. <br>
Risk: Gateway tokens or a custom server path could leak credentials or execute an untrusted launcher target. <br>
Mitigation: Keep TRAECN_GATEWAY_TOKEN out of logs and shared configuration, and set TRAECN_MCP_SERVER_PATH only to a trusted TRAECNclaw server. <br>
Risk: Stopping generation, deleting conversations, or approving commands can affect user work or make irreversible changes. <br>
Mitigation: Use these actions only for explicit user-directed requests, pass exact task or conversation identifiers, require acknowledgements, and record concise audit reasons. <br>
Risk: Mock output or non-terminal task states can be mistaken for completed live TraeCN evidence. <br>
Mitigation: Use mock mode only for development and treat non-terminal task states as incomplete until a final task result is retrieved. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp) <br>
- [MCP surface](references/mcp-surface.md) <br>
- [MCP tool contracts](references/mcp-tool-contracts.json) <br>
- [MCP call examples](references/mcp-call-examples.json) <br>
- [MCP client configuration](assets/mcp-client-config.json) <br>
- [Direct MCP client configuration](assets/mcp-client-config.direct.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance, MCP JSON-RPC tool calls, JSON task/status results, and MCP client configuration JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and a local TRAECNclaw gateway; the release exposes a 20-tool MCP surface with explicit acknowledgements for destructive or sensitive actions.] <br>

## Skill Version(s): <br>
0.5.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
