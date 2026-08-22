## Description:

Give your AI hands. Register any API via OpenAPI spec - agents get Ed25519 identity, encrypted credential injection, rate limiting, and audit logging automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mirajmahmudul](https://clawhub.ai/user/mirajmahmudul)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect an agent to the AgentDevX hosted gateway, register APIs from OpenAPI specs, configure MCP access, and use managed agent identity, credential vault, memory, rate limiting, and audit logging features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AgentDevX can receive routed API calls and host agent-related credentials or memory.

Mitigation: Install only after reviewing the service terms, dashboard controls, audit logs, and deletion process; avoid highly sensitive secrets until that review is complete.

Risk: The skill can auto-register an agent with a third-party hosted gateway on first tool use.

Mitigation: Do not invoke the skill's tools if third-party self-provisioning is not acceptable; use the AgentDevX dashboard to revoke access or delete the account.

## Reference(s):

- [AgentDevX Gateway](https://agentdevx.onrender.com)
- [AgentDevX MCP Server on Smithery](https://smithery.ai/server/io.github.mirajmahmudul/agentdevx)
- [AgentDevX SDK](https://github.com/mirajmahmudul/agentdevx-sdk)
- [AgentDevX npm Package](https://www.npmjs.com/package/@agentdevx/install)
- [ClawHub Skill Page](https://clawhub.ai/mirajmahmudul/skills/agentdevx-skill)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to make routed API calls and configure an MCP server through AgentDevX.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
