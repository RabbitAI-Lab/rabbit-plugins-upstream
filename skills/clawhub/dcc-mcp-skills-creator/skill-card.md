## Description:

Create, edit or validate DCC-MCP tool skill packages (SKILL.md and tools.yaml). Use dcc-mcp-creator for complete adapter repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical artists use this skill to scaffold, edit, and validate DCC-MCP skill packages with current metadata, tool schemas, runtime contracts, and reference documentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create and modify local DCC-MCP skill package files in a user-selected parent directory.

Mitigation: Confirm the target parent directory before running file-writing tools, then review and validate the generated skill directory before loading it.

Risk: Installing from an unreviewed moving branch, tag, or registry result can introduce unreviewed skill instructions or scripts.

Mitigation: Use the verified install procedure with a full commit hash from an independent review record and stop on any verification error.

## Reference(s):

- [DCC-MCP Skills Creator on ClawHub](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [Skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [Authoring Workflow](references/AUTHORING_WORKFLOW.md)
- [DCC Tool Contracts](references/DCC_TOOL_CONTRACTS.md)
- [Tool Runtime Contract](references/TOOL_RUNTIME_CONTRACT.md)
- [Package Validation](references/PACKAGE_VALIDATION.md)
- [Taxonomy Compatibility](references/TAXONOMY_COMPATIBILITY.md)
- [Distribution Boundary](references/DISTRIBUTION.md)
- [Verified Install](references/VERIFIED_INSTALL.md)
- [Task Reflection](references/TASK_REFLECTION.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON/YAML configuration, Python code, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or validate local DCC-MCP skill package files when the agent is authorized to use the bundled tools.]

## Skill Version(s):

0.19.106 (source: metadata.dcc-mcp.version and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
