## Description: <br>
Infrastructure skill for creating, validating, scaffolding, and reviewing DCC-MCP skills for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to scaffold, validate, and improve DCC-MCP skill packages with current SKILL.md, tools.yaml, prompt, script, and reference-file conventions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_skill workflow can create a new directory tree and scaffold files at the requested parent_dir. <br>
Mitigation: Review parent_dir before invocation and inspect generated files before loading, committing, or publishing the new skill. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [Publisher profile](https://clawhub.ai/user/loonghao) <br>
- [Homepage metadata](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, Python code, YAML configuration, shell commands, and structured validation reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The create_skill tool writes a new skill directory and scaffold files only when directed; validation returns a structured report.] <br>

## Skill Version(s): <br>
0.19.87 (source: evidence.release.version and metadata.dcc-mcp.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
