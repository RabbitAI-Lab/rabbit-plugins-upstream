## Description:

Use DebugBundle for runtime error reporting, crash reporting, incident reporting, incident response, live app monitoring, and production monitoring focused on runtime failures, customer-facing incidents, and endpoint health—not generic infrastructure metrics. Investigate exceptions, alerts, logs, observability signals, health checks, and debug bundles; review product analytics; and guide evidence-based fixes through CLI primarily, with MCP where needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate production runtime failures, customer-facing incidents, endpoint health, and product analytics, then guide evidence-based debugging through the CLI or MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Production diagnostics may expose sensitive information or prompt consequential account changes.

Mitigation: Confirm the project and exact requested changes, especially billing, membership, capture rules, and monitoring; keep reads scoped and make changes only with explicit authorization.

Risk: The bundled skill review does not cover external npm code or runtime configuration contents.

Mitigation: Review the installed package and relevant runtime configuration before relying on hosted operations.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and diagnostic summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped findings and recommendations; management changes require explicit user authorization.]

## Skill Version(s):

1.18.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
