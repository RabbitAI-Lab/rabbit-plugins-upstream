## Description:

Guides agents through scoped production debugging, incident response, endpoint health checks, and product analytics with DebugBundle's CLI and MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[debugbundle](https://clawhub.ai/user/debugbundle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and on-call engineers can use this skill to investigate runtime failures, customer-facing incidents, endpoint health, and product behavior, then guide evidence-based debugging and follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because one local path-like reference could not be resolved, so the scan evidence is incomplete.

Mitigation: Review the unresolved reference and scan results before relying on the skill.

Risk: Hosted debugging can involve credentials and sensitive incident evidence.

Mitigation: Use scoped access and avoid exposing credential values or raw sensitive payloads.

## Reference(s):

- [DebugBundle MCP documentation](https://debugbundle.com/docs/mcp)
- [DebugBundle analytics documentation](https://debugbundle.com/docs/analytics)
- [DebugBundle CLI analytics documentation](https://debugbundle.com/docs/cli/analytics)
- [DebugBundle MCP tools reference](https://debugbundle.com/docs/mcp/tools)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the selected project, evidence source, and available incident or analytics data.]

## Skill Version(s):

1.23.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
