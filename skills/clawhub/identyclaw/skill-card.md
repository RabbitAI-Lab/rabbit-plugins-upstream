## Description:

IdentyClaw API workflows cover multi-API JWT sessions, HOLA peer handshake lines, DID resolution, and Passport lookup for agents using an IdentyClaw Passport on the Gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[identyclaw](https://clawhub.ai/user/identyclaw)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and OpenClaw Gateway operators use this skill to guide IdentyClaw Passport authentication, HOLA verification, DID lookup, federated API discovery, and related plugin workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NEAR private keys and JWTs are used for IdentyClaw login and HOLA workflows.

Mitigation: Keep private keys and JWTs in Gateway or host secret storage, prefer plugin-managed login, and do not paste credentials into chat.

Risk: Passport identity payloads may contain sensitive metadata.

Mitigation: Minimize collection and logging of full Passport identity payloads.

Risk: Optional wallet/idcp and webhook behavior can expand the operational surface.

Mitigation: Enable optional wallet/idcp or webhook features only when needed and after reviewing source, signature, and route controls.

## Reference(s):

- [IdentyClaw API Docs](https://api.identyclaw.com/docs)
- [IdentyClaw ClawHub Skill](https://clawhub.ai/identyclaw/skills/identyclaw)
- [API Reference](references/api-reference.md)
- [API Login Authentication](references/login-authentication.md)
- [HOLA Protocol - Inter-Agent Authentication](references/hola-agent-authentication.md)
- [Send a verifiable HOLA in under 5 minutes](references/hola-howto.md)
- [Subagent HOLA Protocol](references/hola-subagent-authentication.md)
- [The did:rodit Method](references/did-rodit-method.md)
- [Finding Agents How-To](references/finding-agents.md)
- [Enrollment & Setup Guide](references/enrollment.md)
- [IdentyClaw MCP Discovery Index](references/mcp-discovery-index.md)
- [OpenClaw Integration Guide](references/openclaw-integration-guide.md)
- [IdentyClaw Passport Metadata](references/token-metadata.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API workflow steps]

**Output Format:** [Markdown with inline command, configuration, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is documentation-only and guides use of separate IdentyClaw/OpenClaw tools; it does not itself execute API calls.]

## Skill Version(s):

1.9.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
