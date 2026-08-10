## Description:

Operate TraeCN through TRAECNclaw's focused stdio MCP tools for sending or stopping work, selecting workspace/model/mode/conversation context, inspecting or changing Trae settings, managing conversations, and resolving exceptional questions or command approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MCP-capable agents use this skill to operate TraeCN through a focused tool surface while leaving queueing, notifications, recovery, and routine interaction mechanics to the gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gateway access can affect real TraeCN work, including command approvals, stopping visible generation, settings changes, and permanent conversation deletion.

Mitigation: Install only with the matching TRAECNclaw server from a trusted source, review command approvals and deletion requests carefully, and use the skill's required acknowledgements and audit reasons for high-impact actions.

Risk: Remote or exposed gateway access could disclose or modify TraeCN state.

Mitigation: Keep the gateway bound to 127.0.0.1 unless remote access is explicitly secured, and do not expose tokens, authorization headers, .env files, or TraeCN profile data.

Risk: Mock mode and non-terminal task states can be mistaken for live or final TraeCN results.

Mitigation: Use mock mode only for development and treat non-terminal task states as incomplete until a final result is returned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp)
- [MCP surface](references/mcp-surface.md)
- [MCP tool contracts](references/mcp-tool-contracts.json)
- [MCP call examples](references/mcp-call-examples.json)
- [MCP server configuration schema](https://json.schemastore.org/mcp-servers.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON MCP configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node and a matching TRAECNclaw server; optional environment variables configure the local gateway host, port, token, and client ID.]

## Skill Version(s):

0.5.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
