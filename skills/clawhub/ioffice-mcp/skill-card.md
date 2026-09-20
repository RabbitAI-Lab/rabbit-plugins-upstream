## Description:

ioffice-mcp helps agents access iOffice workspace and facility data through an MCP server for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, mail, and health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, facilities teams, workplace operations staff, and developers use this skill to query and manage iOffice workplace resources through an MCP server using their own authorized tenant credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive workplace data such as users, visitors, reservations, spaces, floor plans, maintenance requests, moves, and mail records.

Mitigation: Install and use it only with employer authorization, scoped tenant credentials, and least-privilege access.

Risk: Write and action tools can create, update, delete, check in or out, approve, deliver, return, or otherwise change workplace records.

Mitigation: Require explicit confirmation before create, update, delete, check-in/out, approval, delivery, return, and related state-changing actions.

Risk: Bulk extraction of employee directories, floor plans, or workspace data may violate workplace or service policies.

Mitigation: Avoid bulk extraction and follow employer IT, security, acceptable-use, and Eptura/iOffice tenant policies.

## Reference(s):

- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)
- [ioffice-mcp source link declared in artifact](https://github.com/chrischall/ioffice-mcp)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls]

**Output Format:** [Markdown with JSON and shell command snippets; MCP tools return structured iOffice data, previews, receipts, and health-check guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact and full views; compact is the default and strips media fields and image URLs.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
