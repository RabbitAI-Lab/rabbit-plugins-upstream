## Description:

Build, scaffold, and deploy Power Automate cloud flows using the FlowStudio MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ninihen1](https://clawhub.ai/user/ninihen1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to create, update, deploy, verify, and test Power Automate cloud flow definitions through FlowStudio MCP without opening the Power Automate portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to create or modify live Power Automate cloud flows, which may send messages, write records, start approvals, or call external APIs.

Mitigation: Review generated flow definitions before deployment, confirm the target environment and flow name, and require explicit user approval before triggering test runs.

Risk: FlowStudio JWTs, connector credentials, client secrets, and HTTP callback URLs can expose access if copied into flow definitions or shared logs.

Mitigation: Treat tokens and callback URLs as secrets, avoid hardcoding secrets, and use parameters, environment variables, or approved connection mechanisms.

Risk: Webhook or arbitrary JSON input can cause incorrect downstream behavior if the flow assumes unvalidated fields.

Mitigation: Prefer explicit JSON schemas and validate webhook input before using it in downstream actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ninihen1/skills/power-automate-build)
- [FlowStudio MCP](https://mcp.flowstudio.app)
- [Flow Definition Schema](references/flow-schema.md)
- [Trigger Types](references/trigger-types.md)
- [Common Build Patterns](references/build-patterns.md)
- [Action Patterns: Core](references/action-patterns-core.md)
- [Action Patterns: Data Transforms](references/action-patterns-data.md)
- [Action Patterns: Connectors](references/action-patterns-connectors.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON flow definitions, Python and shell snippets, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing instructions for building and deploying Power Automate flows via FlowStudio MCP; deployment can affect live cloud flows.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
