## Description:

TRAECNclaw MCP lets an MCP-capable agent operate TraeCN through focused stdio tools for task delegation, workspace, model, mode, conversation, settings, and exceptional interaction handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external MCP-capable agents use this skill to delegate coding work to a local TraeCN gateway, manage TraeCN context, inspect or change visible settings, and handle command approvals or questions with explicit acknowledgements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An MCP-capable agent can operate a local TraeCN gateway and trigger high-impact actions such as stopping visible work, deleting conversations, or approving commands.

Mitigation: Keep the gateway bound to 127.0.0.1 unless secured, use a trusted matching TRAECNclaw server, and require exact identifiers, explicit acknowledgements, and audit reasons for high-impact operations.

Risk: Command approvals may expose workspace, credential, or Git hook risks that cannot be judged from command text alone.

Mitigation: Review every returned command and its risk classification before approval; approvals require the exact expected command, acknowledgeRisk:true, and a concise audit reason.

Risk: Conversation deletion is permanent and cannot be restored by the gateway.

Mitigation: Delete only an inactive conversation explicitly identified by the user after re-reading the listed conversation ID and exact title, and pass acknowledgePermanentDeletion:true.

Risk: Gateway tokens, authorization headers, .env contents, or TraeCN profile data could be exposed if handled carelessly.

Mitigation: Do not print, log, or persist secrets; keep the primary gateway token confidential and rely on redacted local security audit logging for high-impact actions.

## Reference(s):

- [TRAECNclaw MCP Skill Page](https://clawhub.ai/luckycat133/skills/traecnclaw-mcp)
- [MCP Surface](references/mcp-surface.md)
- [MCP Tool Contracts](references/mcp-tool-contracts.json)
- [MCP Call Examples](references/mcp-call-examples.json)
- [MCP Client Configuration Template](assets/mcp-client-config.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and MCP tool-call arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node and a trusted matching TRAECNclaw server; gateway actions are scoped through explicit MCP tool contracts.]

## Skill Version(s):

0.5.9 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
