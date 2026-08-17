## Description:

Agentdevx Skill lets agents use AgentDevX to register APIs from OpenAPI specs with Ed25519 identity, encrypted credential injection, rate limiting, and audit logging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mirajmahmudul](https://clawhub.ai/user/mirajmahmudul)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect agents to the AgentDevX hosted gateway for API registration, MCP access, credential injection, persistent memory, and audited tool use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically contact a third-party hosted gateway and create an account or token on first use.

Mitigation: Install and invoke it only after accepting the external service interaction and reviewing the dashboard and revocation process.

Risk: API calls, credentials, and stored memory may route through AgentDevX servers.

Mitigation: Avoid private prompts, sensitive credentials, internal systems, or business-critical APIs unless the service's data handling meets the user's requirements.

Risk: The external gateway can expand agent access to registered APIs.

Mitigation: Review available tools and audit logs before granting access to high-impact APIs or credentials.

## Reference(s):

- [AgentDevX gateway](https://agentdevx.onrender.com)
- [AgentDevX MCP server listing](https://smithery.ai/server/io.github.mirajmahmudul/agentdevx)
- [AgentDevX SDK](https://github.com/mirajmahmudul/agentdevx-sdk)
- [AgentDevX install package](https://www.npmjs.com/package/@agentdevx/install)
- [ClawHub skill page](https://clawhub.ai/mirajmahmudul/skills/agentdevx-skill)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash and JSON configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to make outbound calls to the AgentDevX hosted gateway and configure an MCP server.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
