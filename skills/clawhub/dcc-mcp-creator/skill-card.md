## Description: <br>
Infrastructure skill - guide developers and agents through creating or modernizing a DCC-MCP adapter or standalone internal MCP service for Nuke, Blender, 3ds Max, Unreal, ZBrush, Houdini, Maya, and custom studio systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to create or modernize DCC-MCP adapters and standalone internal MCP services, including server composition, dispatch, gateway wiring, packaging, runtime integration, and verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated or modernized adapters may expose private services, UI automation, memory, or network access. <br>
Mitigation: Review generated adapter code and configuration before running it outside local development. <br>
Risk: The skill can guide file editing and shell command use in a project. <br>
Mitigation: Inspect proposed changes and run the project's validation gates before deployment. <br>


## Reference(s): <br>
- [DCC-MCP Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>
- [Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-creator/SKILL.md) <br>
- [Adapter And Service Workflow](references/ADAPTER_WORKFLOW.md) <br>
- [Internal Standalone Service Workflow](references/INTERNAL_SERVICE_WORKFLOW.md) <br>
- [Host Pattern Matrix](references/HOST_PATTERN_MATRIX.md) <br>
- [Core Escalation Checklist](references/CORE_ESCALATION_CHECKLIST.md) <br>
- [Testing And Release](references/TESTING_AND_RELEASE.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide file edits and command execution in the user's project.] <br>

## Skill Version(s): <br>
0.19.90 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
