## Description:

Guides agents through DebugBundle runtime incident investigation, health monitoring, product analytics, and evidence-based debugging using the CLI primarily and MCP when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and incident responders use this skill to investigate production runtime failures, customer-facing incidents, endpoint health, and product usage, then organize captured evidence into focused debugging guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan could not resolve one local reference, so the available scan evidence does not cover that reference.

Mitigation: Inspect the unresolved reference and review the skill before relying on its guidance.

Risk: Debugging workflows may involve member credentials and sensitive captured evidence.

Mitigation: Do not expose credential values or raw sensitive payloads; keep project tokens limited to SDK ingestion.

Risk: Some monitoring and incident-management operations can change hosted state or send external requests.

Mitigation: Use scoped reads first, target only appropriate public endpoints, and make changes only when the user explicitly requests them.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown text with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the incident, health check, or analytics question being investigated.]

## Skill Version(s):

1.21.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
