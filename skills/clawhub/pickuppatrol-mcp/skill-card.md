## Description:

Guides agents in reading and changing children's school dismissal plans in PickUp Patrol using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or authorized caregivers use this skill to inspect students, school dismissal options, weekly defaults, and date-specific plans, then make and verify requested changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect student, date, transportation option, or note may change how a child leaves school.

Mitigation: Confirm identifiers, dates, and option requirements before writes; re-read the plan and note afterward to verify the requested change.

Risk: Authentication cookies and temporary login files may expose account access if retained or shared.

Mitigation: Keep credentials out of command lines and logs, protect temporary authentication files, and remove them when finished.

Risk: A write may appear successful despite being ignored after a school cutoff.

Mitigation: Re-read the date-specific plan after writing and compare the transportation option and note, rather than relying on the response status alone.

## Reference(s):

- [PickUp Patrol API reference](references/api.md)
- [pickuppatrol-mcp ClawHub release](https://clawhub.ai/chrischall/skills/pickuppatrol-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes instructions to check requested changes against subsequent reads.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
