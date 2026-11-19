## Description:

Runtime error reporting and incident response for live apps with DebugBundle, using the CLI primarily and MCP where needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate live application failures, customer-facing incidents, endpoint health, logs, and product analytics through scoped DebugBundle workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports medium confidence because a local path-like reference in the documentation could not be resolved.

Mitigation: Review that reference and confirm it is expected before installing or following it.

Risk: Hosted workflows may use access tokens and handle sensitive incident or analytics data.

Mitigation: Keep credentials out of chat and tool output, use scoped access, and avoid exposing raw sensitive payloads.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools documentation](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance, shell commands, configuration examples, and incident or analytics summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scoped to the user's requested runtime investigation and project; may include concise findings and recommended next steps.]

## Skill Version(s):

1.28.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
