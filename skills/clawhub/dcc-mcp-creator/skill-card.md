## Description:

Build or modernize DCC-MCP adapters and standalone studio MCP services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and studio engineers use this skill to build or modernize DCC-MCP host adapters and private standalone MCP services, including runtime integration and release checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated adapter code may behave unexpectedly in a production DCC or studio environment.

Mitigation: Review generated code and validate with local checks before live-host acceptance.

Risk: Host launches, UI control, or gateway exposure can affect live systems or widen access.

Mitigation: Keep live host launches, UI control, and gateway exposure under operator control.

Risk: Private-service credentials or publishing steps may expose sensitive access or code.

Mitigation: Handle credentials and publishing as operator-controlled steps; confirm scope before release.

## Reference(s):

- [Skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-creator/SKILL.md)
- [Adapter and service workflow](references/ADAPTER_WORKFLOW.md)
- [Internal service workflow](references/INTERNAL_SERVICE_WORKFLOW.md)
- [Runtime integration](references/RUNTIME_INTEGRATION.md)
- [Testing and release](references/TESTING_AND_RELEASE.md)
- [Core protocol type ownership](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/docs/adr/027-protocol-type-ownership.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Guidance]

**Output Format:** [Code and Markdown guidance with configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated code before production use; live-host acceptance and publishing require operator approval.]

## Skill Version(s):

0.19.108 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
