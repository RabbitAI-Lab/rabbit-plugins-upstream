## Description:

Access iOffice workspace and facility data through MCP for buildings, floors, spaces, reservations, visitors, maintenance requests, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, workplace operations teams, and developers use this skill to connect an agent to an authorized iOffice/Eptura tenant for room booking, visitor workflows, maintenance requests, moves, mail, and facility data lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized automation against an organization's iOffice/Eptura tenant may violate employer or service policies.

Mitigation: Install only when authorized to automate the tenant and follow employer IT and acceptable-use requirements.

Risk: The skill exposes broad workplace administration abilities, including user, delete, and facility-management actions.

Mitigation: Use a least-privilege token or account and review high-impact actions before enabling the server.

Risk: Enabling the skill depends on a third-party npm/source package.

Mitigation: Review the npm/source package before enabling it and pin versions when your environment requires reproducibility.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with JSON and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing instructions for configuring and using an iOffice MCP server; tool calls require an authorized tenant and credentials.]

## Skill Version(s):

3.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
