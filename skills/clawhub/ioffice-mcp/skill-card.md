## Description:

Helps authorized employees access and manage iOffice workplace facilities, reservations, visitors, maintenance, moves, and mail through an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees authorized by their employer to use an iOffice/Eptura tenant can find workplace information and manage room bookings, visitors, maintenance requests, moves, and mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized automation could expose or alter employer workplace records.

Mitigation: Use only with employer authorization and a least-privileged tenant credential.

Risk: Deletion, approvals, check-ins, deliveries, and user-management actions affect live records.

Mitigation: Verify the intended record and review the action preview before confirming changes.

Risk: Installing an unverified integration could introduce unwanted behavior.

Mitigation: Verify the npm package or source repository before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [MCP tool responses and Markdown setup instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses support compact or full views; changes return receipts or confirmation previews.]

## Skill Version(s):

3.2.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
