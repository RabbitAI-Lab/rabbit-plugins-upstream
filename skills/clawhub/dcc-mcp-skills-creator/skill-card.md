## Description: <br>
Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to scaffold, validate, and review DCC-MCP skill packages, including SKILL.md, tools.yaml, scripts, prompts, and reference documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The creation tool writes a new skill folder under the parent directory supplied by the caller. <br>
Mitigation: Use a dedicated skills workspace and review generated scaffolds before loading them into production adapters. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [DCC-MCP Skills Creator Source Homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [AUTHORING_WORKFLOW.md](references/AUTHORING_WORKFLOW.md) <br>
- [DCC_TOOL_CONTRACTS.md](references/DCC_TOOL_CONTRACTS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance, JSON-like validation reports, YAML configuration, and generated skill files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create a new skill directory containing SKILL.md, tools.yaml, agents, scripts, and references when the explicit creation tool is invoked.] <br>

## Skill Version(s): <br>
0.19.83 (source: SKILL.md metadata.dcc-mcp.version and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
