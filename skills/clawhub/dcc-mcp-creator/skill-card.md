## Description: <br>
Guides developers and agents through creating or modernizing DCC-MCP adapters or standalone internal MCP services for DCCs and custom studio systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, scaffold, modernize, test, and release DCC-MCP adapters or private standalone MCP services while following shared runtime, gateway, dispatcher, lifecycle, and packaging contracts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent toward command execution, file edits, adapter packaging, and service startup changes in DCC-MCP infrastructure. <br>
Mitigation: Review commands and file changes before execution, and scan the resulting skill or adapter before deployment. <br>
Risk: Development services or standalone MCP services could be exposed beyond loopback if operators change network binding defaults. <br>
Mitigation: Keep services on loopback unless TLS, authentication, firewall controls, and operator-owned shutdown and audit policies are in place. <br>
Risk: Adapters or internal services may need credentials for private systems. <br>
Mitigation: Keep credentials in the normal secret store or process environment and avoid placing them in SKILL.md, examples, logs, or result payloads. <br>


## Reference(s): <br>
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>
- [Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces implementation guidance for agents; file edits and command execution remain subject to the hosting agent's approval and tool policies.] <br>

## Skill Version(s): <br>
0.19.91 (source: evidence.release.version and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
