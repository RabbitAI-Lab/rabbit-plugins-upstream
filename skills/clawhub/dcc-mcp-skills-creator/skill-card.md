## Description:

Create, validate, scaffold, and review DCC-MCP skill packages for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to scaffold DCC-MCP skill packages, generate current SKILL.md templates, and validate installable skill directories before loading them into adapters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The create_skill tool writes durable scaffold files under the requested parent directory.

Mitigation: Review the parent_dir argument before running create_skill, then validate generated skill directories before deployment.

## Reference(s):

- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md)
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md)
- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [Source Skill Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, YAML, Python code, shell commands, and structured validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create durable skill scaffold files when create_skill is invoked; validation returns structured issue data.]

## Skill Version(s):

0.19.97 (source: evidence.release.version and metadata.dcc-mcp.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
