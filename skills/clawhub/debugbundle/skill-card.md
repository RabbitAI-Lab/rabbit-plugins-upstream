## Description:

Use DebugBundle for runtime error reporting, crash reporting, incident reporting, incident response, live app monitoring, and production monitoring focused on runtime failures, customer-facing incidents, and endpoint health—not generic infrastructure metrics. Investigate exceptions, alerts, logs, observability signals, health checks, and debug bundles; review product analytics; and guide evidence-based fixes through CLI primarily, with MCP where needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate production runtime failures, customer-facing incidents, and endpoint health with scoped incident, log, health-check, and product-analytics evidence, then guide evidence-based fixes through the CLI or MCP.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted operations could target the wrong project or API host.

Mitigation: Confirm the intended project and API host with a scoped read before connecting or taking action.

Risk: Broad credentials or unreviewed monitoring and account changes could expose data or alter settings unexpectedly.

Mitigation: Use appropriately scoped member credentials and review proposed monitoring or account changes before authorizing them.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools reference](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle ClawHub release](https://clawhub.ai/debugbundle/skills/debugbundle)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Analysis, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-based troubleshooting steps and scoped operational guidance.]

## Skill Version(s):

1.18.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
