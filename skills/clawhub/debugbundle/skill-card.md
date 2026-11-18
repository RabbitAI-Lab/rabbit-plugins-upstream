## Description:

Supports runtime error reporting and incident response for live apps through crash and production monitoring, endpoint health checks, debug bundles, product analytics, and CLI-first investigation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and engineers use this skill to investigate live application failures, customer-facing incidents, exceptions, logs, endpoint health, and product usage. It guides scoped DebugBundle CLI operations first, with MCP guidance where needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found no issues but has medium confidence and incomplete coverage because one local reference could not be resolved.

Mitigation: Review the missing reference and consider publisher trust before installing if greater assurance is needed.

Risk: Hosted incident and analytics workflows use credentials and can expose sensitive operational data.

Mitigation: Keep credentials out of chat and logs, use appropriately scoped access, and follow the skill's credential handling guidance.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools reference](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides scoped operational guidance; write actions require explicit authorization.]

## Skill Version(s):

1.26.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
