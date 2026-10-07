## Description:

Connects an agent to iOffice workplace data and actions for space, reservation, visitor, maintenance, move, and mail workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees use the skill to find workplace resources and manage room reservations, visitors, maintenance requests, moves, and mail in their iOffice tenant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available actions can modify or delete workplace, directory, visitor, mail, move, reservation, and maintenance data beyond personal bookings.

Mitigation: Use only with tenant authorization and a credential restricted to the minimum necessary permissions; review the target and effect before confirming changes.

Risk: Workplace records may contain sensitive employee or visitor information, and automation may be subject to employer policies.

Mitigation: Limit access to authorized users and tasks, and check employer policies before connecting the tenant.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ioffice-mcp)
- [ioffice-mcp npm package](https://www.npmjs.com/package/ioffice-mcp)
- [Project repository listed in skill documentation](https://github.com/chrischall/ioffice-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include workplace records, write-action receipts, or confirmation previews.]

## Skill Version(s):

3.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
