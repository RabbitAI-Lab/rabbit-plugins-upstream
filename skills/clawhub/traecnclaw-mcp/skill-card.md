## Description: <br>
Operate TraeCN through focused stdio MCP tools for sending work, changing context, managing settings and conversations, and resolving exceptional approvals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luckycat133](https://clawhub.ai/user/luckycat133) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and MCP-capable agents use this skill to operate TraeCN through a focused local MCP surface while the gateway handles queueing, recovery, notifications, safe approvals, and keep/revert gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The local MCP bridge can control TraeCN settings, conversations, task cancellation, visible generation stops, and approval decisions. <br>
Mitigation: Use the focused tools only for the current user request and review high-impact actions before execution. <br>
Risk: A remote or exposed gateway, leaked gateway token, or untrusted server path could broaden control beyond the intended local setup. <br>
Mitigation: Keep the gateway bound to loopback unless remote access is deliberately secured, protect TRAECN_GATEWAY_TOKEN, and set TRAECN_MCP_SERVER_PATH only to a trusted file. <br>
Risk: Conversation deletion is permanent, and stopping visible work may interrupt work that was not submitted through the gateway. <br>
Mitigation: Delete only inactive conversations explicitly identified by the user, re-read the exact ID and title before deletion, and require audit reasons for visible-generation stops. <br>
Risk: Unsafe or ambiguous command approvals can affect the user's workspace or environment. <br>
Mitigation: Approve only after checking the exact expected command and risk, require acknowledgeRisk for approvals, and rely on the local audit log for high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp) <br>
- [MCP Surface](references/mcp-surface.md) <br>
- [MCP Tool Contracts](references/mcp-tool-contracts.json) <br>
- [MCP Call Examples](references/mcp-call-examples.json) <br>
- [MCP Client Configuration](assets/mcp-client-config.json) <br>
- [Direct MCP Client Configuration](assets/mcp-client-config.direct.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance plus stdio MCP JSON-RPC tool calls and structured JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node and a trusted TRAECNclaw gateway/server.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
