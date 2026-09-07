## Description:

Infrastructure skill for creating, validating, scaffolding, and reviewing DCC-MCP skills for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold and validate DCC-MCP skill packages, including SKILL.md, tools.yaml, scripts, prompts, and reference documentation. It is intended for skill authoring and modernization, not for creating a full DCC-MCP adapter repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill scaffolds may contain placeholder metadata, schemas, or instructions that are unsuitable for publication if used without review.

Mitigation: Inspect generated SKILL.md and tools.yaml, replace placeholders with concrete behavior, and validate the installable skill directory before loading or publishing.

Risk: The create_skill tool writes files under the requested parent directory.

Mitigation: Choose a parent_dir intended for modification and avoid running the tool against sensitive or unrelated directories.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [Clawdis Homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [DCC-MCP Skill Authoring Workflow](references/AUTHORING_WORKFLOW.md)
- [DCC-MCP Tool Contracts](references/DCC_TOOL_CONTRACTS.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, YAML configuration, Python scaffold code, shell commands, and structured validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates files only when the create_skill tool is directed at a target parent directory; validation reports are read-only.]

## Skill Version(s):

0.19.100 (source: metadata.dcc-mcp.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
