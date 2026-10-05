## Description:

Helps agents investigate runtime failures, customer-facing incidents, endpoint health, and product analytics using DebugBundle, primarily through its CLI and optionally through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate production errors, monitor endpoint health, review product analytics, and plan evidence-based fixes with DebugBundle. Changes to incidents or monitoring settings require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to incident, health, analytics, and project-management data can expose sensitive information.

Mitigation: Limit reads to the requested project and records, and avoid disclosing credentials or raw sensitive payloads.

Risk: Resolving incidents or changing monitoring, analytics, webhooks, or billing settings can alter production operations.

Mitigation: Require explicit user approval for each intended change and verify the resulting state.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle skill on ClawHub](https://clawhub.ai/debugbundle/skills/debugbundle)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with optional shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped incident, health, and analytics findings; proposed changes require explicit approval.]

## Skill Version(s):

1.13.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
