## Description:

Guides developers and agents through creating or modernizing DCC-MCP adapters and standalone internal MCP services for DCC and custom studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, implement, validate, and release DCC-MCP adapter/server integrations for DCC hosts or private internal services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to modify adapter or internal service code and run development commands for DCC-MCP infrastructure.

Mitigation: Review proposed code changes and development commands before applying them, especially when they affect service exposure, raw UI control, credentials, memory, or telemetry settings.

Risk: Generated adapter or service configuration may expose private studio systems beyond the intended loopback or intranet boundary.

Mitigation: Confirm network binding, authentication, TLS, allow-lists, secret handling, and operator-owned deployment controls before using generated configuration outside local development.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [OpenClaw Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose adapter or service code changes and development validation commands.]

## Skill Version(s):

0.19.92 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
