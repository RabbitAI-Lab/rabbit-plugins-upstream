## Description: <br>
Infrastructure skill - guide developers and agents through creating or modernizing a DCC-MCP adapter or standalone internal MCP service for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create or modernize DCC-MCP adapters and standalone internal MCP services. It guides server composition, host-thread dispatch, sidecar and gateway wiring, readiness, diagnostics, packaging, runtime integration, and validation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to edit local adapter code, run validation commands, and configure local services. <br>
Mitigation: Review generated or modified adapter code and run the documented validation and smoke tests before deployment. <br>
Risk: Exposing an adapter or standalone service beyond loopback can introduce authentication, network, and audit risks. <br>
Mitigation: Keep development on loopback by default; before intranet exposure, require operator-owned TLS termination, authentication, network allow-lists, secret management, audit retention, and shutdown ownership. <br>
Risk: Credentials or private deployment details could be included in generated skill files, examples, logs, or result payloads. <br>
Mitigation: Keep credentials in operator-managed secret storage or process environment, and avoid placing them in SKILL.md, tool definitions, examples, logs, or outputs. <br>


## Reference(s): <br>
- [DCC-MCP Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>
- [Metadata homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline code and shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide local code edits, validation commands, service configuration, adapter packaging, and release checks.] <br>

## Skill Version(s): <br>
0.19.89 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
