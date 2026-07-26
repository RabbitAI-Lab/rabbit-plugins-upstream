## Description: <br>
IdentyClaw API workflows cover multi-API JWT sessions, HOLA peer handshake lines, DID resolution, and Passport lookup for agents that use IdentyClaw Passport authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[identyclaw](https://clawhub.ai/user/identyclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this workflow skill to establish IdentyClaw API sessions, create and verify HOLA authentication lines, resolve Passport and DID identity data, and discover home or federated API capabilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can involve a long-lived Passport signing key and short-lived JWT sessions. <br>
Mitigation: Use the OpenClaw plugin path where possible, keep keys and JWTs out of chat and logs, and limit local credential access to trusted Gateway environments. <br>
Risk: Setup guidance may include high-impact installation or communication steps that need operator review. <br>
Mitigation: Review installation commands and independently verify package signatures or sources before execution. <br>
Risk: Autonomous communication workflows can send messages or attachments to unintended recipients if enabled without controls. <br>
Mitigation: Require explicit recipient, approval, attachment, and inbound-content controls before enabling autonomous email or inter-agent communication workflows. <br>


## Reference(s): <br>
- [IdentyClaw API Docs](https://api.identyclaw.com/docs) <br>
- [IdentyClaw MCP](https://api.identyclaw.com/mcp) <br>
- [ClawHub Skill Page](https://clawhub.ai/identyclaw/skills/identyclaw) <br>
- [OpenClaw IdentyClaw Plugin](https://clawhub.ai/plugins/@identyclaw/openclaw-identyclaw-plugin) <br>
- [API Reference](references/api-reference.md) <br>
- [API Login Authentication](references/login-authentication.md) <br>
- [HOLA Protocol - Inter-Agent Authentication](references/hola-agent-authentication.md) <br>
- [Send a verifiable HOLA in under 5 minutes](references/hola-howto.md) <br>
- [Subagent HOLA Protocol](references/hola-subagent-authentication.md) <br>
- [Finding Agents How-To](references/finding-agents.md) <br>
- [The did:rodit Method](references/did-rodit-method.md) <br>
- [IdentyClaw MCP Discovery Index](references/mcp-discovery-index.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown] <br>
**Output Format:** [Markdown guidance with command examples, API workflow steps, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide use of local credentials, JWT sessions, HOLA lines, DID resolution, and federated API discovery.] <br>

## Skill Version(s): <br>
1.8.3 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
