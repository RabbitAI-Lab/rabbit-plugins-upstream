## Description:

Provides shell guidance for reading and changing children's PickUp Patrol dismissal plans, including weekly defaults, date-specific plans, and school cutoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized caregivers can use the skill to inspect their children's school dismissal plans and prepare changes to daily or weekly transportation arrangements through their own PickUp Patrol account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect write could change a child's real dismissal arrangements.

Mitigation: Require human review of the child, date, transportation option, note, and school cutoff before each write; avoid unattended automation.

Risk: Account credentials, session cookies, or authentication responses could be exposed.

Mitigation: Keep passwords, cookies, authentication responses, and temporary files private.

Risk: A change may be silently ignored after a school cutoff despite a successful-looking response.

Mitigation: Re-read the plan and verify both the transportation option and note after writing.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change live account data when executed with an authenticated session.]

## Skill Version(s):

1.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
