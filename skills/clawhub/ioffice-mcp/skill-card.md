## Description:

Connects an agent to an authorized iOffice workplace tenant to find and manage facilities, reservations, visitors, maintenance, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and workplace administrators use the skill to look up facility records and manage room bookings, visitors, service requests, moves, and mail in their organization's iOffice tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can read sensitive workplace and people records and change shared tenant data.

Mitigation: Use only with employer authorization and a least-privileged token; review each create, update, or delete action before execution.

Risk: Tenant credentials in MCP configuration can grant broad access if exposed.

Mitigation: Protect the MCP configuration as a secret and prefer token authentication over a username and password.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language answers with workplace record details and action confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on tenant access and the selected record view.]

## Skill Version(s):

3.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
