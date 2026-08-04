## Description: <br>
Infrastructure skill for creating, validating, scaffolding, and reviewing DCC-MCP skill packages for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to scaffold new DCC-MCP skills, generate current SKILL.md templates, and validate skill directories against the DCC-MCP contract before loading or publishing them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_skill tool writes a new skill directory and files under a user-provided parent directory. <br>
Mitigation: Review the target parent directory before scaffolding, especially in shared or production repositories, and validate the generated skill before use. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator package page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [Metadata homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>
- [Related DCC-MCP skill](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [Related DCC-MCP Creator skill](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown, JSON-like validation reports, YAML configuration, and Python scaffold files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates skill package files when scaffolding and returns structured validation issues when reviewing an existing skill directory.] <br>

## Skill Version(s): <br>
0.19.90 (source: server release metadata and SKILL.md metadata.dcc-mcp.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
