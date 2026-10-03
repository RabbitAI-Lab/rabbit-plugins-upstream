## Description:

Helps authorized employees access and manage iOffice workplace and facility records through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees use this skill to look up workspace information and manage reservations, visitors, maintenance requests, moves, and mail in their employer's iOffice tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An external package handles credentials for workplace data.

Mitigation: Install only if you trust the package and use a least-privilege token where possible.

Risk: Administrative or state-changing actions can alter workplace records.

Mitigation: Confirm workplace authorization and review create, update, delete, approval, delivery, check-in, and checkout actions before execution.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and MCP tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the configured tenant and account permissions.]

## Skill Version(s):

3.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
