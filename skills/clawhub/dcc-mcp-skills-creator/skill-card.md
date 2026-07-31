## Description: <br>
DCC-MCP Skills Creator helps agents create, validate, scaffold, and review DCC-MCP skill packages for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to author DCC-MCP skill packages, generate current scaffold files, validate skill directories, and review completed task evidence for contract-safe skill improvements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scaffold creation workflow writes skill package files under a user-selected parent directory. <br>
Mitigation: Review the target parent directory before generation and inspect the generated files before loading or publishing the skill. <br>
Risk: The skill can guide users toward separate CLI installation or update actions. <br>
Mitigation: Approve CLI installation or update commands only when the DCC-MCP tooling source is trusted for the environment. <br>
Risk: Skill improvement proposals can introduce incorrect or misleading authoring guidance if accepted without review. <br>
Mitigation: Validate proposed changes with the skill validator or DCC-MCP CLI linting and review the resulting package before deployment. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator ClawHub page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [DCC-MCP Skills Creator source homepage](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, generated skill files, YAML configuration, Python code, and structured validation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated scaffolds can include SKILL.md, tools.yaml, agents/openai.yaml, scripts, and references; validation returns errors, warnings, and issue details.] <br>

## Skill Version(s): <br>
0.19.89 (source: metadata.dcc-mcp.version and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
