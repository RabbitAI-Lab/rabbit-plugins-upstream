## Description:

Operate TraeCN through TRAECNclaw's focused stdio MCP tools for sending or stopping work, selecting workspace/model/mode/conversation context, changing Trae settings, managing conversations, and resolving exceptional questions or command approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MCP-capable agents use this skill to operate TraeCN through a focused 20-tool stdio MCP surface while leaving queueing, recovery, notifications, routine questions, and keep/revert gates to the gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A gateway exposed beyond loopback or a leaked gateway token could allow unintended access to TraeCN control surfaces.

Mitigation: Keep the gateway bound to 127.0.0.1 unless remote access is secured, protect TRAECN_GATEWAY_TOKEN, and install only the matching TRAECNclaw server from a trusted source.

Risk: Approving an exceptional shell command can run work outside the intended user scope.

Mitigation: Review the exact returned command and risk classification before approval; approvals require expectedCommand, acknowledgeRisk:true, and a short audit reason.

Risk: Deleting a conversation is permanent and cannot be restored by the gateway.

Mitigation: Delete only an inactive conversation that the user explicitly named or unambiguously identified, then re-read the listed ID and exact title before sending acknowledgePermanentDeletion:true.

Risk: Stopping visible generation may interrupt work owned by the user or another agent.

Mitigation: Prefer traecn_cancel_task when a gateway task ID exists; use traecn_stop_generation only for the active conversation with acknowledgeUntrackedWork:true and an audit reason.

Risk: Mock mode and non-terminal task states can be mistaken for completed TraeCN evidence.

Mitigation: Use mock mode only for development and treat mock results or non-terminal task states as incomplete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp)
- [ClawHub Publisher Profile](https://clawhub.ai/user/luckycat133)
- [MCP surface](references/mcp-surface.md)
- [MCP tool contracts](references/mcp-tool-contracts.json)
- [MCP call examples](references/mcp-call-examples.json)
- [MCP client config template](assets/mcp-client-config.json)
- [MCP servers JSON schema](https://json.schemastore.org/mcp-servers.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, tool-call schemas, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce MCP tool calls that delegate work, change TraeCN context, mutate settings, stop generation, delete inactive conversations, or resolve command approvals.]

## Skill Version(s):

0.6.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
