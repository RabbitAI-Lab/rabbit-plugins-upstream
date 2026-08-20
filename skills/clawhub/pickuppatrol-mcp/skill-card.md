## Description:

Read and change your children's school dismissal plans on PickUp Patrol (app.pickuppatrol.net) from a shell with curl, including students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and authorized developers use this skill to inspect PickUp Patrol student dismissal data and prepare shell commands for updating one-day plans or weekly defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes commands that can make live changes to a child's school dismissal plan.

Mitigation: Run write commands only for children and school accounts you are authorized to manage, confirm student IDs, dates, transportation options, and notes before execution, and re-read the record afterward.

Risk: Session cookies, authentication responses, exported passwords, or saved student JSON can expose sensitive account and student information.

Mitigation: Keep cookie jars, auth responses, exported passwords, and temporary student files private, and delete temporary files when finished.

Risk: A failed login attempt can count against the PickUp Patrol account and may lead to lockout.

Mitigation: Do not retry rejected credentials automatically; stop after one failure and fix the credential source before trying again.

## Reference(s):

- [PickUp Patrol skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)
- [PickUp Patrol API reference](artifact/references/api.md)
- [PickUp Patrol API endpoint](https://app.pickuppatrol.net/api/json/reply)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces curl and jq-oriented guidance for live PickUp Patrol API reads and writes; it does not store credentials.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
