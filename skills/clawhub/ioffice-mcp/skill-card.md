## Description:

Access iOffice workspace and facility data via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workplace operations staff use this skill to work with iOffice buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail through an MCP server connected to their own tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad workplace administration and user-management actions in an iOffice tenant.

Mitigation: Install only with authorization, prefer a least-privilege token, and require explicit confirmation before deletes, approvals, account changes, or shared workplace data changes.

Risk: The skill accesses workplace and facility data that may be governed by employer and Eptura policies.

Mitigation: Use it only for authorized tenant workflows and avoid bulk extraction of floor plans, employee directories, or other workplace data.

## Reference(s):

- [npm package](https://www.npmjs.com/package/ioffice-mcp)
- [Source repository](https://github.com/chrischall/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, setup configuration, authentication guidance, and workflow steps.]

## Skill Version(s):

2.1.10 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
