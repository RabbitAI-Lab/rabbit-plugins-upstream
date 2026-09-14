## Description:

Access iOffice workspace and facility data via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and workplace operations teams use this skill through an MCP server to query and manage iOffice buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail for an authorized tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad workplace administration actions in an iOffice/Eptura tenant.

Mitigation: Install and use it only with explicit authorization from the tenant owner or employer.

Risk: Credential misuse could expose or alter tenant data.

Mitigation: Use a least-privilege, revocable token rather than broad username and password credentials.

Risk: Unpinned external code execution may run a package version that has not been reviewed.

Mitigation: Pin and review the MCP package version or source commit before running it.

Risk: Create, update, delete, approval, check-in/out, delivery, return, and workflow-transition actions can change operational records.

Mitigation: Require explicit confirmation before executing write or state-transition actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [npm package](https://www.npmjs.com/package/ioffice-mcp)
- [Source repository](https://github.com/chrischall/ioffice-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with MCP tool calls, JSON configuration examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return compact or full iOffice records depending on the requested view.]

## Skill Version(s):

2.3.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
