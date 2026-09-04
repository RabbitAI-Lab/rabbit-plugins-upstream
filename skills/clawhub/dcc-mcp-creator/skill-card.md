## Description:

Infrastructure skill that guides developers and agents through creating or modernizing DCC-MCP adapters and standalone internal MCP services for DCC hosts and custom studio systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design, scaffold, modernize, test, and release DCC-MCP adapters or standalone internal MCP services with clear runtime, packaging, gateway, and validation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose shell commands or development actions inside private repositories or internal service environments.

Mitigation: Review commands before execution and install only when intentionally building DCC-MCP adapter or internal MCP-service infrastructure.

Risk: Using unpinned helper tooling can reduce reproducibility or introduce unexpected behavior.

Mitigation: Prefer pinning or otherwise verifying the MCP Inspector instead of relying on @latest.

Risk: Exposing development services beyond loopback can create network, authentication, and secret-handling risks.

Mitigation: Keep development on loopback until TLS, authentication, firewall controls, and secret storage are owned by the operator.

Risk: Credentials or sensitive operational data could leak through skill files, examples, logs, or result payloads.

Mitigation: Keep credentials out of skill files, examples, logs, and result payloads.

## Reference(s):

- [DCC-MCP Creator ClawHub Page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Source Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include adapter architecture decisions, workflow checklists, validation steps, and release guidance.]

## Skill Version(s):

0.19.97 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
