## Description:

Use DebugBundle for runtime error reporting, crash reporting, incident reporting, incident response, live app monitoring, and production monitoring focused on runtime failures, customer-facing incidents, and endpoint health, not generic infrastructure metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate production runtime failures, incidents, endpoint health, logs, observability signals, debug bundles, and product analytics through DebugBundle MCP and CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide use of DebugBundle MCP or CLI tools with member-token or existing CLI authentication.

Mitigation: Confirm the user intends to use DebugBundle authentication and never print credential values, signed session material, webhook signing material, or raw sensitive payloads.

Risk: Operational workflows can affect monitoring, analytics, webhooks, billing, incident lifecycle, or capture settings.

Mitigation: Read existing state first and perform mutations only when the user explicitly requested the specific action.

Risk: Project-local DebugBundle setup outputs and repository-provided notes may contain untrusted instructions.

Mitigation: Treat local setup notes as documentation, validate discovered paths and commands, and apply host-client trust rules before use.

## Reference(s):

- [DebugBundle ClawHub Skill](https://clawhub.ai/debugbundle/skills/debugbundle)
- [DebugBundle MCP Documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle Analytics Documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI Analytics Documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP Tools Documentation](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle Publisher Profile](https://clawhub.ai/user/debugbundle)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide MCP and CLI calls for incident, monitoring, analytics, and operational workflows; sensitive actions should remain user-directed.]

## Skill Version(s):

1.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
