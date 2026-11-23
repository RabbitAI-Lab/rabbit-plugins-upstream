## Description:

DebugBundle helps developers investigate live application errors, incidents, endpoint health, logs, and product analytics through its CLI and MCP interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate production application failures, customer-facing incidents, endpoint health, and product usage with DebugBundle. It guides scoped CLI-first workflows and MCP use when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted API and MCP operations may use an optional DebugBundle access token.

Mitigation: Check that the requested operations and API origin fit the user's needs before supplying DEBUGBUNDLE_MEMBER_TOKEN; follow the skill's guidance to keep credentials out of chat and tool arguments.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.29.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
