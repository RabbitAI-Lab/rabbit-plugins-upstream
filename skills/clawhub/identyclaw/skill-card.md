## Description:

IdentyClaw provides workflow guidance for multi-API JWT sessions, HOLA peer handshakes, DID resolution, Passport lookup, and agent discovery metadata for OpenClaw agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[identyclaw](https://clawhub.ai/user/identyclaw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw Gateway operators use this skill to configure IdentyClaw Passport API access, authenticate home or federated sessions, exchange and verify HOLA lines, resolve DIDs, and look up agent identity metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NEAR private keys or JWTs can be exposed if copied into chat, logs, or generated instructions.

Mitigation: Keep credentials in Gateway or host configuration and avoid displaying them in agent-visible messages or logs.

Risk: Federated API endpoints may expose different product routes or come from untrusted hosts.

Mitigation: Only configure federated API endpoints that the operator trusts and discover each peer's resources before making product calls.

Risk: Passport metadata can include sensitive contact, geographic, and facial-trait information.

Mitigation: Minimize collection and logging of Passport metadata and share only the fields required for the workflow.

## Reference(s):

- [IdentyClaw API Docs](https://api.identyclaw.com/docs)
- [IdentyClaw ClawHub Skill](https://clawhub.ai/identyclaw/skills/identyclaw)
- [IdentyClaw MCP](https://api.identyclaw.com/mcp)
- [API Reference](references/api-reference.md)
- [API Login Authentication](references/login-authentication.md)
- [Send a verifiable HOLA in under 5 minutes](references/hola-howto.md)
- [HOLA Protocol - Inter-Agent Authentication](references/hola-agent-authentication.md)
- [Subagent HOLA Protocol](references/hola-subagent-authentication.md)
- [GET /api/holanonce16ts - HOLA nonce response](references/holanonce-api.md)
- [Finding Agents How-To](references/finding-agents.md)
- [The did:rodit Method](references/did-rodit-method.md)
- [IdentyClaw Passport Metadata](references/token-metadata.md)
- [IdentyClaw MCP Discovery Index](references/mcp-discovery-index.md)
- [Client-Side Agent Authentication](references/mcp-auth-tools.md)
- [Enrollment & Setup Guide](references/enrollment.md)
- [OpenClaw Integration Guide](references/openclaw-integration-guide.md)
- [Channel-Agnostic Collaboration Envelope](references/collaboration-envelope.md)
- [IdentyClaw ClawHub Skill Reference](references/identyclaw-skill.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires IdentyClaw Passport credentials; recommended flows keep authentication in the OpenClaw IdentyClaw plugin or host configuration.]

## Skill Version(s):

1.8.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
