## Description: <br>
Create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[loonghao](https://clawhub.ai/user/loonghao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical artists use this skill to scaffold and validate DCC-MCP skill packages, including SKILL.md metadata, tools.yaml contracts, scripts, prompts, and authoring guidance. It is for skill packages in the dcc-mcp-core ecosystem, not for creating a complete DCC-MCP adapter repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scaffold tool creates files in the directory supplied by the user. <br>
Mitigation: Run it only against the intended workspace path and review generated SKILL.md, tools.yaml, scripts, prompts, and references before loading the skill into a production DCC environment. <br>
Risk: Generated or proposed skill changes can encode incorrect workflow assumptions if the task evidence is incomplete. <br>
Mitigation: Validate the resulting skill directory with the provided validator or dcc-mcp-cli lint, and keep improvement inputs bounded and redacted. <br>


## Reference(s): <br>
- [DCC-MCP Skills Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator) <br>
- [DCC-MCP Skills Creator source](https://github.com/dcc-mcp/dcc-mcp-core/blob/main/skills/dcc-mcp-skills-creator/SKILL.md) <br>
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md) <br>
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md) <br>
- [DCC-MCP skill](https://clawhub.ai/loonghao/skills/dcc-mcp) <br>
- [DCC-MCP Creator skill](https://clawhub.ai/loonghao/skills/dcc-mcp-creator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, YAML configuration, Python code, shell commands, and structured validation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create files in a user-provided directory and may return validation issues for an existing skill directory.] <br>

## Skill Version(s): <br>
0.19.91 (source: server release metadata and metadata.dcc-mcp.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
