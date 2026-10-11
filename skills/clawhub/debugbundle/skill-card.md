## Description:

Guides developers through DebugBundle incident investigation, runtime monitoring, health checks, and product analytics, using the CLI first and MCP when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident responders use this skill to investigate runtime failures and customer-facing incidents, check endpoint health, review product analytics, and guide evidence-based fixes through DebugBundle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident and management actions can alter monitoring, automation, access, or billing settings.

Mitigation: Review the exact action and affected records, require explicit authorization before writes, and verify the resulting state.

Risk: Incident bundles and analytics may contain sensitive customer or credential data.

Mitigation: Limit access to the intended project, preserve consent and redaction, and never disclose credentials or raw sensitive payloads.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incident findings and recommendations should identify the checked scope and distinguish confirmed results from unavailable actions.]

## Skill Version(s):

1.14.0 (source: server-resolved release and pinned package versions)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
