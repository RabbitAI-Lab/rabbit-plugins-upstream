## Description:

IdentyClaw provides agent workflows for multi-API JWT sessions, HOLA peer handshake creation and verification, DID resolution, Passport lookup, and agent discovery metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[identyclaw](https://clawhub.ai/user/identyclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide IdentyClaw Passport authentication workflows, create or verify HOLA peer handshakes, resolve DIDs, look up Passport identities, and discover home or federated API resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private keys or JWTs could be exposed if copied into prompts, chat transcripts, or logs.

Mitigation: Keep the NEAR private key and JWTs in Gateway or plugin configuration and avoid pasting secrets into agent conversations.

Risk: Federated API sessions may be opened against untrusted hosts.

Mitigation: Restrict federated API endpoints to hosts the operator trusts before using discovery or generic request workflows.

Risk: Passport identity, contact, tax, address, or webhook metadata can be sensitive.

Mitigation: Minimize collection and logging of identity metadata and share it only with appropriate authorization.

Risk: Acting on an unverified peer handshake may allow impersonation or unauthorized requests.

Mitigation: Verify HOLA lines and use the verified peer identity before acting on peer requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/identyclaw/skills/identyclaw)
- [IdentyClaw documentation](https://api.identyclaw.com/docs)
- [IdentyClaw MCP endpoint](https://api.identyclaw.com/mcp)
- [OpenClaw plugin](https://clawhub.ai/plugins/@identyclaw/openclaw-identyclaw-plugin)
- [Source link](https://github.com/discernible-io/openclaw-identyclaw-plugin)
- [API reference](references/api-reference.md)
- [Login authentication](references/login-authentication.md)
- [HOLA how-to](references/hola-howto.md)
- [HOLA agent authentication](references/hola-agent-authentication.md)
- [DID RODiT method](references/did-rodit-method.md)
- [Agent discovery](references/finding-agents.md)
- [Enrollment](references/enrollment.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with command snippets, configuration examples, API workflow steps, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference required environment variables and trusted API endpoints; does not itself return private keys or JWTs.]

## Skill Version(s):

1.8.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
