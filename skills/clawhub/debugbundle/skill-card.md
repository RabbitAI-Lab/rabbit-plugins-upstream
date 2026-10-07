## Description:

Guides agents investigating runtime failures, customer-facing incidents, endpoint health, and product analytics using DebugBundle's CLI or MCP connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate production exceptions, alerts, health checks, and product-usage patterns, then propose evidence-based fixes and authorized monitoring changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident and analytics queries may expose sensitive project or customer information.

Mitigation: Limit reads to the intended project and records; preserve redaction and avoid exposing credentials or raw sensitive payloads.

Risk: Resolving incidents or changing monitoring, capture rules, integrations, analytics settings, or billing can alter production operations.

Mitigation: Require explicit user approval for the specific change, verify the target scope, and confirm the resulting state.

Risk: A member token grants access to hosted DebugBundle operations.

Mitigation: Provide it only when hosted access is intended; never disclose tokens in chat or command arguments.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and structured findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped incident and analytics findings; management changes require user approval.]

## Skill Version(s):

1.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
