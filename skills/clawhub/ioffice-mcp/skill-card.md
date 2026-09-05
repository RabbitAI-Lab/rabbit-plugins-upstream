## Description:

Access iOffice workspace and facility data via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace administrators, and facility teams use this skill to query and manage iOffice buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail through an MCP server connected to their own authorized tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad iOffice workplace administration capability, including create, update, delete, and workflow state-transition tools.

Mitigation: Install only for authorized tenants, use least-privilege credentials, and require careful confirmation for write or administrative actions.

Risk: Username and password authentication can expose higher-value credentials if used instead of a scoped token.

Mitigation: Prefer IOFFICE_TOKEN, avoid username/password where possible, and store credentials only in approved secret-management locations.

Risk: Automating employee, visitor, room, floor-plan, maintenance, move, and mail data may conflict with employer policy or service terms if used for bulk extraction or unauthorized administration.

Mitigation: Confirm authorization with the tenant owner or employer IT team, avoid bulk extraction, and separate everyday booking workflows from tenant or user administration.

Risk: Full read views may return media such as avatars, visitor photos, space images, or floor-plan image URLs.

Mitigation: Use the default compact view unless media is specifically needed, and limit full-view access to users and workflows with a valid business need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with JSON and shell command code blocks, plus structured MCP tool calls and responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read tools support compact or full views; compact is the default and removes media fields and image URLs.]

## Skill Version(s):

2.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
