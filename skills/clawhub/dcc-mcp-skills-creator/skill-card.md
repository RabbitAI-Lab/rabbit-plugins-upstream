## Description:

Infrastructure skill - create, validate, scaffold, and review DCC-MCP skills for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to create, validate, scaffold, and review DCC-MCP skill packages, including SKILL.md, tools.yaml, scripts, prompts, and authoring references. It is intended for skill package authoring rather than full DCC-MCP adapter repository creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill instructions or scaffolded files may include incorrect or misleading guidance if scaffold parameters are untrusted.

Mitigation: Treat scaffold parameters as trusted input, inspect generated SKILL.md and related files, and run validation before installing or publishing.

Risk: Installer commands that use npx can execute marketplace tooling in the current shell context.

Mitigation: Prefer a verified or preinstalled CLI and avoid running npx --yes from an elevated shell unless the publisher and source are trusted.

## Reference(s):

- [DCC-MCP Skills Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [DCC-MCP Skills Creator Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [AUTHORING_WORKFLOW.md](references/AUTHORING_WORKFLOW.md)
- [DCC_TOOL_CONTRACTS.md](references/DCC_TOOL_CONTRACTS.md)
- [Agent Plugin 1.0 Schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown, YAML, Python scaffold files, shell commands, and structured validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can create files in a requested skill directory and can return a SKILL.md template or validation report.]

## Skill Version(s):

0.19.99 (source: metadata.dcc-mcp.version and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
