## Description:

Provides shell guidance for reading and changing children's school dismissal plans on PickUp Patrol, including weekly defaults, date-specific changes, and school cutoff times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or guardians with a PickUp Patrol account can use this guide to inspect school dismissal options and student plans, then prepare and verify changes from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing account credentials, session cookies, or student data stored in temporary files.

Mitigation: Use your own account; protect and delete temporary authentication, cookie, and student files after use.

Risk: Incorrect write commands can change live student dismissal plans or overwrite student fields.

Mitigation: Review every PUT/PATCH command before running it, back up full student JSON before whole-record updates, and re-read plans to verify changes.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for authenticated reads, plan updates, and verification of changes.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
