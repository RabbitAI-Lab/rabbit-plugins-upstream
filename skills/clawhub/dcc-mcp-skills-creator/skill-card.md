## Description: <br>
Infrastructure skill for creating, validating, scaffolding, and reviewing DCC-MCP skills for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create DCC-MCP skill packages, generate current SKILL.md and tools.yaml scaffolds, validate installable skill directories, and review completed task evidence for contract-safe skill improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_skill tool writes a new directory and files at the requested parent_dir. <br>
Mitigation: Review the target parent_dir before running create_skill and keep the requested path inside an intended workspace. <br>
Risk: Generated or modified DCC-MCP skill packages may contain invalid contracts or unsafe assumptions if used without review. <br>
Mitigation: Run validate_skill_dir or the equivalent dcc-mcp-core validation before loading a generated or changed skill into an adapter. <br>


## Reference(s): <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>
- [Metadata Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, Python code, YAML configuration, shell commands, generated skill files, and JSON validation reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The create_skill tool writes a new skill directory under the requested parent directory; validation tools return structured status and issue details.] <br>

## Skill Version(s): <br>
0.19.86 (source: metadata.dcc-mcp.version and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
