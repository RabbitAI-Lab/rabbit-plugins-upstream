## Description:

TRAECNclaw MCP lets an MCP-capable agent operate TraeCN through focused stdio tools for sending work, selecting workspace, model, mode, and conversation context, managing settings and conversations, and resolving exceptional approvals or questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and MCP-capable agents use this skill to control a local TraeCN session through scoped tools while the gateway manages queueing, notifications, recovery, and interaction safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A gateway exposed beyond loopback could allow unintended access to TraeCN controls.

Mitigation: Keep TRAECN_GATEWAY_HOST bound to 127.0.0.1 unless remote access is explicitly secured.

Risk: Command approvals and permanent conversation deletion can have high-impact or irreversible effects.

Mitigation: Review the exact command or conversation title and require the documented acknowledgement fields before allowing the tool call.

Risk: Secrets or profile data could be exposed through careless setup or output handling.

Mitigation: Do not print, log, or persist TRAECN_GATEWAY_TOKEN, .env contents, authorization headers, or TraeCN profile data.

## Reference(s):

- [MCP surface](artifact/references/mcp-surface.md)
- [MCP tool contracts](artifact/references/mcp-tool-contracts.json)
- [MCP call examples](artifact/references/mcp-call-examples.json)
- [MCP client configuration](artifact/assets/mcp-client-config.json)
- [Direct MCP client configuration](artifact/assets/mcp-client-config.direct.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [MCP tool calls and structured JSON results, with setup guidance and client configuration JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and a TRAECNclaw gateway; high-impact approvals, stops, and conversation deletion require scoped acknowledgements.]

## Skill Version(s):

0.5.5 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
