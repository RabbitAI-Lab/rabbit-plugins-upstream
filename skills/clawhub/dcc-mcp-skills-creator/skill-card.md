## Description:

Creates, edits, and validates DCC-MCP tool skill packages, including SKILL.md and tools.yaml files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, update, and validate DCC-MCP skill packages for tool integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scaffolding or editing a skill may modify files in an unintended local directory.

Mitigation: Review the target parent directory before creating or updating a skill package.

Risk: Installing an unreviewed revision may introduce unwanted skill behavior.

Mitigation: Use the verified installation procedure with a full commit ID from a trusted review record.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/loonghao/skills/dcc-mcp-skills-creator)
- [Declared skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-mcp-skills-creator/SKILL.md)
- [Skill authoring workflow](artifact/references/AUTHORING_WORKFLOW.md)
- [Package validation](artifact/references/PACKAGE_VALIDATION.md)
- [Verified installation procedure](artifact/references/VERIFIED_INSTALL.md)

## Skill Output:

**Output Type(s):** [Code, Configuration, Guidance]

**Output Format:** [Skill package files and text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local skill packages and reports validation results.]

## Skill Version(s):

0.19.107 (source: skill metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
