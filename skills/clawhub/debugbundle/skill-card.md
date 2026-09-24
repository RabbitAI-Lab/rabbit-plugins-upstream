## Description:

DebugBundle helps agents investigate runtime failures, customer-facing incidents, endpoint health, exceptions, alerts, logs, observability signals, debug bundles, and product analytics using the DebugBundle CLI first and MCP capabilities when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, incident responders, and support engineers use this skill to inspect DebugBundle runtime evidence, scope incident or analytics reads, and guide evidence-based fixes. The skill is intended for debugging production behavior while preserving explicit authorization requirements for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent access to DebugBundle can expose hosted incident, analytics, health-check, or project context if scoped incorrectly.

Mitigation: Confirm the intended project before hosted reads, use explicit project and source scope, and keep member tokens out of chat.

Risk: CLI or MCP operations can change incidents, analytics settings, health checks, capture rules, webhooks, billing, or integrations.

Mitigation: Require explicit user authorization for mutations and verify the resulting state after the action.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle ClawHub skill page](https://clawhub.ai/debugbundle/skills/debugbundle)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and scoped CLI or MCP action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hosted operations may require DebugBundle member authentication, project scoping, and explicit authorization for mutations.]

## Skill Version(s):

1.11.0 (source: server release metadata and ClawHub install metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
