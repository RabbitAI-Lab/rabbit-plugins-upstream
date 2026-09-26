## Description:

Connects an agent to iOffice workplace data and tools for managing spaces, reservations, visitors, maintenance requests, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees with authorized iOffice access can find workplace information and manage room bookings, visitors, maintenance requests, moves, and mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector offers tenant-wide administrative create, update, and delete actions beyond its personal-use framing.

Mitigation: Use a least-privileged account; enable administrative actions only when expressly intended and controlled.

Risk: Workplace automation may be unauthorized under an employer's policies.

Mitigation: Confirm employer approval before connecting an iOffice account or performing workplace actions.

## Reference(s):

- [ioffice-mcp ClawHub listing](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown guidance and iOffice tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may omit image media by default; request the full view when needed.]

## Skill Version(s):

3.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
