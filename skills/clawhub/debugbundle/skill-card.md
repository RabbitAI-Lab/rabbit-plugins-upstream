## Description:

Helps agents investigate runtime failures, incidents, endpoint health, and product analytics using DebugBundle CLI or MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to inspect DebugBundle evidence, diagnose production failures and endpoint health, review product analytics, and guide evidence-based fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A member token or saved CLI login may permit sensitive project, incident, analytics, webhook, billing, or management reads and writes.

Mitigation: Review requested actions, scope access to the intended project, and explicitly authorize sensitive changes before execution.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)
- [DebugBundle ClawHub release](https://clawhub.ai/debugbundle/skills/debugbundle)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hosted operations may require member authentication and a scoped project.]

## Skill Version(s):

1.16.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
