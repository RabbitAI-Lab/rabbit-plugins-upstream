## Description:

Read and change children's school dismissal plans on PickUp Patrol using shell commands, including student records, weekly defaults, date-specific changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized caregivers use this skill to inspect student dismissal plans and prepare changes to daily plans or weekly defaults from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The login example may leave active session data in predictable temporary files.

Mitigation: Use only on a trusted single-user machine, protect the cookie jar as an active session, and delete temporary authentication files after use.

Risk: Incorrect or unaccepted writes can affect a child's real dismissal arrangements.

Mitigation: Check the school's option rules and cutoff time before writing, then re-read the plan and verify the transportation and note.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use authenticated PickUp Patrol requests; re-read changes to confirm they took effect.]

## Skill Version(s):

1.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
