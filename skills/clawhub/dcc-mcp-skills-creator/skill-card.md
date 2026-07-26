## Description: <br>
Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to create, validate, scaffold, and review DCC-MCP skill packages, including SKILL.md files, tools.yaml declarations, scripts, prompts, and taxonomy metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create files in a user-selected parent directory. <br>
Mitigation: Review the parent directory before running create_skill and inspect generated files before deployment. <br>
Risk: Adding generated or existing skill paths changes what the DCC-MCP server can discover. <br>
Mitigation: Review skill paths and run validation before loading new or changed skills into an adapter. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>
- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, YAML configuration, Python code, shell commands, and structured validation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The create_skill tool writes a new skill directory; validate_skill_dir returns a structured validation report.] <br>

## Skill Version(s): <br>
0.19.79 (source: metadata.dcc-mcp.version and release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
