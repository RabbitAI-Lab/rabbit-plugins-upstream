## Description:

Build or modernize DCC-MCP adapters and standalone studio MCP services. For individual tool skill packages, use dcc-mcp-skills-creator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement or modernize DCC-MCP adapters and standalone studio MCP services in an owning project. It provides guidance for runtime shape, host dispatch, core escalation, async recovery, testing, release, and failure routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Debugging guidance may execute a mutable npm package via npx @modelcontextprotocol/inspector@latest.

Mitigation: Pin and review the MCP Inspector version before use, or run the debug workflow in a sandboxed development environment without unnecessary secrets.

Risk: The skill is a developer workflow that can guide agents to edit code and run local commands.

Mitigation: Review proposed changes and commands before execution, and use a development workspace appropriate for code-modifying adapter work.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator)
- [Source Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md)
- [Async Recovery](references/ASYNC_RECOVERY.md)
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md)
- [Failure Analysis and Bug Routing](references/FAILURE_ROUTING.md)
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md)
- [Integration Examples](references/INTEGRATION_EXAMPLES.md)
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Runtime Integration](references/RUNTIME_INTEGRATION.md)
- [Testing And Release](references/TESTING_AND_RELEASE.md)
- [ADR-027 Protocol Type Ownership](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/docs/adr/027-protocol-type-ownership.md)
- [DCC-MCP Core Remote Server Example](https://github.com/dcc-mcp/dcc-mcp-core/tree/main/examples/remote-server)
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits and validation commands for adapter or service projects.]

## Skill Version(s):

0.19.106 (source: server release and metadata.dcc-mcp.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
