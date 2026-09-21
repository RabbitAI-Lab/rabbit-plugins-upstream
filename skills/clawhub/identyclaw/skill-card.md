## Description:

IdentyClaw API workflows - multi-API JWT sessions, HOLA peer handshake lines, DID resolution, and Passport lookup for OpenClaw agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[identyclaw](https://clawhub.ai/user/identyclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw Gateway operators use this skill to guide agents through IdentyClaw Passport authentication, HOLA peer verification, DID resolution, agent discovery, and federated API sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verified identity may be mistaken for permission to act on inbound tasks.

Mitigation: Deny unknown senders by default, allow only specific task types, isolate tools, and require human approval for consequential actions.

Risk: NEAR private keys, JWTs, or identity metadata could be exposed through chat, logs, or shared workspace files.

Mitigation: Keep private keys and JWTs out of chat and logs, prefer Gateway-held plugin workflows, and minimize collection or storage of full Passport metadata.

Risk: Optional wallet or on-chain tools can perform consequential actions if enabled broadly.

Mitigation: Leave wallet and idcp tools disabled unless needed, allowlist them narrowly, and review on-chain actions before execution.

## Reference(s):

- [IdentyClaw API Docs](https://api.identyclaw.com/docs)
- [ClawHub Skill Page](https://clawhub.ai/identyclaw/skills/identyclaw)
- [OpenClaw IdentyClaw Plugin](https://clawhub.ai/plugins/@identyclaw/openclaw-identyclaw-plugin)
- [API Reference](references/api-reference.md)
- [API Login Authentication](references/login-authentication.md)
- [HOLA How-To](references/hola-howto.md)
- [HOLA Agent Authentication](references/hola-agent-authentication.md)
- [DID RODiT Method](references/did-rodit-method.md)
- [OpenClaw Integration Guide](references/openclaw-integration-guide.md)
- [Token Metadata](references/token-metadata.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to API, HOLA, DID, MCP documentation, OpenClaw plugin configuration, and credential-handling workflows.]

## Skill Version(s):

1.9.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
