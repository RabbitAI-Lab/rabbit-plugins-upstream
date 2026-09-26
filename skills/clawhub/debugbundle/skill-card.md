## Description:

Helps developers investigate runtime failures, customer-facing incidents, endpoint health, and product analytics with DebugBundle, then guide evidence-based fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate application errors, incidents, health checks, and product analytics, and to plan or perform explicitly authorized operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access can expose sensitive incident, analytics, health-check, and management data.

Mitigation: Use the intended DebugBundle project, keep member tokens private, and limit reads to the requested scope.

Risk: Resolving incidents or changing monitoring and project settings can alter live operations.

Mitigation: Require explicit authorization for the specific change and verify the resulting state.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline CLI commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize scoped incidents, health checks, and analytics, and propose evidence-based fixes.]

## Skill Version(s):

1.12.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
