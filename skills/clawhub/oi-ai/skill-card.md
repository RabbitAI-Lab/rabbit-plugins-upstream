## Description:

Route Oi requests through MCP for Contexts, Workflows, Skills, Guardrails, Brain, Connections, prompts, resources, sessions, and reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carhaix](https://clawhub.ai/user/carhaix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route agent requests through Oi MCP for marketplace and organization resources, connected-provider actions, guardrails, durable feedback, and usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests to organization resources and connected providers through Oi MCP.

Mitigation: Install it only when that routed integration is intended, and verify the selected organization, provider, and action before use.

Risk: Consequential actions can include Brain memory changes, publishing, guardrail changes, billing-related flows, and external-provider writes.

Mitigation: Require explicit user confirmation for those actions and review returned Oi confirmation prompts before proceeding.

Risk: Authentication may rely on OAuth tokens or an organization API key.

Mitigation: Store bearer tokens in OpenClaw secret or environment fields, avoid placing secrets in prompts or logs, and rotate keys if access changes or exposure is suspected.

## Reference(s):

- [Oi Skill on ClawHub](https://clawhub.ai/carhaix/skills/oi-ai)
- [Oi MCP Authentication for OpenClaw](references/authentication.md)
- [Oi MCP Tools](references/mcp-tools.md)
- [Oi Product Surfaces](references/product-surfaces.md)
- [Oi MCP authentication guide](https://www.oioioi.ai/resources/authentication)
- [OpenClaw MCP CLI](https://docs.openclaw.ai/cli/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline tool names and shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP routing decisions, confirmation prompts, setup commands, and concise status or risk guidance.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
