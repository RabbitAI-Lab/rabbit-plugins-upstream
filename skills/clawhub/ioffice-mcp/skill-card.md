## Description:

Connects an agent to iOffice to manage workplace spaces, reservations, visitors, maintenance, moves, and mail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and facilities teams use this skill to query and update their organization's iOffice workplace records, including room bookings, visitors, maintenance requests, moves, and mail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized automation or access to workplace data may violate employer policy.

Mitigation: Confirm employer approval before installing or using the connector.

Risk: Exposed or overprivileged credentials could grant access to tenant data.

Mitigation: Use least-privilege credentials, keep secrets in project-local configuration or a secrets manager, and rotate tokens periodically.

Risk: Write and delete actions can change or remove workplace records.

Mitigation: Review the target and intended changes before confirming each action.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [iOffice MCP package](https://www.npmjs.com/package/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown and text responses from iOffice tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated iOffice tenant connection.]

## Skill Version(s):

3.2.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
