## Description:

Helps investigate runtime failures, customer-facing incidents, endpoint health, and product analytics using DebugBundle's CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate live application errors, crashes, alerts, health checks, and product analytics, then guide evidence-based fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected project incident, analytics, health, or configuration data may be sensitive.

Mitigation: Use only intended projects and scoped reads with appropriate existing authentication; avoid exposing credentials or raw sensitive payloads.

Risk: Management actions can change billing, access, alerts, webhooks, automation, capture rules, or monitoring.

Mitigation: Review each requested change, require explicit authorization for the selected action and records, and verify the result afterward.

## Reference(s):

- [DebugBundle skill listing](https://clawhub.ai/debugbundle/skills/debugbundle)
- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle analytics](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics](https://debugbundle.com/docs/cli/analytics)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped incident and analytics findings; no credential values or raw sensitive payloads.]

## Skill Version(s):

1.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
