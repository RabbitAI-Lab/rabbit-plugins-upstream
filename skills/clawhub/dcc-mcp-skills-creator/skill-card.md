## Description:

Creates, validates, scaffolds, and reviews DCC-MCP skill packages for the dcc-mcp-core ecosystem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical directors use this skill to scaffold and validate DCC-MCP skill packages, generate current SKILL.md templates, and review completed task evidence for reusable skill improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scaffold tool writes a new skill directory under a user-supplied parent directory.

Mitigation: Review the target parent_dir before execution, avoid sensitive locations, and run validation after scaffolding.

Risk: The skill references a CLI installation path that can install or update local tooling.

Mitigation: Use that path only after explicit user consent, consistent with the security guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [OpenClaw homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [DCC-MCP Skill Authoring Workflow](artifact/references/AUTHORING_WORKFLOW.md)
- [DCC-MCP Tool Contracts](artifact/references/DCC_TOOL_CONTRACTS.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Structured tool results plus generated Markdown, YAML, and Python files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a new skill file tree only when the scaffold tool is called with a target parent directory; validation is read-only.]

## Skill Version(s):

0.19.92 (source: server release and metadata.dcc-mcp.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
