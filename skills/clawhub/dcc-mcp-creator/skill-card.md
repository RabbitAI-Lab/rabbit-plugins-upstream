## Description:

Infrastructure skill - guide developers and agents through creating or modernizing a DCC-MCP adapter or standalone internal MCP service for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modernize, validate, and release DCC-MCP adapters or standalone internal MCP services for DCC hosts and custom studio systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide local code edits and command execution while creating adapters or internal MCP services.

Mitigation: Review generated adapter changes and validation commands before applying them to production DCC or intranet environments.

Risk: Standalone internal services may be exposed beyond loopback if operators choose an intranet deployment.

Mitigation: Require operator-owned TLS, authentication, firewall policy, secret storage, audit controls, and shutdown ownership before intranet exposure.

Risk: Network package installation through the npx installer executes a fetched package command.

Mitigation: Prefer the native OpenClaw install path when available and treat npx installation as a network-executed package command.

## Reference(s):

- [DCC-MCP Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [DCC-MCP Creator homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)
- [DCC-MCP skill](https://clawhub.ai/loonghao/skills/dcc-mcp)
- [DCC-MCP Skills Creator](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are implementation guidance for agent-mediated code edits and validation workflows; generated adapter changes should be reviewed before production use.]

## Skill Version(s):

0.19.99 (source: metadata.dcc-mcp.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
