## Description:

Read and change your children's school dismissal plans on PickUp Patrol (app.pickuppatrol.net) from a shell with curl: students, weekly defaults, day-by-day changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and developers with authorized PickUp Patrol accounts use this skill to generate shell commands and guidance for reading student dismissal data, transportation options, weekly defaults, and date-specific plans. It also guides reviewed changes to live dismissal plans and verification after updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose PickUp Patrol credentials, session cookies, and child dismissal information to an agent with shell access.

Mitigation: Use it only in a trusted shell, keep passwords and cookie jars out of logs and repositories, and avoid sharing captured responses that include personal or school data.

Risk: Generated write commands can change live school dismissal plans.

Mitigation: Confirm every write before running it, read transportation rules first, and re-read the affected plan after each change to verify the transportation ID and note.

Risk: Repeated rejected logins can contribute to account lockout.

Mitigation: Stop after one failed login attempt and correct credentials before trying again.

Risk: The reference material documents broad account-management endpoints in addition to dismissal-plan operations.

Mitigation: Limit use to dismissal-plan workflows unless the user has explicitly reviewed and authorized a broader account action.

## Reference(s):

- [PickUp Patrol API reference](artifact/references/api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authorized PickUp Patrol credentials and a session cookie jar; write operations should be confirmed before execution and re-read afterward.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
